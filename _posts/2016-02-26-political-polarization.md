---
layout: post
title: "Political Polarization in the US House of Representatives"
---
I've created an interactive graph of <a href="http://bl.ocks.org/ChickenProp/raw/9dd807b7a14f7b797421/">historical levels of political polarization in the US House of Representatives</a>. It would be tricky to embed in this blog, so I'm only linking it. Summary:

> The x-axis on this graph is based on [DW-NOMINATE](https://en.wikipedia.org/wiki/NOMINATE_%28scaling_method%29) left-right scores of each member of each U.S. House of Representatives from 1865 to 2015. This uses a member's voting record to measure the direction and extremity of their political views, regardless of party affiliation.
>
> If a member's score on this axis is known, it's possible to predict their vote on any given issue with high confidence, given no other information about the member. Members whose votes are typically left-aligned receive negative scores, while members whose votes are typically right-aligned receive positive scores.
>
> (However, see [The Thin Blue Line That Stays Strangely Horizontal](http://slatestarcodex.com/2013/09/21/the-thin-blue-line-that-stays-bizarrely-horizontal/), which questions the validity of DW-NOMINATE.)

Background: I made this last year for a [Udacity](https://en.wikipedia.org/wiki/Udacity) course, "Data Visualization and D3.js". I needed to submit a visualization for marking, and this was my submission. I'm grateful for feedback provided by Udacity and by some of my friends. Without that, the result would certainly have been worse.

The source is [available on GitHub](https://github.com/ChickenProp/dwnom-interactive), including datasets and some python scripts I used to process them. The README also documents some of the design history.

I'm aware of one bug: in firefox (38.6.1 on linux), the legend appears to display the 5-95 and 25-75 percentile boxes identically. They're implemented as rects with `fill-opacity: 0.3`: the 25-75 boxes have two of these rects on top of each other. This is also how the paths on the graph itself are colored.

I assume there are other bugs.
