---
title: The Mathematics of Matched Betting
layout: draft
---
I've been doing a little bit of matched betting lately. This post isn't advice about that. Instead, I want to go into the math behind it, a little deeper than I've seen other places do.

Fundamentally, matched betting is about placing two complementary bets at the same time, such that whichever wins your profit is the same. If you do this entirely with your own money, your profit will (under reasonable assumptions) be negative. But bookmakers often offer free bets; you can use matched betting to extract most of the amount of that free bet as actual money.

So for example: you have a £10 free bet at a bookmaker. You find a football game, say Manchester Utd versus Liverpool, that you want to bet on. The bookmaker offers odds of $4$ on Liverpool, and you bet your £10 on them.

A note on odds: the usual convention in gambling seems to be to use decimal odds. Odds of $x$ mean that your potential winnings are $x-1$ times your stake. Thus, odds of $4$ mean a bet of £10 has the potential to pay out £30. If you're used to odds notated $a:b$ or (equivalently) $a/b$, then the decimal odds are given by $a/b + 1$.

So if Liverpool wins, you'll earn £30; if they lose or draw, you lose nothing. You then look up the same match at a betting exchange. An exchange allows you to take both sides of a bet, which a bookmaker won't. The exchange offers odds of 4.3 to lay Liverpool; this means that you win your bet in the exchange only if Liverpool *doesn't* win. You accept a stake of £6.98, which means your own stake is £23.03.

Now if Liverpool wins the match, the bookmaker pays you £30 and you lose £23.03 in the exchange, for a net profit of £6.97. And if Liverpool loses, you earn £6.98 in the exchange and lose nothing at the bookmaker, for a net profit of £6.98. You've turned a £10 free bet into almost £7 of actual money.

