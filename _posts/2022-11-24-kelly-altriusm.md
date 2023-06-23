---
title: On Kelly and altruism
layout: post
tags: [rationality, math]
lw_xpost: true
external_comments:
  - name: LessWrong
    url: https://lesswrong.com/posts/XnnfYrqaxqvirpxFX/on-kelly-and-altruism
---
*One-sentence summary: Kelly is not about optimizing a utility function; in general I recommend you either stop pretending you have one of those, or stop talking about Kelly.*

There was a [twitter thread](https://twitter.com/SBF_FTX/status/1337250686870831107) that triggered some confusion amongst myself and some other people in a group chat I'm in.[^author]

[^author]: The [author](https://en.wikipedia.org/wiki/Sam_Bankman-Fried) of the tweets is, as the saying goes, best known for other work. That other work is not relevant here.

The relevant tweets are these (I've omitted some):

> 3) Let’s say you were offered a coin flip.  75% it comes up heads, 25% it comes up tails; 1:1 payout.  How much would you risk?

> 4) There are a number of ways to approach this question, but to start: what do you want, in the first place?  What’s your utility function?

> 5) In other words--how cool would it be to make \\$10,000?  How about \\$1,000,000--is that 100 times as good?
>
> For most people the answer is ‘no, it’s more like 10 times as good’.  This is because of decreasing marginal utility of money.

> 8) One reasonable utility function here is U = log(W): approximating your happiness as logarithmic in your wealth.  That would mean going from \\$10k to \\$100k is worth about as much as going from \\$100k to \\$1m, which feels…. reasonable?
>
> (this is what the Kelly Criteria assumes)

> 9) So, if you have \\$100k, Kelly would suggest you risk half of it (\\$50k).  This is a lot!  But also 75% odds are good.

> 10) What about a wackier bet?  How about you only win 10% of the time, but if you do you get paid out 10,000x your bet size?  (For now, let’s assume you only get to do this bet once.)

> 11) Kelly suggests you only bet \\$10k: you’ll almost certainly lose.  And if you kept doing this much more than \\$10k at a time, you’d probably blow out.
>
> That this bet is great expected value; you win 1,000x your bet size, way better than the first one!  It’s just very risky.

> 12) In many cases I think \\$10k is a reasonable bet.  But I, personally, would do more.  I’d probably do more like \\$50k.
>
> Why?  Because ultimately my utility function isn’t really logarithmic.  It’s closer to linear.

> 13) Sure, I wouldn’t care to buy 10,000 new cars if I won the coinflip.  But I’m not spending my marginal money on cars anyway.  I’m donating it.
>
> And the scale of the world’s problems is…. Huge.

> 14) 400,000 people die of malaria each year.  It costs something like \\$5k to save one person from malaria, or \\$2b total per year.  So if you want to save lives in the developing world, you can blow \\$2b a year just on malaria.

> 15) And that’s just the start.  If you look at the scale of funds spent on diseases, global warming, emerging technological risk, animal welfare, nuclear warfare safety, etc., you get numbers reaching into the trillions.

> 16) So at the very least, you should be using that as your baseline: and kelly tells you that when the backdrop is trillions of dollars, there’s essentially no risk aversion on the scale of thousands or millions.

> 17) Put another way: if you’re maximizing EV(log(W+\\$1,000,000,000,000)) and W is much less than a trillion, this is very similar to just maximizing EV(W).

> 18) Does this mean you should be willing to accept a significant chance of failing to do much good sometimes?
>
> Yes, it does.  And that’s ok.  If it was the right play in EV, sometimes you win and sometimes you lose.

> 19) And more generally, if you look at everyone contributing to the cause as one portfolio--which is certainly true from the perspective of the child dying from malaria--they aren’t worried about who it was that funded their safety.

> 22) So given all that, why not bet all \\$100k?  Why only \\$50k?
>
> Because if you bet \\$100k and lose, you can never bet again.  And to the extent you think you have future ways to provide value that are contingent on having some amount of funding, it can be important to keep that.

The thing we were trying to figure out was, is his math right? And here's my current understanding of that matter.

### On Kelly

The first thing I'd say is, I think the way he talks about [Kelly](https://en.wikipedia.org/wiki/Kelly_criterion) here is confusing. My understanding is:

Under a certain betting framework, if you place bets that each maximize expected log-money, then you get (something good). See Appendix Ⅰ for the definition of the framework, if you want the technical details.

If you happen have a utility function, and that utility function increases logarithmically with money, then you maximize your expected utility while also getting (something good).

If you happen to have a utility function, and that utility function increases linearly with money - or something else other than logarithmically - then you have to choose between maximizing your expected utility and getting (something good). And by definition, you'd rather maximize your expected utility. (More likely: that's not your utility function. Even more likely: you don't have a utility function.)

