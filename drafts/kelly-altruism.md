---
title: On Kelly and altruism
layout: draft
tags: rationality
explicit-math: true
---
There was a [twitter thread](https://twitter.com/SBF_FTX/status/1337250686870831107) that triggered some confusion amongst myself and some other people in a group chat I'm in.[^author]

[^author]: The [author](https://en.wikipedia.org/wiki/Sam_Bankman-Fried) of the tweets is, as the saying goes, best known for other work. That other work is not relevant here.

The relevant tweets are these (I've omitted some):

> 3) Let’s say you were offered a coin flip.  75% it comes up heads, 25% it comes up tails; 1:1 payout.  How much would you risk?

> 4) There are a number of ways to approach this question, but to start: what do you want, in the first place?  What’s your utility function?

> 5) In other words--how cool would it be to make $10,000?  How about $1,000,000--is that 100 times as good?
>
> For most people the answer is ‘no, it’s more like 10 times as good’.  This is because of decreasing marginal utility of money.

> 8) One reasonable utility function here is U = log(W): approximating your happiness as logarithmic in your wealth.  That would mean going from $10k to $100k is worth about as much as going from $100k to $1m, which feels…. reasonable?
>
> (this is what the Kelly Criteria assumes)

> 9) So, if you have $100k, Kelly would suggest you risk half of it ($50k).  This is a lot!  But also 75% odds are good.

> 10) What about a wackier bet?  How about you only win 10% of the time, but if you do you get paid out 10,000x your bet size?  (For now, let’s assume you only get to do this bet once.)

> 11) Kelly suggests you only bet $10k: you’ll almost certainly lose.  And if you kept doing this much more than $10k at a time, you’d probably blow out.
>
> That this bet is great expected value; you win 1,000x your bet size, way better than the first one!  It’s just very risky.

> 12) In many cases I think $10k is a reasonable bet.  But I, personally, would do more.  I’d probably do more like $50k.
>
> Why?  Because ultimately my utility function isn’t really logarithmic.  It’s closer to linear.

> 13) Sure, I wouldn’t care to buy 10,000 new cars if I won the coinflip.  But I’m not spending my marginal money on cars anyway.  I’m donating it.
>
> And the scale of the world’s problems is…. Huge.

> 14) 400,000 people die of malaria each year.  It costs something like $5k to save one person from malaria, or $2b total per year.  So if you want to save lives in the developing world, you can blow $2b a year just on malaria.

> 15) And that’s just the start.  If you look at the scale of funds spent on diseases, global warming, emerging technological risk, animal welfare, nuclear warfare safety, etc., you get numbers reaching into the trillions.

> 16) So at the very least, you should be using that as your baseline: and kelly tells you that when the backdrop is trillions of dollars, there’s essentially no risk aversion on the scale of thousands or millions.

> 17) Put another way: if you’re maximizing EV(log(W+$1,000,000,000,000)) and W is much less than a trillion, this is very similar to just maximizing EV(W).

> 18) Does this mean you should be willing to accept a significant chance of failing to do much good sometimes?
>
> Yes, it does.  And that’s ok.  If it was the right play in EV, sometimes you win and sometimes you lose.

> 19) And more generally, if you look at everyone contributing to the cause as one portfolio--which is certainly true from the perspective of the child dying from malaria--they aren’t worried about who it was that funded their safety.

> 22) So given all that, why not bet all $100k?  Why only $50k?
>
> Because if you bet $100k and lose, you can never bet again.  And to the extent you think you have future ways to provide value that are contingent on having some amount of funding, it can be important to keep that.

The thing we were trying to figure out was, is his math right? And here's my current understanding of that matter.

### On Kelly

The first thing I'd say is, I think the way he talks about [Kelly](https://en.wikipedia.org/wiki/Kelly_criterion) here is confusing. My understanding is:

Under a certain betting framework, if you place bets that maximize expected log-money, then you get (something good).

If you happen have a utility function, and that utility function increases logarithmically with money, then you maximize your expected utility while also getting (something good).

If you happen to have a utility function, and that utility function increases linearly with money - or something else other than logarithmically - then you have to choose between maximizing your expected utility and getting (something good). And by definition, you'd rather maximize your expected utility. (More likely: that's not your utility function. Even more likely: you don't have a utility function.)

