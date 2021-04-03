---
title: "A command-line grammar of graphics"
layout: post
lw_xpost: true
external_comments:
  - name: LessWrong
    url: https://lesswrong.com/posts/cs3GK3BJteLETyucu/a-command-line-grammar-of-graphics
---
Sometimes I'm at my command prompt and I want to draw a graph.

Problem: I don't know [gnuplot](https://en.wikipedia.org/wiki/Gnuplot). Also, there's a couple things about it that bug me, and make me not enthusiastic about learning it.

One is that it seems not really designed for that purpose. It implements a whole language, and the way to use it for one-off commands is just to write a short script and put it in quotes.

The other is its whole paradigm. At some point in the distant past I discovered [ggplot2](https://en.wikipedia.org/wiki/Ggplot2), and since then I've been basically convinced that the "grammar of graphics" paradigm is the One True Way to do graphs, and everything else seems substandard. No offense, gnuplot, it's just... you're trying to be a graphing library, and I want you to be a graphing library that *also* adheres to my abstract philosophical notions of [what a graphing library should be](https://en.wikipedia.org/wiki/No_true_Scotsman).

If you're not familiar with the grammar of graphics, I'd summarize it as: you build up a graph out of individual components. If you want a scatter plot, you use the "draw points" component. If you want a line graph, you use the "draw line segments" component. If you want a line graph with the points emphasized, you use both of those components. Want to add a bar chart on top of that too? Easy, just add the "draw bars" component. Want a smoothed curve with confidence intervals? There's a "smooth this data" component, and some clever (but customizable) system that feeds the output of that into the "draw a line graph" and "draw a ribbon" components. [Here's a gallery](https://www.r-graph-gallery.com/ggplot2-package.html) of things it can do

So, rather than adapt myself to the world, I've tried to adapt the world to myself.

There's a python implementation of the paradigm, called [plotnine](https://plotnine.readthedocs.io/en/stable/).[^other-ggs] (It has its own [gallery](https://plotnine.readthedocs.io/en/stable/gallery.html).) And now I've written a command-line interface to plotnine.

It's not as powerful as it plausibly could be. But it's pretty powerful[^power], and if I stop developing now I might find it fully satisfies my needs in future. For example, I took a [dataset](https://github.com/owid/covid-19-data/tree/master/public/data/) of covid cases-per-capita timeseries for multiple countries. Then both of these graphs came from the same input file, only manipulated by grep to restrict to twelve countries:

<div style="display: flex">
<a href="https://raw.githubusercontent.com/ChickenProp/p9-cli/41f856cb159f96d6e809d85ac77e99e3bc5bd7cd/examples/time-series.png"><img src="https://raw.githubusercontent.com/ChickenProp/p9-cli/41f856cb159f96d6e809d85ac77e99e3bc5bd7cd/examples/time-series.png" width="300" height="186" alt="A time series graph"></a>
<a href="https://raw.githubusercontent.com/ChickenProp/p9-cli/41f856cb159f96d6e809d85ac77e99e3bc5bd7cd/examples/change-in-rank.png"><img src="https://raw.githubusercontent.com/ChickenProp/p9-cli/41f856cb159f96d6e809d85ac77e99e3bc5bd7cd/examples/change-in-rank.png" width="300" height="429" alt="A change in rank graph"></a>
</div>

(The second one isn't a type of graph that needs to be implemented specifically. It's just a combination of the components "draw points", "draw line segments" and "draw text".)

Now admittedly, I had to use a pretty awful hack to get that second one to work, and it wouldn't shock me if that hack stops working in future. On the other hand, I deliberately tried to see what I could do without manipulating the data itself. If I wasn't doing that, I would have used a tool that I love named [q](https://github.com/harelba/q), which lets you run sql commands on csv files, and then there'd be no need for the awful hack.

Anyway. If you're interested, you can [check it out on github](https://github.com/ChickenProp/p9-cli). There's documentation there, and examples, including the awful hack I had to use in the above graph. To set expectations: I don't anticipate doing more work on this unprompted, in the near future. But if people are interested enough to engage, requesting features or contributing patches or whatever, I do anticipate engaging back. I don't want to take on significant [responsibility](http://reasonableapproximation.net/2020/04/13/in-my-culture-responsibility-oss.html), and if this ever became a large active project I'd probably want to hand it over to someone else, but I don't really see that happening.

[^other-ggs]: I'm aware of two other things that could plausibly be called python implementations of the grammar of graphics, but on reflection I exclude them both.

    The first is a package that used to literally be called ggplot. The creator of the original ggplot2 (if there was a prior non-2 ggplot, I can't find it) pointed out that the name was confusing, so it got renamed to [ggpy](http://yhat.github.io/ggpy/), and now it's defunct anyway. But I don't count it, because under the hood it didn't have the grammar thing going on. It had the surface appearance of something a lot like ggplot2, but it didn't have the same flexibility and power.

    The other is [one](https://github.com/ChickenProp/gragrapy) I started writing myself. I exclude it for being nowhere near complete; I abandoned it when I discovered that plotnine existed and was further along. I did think mine had the nicer API - I was trying to make it more pythonic, where plotnine was trying to be a more direct translation of ggplot2. But that hardly seemed to matter much, and if I really cared I could [implement](https://github.com/ChickenProp/gragrapy/tree/plotnine) my API on top of plotnine.

    I only remember two things plotnine was missing that I supported. One was the ability to map aesthetics simultaneously before and after the stat transform (ggplot2 only allows one or the other for each aesthetic). I'm not convinced that was actually helpful. Coincidentally, a few days ago plotnine 0.8.0 came out with [the same feature](https://plotnine.readthedocs.io/en/stable/generated/plotnine.mapping.stage.html), but more powerful because it supports after-scale too. The other was a rudimentary CLI, and now plotnine has one of those too.

[^power]: Most of this power, to be clear, comes from plotnine itself, from the grammar of graphics paradigm, and from python's scientific computing ecosystem. My own contribution is currently less than 250 lines of python; I may have used some design sense not to excessively *limit* the power available, but I didn't *provide* the power.