(I'm ignoring for now the commission that the exchange will usually collect when you win a bet on them. With 2% commission, you would instead accept stakes of £7.01, wagering your own £23.13; if Liverpool doesn't win, you would earn $£7.01 · 0.98 = £6.87$, which is also what you'd earn if Liverpool does win.)

Before bookmakers will give you a free bet, you'll usually have to place a bet with them using your own money.

This has been a very brief introduction to matched betting. Now, into the math. I'm going to be focusing on two kinds of bet: qualifying bets, which are usually known as just bets, and free bets, where you don't lose anything if your back bet loses. I'm also going to ignore rounding; let's just pretend that the sterling is infinitely divisible.

Some definitions:

We can think of a "matched bet" as an object with six values, $(O_b, O_l, S_b, S_l, C_b, C_l)$ representing a pair of back and lay bets. (A "free bet" and "qualifying bet" are also matched bets.)

$O_b, O_l$ are the odds on the back and lay bets. It's typically safe to assume $O_b < O_l$; otherwise, modulo commission, you could make a profit even on your qualifying bets. Also, because we're using decimal odds, we have $O_b, O_l ≥ 1$ (anything less than 1 corresponds to a probability below 0.)

$S_b, S_l ≥ 0$ are the stakes on the back and lay bets. Note that $S_l$ is the stake offered by the *other party* to your lay bet; it's the amount you stand to win on that bet, not the amount you stand to lose. This may seem strange, but it's the convention used.

And $C_b, C_l ∈ [0, 1]$ are the commission charged on your winnings on each side. Usually $C_b = 0$: bookmakers don't charge commissions, they make money by offering low odds.

(I'll typically use these symbols by themselves. But when I want to talk about multiple bets, I can use them as functions: $S_l(B_1), S_l(B_2)$.)

A matched bet is one that gives the same profit no matter which side wins; as such, these six values are over-determined. Knowing any five of them will fix the value of the sixth.

Now let $R_{xy}$ (where $x,y ∈ \{b,l\}$) be your return on side $y$ if your bet on side $x$ wins. So for a qualifying bet, we have:

    $$ \begin{align}
         R_{bb} &= S_b (O_b - 1) (1 - C_b)     \\
         R_{bl} &= - S_l (O_l - 1)             \\
         R_{lb} &= - S_b                       \\
         R_{ll} &= S_l (1 - C_l).
    \end{align} $$

For a free bet, the only change is

    $$ R_{lb} = 0. $$

So your profit is $R_{bb} + R_{bl}$ if your back bet wins; and $R_{lb} + R_{ll}$ if your lay bet wins.

**Optimal lay stake**

The first question we'll ask is, given $O_·, C_·$ and $S_b$, what should we choose $S_l$ to be to eliminate all risk? We need

    $$ R_{bb} + R_{bl} = R_{lb} + R_{ll}. $$

Rearranging, we get

    $$ R_{ll} - R_{bl} = R_{bb} - R_{lb}                       \\
       S_l (R_{ll}/S_l - R_{bl}/S_l) = R_{bb} - R_{lb}         \\
       S_l = { R_{bb} - R_{lb} \over R_{ll}/S_l - R_{bl}/S_l } $$

which seems circular, but when we substitute values $S_l$ disappears from the right hand side. For a qualifying bet, this gives

    $$ \begin{align}
        S_l &= { S_b (O_b - 1) (1 - C_b) + S_b \over (1 - C_l) + (O_l - 1) } \\
            &= S_b { O_b + C_b - O_bC_b \over O_l - C_l }.
    \end{align}$$

And for a free bet, we have

    $$ S_l = S_b { (O_b - 1)(1 - C_b) \over O_l - C_l }. $$

A thing to note here is that $O_l$ only appears in the term $O_l - C_l$. In other words, the effect of lay commission is to decrease the effective lay odds in the most natural way. This will show up again, but it's not universal.

**Profit**

Next, we'll want to know how much profit we make. This is given by

    $$ P = R_{lb} + R_{ll} $$

using the lay stake that we just calculated. Under a qualifying bet, this is

    $$ \begin{align}
        P_q &= -S_b + S_l (1 - C_l)                                    \\
            &= S_b(1 - C_l){ O_b + C_b - O_bC_b \over O_l - C_l } - S_b
    \end{align} $$

and for a free bet, it's

    $$ \begin{align}
        P_f &= S_l (1 - C_l)                                           \\
            &= S_b (1 - C_l) (1 - C_b) { O_b - 1 \over O_l - C_l }.
    \end{align} $$

We can look at these functions graphically:

each line represents a contour of the function, a set of points that all have the same profit. The sets of contours look superficially similar, but they're generally steeper for a free bet.

We can reparameterise in terms of $O_b$ and $σ = O_l - O_b$, the spread between the back and lay odds. Since $O_l ≥ O_b$, we only need to consider $σ ≥ 0$. This gives us

    $$ \begin{align}
        P_q &= S_b(1 - C_l){ O_b + C_b - O_bC_b \over O_b + σ - C_l } - S_b
        P_f &= S_b (1 - C_l) (1 - C_b) { O_b - 1 \over O_b + σ - C_l }.
    \end{align} $$

These are more distinct. Looking at these graphs, it seems that for a qualifying bet, having low $σ$ is more significant than having high $O_b$; but for a free bet, having high $O_b$ is more significant than having low $σ$.

**Improving on a free bet**

We can be more precise, and figure out some ways to improve on a bet. Since the two types have different behaviours, we'll treat them separately.

To maximise profit, we usually need to consider that $S_b, C_b$ and $C_l$ are fixed, and find the dependence of $P$ on $O_b$ and $O_l$. For a free bet, that means we want to maximise the term

     $$ P_f ∝ {O_b - 1 \over O_l - C_l}. $$

This tells us several things. The first is that we want high back odds and low lay odds. That's not surprising, but it's also not very helpful; we expect back and lay odds to more-or-less rise and fall together. But it does tell us that adding a constant to both odds will increase profit; odds of 5 and 6 will be better than odds of 4 and 5. (We could also see this on the graph of $P_f(O_b, σ)$.)

If we set $σ = 0$, the term to maximise is

    $$ { O_b - 1 \over O_b - C_l } $$

which takes all values in $[0, 1)$, just as it does when $σ > 0$.

That is, given a free bet $B_1$ with $σ(B_1) ≥ 0$, we can find a free bet $B_2$ with $σ(B_2) = 0$ and $P_f(B_2) = P_f(B_1)$, and $S_b, C_l, C_b$ equal between $B_1$ and $B_2$.

Or: given odds $O_b, O_l$, we can calulate the odds $O'$ that would give you the same profit, if you could find these odds for both a back and a lay bet.

In turn, that tells you that if you want to improve your profits, you can ignore bets with $O_b < O'$. (Because those bets have lower back odds and surely also higher lay odds, and so lower profit.) This is a useful thing to know, that matched bet calculators don't tell you.

To find $O'$:

    $$ { O_b - 1 \over O_l - C_l } = { O' - 1 \over O' - C_l } \\
       (O_b - 1)(O' - C_l) = (O' - 1)(O_l - C_l)               \\
       O'(O_b - 1 - O_l + C_l) = O_bC_l - O_l                  \\
       O' = { O_l - O_bC_l \over 1 + O_l - O_b - C_l }         $$

or

     $$ O' = O_b { 1 - C_l + σ/O_b \over 1 - C_l + σ } $$

which isn't exactly simpler but I think is more aesthetically pleasing (consider that $1-C_l$ is approximately as fundamental as $C_l$ itself).

We can also calculate $O'$ and $P_f$ as functions of each other:

    $$ P_f = S_b (1 - C_l) (1 - C_b) { O' - 1 \over O' - C_l }             \\
       (O' - C_l)P_f = S_b(1 - C_l)(1 - C_b)(O' - 1)                       \\
       O'P_f - O'(S_b(1 - C_l)(1 - C_b)) = C_lP_f - S_b(1 - C_l)(1 - C_b)  \\
       O' = {    C_lP_f - S_b(1 - C_l)(1 - C_b)
              \over P_f - S_b(1 - C_l)(1 - C_b) }                          $$

$P_f$ approaches an asymtote at $S_b (1 - C_l)(1 - C_b)$, but slowly. With $C_b = 0, C_l = 0.02$, extracting 80% of a free bet is only possible if $O_b ≥ 5.36$. For 90%, you need $O_b ≥ 12.03$. Such bets are rare in my experience, and have high spread.
