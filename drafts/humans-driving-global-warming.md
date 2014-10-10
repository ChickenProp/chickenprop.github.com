---
layout: draft
title: 'Is there "99.999% certainty humans are driving global warmning"?'
---
([Spoiler alert](http://en.wikipedia.org/wiki/Betteridge%27s_law_of_headlines): no. But it's not as bad as I would have guessed.)

I'm definitely not a climate scientist. I think I'm more skeptical than most of my peers about AGW, for reasons that have nothing to do with thinking that I understand climate science, and which aren't relevant here.

But I do know something about statistics, and when [reddit tells me](http://www.reddit.com/r/science/comments/2ff60m/new_study_concludes_that_there_is_99999_certainty/) that a new study shows [99.999% certainty that humans are driving global warming](http://theconversation.com/99-999-certainty-humans-are-driving-global-warming-new-study-29911), my potential-bullshit detector goes PING-PING-PING.

PING! My impression of the general quality of science reporting is somewhere between "atrocious" and "depressing", so I think there's a good chance that the article is misrepresenting the study.

PING! And I remember that a lot of scientists are not statisticians, and that there's a good chance they made a mistake in the paper.

PING! Something else I think of is the notion of [confidence levels inside and outside an argument](http://lesswrong.com/lw/3be/confidence_levels_inside_and_outside_an_argument/). Even if the study does make the 99.999% claim, and it contains no internal mathematical or statistical errors, it might not be using a model that corresponds to reality. And even if it's not obvious how the model might differ from reality, we need to consider the possibility that there is a problem we don't see, and adjust our probability estimates accordingly. (The boundary between this PING and the previous PING is not necessarily well-defined.)

So here are three potential ways in which the claim might be bullshit. They seem pretty exhaustive. Either the premises are wrong - or the inferences are wrong - or the reporting misrepresents the conclusion - or the reporting is correct.

So let's take them one at a time.

### Bad reporting?

I'm surprised to discover that the linked article was actually written by the authors of the paper. That's a good sign. But reading closely, "driving" is an exaggeration.

The article contains this passage:

> The 2013 Intergovernmental Panel on Climate Change Fifth Assessment Report provided an expert consensus that:

> > It is extremely likely [defined as 95-100% certainty] that more than half of the observed increase in global average surface temperature from 1951 to 2010 was caused by the anthropogenic [human-caused] increase in greenhouse gas concentrations and other anthropogenic forcings together.

The latter quote can fairly be read as, "it is extremely likely that humans are driving global warming". But that conclusion comes from an expert consensus, not the paper being reported on. When the authors talk about their own paper, they use weaker phrasing:

> global average temperature over the past 60 years would [not] have been as high without human-caused greenhouse gas emissions

and

> objective assessment linking global temperature increases to human activity

and

> humans are contributing to significant changes in our climate

*Contributing* and *driving* are very different. This is a small, but fairly forgivable, amount of bullshit.

### Bad science?

It turns out that the [actual paper](http://www.sciencedirect.com/science/article/pii/S2212096314000163) is open-access. That's awesome! And it's only twelve pages long, with lots of tables and pretty graphs (and a few ugly graphs).

I said above that I know something about statistics. I do not know enough about statistics to sensibly evaluate this paper, but I can make a few comments.

The authors describe their method thus:

> We developed a statistical model that related global temperature to various well-known drivers of temperature variation, including El Niño, solar radiation, volcanic aerosols and greenhouse gas concentrations. We tested it to make sure it worked on the historical record and then re-ran it with and without the human influence of greenhouse gas emissions.

More precisely, their model is the sum of a linear regression and an [autoregressive moving-average model](http://en.wikipedia.org/wiki/Autoregressive%E2%80%93moving-average_model). I haven't encountered ARMA models before, but it looks like the factors taken into account are:

1. The factors listed above:
    - **f(eCO<sub>2</sub>)** (equivalent carbon dioxide) combines greenhouse gasses, aerosols and particulates into a single number. I guess this number is meant to be something like, "if we removed all the greenhouse gases and stuff and replaced them with this amount of CO<sub>2</sub>, then [[some relevant factor like the amount of heat sent back to Earth by the atmosphere]] would be conserved". *f* is a logarithmic function, because apparently that's what the relationship in question looks like.
    - **SOI** (southern oscillation index) is [this thing](http://en.wikipedia.org/wiki/El_Ni%C3%B1o_Southern_Oscillation).
    - **TSI** (total solar irradiance) measures how much sunlight the Earth's atmosphere receives.
    - **VOLRF** (volcanic stratospheric aerosol radiative forcing) measures the effect on global temperature from the stuff released by volcanic activity.
2. White noise, uncorrelated month-on-month.
3. The white noise from (2) that went into the calculations 1, 2, 12 and 24 months ago. (But not the additional white noise from (3) that went into those calculations.) (This is the moving-average part of the ARMA model.)
4. The factors (2), (3) and (4) that went into the previous month. (This is the autoregressive part of the ARMA model.)

I have no reason to think this is a bad model, and the authors spend some time justifying it. I don't feel particularly capable of evaluating their arguments.

Having developed the model, their approach is as follows: they run a simulation of the model over the time period (1882-2010), and count the largest number of consecutive months where temperature exceeds the mean 20th century average for that month. (I'm not sure whether they're comparing to actual 20th century averages, or simulated ones.) They also count the number of ten-year windows during which temperatures fell.

Then they do the same thing again, but removing the effects of eCO<sub>2</sub>. They do that by simply setting the regression parameter to zero.

They do both of these things lots of times, and compare the results. They find that with eCO<sub>2</sub> removed, there are far fewer consecutive hot months, and far more ten-year cooling periods.

Before I go into any depth on the results, some extra details that probably don't matter too much. Firstly, when they run a simulation of the model, they actually run two simulations. The first simulation is used to generate new parameter estimates, and those estimates are used to run the second simulation, which temperatures are taken from. I assume, but I'm not actually sure, that the new estimates are generated in the same way as the original ones, just using different data.

Secondly, they actually use two different sets of paramater estimates. One ("model B") was generated from the whole time series, the other ("model E") was generated from just the data from 1950 onwards. The parameters used in the models are identical, and the *values* of the parameters are very similar.

Thirdly, they actually use *three* different sets of parameter estimates. "Model F" uses almost the same parameters as models B and E, but it doesn't include a term for f(eCO<sub>2</sub>) and it was only trained on the data for 1882-1949. This gets very similar results as when you set that term to zero in models B and E, which is used to justify doing that.

So, the results:

> The chance of observing 304 consecutive months or more with temperature exceeding the 20th century average for the corresponding month is approximately 24.9 percent when eCO<sub>2</sub> forcing is included in Model B and 52.9 percent in Model E (Fig. 7a). When eCO<sub>2</sub> forcing is excluded from the simulations the probability of this occurring is less than 0.001 percent for both Models B and E. Under the scenario that climate like that observed from 1882 to 1949 had continued to 2010 (Model F, Table 3), the chance of observing the anomalous temperature event is also very small; only about 0.04 percent.

from which they conclude

> The results of our statistical analysis would suggest that it is highly likely (99.999 percent) that the 304 consecutive months of anomalously warm global temperatures to June 2010 is directly attributable to the accumulation of global greenhouse gases in the atmosphere.

*pingpingpingpingpingpingping*

You can't do this!

Okay, numerically it isn't totally awful, but this is an example of "getting a not-totally-wrong answer by a totally-wrong method".

Bayes 101:

    $$ { P(H_0|O) \over P(H_1|O) }
           = { P(H_0) \over P(H_1) } \cdot { P(O|H_0) \over P(O|H_1) } $$

One way that we might instantiate this formula is: `$H_0$` represents model B, and `$H_1$` represents model $B$ with the f(eCO<sub>2</sub>) parameter set to 0. (`$P(H_0)$` and `$P(H_1)$` represent how likely we think it is that these models accurately represent the real world.) $O$ is the observation of 304 or more consecutive warm months.

The conclusion appears to read: "`$P(O|H_1) < 10^{-5}$`, therefore `$P(H_0|O) > 1 - 10^{-5}$`". (At least, I assume this is the reasoning for the 99.999 percent figure, since they don't actually explain it.) This is not a valid inference.

What we actually get from the data is the Bayes factor,

    $$ { P(O|H_0) \over P(O|H_1) }, $$

where `$P(O|H_1)$` is "less than 0.001 percent" - I'm going to be unfair and round it to *exactly* 0.001 percent, or $0.00001$. (Hey, if it was much less than that, they would have picked a lower number to say it was less than.) And `$P(O|H_0)$` is "approximately 24.9 percent", or $0.249$. Then the Bayes factor comes out at $24900$.

If we assume that `$H_0$` and `$H_1$` are exhaustive and mutually exclusive (i.e. precisely one of them is true), then after a small amount of arithmetic we finish with

    $$ P(H_0|O) = { 24900 \over 24901 } \approx 0.99996 $$

in other words, using the numbers from the article, and doing slightly better math, **there is only 99.996 percent certainty that humans are driving global warming**. In your *face*, scientists!

Okay, yeah. Like I said, the actual conclusion wasn't totally wrong, but the method was.

(If instead of model B, we choose model E, then we get 99.998% certainty.)


---

(Notes that might enter the finished version in some form.)

What problems might there be?

One thing that seems a little sketchy is that data for f(eCO<sub>2</sub>) is only available yearly, but the simulation is run monthly. Monthly values were obatined by linear interpolation - which I interpret to mean something like, if f(eCO<sub>2</sub>) was 0 in 1910 and 12 in 1911, then they model it as being 0 in July 1910, 1 in August 1910, ..., 11 in June 1911, and 12 in July 1911. Given that f(eCO<sub>2</sub>) is basically