(I don't think any human has a utility function. I think it can be a useful shorthand to talk as though we do, sometimes. I think this is not one of those times.)

The (something good) is that, over a long enough time, you'll almost certainly get more money than someone else who was offered the same bets as you and started with the same amount of money but regularly bet different amounts on them. But this is NOT the same thing as maximizing your average (AKA "expected") amount of money over time; "almost certainly" hides a small number of outcomes that make a lot of difference to that calculation.

This sounds like a very good thing to me! Like, do I want to maximize the most-likely amount of money that I'll have in the future, *and* the median, *and* the 1st percentile and 99th percentile and in fact *every* percentile, *all at once*? Oh, and while I'm at it, minimize "the expected time I'll take to reach any given amount of money much more than what I have now"? Yes please!

(Oh, also, I don't need to choose whether I'm getting that good thing for money or log-money or what. It's the same for any monotonically increasing function of money.)

Separately from that: yeah, I think going from $10k to $100k sounds about as good as going from $100k to $1m. So if we're in a situation where it makes sense to pretend I have a utility function, then it's probably reasonable to pretend my supposed utility function is logarithmic in money.

So that's convenient. I dunno if it's a coincidence or what, but it's useful. If we tried to pretend my utility function was linear in money then I'd be sad about losing that good thing, and then it would be hard to keep pretending.

To me, Kelly is about getting that good thing. If you have a utility function, just place whatever bet size maximizes expected utility. If instead you want to get that good thing, Kelly tells you how to do that, under a certain betting framework. And the way to do that is to place bets that maximize expected log-money.

If you have a utility function and it's proportional to log-money, then you'll happen to get the good thing; but far more important than that, will be the fact that you're maximizing expected log-money. If you bet according to a different utility function, then a Kelly bettor will almost certainly be richer than you over time; but you're (for now) sitting on a bigger pile of expected utility, which is what you care about.

Or maybe you want to mix things up a bit. For example, you might care a bit more about your average returns, and a bit less about being the richest person in the room, than a Kelly bettor. Then you could bet something above the Kelly amount, but less than your full bankroll. You'll almost certainly end up with less than the Kelly bettor, but *on average* you'll still earn more than them.

I'm not sure what to call this good thing. I'm going to go with "Kelly-optimizing" one's bankroll. I want to clarify a few things about Kelly-optimization:

* It might be a meaningful concept in situations unlike the betting framework we're currently talking about. In those situations, the name might be confusing, because what "Kelly betting" normally means might not be a thing you can do - or it might be a thing you can do, but it doesn't Kelly-optimize.

* In some situations, different good things about Kelly optimization might not all come together. You might need to choose between them.

* Similarly, in some situations, Kelly-optimization might not come from maximizing expected log-money. (When it doesn't, might one still have a utility function that's maximized in expectation by Kelly-optimizing one's bankroll? I think the answer is roughly "yes but it would be weird and for our current purposes we can say no".)

### On the tweets

So in this lens, the author's argument seems confused. "My utility function is linear in money, so Kelly says" no it doesn't, if you have a utility function or if you're maximizing the expected value of anything then Kelly can go hang.

...but not everyone thinks about Kelly the same way I do, and I don't necessarily think that's wrong of them. So, what are some non-confused possibilities?

One is that the author has a utility function that's roughly linear in his own wealth. Or, more likely, *roughly values* money in a way that's roughly linear in his own wealth, such that Kelly-optimizing isn't optimizing according to his preferences. And then yeah I think the argument basically goes through. If you want to maximize expected log of "money donated to charity", then yes, that will look a lot like maximizing expected "money you personally donate to charity". This has nothing to do with Kelly, according to me.

Another is that the author wants to Kelly-optimize the amount of money he can donate. In that case I think it doesn't matter that the backdrop is trillions of dollars. To Kelly-optimize the total amount donated to charity, he should Kelly-optimize the amount he personally donates.

But here we come to the "everyone contributing to the cause" argument.

Suppose you have two people who each want to Kelly-optimize their own bankroll. Alice gets offered a handful of bets, and Kellies them. Bob gets offered a handful of bets, and Kellies them.

And now suppose instead they both want to Kelly-optimize their total bankroll. So they combine them into one. Whenever Alice gets a bet, she Kellies according to *their combined bankrolls*. Whenever Bob gets a bet, he Kellies according to *their combined bankrolls*. And in the end, their total bankroll will almost certainly be higher than the sum of the individual bankrolls, in the first case.

But to be clear, I think the value doesn't come from combining their money but from combining their bets. I've assumed the combined bankroll gets twice as many bets as either of the individual ones. That might not be the case - perhaps one bet is offered per day, anyone who wants can accept it, and it must be accepted in the morning and pays out in the afternoon. In that case teaming up doesn't help.

But I do think something like this, combined with reasonable assumptions about charity and how bets are offered, suggests betting above Kelly. Like, maybe Alice and Bob don't want to literally combine their bankrolls, but they do trust each other pretty well and are willing to give or lend each other moderate amounts of money, and the two of them encounter different bets. Then I think to Kelly-optimize their individual or combined bankrolls, each of them should probably be betting above Kelly.

Or maybe Alice doesn't encounter bets (or can't act on them or doesn't trust herself to evaluate them or...), but she does encounter Bob and Carol and Dennis and somewhat trusts all of them to be aligned with her values. Then I think "Alice gives each of them money, and wants each of them to make above-Kelly bets" is correct, provided she'll be willing to give them more money in future if they get unlucky.

### Conclusion

So was the tweeter's math right? Man, I dunno. I'm inclined to say something like, "not as written but he was hand waving in the right directions"? Such that if he'd tried to be rigorous I expect that he'd have succeeded, though I also expect he'd have used the word "Kelly" in ways that I'd say were confusing.

In any case I think *I* understand what's going on better than I used to. Hopefully you do, too.
