---
layout: draft
title: "Ruining an expected-log-money maximizer"
lw_xpost: true
tags: [rationality, math]
---
Suppose you have a game where you can bet any amount of money. You have a 60% chance of doubling your stake and a 40% chance of losing it.

Consider agents Linda and Logan, and assume they both have £1[^gbp]. Linda has a utility function that's linear in money (and has no other terms), \\( U\_\\text{Linda}(m) = m \\). She'll bet all her money on this game. If she wins, she'll bet it again. And again, until eventually she loses and has no more money.

[^gbp]: They use GBP because gambling winnings are untaxed in the UK, and also the £ symbol doesn't interfere with my math rendering.

Logan has a utility function that's logarithmic in money, \\( U\_\\text{Logan}(m) = \\ln(m) \\). He'll bet 20% of his bankroll every time, and his wealth will grow exponentially.

Some people take this as a reason to be Logan, not Linda. Why have a utility function that causes you to make bets that leave you eventually destitute, instead of a utility function that causes you to make bets that leave you rich?

### In defense of Linda

I make three replies to this. Firstly, the utility function is not up for grabs! You should be very suspicious any time someone suggests changing how much you value something.

"Because if Linda had Logan's utility function, she'd be richer. She'd be doing better according to her current utility function." My second reply is that this is confused. Before the game begins, pick a time \\(t\\). Ask Linda which distribution over wealth-at-time-\\(t\\) she'd prefer: the one she gets from playing her strategy, or Logan's strategy? She'll answer, hers: it has an expected wealth of \\( £1.2^t \\). Logan's only has an expected wealth of \\( £1.04^t \\).

And, at some future time, after she's gone bankrupt, ask Linda if she thinks any of her past decisions were mistakes, given what she knew at the time. She'll say no: she took the bet that maximized her expected wealth at every step, and one of them went against her, but that's life. Just think of how much money she'd have right now if it hadn't! (And nor had the next one, or the one after....) It was worth the risk.

You might ask "but what happens after the game finishes? With probability 1, Linda has no money, and Logan has infinite". But there is no after! Logan's never going to stop. You could consider various limits as \\( t→∞ \\), but limits aren't always well-behaved[^convergence]. And if you impose some stopping behavior on the game - a fixed or probabilistic round limit - then you'll find that Linda's strategy just uncontroversially gives her better payoffs (according to \\( U\_ν \\)) after the game than Logan's, when her probability of being bankrupt is only *extremely close* to 1.

[^convergence]: I think that Linda's strategy [converges in probability](https://en.wikipedia.org/wiki/Convergence_of_random_variables#Convergence_in_probability) to the random variable that's always 0; and Logan's converges pointwise to a function that's 0 everywhere so it doesn't converge in probability to anything. But I haven't checked in detail.

Or, "but at some point Logan is going to be richer than Linda ever was! With probability 1, Logan will surpass Linda according to Linda's values." Yes, but you're comparing Logan's wealth at time \\( t\_2 \\) to Linda's wealth at time \\( t\_1 \\). And when Logan's wealth does surpass the amount she had when she lost it all, she can console herself with the knowledge that if she *hadn't* lost it all, she'd be *raking it in* right now. She's okay with that.

I suppose one thing you could do here is pretend you can fit infinite rounds of the game into a finite time. Then Linda has a choice to make: she can either maximize expected wealth at \\( t\_n \\) for all finite \\( n \\), or she can maximize expected wealth at \\( t\_ω \\), the timestep immediately after all finite timesteps. We can wave our hands a lot and say that making her own bets would do the former and making Logan's bets would do the latter, though I don't endorse the way we're treating infinties here.

Even then, I think what we're saying is that Linda is underspecified. Suppose she's offered a loan, "I'll give you £1 now and you give me £2 in a week". Will she accept? I can imagine a Linda who'd accept and a Linda who'd reject, both of whom would still be expected-money maximizers, just taking the expectation at different times and/or expanding "money" to include debts. So you could imagine a Linda who makes short-term sacrifices in her expected-money in exchange for long-term gains, and (again, waving your hands harder than doctors recommend) you could imagine her taking Logan's bets. But this is more about delayed gratification than about Logan's utility function being better for Linda than her own, or anything like that.

