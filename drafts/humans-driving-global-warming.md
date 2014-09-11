---
layout: draft
title: 'Is there "99.999% certainty humans are driving global warmning"?'
---
([Spoiler alert](http://en.wikipedia.org/wiki/Betteridge%27s_law_of_headlines): no. But it's not as bad as I would have guessed.)

I'm definitely not a climate scientist. I think I'm more skeptical than most of my peers about AGW, for reasons that have nothing to do with thinking that I understand climate science, and which aren't relevant here.

But I do know something about statistics, and when [reddit tells me](http://www.reddit.com/r/science/comments/2ff60m/new_study_concludes_that_there_is_99999_certainty/) that a new study shows [99.999% certainty that humans are driving global warming](http://theconversation.com/99-999-certainty-humans-are-driving-global-warming-new-study-29911), my potential-bullshit detector goes PING-PING-PING.

PING! My impression of the general quality of science reporting is somewhere between "atrocious" and "depressing", so I think there's a good chance that the article is misrepresenting the study.

PING! And I remember that a lot of scientists are not statisticians, and that there's a good chance they made a mistake in the paper.

PING! Something else I think of is the notion of [confidence levels inside and outside an argument](http://lesswrong.com/lw/3be/confidence_levels_inside_and_outside_an_argument/). Even if the study does make the 99.999% claim, and it contains no internal mathematical or statistical errors, it might not be using a model that corresponds to reality. (The difference between this PING and the previous PING is that here, the scientists may be doing correct science, but they're doing it on flawed premises. In the other PING, the premises might be correct, but the science is bad.)

So here are three potential ways in which the claim might be bullshit. They seem pretty exhaustive. Either the premises are wrong - or the inferences are wrong - or the reporting misrepresents the conclusion - or the reporting is correct.

So let's take them one at a time.

### Bad reporting?

I'm surprised to discover that the linked article was actually written by the authors of the paper. That's a good sign. But reading closely, "driving" is an exaggeration.

The article contains this passage:

> The 2013 Intergovernmental Panel on Climate Change Fifth Assessment Report provided an expert consensus that:

> > It is extremely likely [defined as 95-100% certainty] that more than half of the observed increase in global average surface temperature from 1951 to 2010 was caused by the anthropogenic [human-caused] increase in greenhouse gas concentrations and other anthropogenic forcings together.

The latter quote can fairly be read as, "it is extremely likely that humans are driving global warming". But that conclusion comes from an expert consensus, not the paper being reported on. When the authors talk about their own paper, they use weaker phrasing:

> global average temperature over the past 60 years would [not] have been as high without human-caused greenhouse gas emissions

> objective assessment linking global temperature increases to human activity

> humans are contributing to significant changes in our climate

*Contributing* and *driving* are very different. This is a small, but fairly forgivable, amount of bullshit.

### Bad science?

It turns out that the [actual paper](http://www.sciencedirect.com/science/article/pii/S2212096314000163) is open-access. That's awesome! And it's only twelve pages long, with lots of tables and pretty graphs (and a few ugly graphs).

I said above that I know something about statistics. I do not know enough about statistics to sensibly evaluate this paper, but I can make a few comments.

The authors describe their method thus:

> We developed a statistical model that related global temperature to various well-known drivers of temperature variation, including El Niño, solar radiation, volcanic aerosols and greenhouse gas concentrations. We tested it to make sure it worked on the historical record and then re-ran it with and without the human influence of greenhouse gas emissions.

More precisely, their model is the sum of a linear regression and an [autoregressive moving-average model](http://en.wikipedia.org/wiki/Autoregressive%E2%80%93moving-average_model). I haven't encountered ARMA models before, but it looks like the factors taken into account are:

1. The factors listed above:

  - **f(eCO<sub>2</sub>)** (equivalent carbon dioxide) combines greenhouse gasses, aerosols and particulates into a single number. I guess this number is meant to be something like, "if we removed all the greenhouse gases and stuff and replaced them with this amount of CO<sub>2</sub>, then <some relevant factor like the amount of heat sent back to Earth by the atmosphere> would be conserved". *f* is a logarithmic function, because apparently that's what the relationship in question looks like.

  - **SOI** (southern oscillation index) is [this thing](http://en.wikipedia.org/wiki/El_Ni%C3%B1o_Southern_Oscillation).

  - **TSI** (total solar irradiance) measures how much sunlight the Earth's atmosphere receives.

  - **VOLRF** (volcanic stratospheric aerosol radiative forcing) 

2. The difference between "the previous month's temperature", and "the temperature that would have been predicted if we modelled it with only (1)". (This is the autoregressive part of the ARMA model.)

3. White noise, uncorrelated month-on-month.

4. The white noise from (3) that went into the calculations 1, 2, 12 and 24 months ago. (But not the additional white noise from (4) that went into those calculations.) (This is the moving-average part of the ARMA model.)
