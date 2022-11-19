---
layout: post
title: Silly Things to do with Shebang Lines
tags: [software]
comments: true
---
*(Fri, 6 Dec 2013: Importing this post from its [original home as a gist](https://gist.github.com/ChickenProp/492976).)*

The recent post on Hacker News about [#! semantics](http://news.ycombinator.com/item?id=1536776) surprised me. I had always assumed that a shebang line like

    #! /usr/bin/prog -a -b

Would be equivalent to calling

    $ /usr/bin/prog -a -b <file>

\- but instead, it's

    $ /usr/bin/prog '-a -b' <file>

This could only surprise me because I hadn't found out the hard way, so maybe it's not a big deal. Most scripts that I write don't have even a single argument on the shebang line. Most of the rest are Perl scripts, and `perl` is clever when it comes to parsing a single argument that looks like multiple arguments:

    $ echo hi there | perl '-a -n -l -e print $F[0]'
    hi

But this behaviour does have consequences, especially with the use of higher-order commands such as `sudo`, `nice` and `env`. For example, the following shebang lines will not work as intended:

    #! /usr/bin/sudo -u phil sh
    #! /usr/bin/nice -n 19 sh
    #! /usr/bin/env perl -n

(Scripts using `sudo` and `nice` in a shebang seem unlikely to be distributed, but might find use in site-local maintenance scripts. `env` can be used to make a script more portable, in case a program isn't in a consistent location across systems.)

So I got to thinking about a program that would act like `env` for this purpose, but splitting its arguments on whitespace, or even doing full shell-like parsing of quotes.

Of course, such a program already exists: its name is shell. `sh` accepts the `-c` option to pass a shell expression on the command line. If this expression comes from a shebang line, word-splitting will be performed just like when typing directly into a shell. As a bonus (arguably), you even get to use things like pipelines, output redirection, shell built-in commands, and forking to the background, all in the shebang line of a script.

There is one downside: normally with a shebang line you can think of the script name and any arguments as being implicitly appended. This no longer holds: `sh -c` takes an expression, not a program name, and expressions don't take arguments in the same way that programs do. Instead you need to access these arguments through shell variables `$0` through `$9`, `$*` and `$@`.

Alas, my first tests failed. It seems that `-c` requires its argument to be, well, a separate argument, so it's not much use with a shebang. (This is the case when `sh` is linked to Bash. Perhaps other shells are different, but if it doesn't work in Bash's `sh`-emulation mode, it probably can't be considered portable.)

So I went ahead and wrote a small script to get this behaviour. I even improved on what I could have done with `sh -c`: by default the script name and arguments are implicitly appended, but passing `-c` at the start of the first argument disables this.

I named this script `/usr/bin/cmd`, so for example the following shebang lines are now possible, and do what you would expect:

    #! /usr/bin/cmd sudo -u phil sh
    #! /usr/bin/cmd nice -n 19 sh
    #! /usr/bin/cmd perl -n

But you can also do things like

    #! /usr/bin/cmd grep -v '^#' | perl

to strip comments from the input before you process it. Or perhaps

    #! /usr/bin/cmd -c perl "$0" | xargs grep "$@"

to generate a list of filenames in perl and search them for a pattern given on the command line. On a similar note,

    #! /usr/bin/cmd -c perl "$0" "$@" | xgraph -nl -m &

might save having a separate file just to pipe the output of a perl script into xgraph.

I have a lisp program which expects an S-expression as input, but I can use

    #! /usr/bin/cmd (echo \(&&perl -lne'chomp,print"($_)"'&&echo \)) | sbcl --script

and now it expects plain text. (It could be cleaner, but I wanted to keep it less than 80 characters, and semicolons don't interact well with parentheses and emacs' paredit-mode. This example is probably a little more extreme than is sensible.)

There are also some pitfalls to `cmd`. If you have a system which *does* split shebang lines, I think normal behaviour will still work, but anything fancy - any use of `-c`, or shell processing - will fail. I don't think it would even be possible to port, unless there's some way to tell where the shebang arguments stop and the command-line arguments begin. (You could work this out in most cases by checking which argument names an executable file with `cmd` on the shebang, but that seems fragile.)

You need to be careful in `-c` mode to quote properly. Otherwise it will seem to work, but break mysteriously when an argument contains a literal space or wildcard. I think `"$0"` and `"$@"` are the constructs you want in almost all cases: everything else I've tried fails, and I haven't found anywhere that these fail. (Perhaps an option to `cmd` which would cause it to replace `%` or something with `"$0" "$@"` would be a good idea.)

If you want to be portable, you also need to worry about the length of your shebang lines. 127 bytes seem to be accepted on all modern systems, but I'll admit that I don't recognise (except perhaps in passing) many of the names in the originally linked article. (But if you want to be portable, you also want to wait until `cmd` is installed as standard on most systems. This might take a while.)

One pitfall that seems to have been avoided: I was worried that `perl` (which performs its own parsing of the shebang line) would be too clever for `cmd`, and recognise switches intended for programs later in a pipeline. This doesn't seem to happen:

    #!/usr/bin/cmd -c perl "$0"; echo -l
    print "hi";

produces output "hi-l", as intended. But I don't know exactly what rules `perl` uses, so there may be edge cases.

And I'm sure there are problems that I haven't anticipated. Which is the worst kind of problem.

Ultimately, I'm not sure how much use `cmd` will be. But until a few days ago, I don't think I'd ever thought about using a shell script in a shebang line, so I guess there's territory yet to explore. I'd be interested in hearing more ideas on  the subject.

If you're interested, `cmd` can be found at <http://github.com/ChickenProp/cmd>.