I'm not sure I've ever seen a treatment of utility functions that deals with this problem? (The problem being "what if your utility function is such that maximizing expected utility at time \\(t\_1\\) doesn't maximize expected utility at time \\(t\_2\\)?") It's no more a problem for Linda than for Logan, it's just less obvious for Logan given this setup.

So I don't agree that Linda would prefer to have Logan's utility function.

### Counterattack

And my third reply is: if you think this is embarrassing for Linda, watch me make Logan do the same. Maybe not *quite* the same. I think the overall story matches, but there are notable differences.

I can't offer Logan a bet that he'll stake his entire fortune on. No possible reward can convince him to accept the slightest chance of running out of money. He won't risk his last penny to get \\( £(3 ↑↑↑ 3) \\), even if his chance of losing is \\( 1 / (3 ↑↑↑↑ 3) \\)[^knuth].

[^knuth]: This is using [Knuth's up-arrow notation](https://en.wikipedia.org/wiki/Knuth%27s_up-arrow_notation), but if you're not familiar with it, you can think of these numbers as "obscenely large" and "even more obscenely tiny" respectively.

But I can offer him a bet that he'll stake *all but a penny* on. I can make the odds of that bet 60/40 in his favor, like the bets Linda was taking above, or any other finite probability. Then if he wins, I can offer him another bet at the same odds. And another, until he eventually loses and can't bet any more. And just like Linda, he'll be able to see this coming and he'll endorse his actions every step of the way.

How do I do this? I can't simply increase the payoff-to-stake ratio of the bet. If a bet returns some multiple of your stake, and has a 60% chance of winning, Logan's preferred amount to stake will never be more than 60% of his bankroll.

But who says I need to give him that option? Logan starts with £1, which he values at \\( \ln(100) ≈ 4.6052 \\).[^zero-point] I can offer him a bet where he wagers £0.99 against £20.55 from me, with 60% chance of winning. He values that bet at

[^zero-point]: I'm setting Logan's zero-utility point at £0.01, which means we take the log of the number of pennies he has. But we could do it in pounds instead, or use a different base of logarithm, without changing anything.

<p>
\[ 0.4\ln(100 - 99) + 0.6\ln(100 + 2055) ≈ 4.6053 \]
</p>

so he'll accept it. He'd *rather* wager some fraction of £0.99 against the same fraction of £20.55 (roughly £0.58 against £11.93), but if that's not on the table, he'll take what he can get.

If he wins he has £21.55 to his name, which he values at \\( \\ln(2155) ≈ 7.6755 \\). So I offer him to wager £21.54 against my £3573.85, 60% chance of winning, which he values at... still \\( 7.6755 \\) but it's higher at the 7th decimal place. And so on, the stakes I offer growing exponentially - Logan is indifferent between a certainty of \\( £x \\) and a 60% chance of \\( £x^{5/3} \\) (plus 40% chance of £0.01), so I just have to offer slightly more than that (minus his current bankroll).

Admittedly, I'm not giving Logan much choice here. He can either bet everything or nothing. Can I instead offer him bets where he chooses how much of his money to put in, and he still puts in all but a penny? I'm pretty sure yes: we just need to find a function \\( f : ℝ\_{>0}^2 → ℝ\_{>0} \\) such that whenever \\( a ∈ (0, x] \\),

<p>
\[ \ln(x) < 0.4\ln(a) + 0.6\ln(f(x, a)) \\
   {d \over d a}(0.4\ln(a) + 0.6\ln(f(x, a))) < 0 \]
</p>

Then if Logan's current bankroll is \\( x \\), I tell him that if he wagers \\( w \\), I'll wager \\( f(x, x-w) - x \\) (giving him 60% chance of coming away with \\( f(x, x-w) \\) and 40% chance of coming away with \\( x-w \\)). He'll want to bet everything he can on this. I spent some time trying to find an example of such a function but my math isn't what it used to be; I'm just going to hope there are no hidden complications here.

So what are the similarities and differences between Linda and Logan?

Difference: Logan's bets grow a lot faster than Linda's. For some fixed probability of bankrupting them, I need a lot less money for Linda than Logan. Similarity: I need an infinite bankroll to pull this off with probability 1, so who cares how fast the bets grow?

Difference: the structure of bets I'm offering Logan is really weird. Why on Earth would I offer him rewards exponential in his stake? Similarity: why on Earth would I offer any of these bets? They all lose money for me. Am I just a cosmic troll trying to bankrupt some utilitarians or something? (But the bets I'm offering Logan are still definitely weirder.)

