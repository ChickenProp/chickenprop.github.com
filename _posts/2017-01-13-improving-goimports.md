---
layout: post
title: Improving goimports
tags: [software]
comments: true
---

*Epistemic status: Pure dilettantism. I have never used Go. This might make me unqualified to say what I'm about to say. But it's okay, because I use the word "seems" a lot.*

In Go, if you have an unused import, your program fails to compile. This has made a lot of people mildly annoyed and been sometimes regarded as a bad idea, but not universally.

The devs [decline](https://golang.org/doc/faq#unused_variables_and_imports) to add a compiler flag to change this behaviour, "because compiler options should not affect the semantics of the language and because the Go compiler does not report warnings, only errors that prevent compilation". This strikes me as reasonable, if not the decision I personally would make.

Instead, they suggest this pattern:

```go
import "unused"

// This declaration marks the import as used by referencing an
// item from the package.
var _ = unused.Item  // TODO: Delete before committing!
```

\- that is, add a line of code to trick the compiler into thinking that you're using the import, even though you're not. (Unless you forget to delete the trick line, which the compiler won't verify for you.)

This does not strike me as a very good substitute. With a compiler flag, I could turn it on while debugging and turn it off for production to make sure I had no unused imports. I could use a commit hook to keep unused imports out of the repository. By tricking the compiler, there's no particularly easy way to do this. (I suppose I could put the string "FAKEIMPORT" is a comment on those lines, and grep for that string. This is still not a great solution.)

I also refer to the devs' opinion that "if it's worth complaining about, it's worth fixing in the code. (And if it's not worth fixing, it's not worth mentioning.)" I claim that there's no fundamental difference between

```go
import unused
```

and

```go
import unused
var _ = unused.Item
```

Neither affects the semantics of the program, if we ignore that the first one doesn't compile[^semantics]. If one is worth complaining about, so is the other. But the devs are sending mixed signals. It seems the first is worth complaining about, because the compiler complains. But it seems the second is not, because the devs recommend it. This should be a sign that something about this whole situation is less than ideal[^clarify].

(For myself, I would say that both are worth complaining about in production, and neither is worth complaining about when debugging. But the trick works equally well in both instances.)

There is another solution, in the form of a tool called [`goimports`](https://godoc.org/golang.org/x/tools/cmd/goimports). The idea is that you don't write imports at all. If you have a symbol that isn't imported, it searches your filesystem for an appropriate package and adds an import line. If you have an unused import, it deletes it.

But [word on the street](https://news.ycombinator.com/item?id=12208242) is that some names are ambiguous, supplied by multiple packages, and `goimports` has no way to choose which one you mean. So if you comment out a line, and then uncomment it, `goimports` might add back a different import than the one you originally used. This, too, seems less than ideal.

---

All of which is to say: although I don't use Go, it seems to me that Go has a problem, and that the existing solutions aren't perfect.

I propose a new solution, which could be implemented as two new modes for `goimports` to run in or as one or two completely new tools.

In the first mode, this tool acts like `goimports`, but more conservatively. Instead of removing unused imports, it merely comments them out. And instead of searching your filesystem for packages, it merely searches your comment lines, and uncomments them if there's a match.

So if you're debugging, and comment out the only use of a package, this tool will comment out the import for you. When you uncomment that use, the import will be added back in, but without the ambiguous naming problem. At no point do you have to trick the compiler, so you don't have to remember to stop tricking the compiler.

In the second mode, this tool checks for commented out import lines, and tells you whether it found any (or optionally deletes them). It can be called in commit hooks, to prevent such lines from cluttering up a repository.

This seems to me like it would be an improvement on the status quo.

[^semantics]: At least, they don't look like they do. Not knowing Go, it's conceivable that they could. If the second can have effects, then the devs' recommendation seems particularly bad. In that case, if a `var _ = unused.Item` line shows up in a codebase, it's *probably* a mistake - but you can't be sure without checking, which takes much longer.

[^clarify]: I want to clarify three things. First, I do not think the devs are wrong to recommend using this trick. Second, I do not think the second version is just as bad as the first. The second version has a more obvious smell, which is valuable, because bad code that smells bad is less bad than bad code that smells good. Third, I said the situation is *less than ideal*, and that's what I meant. I do not think the situation is terrible.
