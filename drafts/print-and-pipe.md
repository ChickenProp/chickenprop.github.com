---
title: "Unix pro tip: Print and pipe"
layout: draft
---
Sometimes you (or at least, I) want to run a command for its output, but also want to pipe it through another command. For example, see the results of a `find` but also count how many hits it got. I've sometimes lamented that there's no easy way to do this. But the other day I had a flash of insight and figured out how:

```sh
find . | tee /dev/stderr | wc -l
proc1 | tee /dev/stderr | proc2    # general case
```

(I'm pretty proud of this. I don't know if it's original to me, but I discovered it independently even if not.)

`tee` will print the output of `proc1` to both stdout and stderr. stderr goes to the terminal and stdout goes to `proc2`.

You can make it more convenient with an alias:

```sh
alias terr='tee /dev/stderr | '
find . | terr wc -l
```

(Putting a pipe in an alias seems to work in both zsh and bash.)

If you want to concatenate the streams, to pipe them to another process, you can use subshells:

```sh
proc1 | ( terr proc2 ) 2>&1 | proc3
```

but note that stderr output from `proc2` will also get sent to `proc3`, unless you send it somewhere else. I haven't yet thought of a use for this.

There are potential issues with buffering here. I'm not aware that `tee` makes any promises[^pun] about which order it writes the streams in. It's going to be interlacing them while it writes, so that it doesn't need to keep a whole copy in memory. So (if the input is large enough) `proc2` will be receiving input before it's finished being written to stderr, and might start *writing* output, and then the output streams can get interlaced.

For some values of `proc2`, commands which start printing before they've finished reading, this is inevitable. But I think useful `proc2`s are likely to be aggregators[^useful] - by which I mean, commands which can't do anything until they've finished reading all their input[^sponge]. In my tests so far, those have been safe, but that doesn't prove much.

We can do a more reliable check with `strace`:

```sh
find . | strace tee /dev/stderr | wc -l
```

By the looks of things, `tee` will read into a buffer, then write it to stdout (the pipe), then write it to the specified target (stderr, which goes to the terminal), and repeat to exhaustion. But the important thing is, it doesn't close any file descriptors until it's finished writing everything, and then it closes the target before it closes stdout. If this is consistent amongst `tee` implementations - and it seems sensible[^order] - then aggregators almost definitely won't interlace their output with the output from `proc1`. I don't want to say "definitely", because there might be other stuff going on that I haven't accounted for. But at any rate, `tee` will finish writing before the aggregator starts.

Anyway, I see this as being the sort of thing that you're likely use manually, not in an automated process. So if the output does get interlaced a little, it's probably not that big a deal.

[^pun]: Note how I didn't say *guaranTEEs*? You're welcome.
[^useful]: In fact, `wc` is the only `proc2` I can currently think of, that I expect to be regularly useful. (And then just piping through `cat -n` does something similar, but it's not ideal.) `numsum` or perhaps some other tools from [num-utils](http://freecode.com/projects/num-utils) could conceivably be handy from time to time.
[^sponge]: You can turn a non-aggregator into an aggregator with [moreutils](https://joeyh.name/code/moreutils/)' `sponge` command, which is like `cat` but reads all its input before writing anything.
[^order]: They could reasonably close their outputs in either order, which might make a difference. But I don't think it's usual for programs to explicitly close their std* streams, that gets taken care of by the surrounding infrastructure. So if `tee` explicitly closes its target, I'd expect that to happen before stdout gets closed.