Difference: I bring Linda down to £0.00, and then she'd like to bet more but she can't because she's not allowed to take on debt. I bring Logan down to £0.01, and then he'd like to bet more but he can't because he's not allowed to subdivide that penny. Similarity: these both correspond to "if your utility reaches 0 you have to stop playing".

(Admittedly, "not allowed to subdivide the penny" feels arbitrary to me in a way that "not allowed to go negative" doesn't. But note that Linda would *totally* be able to take on debt if she's seeing 20% return on investment. Honestly I think a lot of what's going on here, is that "not allowed to go negative" is something that's easy to model mathematically, while "not allowed to infinitely subdivide" is something that's hard to model.)

Difference: for Logan, but not for Linda, I need to know how much money he starts with for this to work. Or at least an upper bound.

But all of that feels like small fry compared to this big similarity. I can (given an infinite bankroll, a certain level of trollishness, and knowledge of Logan's financial situation) offer either one of them a series of bets, such that they'll accept every bet in turn and put as much money as they can on it; and then eventually they'll lose and have to stop betting. They'll know this in advance, and they'll play anyway, they'll lose all or almost all of their money, and they won't regret their decisions. If you think this is a problem for Linda's utility function, it's a problem for Logan's too.

### What about a Kelly bettor?

I've [previously made the case](https://www.lesswrong.com/posts/XnnfYrqaxqvirpxFX/on-kelly-and-altruism) that we should distinguish between "maximizing expected log-money", the thing Logan does; and "betting Kelly", a strategy that merely happens to place the same bets as Logan in certain situations. According to my usage of the term, one bets Kelly when one wants to "rank-optimize" one's wealth, i.e. to become richer with probability 1 than anyone who doesn't bet Kelly, over a long enough time period.

It's well established that when offered the bets that ruin Linda, Kelly bets the same as Logan. But what does Kelly do when offered the bets that ruin Logan?

Well, I now realize that for any two strategies which make the same bet all but finitely many times, neither will be more rank-optimal than the other, according to the definition I gave in that post. That's a little embarrassing, I'm glad I hedged a bit when proposing it.

Still: when offered Logan's all-or-nothing bets, Kelly accepts at most a finite number of them. Any other strategy accepts an infinite number of them and eventually goes bankrupt with probability 1.

What about the bets where Logan got to choose how much he put in? Kelly would prefer to bet nothing (except a finite number of times) than to go all-in infinitely many times. But might she bet smaller amounts, infinitely often?

What are some possible strategies here? One is "bet a fixed amount every time"; this has some probability of eventually going bankrupt (i.e. ending up with less than the fixed amount), but I think the probability is less than 1. I don't think any of these strategies will be more or less rank-optimal than any of the others.

Another is "bet all but a fixed amount every time". This has probability 1 of eventually being down to that amount. Assuming you then stop, this strategy is more rank-optimal the higher that amount is (until it reaches your starting capital, at which point it's equivalent to not betting).

We could also consider "bet some fraction of (your current bankroll minus one penny)". Then you'll always be able to continue betting - except that this is cheating a bit because it relies on infinite subdivisibility, and if we had that it's harder to justify the "can't bet below £0.01" thing. Still, if we could do this, my guess is that you'd have probability 1 of unboundedly increasing wealth, so any fraction here would be more rank-optimal than the other strategies, which can't guarantee ever turning a profit. Different fractions would be differently rank-optimal, but I'm not sure which would be the most rank-optimal. (It could plausibly be unbounded, just increasing rank-optimality as the fraction increases until there's a discontinuity at 1.) You can still do roughly this strategy without infinite subdivisibility, but at some point you'll need to round either to 0 (and stop betting) or 1 (and bet down to your last penny), and then we're no longer more rank-optimal than the other strategies.

So I think the answer is: Kelly will do the fractional-betting thing if she can, and if not she has no strategy she prefers over "never bet". This makes me think that the technical definition of rank-optimality I suggested in the last post is not very useful here. (But nor is the technical definition of growth rate that the actual Kelly originally used.)

My own strategy might be something like "bet some fraction, but if that would give me fewer than say 10 bets remaining then bet a fixed amount". That would give me a tiny chance of going bankrupt, but if I don't go bankrupt I'll be growing unboundedly. Also I'm not going to worry about the difference between £0.00 and £0.01.
