---
title: "Dev log: implementing new syntax in GHC"
layout: post
lw_xpost: true
tags: [software]
external_comments:
  - name: /r/haskell
    url: https://www.reddit.com/r/haskell/comments/1ufkj7r/dev_log_implementing_new_syntax_in_ghc/
---
In September 2024, I started working on a patch to GHC.

The story starts slightly before that. In July 2024 I wondered [Could
UndecidableInstances be
per-instance?](https://www.reddit.com/r/haskell/comments/1dy6gf3/). It seemed
like a fairly small improvement that I could possibly even implement myself. The
answer was, roughly, "someone's suggested it, and people are broadly in favor,
but with different syntax that doesn't yet exist".

> So it seems the story is, people want to phase out use of these annotations
> (which are weird because comments shouldn't change whether a program is
> accepted or not) in favor of extending use of modifier syntax (currently used
> for linear types, e.g. `a %One -> b`). But nailing down the exact details of
> the new syntax is kind of awkward. (Is a semicolon required in such-and-such
> position? How are competing modifiers handled? Is a modifier a type or a type
> constructor or what? And something I didn't see discussed: if I do `type
> MySynonym = ExistingModifier`, can I use `%MySynonym` in the same module? If
> so, does that need extra work or does it come for free?)
>
> So instead of what seems like a fairly-small change, it's a lot more
> ambitious. Definitely no longer something that makes me think "oh yeah, I
> could do that myself".

Then a few months later I decided to try implementing the new syntax
anyway[^yak]. I opened a
[PR](https://gitlab.haskell.org/ghc/ghc/-/merge_requests/14781)[^pr] in
September 2025, and it got merged in April 2026, so about a year and a half
after I started. For most of that period I wasn't putting many hours into it.

[^yak]: I haven't tried making UndecidableInstances per-instance. This yak is
    not yet shaved.

[^pr]: GHC is hosted on gitlab, which calls them "merge requests" rather than
    "pull requests", but I'm sticking to calling them PRs here.

This is how it went. I didn't start writing until January 2026, and I got
distracted and didn't finish writing until June 2026, so there's gonna be a
bunch of detail missing or misremembered. There's no particular theme or
narrative here, it just seemed like a useful kind of thing to have written down.

### ghc

The first step was to get GHC's master branch compiling. This was my second
contribution to GHC, so I'd done it before, and it was easy enough.
([Previously](https://gitlab.haskell.org/ghc/ghc/-/merge_requests/10631)
RyanGlScott had walked me through the process at Zurihac 2023.)

The actual experience of writing the code was pretty great! An awful lot of what
I did was "add a field to a record type, now go fix all the errors and warnings
in the obvious way". It helped that I had some cursory knowledge of GHC
implementation. "Trees that grow" has a bunch of overhead but absolutely pulls
its weight.

There were definitely some parts I had trouble with. Sometimes that was related
to unfamiliar terminology that I couldn't easily find documentation for. What is
"zonking"? (I think I managed to look this up, but I forgot... but as I write
this, I find a note titled "[what is
zonking?](https://github.com/ghc/ghc/blob/a72ff58fa86172b1557e405f7246d27914fdae6e/compiler/GHC/Tc/Zonk/Type.hs#L98)"
in the source code, so, maybe I wasn't very good at looking. In my defense, even
if I had assumed there was such a note there's no obvious place to look for it.
It's also possible I actually did find it and just forgot.) What does it mean to
"synify"? (Sounds like "turn something into syntax"?) Even here I think I could
mostly just "do the obvious thing".

Merge conflicts could be tricky, because I had to fix them without helpful error
messages from the compiler.

Often I had the experience of "which file was that
thing defined in again?" (Maybe an LSP would have helped with this. I didn't try
to get haskell language server running.)

Sometimes it was difficult not to reformat existing code. There's no consistent
coding style. Sometimes `do` blocks are written with braces, sometimes with
layout. Lines aren't reliably broken at any particular width. It seems like a
lot of code was originally written with nice-looking vertical alignment, then
the code changed, and the vertical alignment broke. Fixing these things would
have meant changing more lines, and it seems like the project prefers smaller
patches over consistent formatting. That's probably the right choice. I managed
to resist temptation.

The parser was difficult at times. Sometimes that was related to [shift/reduce
errors](https://haskell-happy.readthedocs.io/en/latest/tips.html#conflict-tips).
(For a while I had a `modifiersShift` which was just "`modifiers`, and then
shift". That went away when I removed modifiers from types.) Sometimes it was
related to: "there are at least three different specifications of what language
GHC accepts[^parser-specs], none of them agree with each other, and sometimes
they use the same names for different things." And sometimes: "the parser has a
lot of production rules and isn't well documented"[^parser-docs]. Production
rules related to expressions seem to include `exp`, `exp2`, `exp_gen(IEXP)`,
`infixexp2`, `infixexp`, `exp10p`, `exp_prag(e)`, `exp10`, `prag_e`, `fexp`,
`aexp`, `aexp1`, `aexp2`. (That's in order they're defined in the source code,
and `optSemi` is defined in the middle of them for some reason.) When I wanted
to parse modifiers on expressions, I had a hell of a time figuring out what to
edit, and it turned out my implementation sucked.

[^parser-specs]: The three I'm thinking of are the GHC source code itself, which
    is not very readable; the [Haskell 2010 language
    report](https://www.haskell.org/onlinereport/haskell2010/haskellch10.html),
    which is wildly out of date; and "piece together descriptions of the spec
    from proposals, and from how the proposals propose to change it", which is
    neither readable nor up-to-date. It would be nice to have dedicated
    documentation for "this is the syntax GHC accepts, including how it varies
    depending on language extensions".

[^parser-docs]: In general, the GHC source code seems *very* well documented.
    And bits of the parser have great documentation. But "what does this
    production rule accept and why does it exist in the first place" is often a
    mystery. To be fair my sense is that this would be very hard to do well. The
    documentation of shift/reduce conflicts could probably be improved though.

Hadrian was kinda confusing. I had a lot of test failures on master until I
figured out to pass `--test-way=normal`, but I don't think I ever figured out
what that did. Even after that, a couple of tests failed locally with a pattern
I never quite pinned down. (Something would happen to make them start failing,
and then they'd fail reliably, and then something would happen to make them pass
again.) When a test failed on CI that wasn't running locally, I fixed it without
figuring out how to make it run locally. (Dunno if I tried removing
`--test-way`.)

I also got test failures if I ran with `--flavour=quickest`. I used that when
iterating on getting the compiler compiling, but once I succeeded at that, I had
to run tests with `--flavour=default` and that meant compiling the whole thing
again. Maybe I should have just stuck with `default` the whole time, I dunno
how much difference it would have made to the iteration speed.

I think the line "Merge request must be rebased, because a fast-forward merge is
not possible" that was attached to the PR while it was open was very misleading.
[Marge Bot](https://gitlab.haskell.org/marge-bot) can merge it, unless there are
actual conflicts. I don't remember if actual conflicts are shown in any way
distinct from a simple "master has some commits your branch doesn't".

The thing I would have most liked to improve was getting intermediate feedback.
I rarely-or-never got replies to "here's what I have so far, it would be nice to
get some preliminary thoughts on it". Of course, this doesn't scale.

Similarly, there was a month where I had nothing to do but wait for comments;
eventually I pinged @triagers and that got the ball rolling. Maybe I should just
done that from the beginning, but I didn't want to seem pushy.

When I did get a review, comments were generally helpful and pushed me to
improve the code, especially documentation.

Again, overall the experience of working on GHC was great.

### `ghc-proposals`

Before you get a large user-facing change into GHC, you need to make a proposal
for it. In my case, someone had already made the proposal, and it had been
[accepted](https://github.com/ghc-proposals/ghc-proposals/blob/master/proposals/0370-modifiers.rst).

Unfortunately, the accepted proposal was deficient in some ways. This is
entirely unsurprising, and not a knock against the author. (If you decide what
you want to build before you start building it, you'll sometimes be mistaken
about what you want or what's possible. But if you start by building it, it
might turn out that other people don't want the thing you want.) So I had to
submit a new proposal suggesting changes to the accepted one.

I had this open in parallel with working on the code. That was helpful
because I could update each based on progress in the other (comments on the
proposal, or experience writing code). It would have been awkward if my patch
proposal had been rejected, but I didn't think that was likely.

Some questions from Simon Peyton Jones (!!Simon Peyton Jones!!) made me drop
"modifiers attached to types and expressions" entirely, after already
implementing them. The original proposal specified that `%a C x` would attach
the modifier to `C` in both types and expressions, and that was what my "make
the obvious-seeming changes in the parser and hope it works" had happened to
implement. But it's not what I would have expected when I thought about it, and
patterns can't parse that way[^pattern-decomposing]. I wasn't sure how to get
patterns and expressions to parse how I'd expect, so I dropped them. Someone
else can figure them out later if they want.

[^pattern-decomposing]: Patterns have a lot in common with types and
    expressions, but there's an important difference here. A type `A b c` can be
    read as `(A b) c`, i.e. "the type `A`, with the type `b` applied to give the
    type `A b`, and then the type `c` applied to give the type `A b c`. Similar
    for expressions. That doesn't work with patterns: if `A b c` is a pattern,
    then `A` and `A b` are *not* patterns, and if you try to write `let (A b) c
    = ...` you get a parse error.

I opened the PR here in November 2024, and got some useful feedback. Then it
languished for a bit until September 2025, after I opened the PR against GHC and
asked for review. That got a bit more useful feedback, and then it was approved
in December 2025.

### `head.hackage`

When the PR on GHC was almost-ready-to-go, it was getting test failures in CI
coming from "this breaks existing code". That was expected, but I still needed
to fix the CI.

You don't want to break existing code accidentally, so you want GHC CI to try
compiling a bunch of it. But you do want to allow breaking it deliberately. But
if you just accept an PR that deliberately breaks compilation, you can't test
that the next PR doesn't accidentally break it further.

GHC's solution to this is a repository named
[head.hackage](https://gitlab.haskell.org/ghc/head.hackage/). It contains a
bunch of patches to existing code, and GHC CI tries to compile the patched
packages. If you break something, you add a patch that allows the package to
compile with both the existing compiler and your changes. In my case, I needed a
[patch](https://gitlab.haskell.org/ghc/head.hackage/-/merge_requests/437) to
[`linear-generics`](https://hackage.haskell.org/package/linear-generics)[^linear-generics-pr].
Notes on how updating this went:

[^linear-generics-pr]: It would have been polite of me to submit a PR to the
    `linear-generics` repository itself, in preparation for the new GHC version.
    Maybe I'll do that at some future point.

- `./run-ci` seems to have two different relevant GHC versions. It compiles and
  runs some Haskell code to coordinate the main work, and it uses the `ghc` on
  your path to do that. I couldn't get that to work with >9.10. Then that
  compiled code uses a separate `ghc` to compile lots more code. The point is to
  test whether that separate GHC is capable of compiling it. So I ended up
  calling

  - `GHC=/path/to/ghc-9.14 ./run-ci`
  - `GHC=/path/to/my-new-ghc ./run-ci`

  in both cases, with ghc-9.10 on my PATH. This makes sense but wasn't well
  documented. (And it's weird that 9.12 didn't work to compile the coordination
  program. That version was released in March 2025. Maybe I misremembered that?)

- If `./run-ci` previously ran beyond a certain point, the next run fails with

      Path '/home/phil/local/src/head.hackage/ci/run/bin/head-hackage-ci' already exists. Use --overwrite-policy=always to overwrite.

  This `--overwrite-policy` is a cabal option but it's not clear how to pass it.
  I just did `rm -r ci/run` to fix the issue.

- I got a bunch of errors relating to semaphors. This sounds like
  [haskell/cabal#9993](https://github.com/haskell/cabal/issues/9993) (which has
  since been fixed), which triggered when cabal and ghc were using incompatible
  `libc` implementations. (Prototypically `glibc` versus `musl`, but maybe
  different versions of the same one could cause the problem.) In my case:

  - `cabal` is provided by `ghcup`. It's statically linked, and I think that
    means it's probably using `musl`.
  - `ghc` was variously from `ghcup` or from my own compilation, but in both
    cases dynamically linked. I have `glibc` on my system.

  Maybe this means `cabal` from `ghcup` could only use semaphors when someone's
  system libc is `musl`?

  `--cabal-option=--semaphore` was hardcoded into the `run-ci` shell script, so
  I edited it to remove that.

- I couldn't figure out how to test just my changes to linear-generics. The docs
  say "Build/test as normal, e.g. `cabal build doctest`". Unclear what folder to
  run that in. I tried that both in the root `head.hackage` folder and the
  `packages/linear-generics-0.2.3` folder, passing `-w /path/to/ghc-9.14`. But
  this version of linear-generics claims not to support template-haskell >=
  2.22, i.e. GHC >= 9.10. So... does head.hackage already have patches for this
  package that `scripts/patch-tool unpack` didn't apply? Does `run-ci` ignore
  version bounds of dependencies?

  So my process ended up being:

  * Patch the library.
  * Run `scripts/patch-tool update-patches`.
  * Run `rm -r ci/run; GHC=... ONLY_PACKAGES=linear-generics ./run-ci`, which
    even though it's a single package still takes a few minutes and puts a lot
    of text in the scrollback after the actual failure.
  * Repeat until the package builds with both GHCs.
  * Rerun full CI, and if there'd been any new failing packages I'd have had to
    repeat for them. (Fixing one package can reveal new failures, in packages
    depending on the previously failing one.)

- CI failed after I submitted the PR, but my impression was that was unrelated
  and expected, so (after a quick look at the output) I ignored it. After a few
  days the PR got merged, and then the next time I pushed to my GHC branch, it
  passed CI.

### Munihac

I went to Munihac in October 2024 to see if I could get more people to work on
this with me. Aras Ergus helped with a commit, but I didn't get as much interest
as I'd hoped. Munihac was also a lot less social than Zurihac, I didn't hang out
with other attendees outside the conference. I don't regret going, but probably
wouldn't go again unless I had specific plans to collaborate with someone there.
