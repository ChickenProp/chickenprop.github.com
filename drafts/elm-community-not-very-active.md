---
title: 'The Elm community is not "very active"'
layout: draft
---

I sometimes see people describe the Elm community as "very active". For example:

* [Elmcraft says](https://elmcraft.org/lore/elm-core-development) "The
Elm community is very active."
* ["Is Elm dead?" says](https://iselmdead.info/) "the community is more active than ever." (I guess that's compatible with "but still not very active", but, well, subtext.)
* [Some /r/elm commenter says](https://www.reddit.com/r/elm/comments/1g27p6a/where_is_the_elmcompiler_being_developed/lrm1pgq/) "The community is very active and productive." (They later clarify: "It's very active compared to similar projects. Tight focus, feature complete. People tend to compare it to dissimilar projects.")

Is this true? Let's get some statistics, including historical ones, and see what comes up.

I think all this data was collected on October 28 2024. I'm splitting things out by year, so we can roughly extrapolate to the end of 2024 by multiplying numbers by 1.2.

### Subreddit

I could export 951 posts from reddit. (That's a weird number; I suspect it means there were 49 posts I couldn't see.) The oldest were in December 2019, which means I have about 4 5/6 years of data. In a given calendar year, I can easily count: how many posts were there? And how many comments were there, on posts made in that calendar year? (So a comment in January 2022 on a post from December 2021, would be counted for 2021.)

| Year                | Posts | Comments |
|---------------------|-------|----------|
| 2020                | 296   | 2156     |
| 2021                | 236   | 1339     |
| 2022                | 215   | 1074     |
| 2023                | 132   | 639      |
| 2024 (extrapolated) | 76    | 505      |
| 2024 (raw)          | 63    | 421      |

By either measure, 2024 has about a quarter of 2020 activity levels.

### Discourse

I got a list of every topic on the discourse, with its creation date, "last updated" date (probably date of last reply in most cases), number of replies and number of views. The first post was in November 2017.

| Year                | Posts (C) | Replies (C) | Views (C) | Posts (U) | Replies (U) | Views (U) |
|---------------------|-----------|-------------|-----------|-----------|-------------|-----------|
| 2017                | 46        | 366         | 90830     | 29        | 151         | 46081     |
| 2018                | 819       | 5273        | 1634539   | 817       | 5284        | 1617704   |
| 2019                | 685       | 4437        | 1113453   | 695       | 4488        | 1137001   |
| 2020                | 610       | 4104        | 882214    | 613       | 4201        | 908361    |
| 2021                | 482       | 3502        | 603199    | 485       | 3528        | 608075    |
| 2022                | 332       | 1698        | 336095    | 329       | 1548        | 319918    |
| 2023                | 294       | 1544        | 221806    | 298       | 1711        | 243834    |
| 2024 (extrapolated) | 224       | 1422        | 115503    | 227       | 1438        | 116898    |
| 2024 (raw)          | 187       | 1185        | 96253     | 189       | 1198        | 97415     |

The "C" columns count according to a post's creation date, and the "U" columns count by "last updated" date.

So posts and replies have fallen to about 35% of 2020 levels. Views have fallen to about 15%.

### Package releases

For every package listed on https://package.elm-lang.org/, I got the release dates of all its versions.[^claude] So we can also ask how frequently packages are getting released, and we can break it up into initial/major/minor/patch updates.

[^claude]: Irrelevant aside, but I think this and the previous section were the first and second times I tried to get an LLM to write code for me. I used Claude. It took some back and forth, due to a combination of bugs, unclear specifications, and me occasionally changing my mind. But overall it worked very well.

My understanding is: if a package has any version compatible with 0.19, then every version of that package is listed, including ones not compatible with 0.19. If not it's not listed at all. So numbers before 2019 are suspect (0.19 was released in August 2018).

| Year                | Total | Initial | Major | Minor | Patch |
|---------------------|-------|---------|-------|-------|-------|
| 2014                | 1     | 1       | 0     | 0     | 0     |
| 2015                | 130   | 24      | 28    | 31    | 47    |
| 2016                | 666   | 102     | 137   | 145   | 282   |
| 2017                | 852   | 170     | 147   | 208   | 327   |
| 2018                | 1897  | 320     | 432   | 337   | 808   |
| 2019                | 1846  | 343     | 321   | 373   | 809   |
| 2020                | 1669  | 288     | 343   | 366   | 672   |
| 2021                | 1703  | 225     | 385   | 359   | 734   |
| 2022                | 1235  | 175     | 277   | 289   | 494   |
| 2023                | 1016  | 155     | 223   | 255   | 383   |
| 2024 (extrapolated) | 866   | 137     | 167   | 204   | 359   |
| 2024 (raw)          | 722   | 114     | 139   | 170   | 299   |

Package releases have declined by about half since 2020. Initial (0.48x) and major (0.49x) releases have gone down slightly faster than minor (0.56x) and patch (0.53x) ones, which might mean something or might just be noise.

### Where else should we look?

The [official community page](https://elm-lang.org/community) gives a few places someone might try to get started. The discourse and subreddit are included. Looking at the others:

* The [twitter](https://twitter.com/elmlang) has had two posts in 2024, both in May.
* [Elm weekly](https://www.elmweekly.nl/), from a quick glance, seems to have had more-or-less weekly posts going back many years. Kudos!
* I once joined the [slack](https://elm-lang.org/community/slack) but I don't know how to access it any more, so I can't see how active it is. Even if I could, I dunno if I could see how active it used to be.
* I don't feel like trying to figure out anything in depth from [meetup](https://www.meetup.com/topics/elm-programming/all/). I briefly note that I'm given a list of "All Elm Meetup groups", which has six entries, of which [exactly one](https://www.meetup.com/elm-gothenburg/) appears to be an Elm meetup group.
* I'm not sure what this [ElmBridge](https://github.com/elmbridge) thing is.

For things not linked from there:

* I'm aware that [Elm Camp](https://elm.camp/elm-camp-archive) has run twice now, in 2023 and 2024, and is planning 2025.
* There's an [Elm online meetup](https://meetdown.app/group/10561/Elm-Online-Meetup) which lately seems to meet for approximately four hours a year.
* There are [nine other Elm meetups](https://meetdown.app/search/elm) listed on that site. Most have had no meetups ever; none of them have had more than one in 2024.
* The [Elm radio](https://elm-radio.com/) podcast hasn't released an episode in 2024. [Elm town](https://elm.town/) seems roughly monthly right now.
* [hnhiring.com](https://hnhiring.com/trends?technologies=elm) shows generally 0-1 Elm jobs/month since 2023. There was also a dry spell from April 2019 to November 2020, but it's clearly lower right now than in 2018, 2021 and 2022.
* [Elmcraft](https://elmcraft.org/) is a website that I think is trying to be a community hub or something? Other than linking to Elm Weekly and the podcasts, it has a "featured article" (from April) and "latest videos" (most recently from 2023).
* How many long-form articles are being written about Elm? Not sure if there's an easy way to get stats on this.

### Summary

I do not think the Elm community is "very active" by most reasonable standards. For example:

* I think that if someone asks me for a "very active" programming language community they can join, and I point them at the Elm community, they will be disappointed.
* I think that if I were to look for an Elm job, I would struggle to find people who are hiring.
* I couldn't find a single Elm meetup that currently runs anywhere close to monthly, either online or anywhere in the world.
* It seems like I could read literally every comment and post written on the two main public-facing Elm forums, in about ten minutes a day. If I also wanted to read the long-form articles, when those are linked... my guess is still under twenty minutes?

If you think you have a reasonable standard by which the Elm community counts as "very active", by all means say so.[^similar]

[^similar]: But I'm not very impressed by the "similar projects" thing from before. ("It's very active compared to similar projects. Tight focus, feature complete. People tend to compare it to dissimilar projects.") Like, I might choose which of Elm, Haskell or Javascript I should learn, or start a project in or something. And then I might compare the activity levels of their communities, because that's likely to be decision-relevant for me. If you don't think I should do that, why not? What other projects should I compare Elm's community to instead, and why? What useful information am I hoping to learn?

I think the idea that the Elm community is "more active than ever" is blatantly false. (That line was added [in January 2022](https://github.com/sylbru/is-elm-dead/commit/4d23790b00f6b2ec86caaaeb3895f92d4168d4d2), at which point it might have been defensible. But it hasn't been removed in almost three years of shrinking, while the surrounding text has been edited multiple times.)

To be clear, none of this is intended to reflect on Elm as a language, or on the quality of its community, or anything else. I do have other frustrations, which I may or may not air at some point. But here I just intend to address the question: is it reasonable to describe the Elm community as "very active"?

(I do get the vibe that the Elm community could be reasonably described as "passionate", and that that can somewhat make up for a lack of activity. But it's not the same thing.)