(I don't think any human has a utility function.[^so-much-the-worse] I think it can be a useful shorthand to talk as though we do, sometimes. I think this is not one of those times. Especially not a utility function that can be expressed purely in terms of money.)

[^so-much-the-worse]: I think I've seen some people, who agree humans don't have utility functions, go on to say: "and so much the worse for utility functions! If humans don't have them we should find something more useful to talk about." My take is: "and so much the worse for humans! If we don't have utility functions we're missing out." But, that doesn't mean we have them.

The (something good) is that, over a long enough time, you'll almost certainly get more money than someone else who was offered the same bets as you and started with the same amount of money but regularly bet different amounts on them.

This is NOT the same thing as maximizing your average (AKA "expected") amount of money over time. "Almost certainly" hides a small number of outcomes that make a lot of difference to that calculation. Someone who repeatedly bets their entire bankroll will *on average* have more money than a Kelly bettor; it's just all concentrated in a single vanishingly unlikely branch where they're incredibly wealthy, and the rest of the time they have nothing. Someone who repeatedly bets more than Kelly but less than their entire bankroll, will *on average* have more than the Kelly bettor but less than the full-bankroll bettor; but still less than the Kelly bettor almost all the time, and very rarely much more.

It still sounds like a very good thing to me! Like, do I want to almost certainly be the richest peson in the room? Do I want to maximize my median payoff, *and* the 1st percentile and 99th percentile and in fact every percentile, *all at once*? Oh, and while I'm at it, maximize my most-likely payoff and minimize "the average time I'll take to reach any given amount of money much more than what I have now"? Yes please!

(Oh, also, I don't need to choose whether I'm getting that good thing for money or log-money or what. It's the same for any monotonically increasing function of money.)

Separately from that: yeah, I think going from \\$10k to \\$100k sounds about as good as going from \\$100k to \\$1m. So if I'm in a situation where it makes sense to pretend I have a utility function, then it's probably reasonable to pretend my supposed utility function is logarithmic in money.

So that's convenient. I dunno if it's a coincidence or what, but it's useful. If I tried to pretend my utility function was linear in money then I'd be sad about losing that good thing, and then it would be hard to keep pretending.

To me, Kelly is about getting that good thing. If you have a utility function, just place whatever bet size maximizes expected utility. If instead you want to get that good thing, Kelly tells you how to do that, under a certain betting framework. And the way to do that is to place bets that each maximize expected log-money.

If you have a utility function and it's proportional to log-money, then you'll happen to get the good thing; but far more important than that, will be the fact that you're maximizing expected log-money. If you have a utility function and it's different, and you bet accordingly, then a Kelly bettor will almost certainly be richer than you over time; but you're (for now) sitting on a bigger pile of expected utility, which is what you care about.

Or maybe you want to mix things up a bit. For example, you might care a bit more about your average returns, and a bit less about being the richest person in the room, than a Kelly bettor. Then you could bet something above the Kelly amount, but less than your full bankroll. You'll almost certainly end up with less than the Kelly bettor, but *on average* you'll still earn more than them thanks to unlikely branches.

I'm not sure what to call this good thing. I'm going to go with "rank-optimizing" one's bankroll, focusing on the "be the richest person in the room" part; though I worry that it suggests competing with other people, where really you're competing with counterfactual versions of yourself. See Appendix Ⅱ for an (admittedly flawed) technical definition of rank-optimization; also, I want to clarify a few things about it:

* It might be a meaningful concept in situations unlike the betting framework we're currently talking about.

* In some situations, different good things about rank-optimization might not all come together. You might need to choose between them.

* Similarly, in some situations, rank-optimization might not come from maximizing expected log-money. (When it doesn't, might one still have a utility function that's maximized in expectation by rank-optimizing one's bankroll? I think the answer is roughly "technically yes but basically no", see Appendix Ⅲ.)

### On the tweets

So in this lens, the author's argument seems confused. "My utility function is linear in money, so Kelly says" no it doesn't, if you have a utility function or if you're maximizing the expected value of anything then Kelly can go hang.

...but not everyone thinks about Kelly the same way I do, and I don't necessarily think that's wrong of them. So, what are some non-confused possibilities?

One is that the author has a utility function that's roughly linear in his own wealth. Or, more likely, *roughly values* money in a way that's roughly linear in his own wealth, such that rank-optimizing isn't optimizing according to his preferences. And then I think the argument basically goes through. If you want to maximize expected log of "money donated to charity", then yes, that will look a lot like maximizing expected "money you personally donate to charity", assuming you don't personally donate a significant fraction of it all. (If you want to maximize expected log of "money donated *effectively* to charity", that's a smaller pot.) This has nothing to do with Kelly, according to me.

Another is that the author wants to rank-optimize the amount of money donated to charity. In that case I think it doesn't matter that the backdrop is trillions of dollars. If he's acting alone, then to rank-optimize the total amount donated to charity, he should rank-optimize the amount he personally donates.

But here we come to the "everyone contributing to the cause" argument.

Suppose you have two people who each want to rank-optimize their own bankroll. Alice gets offered a handful of bets, and Kellies them. Bob gets offered a handful of bets, and Kellies them.

And now suppose instead they both want to rank-optimize their total bankroll. So they combine them into one. Whenever Alice gets a bet, she Kellies according to *their combined bankrolls*. Whenever Bob gets a bet, he Kellies according to *their combined bankrolls*. And in the end, their total bankroll will almost certainly be higher than the sum of the individual bankrolls, in the first case.

...Well, maybe. I think the value here doesn't come from sharing their money but from sharing their bets. I've assumed the combined bankroll gets all of the bets from either of the individual ones. That might not be the case - consider betting on a sports match. Ignoring transaction costs, it doesn't make a difference if one of them Kellies their combined bankroll, or each of them Kellies their individual bankrolls. "Each of them Kellies their combined bankroll" isn't an option in this framework, so teaming up doesn't help.

But I do think something like this, combined with reasonable assumptions about charity and how bets are found, suggests betting above Kelly. Like, maybe Alice and Bob don't want to literally combine their bankrolls, but they do trust each other pretty well and are willing to give or lend each other moderate amounts of money, and the two of them encounter different bets. Then I *think* that to rank-optimize their individual or combined bankrolls, each of them should probably be betting above Kelly.

Or maybe Alice doesn't encounter bets (or can't act on them or doesn't trust herself to evaluate them or...), but she does encounter Bob and Carol and Dennis and somewhat trusts all of them to be aligned with her values. Then if she gives each of them some money, and is willing to give them more in future if they lose money, I *think* that she wants them to make above-Kelly bets. (Just giving them more money to begin with might be more rank-optimal, but there might be practical reasons not to, like not having it yet.)

Does she want people to bet almost their entire bankrolls? Under strong assumptions, and if the total pool is big enough relative to the bettor... I'm not sure, but I think yes?

This relies on individual donors being small relative to the donor pool. When you're small, maximizing expected log of the pool size (which, in this framework, rank-optimizes the pool size) looks a lot like maximizing your own expected contributions linearly. When you're big, that's no longer the case.

It *doesn't* depend on the size of the problem you're trying to solve. That number just isn't an input to any of the relevant calculations, not that I've found. It might be relevant if you're thinking about diminishing marginal returns, but you don't need to think about those if you're rank-optimizing.

I'm not super confident about this part, so I'm leaving it out of the one-sentence summary. But I do think that rank-optimizing charity donations often means betting above Kelly.

### Conclusion

So was the author's math right? Man, I dunno. I'm inclined to say no; he was hand waving in almost the right directions, but I currently think that if he'd tried to formalize his hand waving he'd have made a key mistake. That being: I think that if you want to rank-optimize, the math says "sure, bet high right now, but slow down when you become a big part of the donor pool". I think maybe he thought it said "...but slow down when you get close to solving all the world's problems". It's not entirely clear from the tweets though, in part because he was using the word Kelly in a place where I think it didn't belong. Since I don't want to try comparing this theory to how he actually behaved in practice, I'll leave it there.

In any case I think *I* understand what's going on better than I used to. Kelly is not about optimizing a utility function.

### Appendix Ⅰ: betting framework

Throughout the post I've been assuming a particular "betting framework". What I mean by that is the sequence of bets that's offered and the strategies available to the bettor.

The framework in question is:

* You get offered bets.
* Each bet has a certain probability that you'll win; and a certain amount that it pays out if you win, multiplied by your wager.
* You can wager any amount from zero up to your entire current bankroll.
* If you lose, you lose your entire wager.
* You don't get offered another bet until your first has paid off.
* You keep on receiving bets, and the distribution of bets you receive doesn't change over time.

[Wikipedia's treatment](https://en.wikipedia.org/wiki/Kelly_criterion) relaxes the third and fourth conditions, but I think for my purposes, that complicates things.

### Appendix Ⅱ: technical definition

In Kelly's [original paper](https://www.princeton.edu/~wbialek/rome/refs/kelly_56.pdf), he defines the growth rate of a strategy \\( λ \\) as

<div>
\[ G(λ) = \lim_{n → ∞} {1 \over n} \log {V_n(λ) \over V_0(λ)} \]
</div>

<p>
where \( V_n(λ) \) is the bettor's portfolio after \( n \) steps. This is awkward because \( V_n(λ) \) is a random variable, so so is \( G(λ) \). But in the framework we're using, in the space of strategies "bet some fraction of our bankroll that depends on the parameters of the bet", \( G \) takes on some value with probability \( 1 \). Kelly betting maximizes that value. So we could try to define rank-optimization as finding the strategy that maximizes the growth rate.
</p>

<p>
I find this awkward and confusing, so here's a definition that I think will be equivalent for the framework we're using. A strategy \( λ \) is rank-optimal if for all strategies \( μ \),
</p>

<div>
\[ \lim_{n → ∞} P(V_n(λ) ≥ V_n(μ)) = 1. \]
</div>

(And we can also talk about a strategy being "equally rank-optimal" as or "more rank-optimal" than another, in the obvious ways. I'm pretty sure this will be a partial order in general, and I suspect a total order among strategy spaces we care about.)

<p>
I think this has both advantages and disadvantages over the definition based on growth rate. An advantage is that it works with super- or sub-exponential growth. (Subexponential growth like \( V_n = n \) has a growth rate of \( 0 \), so it's not preferred over \( V_n = 1 \). Superexponential growth like \( V_n = e^{e^n} \) has infinite growth rate which is awkward.)
</p>

<p>
A disadvantage is it doesn't work well with strategies that are equivalent in the long run but pay off at different times. (If we consider a coin toss game, neither of the strategies "call heads" and "call tails" will get a long-run advantage, so we can't use rank-optimality to compare them. The limit in the definition will approach \( {1 \over 2 } \).) I think this isn't a problem in the current betting framework, but I consider it a major flaw. Hopefully there's some neat way to fix it.
</p>

What I don't currently expect to see is a betting framework and space of strategies where

* We can calculate a growth rate for each strategy;
* Rank-optimality gives us a total order on strategies;
* There are strategies \\( λ, μ \\) with \\( G(λ) > G(μ) \\) but \\( μ \\) is more rank-optimal than \\( λ \\).

I wouldn't be totally shocked by that happening, math has been known to throw me some curveballs even in the days when I could call myself a mathematician. But it would surprise me a bit.

<p>
Given this definition, it's clear that a rank-optimal strategy maximizes every percentile of return. E.g. suppose \( λ \) is more rank-optimal than \( μ \), but the median of \( V_n(μ) \) is higher than the median of \( V_n(λ) \). Then we'd have \( P(V_n(μ) > V_n(λ)) ≥ {1 \over 4} \); so this can't hold in the limit.
</p>

It's also clear that rank-optimizing for money is the same as rank-optimizing for log-money, or for any monotonically increasing function of money. (Possible caveats around non-strict monotonic functions and the long-run equivalence thing from above?)

<p>
In some situations a rank-optimal strategy might not maximize modal return. I'm not sure if it will always minimize "expected time to reach some payoff much larger than \( V_0 \)".
</p>

### Appendix Ⅲ: rank-optimization as utility function

A utility function is a function from "states of the world" to real numbers, which represent "how much we value that particular state of the world", that satisfies certain conditions.

When we say our utility function is linear or logarithmic in money, we mean that the only part of the world we care to look at is how much money we have. We maximize our utility in expectation, by maximizing-in-expectation the amount of money or log-money we have.

Suppose I say "my utility function is such that I maximize it in expectation by rank-optimizing my returns". What would that mean?

I guess it would mean that the part of the world state we're looking at isn't my money. It's my strategy for making money, along with all the other possible strategies I could have used and the betting framework I'm in. That's weird.

It also means I'm not expecting my utility function to change in future. Like, with money, I have a certain amount of money now, and I can calculate the utility of it; and I have a random variable for how much money I'll have in future, and I can calculate the utility of those amounts as another random variable. With rank-optimality, I'm not expecting my strategy to be more or less rank-optimal in future. That's convenient because to maximize expected utility I just have to maximize current utility, but it's also weird.

<p>
For that matter, I haven't given a way to quantify rank-optimization. We can say one strategy is "more rank-optimal" than another but not "twice as rank optimal". So maybe I mean my utility function has a \( 1 \) if I'm entirely rank-optimal and a \( 0 \) if I'm not? But that's weird too. If we can calculate growth rate then we can quantify it like that, I guess.
</p>

So in general I don't expect rank-optimizing your returns to maximize your expected utility, for any utility function you're likely to have; or even any utility function you're likely to pretend to have. Not unless it happens to be the case that the way to rank-optimize your returns is *also* a way to maximize some more normal utility function like "expected log-money", for reasons that may have nothing to do with rank-optimization.

*Thanks to Justis Mills for comments; and to various members of the LW Europe telegram channel, especially Verglasz, for helping me understand this.*
