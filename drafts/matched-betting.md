---
title: The Mathematics of Matched Betting
layout: draft
---
I've been doing a little bit of matched betting lately. The idea is that you place two opposite bets on the same event, calibrated so that your profit will be the same no matter which bet wins. If you do this entirely with your own money, your profit will (under reasonable assumptions) be negative. But bookmakers often offer free bets; you can use matched betting to extract most of the amount of that free bet as actual money.

This post isn't advice about how to get into matched betting. That market is probably saturated; if you want to learn, I used [this guide](https://matchedbettingblog.com/matched-betting-intro/) and it served me well. (However, if anyone is inspired to try it by this post, I have a referral code for [smarkets](https://smarkets.com): **safto14**. It looks like if you sign up with that and bet $£20$, both you and I will receive $£10$ in risk-free bets. I swear that's not why I'm posting this.)

(Um, but after that I feel obliged to give at least *some* safety information. So here goes: if you're not a UK citizen currently in the UK, this may be a bad idea. Don't use credit cards to deposit funds; it seems they interpret that as a cash transaction and charge fees. Start small; that way there's less at risk in case you do something silly like use a credit card to deposit funds. Probably don't expect to earn lots of money this way, either in total or per-hour.)

Instead, I want to go into the math behind it, in more depth than I've seen in other places. None of this math is complicated, but some of it is useful, and I haven't seen anyone do it before. (I even deliberately went looking.)

**A simple example**

(If you've seen one example of matched betting, you've seen them all, and you can skip this particular one.)

You have a $£10$ free bet at a bookmaker. You find a football game, say Manchester Utd versus Liverpool, that you want to bet on. The bookmaker offers odds of $4$ on Liverpool, and you bet your $£10$ on them.

A note on odds: the usual convention in gambling seems to be to use decimal odds. Odds of $x$ mean that your potential winnings are $x-1$ times your stake. Thus, odds of $4$ mean a bet of $£10$ has the potential to pay out $£30$. If you're used to odds notated $a:b$ or (equivalently) $a/b$, then the decimal odds are given by $a/b + 1$.

So if Liverpool wins, you'll earn $£30$; if they lose or draw, you lose nothing. You then look up the same match at a betting exchange. An exchange allows you to take both sides of a bet, which a bookmaker won't. The exchange offers odds of $4.3$ to lay Liverpool; this means that you win your bet in the exchange only if Liverpool *doesn't* win. You accept a stake of $£6.98$, which means your own stake is $£23.03$.

Now if Liverpool wins the match, the bookmaker pays you $£30$ and you lose $£23.03$ in the exchange, for a net profit of $£6.97$. And if Liverpool loses, you earn $£6.98$ in the exchange and lose nothing at the bookmaker, for a net profit of $£6.98$. You've turned a $£10$ free bet into almost $£7$ of actual money.

(I'm ignoring for now the commission that the exchange will usually collect when you win a bet on them. With $2\%$ commission, you would instead accept stakes of $£7.01$, wagering your own $£23.13$; if Liverpool doesn't win, you would earn $£7.01 · 0.98 = £6.87$, which is also what you'd earn if Liverpool does win.)

Before bookmakers will give you a free bet, you'll usually have to place a bet with them using your own money. You lose a small amount of money on this bet, but you can use the same principles to ensure that you lose the same amount no matter who wins. You might lose around $£0.50$ on a $£10$ qualifying bet, in which case you end up with around $£6.50$ profit when all's said and done.

This has been a very brief introduction to matched betting. Now, into the math. I'm going to be focusing on two kinds of bet: qualifying bets, which are usually known as just bets, and free bets, where you don't lose anything if your back bet loses. I'm also going to ignore rounding; let's just pretend that the sterling is infinitely divisible.

**Some definitions**

We can think of a "matched bet" as an object with six values, $(O_b, O_l, S_b, S_l, C_b, C_l)$ representing a pair of back and lay bets. (A "free bet" and "qualifying bet" are also matched bets.[^risk-free])

$O_b, O_l$ are the odds on the back and lay bets. It's typically safe to assume $O_b < O_l$; otherwise, modulo commission, you could make a profit even on your qualifying bets. Also, because we're using decimal odds, we have $O_b, O_l ≥ 1$ (anything less than $1$ corresponds to a probability below $0$.)

$S_b, S_l ≥ 0$ are the stakes on the back and lay bets. Note that $S_l$ is the stake offered by the *other party* to your lay bet; it's (roughly) the amount you stand to win on that bet, not the amount you stand to lose. This may seem strange, but it's the convention used.

And $C_b, C_l ∈ [0, 1]$ are the commission charged on your winnings on each side. Usually $C_b = 0$: bookmakers don't charge commissions, they make money by offering low odds. The two exchanges I've used have $C_l = 2\% = 0.02$ (Smarkets) and $C_l = 5\% = 0.05$ (Betfair).

I'm also going to introduce the symbol $C^+ = (1 - C_l)(1 - C_b)$. If you passed $£1$ through your bookmaker and exchange, and they each charged commission and nothing else, you would have $£C^+$ left at the end. $C^+$ isn't enough for us to fully understand a matched bet, we need the individual back and lay commissions as well, but it'll be convenient shorthand.

A matched bet is one that gives the same profit no matter which side wins; as such, these six values are over-determined. Knowing any five of them will fix the value of the sixth.

Now let $R_{xy}$ (where $x,y ∈ \\{b,l\\}$) be your return on side $y$ if your bet on side $x$ wins. So for a qualifying bet, we have:

    $$ \begin{align*}
         R_{bb} &= S_b (O_b - 1) (1 - C_b)     \\
         R_{bl} &= - S_l (O_l - 1)             \\
         R_{lb} &= - S_b                       \\
         R_{ll} &= S_l (1 - C_l).
    \end{align*} $$

For a free bet, the only change is

    $$ R_{lb} = 0. $$

So your profit is $R_{bb} + R_{bl}$ if your back bet wins; and $R_{lb} + R_{ll}$ if your lay bet wins.

**Optimal lay stake**

The first question we'll ask is, given $O_\*$, $C_\*$ and $S_b$, what must $S_l$ be to make our bet a matched bet? Or in other words, what $S_l$ should we choose to eliminate all risk?

We need

    $$ R_{bb} + R_{bl} = R_{lb} + R_{ll} $$

which after some (perhaps silly-seeming) substitution and rearrangement gives

    $$ S_l = { R_{bb} - R_{lb} \over R_{ll}/S_l - R_{bl}/S_l }. $$

This looks circular, but when we substitute for the values of $R_{**}$, $S_l$ disappears from the right hand side. For a qualifying bet, this gives

    $$ S_l = S_b { (O_b - 1)(1 - C_b) + 1 \over O_l - C_l }, $$

and for a free bet,

    $$ S_l = S_b { (O_b - 1)(1 - C_b) \over O_l - C_l }. $$

A thing to note here is that $O_l$ and $C_l$ only appear in the term $O_l - C_l$. In other words, the effect of lay commission is to decrease the effective lay odds in the most natural way. It would be nice if this happened in other contexts too, but unfortunately I haven't come across it. The $O_l - C_l$ term is common, but it's usually accompanied by another $O_l$ and/or $C_l$ somewhere else in the expression.

**Profit**

Next, we'll want to know how much profit we make. This is given by $R_{lb} + R_{ll}$, where we calculate $R_{ll}$ using the lay stake we just found. But since both of these terms are proportional to $S_b$, we'll find it more convenient to think in terms of profit *per unit of back stake*,

    $$ P = { R_{lb} + R_{ll} \over S_b }. $$

Under a qualifying bet, this is

    $$ P_q = C^+ { O_b + C_b/(1 - C_b) \over O_l - C_l } - 1, $$

and for a free bet, it's

    $$ P_f = C^+ { O_b - 1 \over O_l - C_l }. $$

We can look at these functions graphically:

![(Graph of P_f(O_b, O_l))](/images/matched-betting/Pf_Ob_Ol.png)
![(Graph of P_q(O_b, O_l))](/images/matched-betting/Pq_Ob_Ol.png)

each line represents a contour of the function, a set of points that all have the same profit. The sets of contours look superficially similar, but they're generally steeper for a free bet. In both cases, profit increases with $O_b$ and decreases with $O_l$.

We can reparameterise in terms of $O_b$ and $σ = O_l - O_b$, the spread between the back and lay odds. Since $O_l ≥ O_b$, we only need to consider $σ ≥ 0$. This gives us

    $$ \begin{align*}
        P_q &= C^+ { O_b + C_b/(1 - C_b) \over O_b + σ - C_l } - 1  \\
        P_f &= C^+ { O_b - 1 \over O_b + σ - C_l }.
    \end{align*} $$

These are more distinct. Looking at these graphs, it seems that for a qualifying bet, having low $σ$ is more significant than having high $O_b$; but for a free bet, having high $O_b$ is more significant than having low $σ$. We'll make this more precise later.

We can also look at $P_q - P_f$, the difference in profit between a qualifying bet and a free bet. This isn't particularly useful to compare bets: you place qualifying bets to get free bets, and you place free bets to get qualifying bets, and if you're doing pure matched betting, I don't think you'll ever be asking yourself *should I place this bet free or as a qualifier?* Still, the difference is

    $$ P_q - P_f = { 1 \over O_l - C_l } - 1
                 = { 1 - (O_l - C_l) \over O_l - C_l }. $$

If your $O_l$ is unrealistically tiny, you'll make slightly more money on a qualifier than a free bet. But the more $O_l$ grows, the worse a qualifier becomes relative to a free bet. This, too, is suggestive that you should be looking at different sorts of bets for your qualifiers and your free bets.

**Liability**

One more thing is important when making a matched bet: lay liability. This is how much you stand to lose on the exchange where you make your lay bet. It's only important for boring real-world reasons like liquidity and exogenous risk. You need to have this much money in your account at the exchange, which means you need to be able to spare it from your bank account for a week or so. Low-liability bets are also safer if something goes wrong, which makes them a good choice for early dabblers in matched betting.

Liability is simply given by $-R_{bl} = S_l (O_l - 1)$, which is

    $$ S_b (O_l - 1) { (O_b - 1)(1 - C_b) - 1 \over O_l - C_l } $$

for a qualifying bet and

    $$ S_b (O_l - 1) { (O_b - 1)(1 - C_b) \over O_l - C_l }  $$

for a free bet.

Unlike profit, liability increases with both $O_b$ and $O_l$. But it increases arbitrarily with $O_b$, and asymtotically with $O_l$; it's bounded above by roughly $S_b O_b$ for a qualifying bet and $S_b (O_b - 1)$ for a free bet.

**Improving on a free bet**

Matched bet calculators aren't hard to find, and what I've given so far is nothing that they can't do for you. But they don't tell you everything you might want to know. Let's look at a bet, and see how we might find a better bet. Since the two types have different behaviours, we'll treat them separately.

To maximise profit, we usually need to consider that $S_b, C_b$ and $C_l$ are fixed, and find the dependence of $P$ on $O_b$ and $O_l$. For a free bet, that means we want to maximise the term

    $$ P_f ∝ {O_b - 1 \over O_l - C_l}. $$

This tells us a few things. The first is that we want high back odds and low lay odds. We already knew that, and it's not very helpful; we expect back and lay odds to more-or-less rise and fall together. It also tells us that adding a constant to both odds will increase profit; odds of 5 and 6 will be better than odds of 4 and 5. (This, too, we could have deduced before; or we could have seen it on the graph of $P_f(O_b, σ)$.)

But consider what happens when $σ = 0$. Then the term in question is

    $$ { O_b - 1 \over O_b - C_l } $$

which, as $O_b$ ranges from $1$ to $∞$, takes all values in $[0, 1)$. But when $σ > 0$, the possible values are exactly the same; high $σ$ changes the $O_b$ that gives you any particular profit, but it doesn't make any profit value available or unavailable.

What that means is: given any free bet, we can construct another free bet with equal profit but $σ = 0$, not changing $S_b$ or $C_\*$.

Or: given odds $O_b, O_l$, we can calulate the odds $O'$ that would give you the same profit, if you could find these odds for both a back and a lay bet.

In turn, that tells you that if you want to improve your profits, you can ignore bets with $O_b < O'$. (Because for those bets, $P_f(O_b, σ) < P_f(O', σ) ≤ P_f(O', 0)$. The first inequality comes from adding a constant to both odds, and the second comes from reducing $O_l$.) This is a useful thing to know, that matched bet calculators don't tell you.

To find $O'$, we set

    $$ { O_b - 1 \over O_l - C_l } = { O' - 1 \over O' - C_l } $$

and deduce

    $$ \begin{align*}
        O' &= { O_l - O_bC_l \over 1 + O_l - O_b - C_l } \\
           &= O_b { 1 - C_l + σ/O_b \over 1 - C_l + σ }.
    \end{align*} $$

The expression with $σ$ isn't exactly simpler, but I think it's more aesthetically pleasing. (Consider that $1-C_l$ is approximately as fundamental as $C_l$ itself.)

We can also calculate $O'$ and $P_f$ as functions of each other:

    $$ P_f = C^+ { O' - 1 \over O' - C_l }                 \\
       O' = { C_lP_f - C^+ \over P_f - C^+ } $$

(image)

$P_f$ approaches an asymtote at $C^+$, but slowly. With $C_b = 0, C_l = 0.02$, extracting $80\%$ of a free bet is only possible if $O_b ≥ 5.36$. For $90\%$, you need $O_b ≥ 12.03$. Such bets are somewhat rare in my experience, and typically have high spread.

We can go more general. Given a profit, we can calculate the level curve of all bets which generate that profit; the case $σ=0$ gives us only a single point on that curve. The curve divides bet-space into two regions, so that it's easy to see whether a bet gives more or less than this amount of profit.

(Earlier we saw this level curve graphically, for certain specific profits. Now we find the explicit formula for the curve.)

We already have

    $$ \begin{align*}
        P_f &= C^+ { O_b - 1 \over O_l - C_l }    \\
            &= C^+ { O_b - 1 \over O_b + σ - C_l },
    \end{align*} $$

and it's just a matter of rearranging these:

    $$ O_b C^+ = P_f (O_l - C_l) + C^+\\
       O_b (C^+ - P_f) = P_f (σ - C_l) + C^+. $$

These two equations can be used to find $O_b$ in terms of $O_l$ or $σ$, and vice-versa. Both are very simple at heart: they're linear relationships, that could be rearranged to the form $y = mx + c$.

Looking more closely at the second one, notice that $C^+$ is the upper bound on profit. So the term $C^+ - P_f$ can be thought of as how much profit is being left on the table, compared to what you could hypothetically get if odds of $∞$ were a thing. The less profit you leave behind, the less $σ$ has to change to compensate for a given change in $O_b$. In other words, when profit is high, the level curve on the graph of $P_f(O_b, σ)$ becomes shallower, as we saw above.

**Improving on a qualifying bet**

For a qualifying bet, we can't quite do the same thing. If we temporarily assume $C_b = 0$, then the term we want to maximise is

    $$ P_q + 1 ∝ {O_b \over O_l - C_l}. $$

This doesn't work the same as the equivalent term for a free bet. If you keep $σ$ fixed and consider profit as a function of $O_b$, then this function acts differently depending on $\mathrm{sgn}(σ - C_l)$. If $σ ≤ C_l$, then regardless of $O_b$ you get more profit than is ever possible with $σ > C_l$.

This isn't immediately practically important, because $σ > C_l$ is a pretty safe assumption. But it's mathematically significant. For a free bet, setting $σ$ to $0$ doesn't rule out any profit levels, so we could ask "how would we get this particular profit with $σ = 0$?" If we try to ask that for a qualifying bet, the answer is typically that we can't. So the approach we used for a free bet doesn't work on a qualifying bet.

We also can't set $O_b$ to its best possible value, because it can go arbitrarily high. But we can try setting it to its limiting worst value ($O_b = 1$). We find $σ'$ such that

    $$ { O_b + C_b/(1 - C_b) \over O_b + σ - C_l }
       = { 1 + C_b/(1 - C_b) \over 1 + σ' - C_l }, $$

which gives us

    $$ σ' = { σ + (O_b - 1)(1 - C^+) \over 1 + (O_b - 1)(1 - C_b) } $$

Now we know that any bet with a spread less than $σ'$ will give better profit than the bet we started with. Unfortunately, I think this still isn't as good as what we got for a free bet, for three reasons.

1. For a free bet, we had an easy negative test: some bets (those with $O_b < O'$) could be ruled out on a glance, but verifying them took more work. Here, the test is positive: some bets (those with $σ < σ'$) can be accepted on a glance, but verifying the others takes more work.[^graph-shape]

    In practice, I expect the positive test will almost alway be inconclusive, meaning you still need to do the more difficult check on every bet. (I haven't done enough betting myself, while writing this, to say from experience.)

2. My workflow is to find a plausible-looking back bet and then see how it would be matched. With a free bet, I can run the easy test without looking for the match. For a qualifying bet, I need to find both sides of the bet before I can run the easy test.

3. Qualifying bets often must be placed at a minimum odds (on the back side) in order to count. That typically rules out the lowest-spread bets (see below digression).

Still, this is what we have. Following a similar theme as before, we can calculate $σ'$ and $P_q$ as functions of each other:

    $$ P_q = { 1 - C_l \over 1 - C_l + σ' } - 1 \\
       σ' = { 1 - C_l \over P_q + 1 } + C_l - 1. $$

(Note that these equations don't contain $C_b$. That's not because we're assuming it's $0$: when you set $O_b = 1$, $C_b$ completely disappears from the equation for $P_q$.)

(image)

Interestingly, the bounds of $P_q$ don't depend on commission at all. As $σ'$ grows, $P_q$ always approaches an asymtote at $-1$, which isn't surprising: you can't quite lose your entire back stake, but you can get arbitrarily close to that, even with no commission.

On the other edge of the graph, we always have $P_q(O_b=1, σ'=0) = 0$. (That may not be clear on this image, but it's easy to see algrebraically.) That's because at $O_b = O_l = 1$, both bets are completely one-sided. On the back side you have a chance of losing money, but no way to win it; on the lay side you have a chance of winning money, but no way to lose it. In particular, if the back bet wins, you make no profit or loss on either bet, so commission is irrelevant. And so the lay stake is calibrated for your lay winnings, after commission, to cancel out your back loss. (But if someone is willing to give you free maybe-money, you might as well ask for as much maybe-money as they're willing to give you.)

And again, given profit, we can calculate the level curve of bets which return that profit. Unsurprisingly, we find another linear relationship; it comes to

    $$ O_bC^+ + C_b(1 - C_l) = (Pq + 1)(Ol - Cl) \\
       O_b(1 - C_b - Λ) + C_b = Λ(σ - C_l), $$

where

    $$ Λ = { P_q + 1 \over 1 - C_l }. $$

I'm afraid I can offer no particular interpretation of what $Λ$ means, though I observe that we can substitute it into a previous equation, $σ' = 1/Λ + C_l - 1$. Note that if $Λ ≥ 1 - C_b$, equivalently if $P_q + 1 ≥ C^+$, then $σ$ and $O_b$ start to move in opposite directions: for fixed profit, $σ$ goes up as $O_b$ goes down. At this point, you get more profit with low $O_b$ as well as with low $σ$, which would be convenient if it was ever realistically going to happen.

(It turns out that $P_q + 1 ≥ C^+$ precisely when $σ ≤ C_l + C_b/(1 - C_b)$. I noted above that if $C_b = 0$, the possible values of $P_q + 1$ depend on $\mathrm{sgn}(σ-C_l)$. This is the same result, generalized to all values of $C_b$.)

**A digression on odds**

Note that in general, you can expect spread to be lower at lower odds. That's because odds are more sensitive to evidence when they're high than when they're low.

There's a [technical interpretation](https://arbital.com/p/bayes_log_odds/) of that, but I'm just going to illustrate by example. Consider the probabilities $1/5$ and $1/6$. These are complementary to $4/5$ and $5/6$ - the two pairs of probabilities encode the same information. Converting to decimal, probabilities $1/5$ and $1/6$ are decimal odds $1.25$ and $1.2$; and probabilities $4/5$ and $5/6$ are decimal odds $5$ and $6$.

So the difference between the odds $1.25$ and $1.2$ is, in a very important sense, the same as the difference between $5$ and $6$. But when it comes to betting, the spreads of $0.05$ and $1$ are very different.

The takeaway from this is that for qualifying bets, you should be looking at bets with low odds. High odds have better returns, but the effect of low spread is much more significant, and low spread comes with low odds.

**The effects of commission**

I want to explore one more question: how does profit depend on commission? For this, we'll keep $C_b$ and $O_b$ fixed, and explore how $O_l$ and $C_l$ affect profit.

Conveniently, the term we want to maximise is the same,

    $$ \begin{align*}
        P_q + 1 ∝ { 1 - C_l \over O_l - C_l }  \\
        P_f ∝ { 1 - C_l \over O_l - C_l }.
    \end{align*} $$

So if we find the same lay bet on two different exchanges, we can compare them without regard for the back bet we'd be matching.

The two exchanges I've used have $C_l$ of $0.02$ and $0.05$, so they give equal profits when

    $$ { 0.98 \over O_S - 0.02 } = { 0.95 \over O_B - 0.95 } $$

where $O_S$ is the odds offered on Smarkets and $O_B$ is the odds offered on Betfair. This rearranges to

    $$ 98·O_b = 95·O_S. $$

Since $98/95 ≈ 1.03$, it's better to use Betfair than Smarkets if the offered odds are roughly $3%$ lower, which happens to be the difference in commission. So for example, odds of $6$ on Betfair correspond to roughly $6.19$ on Smarkets.

It should be easy to take a bunch of equivalent bets on the two sites, and compare to see which seems likely to give better profit in general. I started doing that, but then I looked at three football games and got bored and stopped.

They all had exactly the same odds on all three positions (win/draw/win), even when they fluctuated slightly pre-game. (I did look at one game as it began, and the two sites didn't quite stay in sync then. But betting while odds are fluctuating a lot is a bad idea.) This suggests that Smarkets typically offers better profits. But Betfair is a more popular site, which probably has advantages; in particular, it's plausible that a large bet would be harder to fully match on Smarkets.

---

And that's it. I'm sure there are other interesting questions you could ask, but I'm going to stop there.

Something that would be nice would be a calculator that can make use of this. The online calculators all seem pretty crap: they only tell you profit, lay stake and lay liability, and only for one bet at a time. Being able to compare bets seems like it would be a pretty important feature, but I haven't seen it anywhere. (Some of them have features to work with more complicated types of bets than I've looked at, but I don't care about that. [Here's one](https://matchedbettingblog.com/matched-betting-calculator/) that's no worse than any other.) I've also seen an excel calculator, which had the neat feature of automatically adding bets to a spreadsheet. But again, only one bet at a time; plus, I don't have excel, and don't keep track of my bets in a spreadsheet. (I use [ledger](http://ledger-cli.org/), though it's not a great fit.)

I've written a command-line tool that can show you multiple bets at a time for comparison purposes. It also shows you, for a free bet, the lowest possible back odds to improve on your highest-profit bet ($O'$); or, for a qualifying bet, the highest possible spread that *won't* improve on it ($σ'$).

But the interface isn't very good, I think partly because of the limits of the command line and partly because of a questionable design decision (see the README). And it can't show graphs, which I think would be nice. If you want to use it anyway, it's [on github](https://github.com/ChickenProp/matched-bets).

If I were to dedicate more time to the project, I currently think I'd start again in Javascript. I think I have a vague idea of how a decent one could work. But right now, as far as I can tell there are no good calculators.

[^risk-free]: I'm assuming that all free bets are "stake not returned", which means that if you win, you collect your winnings but you don't also get to keep the stake that wasn't yours in the first place. If you have a "stake returned" free bet, that effectively increases the odds on the back side by $1$. I've not yet encountered one of these, myself.

    Another type is the "risk-free" bet, which I won't go into here partly because I'm not 100% sure what it means. But I *think* that "£10 in risk-free bets" allows you to make a bet of more than £10, and if you lose, you get £10 back. I think the way to treat it is as putting £10 into a free bet (stake not returned) and the remainder of your stake into a qualifying bet, and so by default you should put in no more than the risk-free amount.

[^graph-shape]: Another way to look at this is by the shape of the "more profitable" space on the graphs of $P_q(O_b, σ)$ and $P_f(O_b, σ)$. In both cases, this is the space below and to the right of one of the level curves. On the $P_f$ graph, it's defined by two lines: $σ = 0$ and the level curve itself. If we add a line with constant $O_b$, that line can carve up the "less profitable" space without entering the "more profitable" space. But on the $P_q$ graph, the "more profitable" space is also defined by the line $O_b = 1$. Any line we draw with constant $O_b ≠ 1$ or $σ ≠ 0$ will carve up the "more profitable" space.
