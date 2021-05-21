---
layout: draft
title: Logically Inducting Pi
lw_xpost: true
---
The purpose here is to figure out the process by which a logical inductor, following the algorithm laid out in MIRI's paper, would come to learn the digits of pi.

An important note here: a logical inductor is an agent satisfying a certain criterion. The paper describes one algorithm which can implement such an agent, and I'll be looking at that agent. But other logical inductors exist, and would learn in quite a different way.

So. Lily is our logical inductor, and we want to know how she comes to learn the digits of pi. What does that mean?

* What does it mean to be a logical inductor? Prior to that, what type of agent is even capable of being one?
* What does it mean for a logical inductor to know something?

In the language of the paper, a logical inductor is a type of **market**, which is a computable sequence of **pricings**, which assign values to sentences in some logical language.

We'll fix the language as being first-order logic over ZF set theory. So the sentences are things like

* Formulas in ZF directly; $\`\`\\\{\\\} = \\\{\\\}"$ and $\`\`6 > 5"$ and $\`\`5 > 6"$.
* Formulas combined with connectives, like $\`\`\\\{\\\} = \\\{\\\} ∧ ¬(6 > 5)"$.
* Existential and universal quantifiers over these, like $\`\`∀x. ∃y. ∃z. y = {x} ∧ z = {y}"$.
* Anything we can clearly convert into one of the above, like $\`\`\text{twin prime conjecture}"$ for the formula representing the [twin prime conjecture](https://en.wikipedia.org/wiki/Twin_prime#Twin_prime_conjecture). (I already snuck these in by referencing the symbols $5$, $6$ and $>$, which aren't basic. They're grounded in terms of sets and set membership.)

So for any sentence like that, you can ask Lily for her price for that sentence, and she'll give you an answer. But that price might change over time, in discrete timesteps. We might ask for $ℙ_1(\`\`\\\{\\\} = \\\{\\\}")$, Lily's price on day 1 for the formula $\`\`\\\{\\\} = \\\{\\\}"$. Or we might ask for $ℙ_{1943}(\`\`\text{twin prime conjecture}")$, her price on day $1943$ for the formula representing the twin prime conjecture.

This is the *type of agent* that can be a logical inductor. But what does it mean for an agent of this type to actually be a logical inductor?

When we have a "market", we can treat the "prices" as, well, prices in a market, from `$ \$0 $` to `$ \$1 $`. And if we have a market with prices, we might as well have **traders**. Travis the trader, every day, gets to look at the current and historical market prices and buy and sell whatever sentences he wants at current prices.

Actually, that's a bit misleading. Travis, every day, gets to *write a simple function* which will look at the current and historical market prices and execute trades. Travis doesn't know the market prices until he's written the function, and the function is constrained in what it can do. I'm not sure if this is important for a lay understanding, but it's an important technical caveat.

(The amount this function buys of a sentence has to be computable through certain operations on prices. The exact operations aren't super important; let's say we can add prices, multiply them, specify them as rational numbers, and take maximums. We need them to be continuous because it's possible for a sentence to refer to *its own price* in a market. So we can construct a sentence $χ_n = \`\`ℙ_n(χ_n) < 0.5"$. If the function were allowed to look at $ℙ_n(χ_n)$, buy if it's less than $0.5$ and sell otherwise, it would generate guaranteed free money. But if the amount it buys is a *continuous* function of prices, then either it always buys, or always sells, or sometimes does neither. We also need these functions to be, roughly speaking, simple enough to easily write down but expressive enough to be useful. (On those two points, speaking roughly is the best I can do.))

So if Lily changes her prices in a predictable manner, Travis (if he expects to trade against Lily) can extract money from her. Suppose for some sentence $φ$, Lily's price $ℙ_n(φ)$ alternates between $0$ and $1$. (It need not be predictable when her price will change, only that it will never stop changing.) Then Travis on day $n$ can buy $1 - 2ℙ_n(φ)$ shares of $φ$. When her price is $0$, Travis will buy a share for free; when her price is $1$, Travis will sell a share for a dollar; over time, Travis will collect dollars. (He might also collect large amounts of credit or debit in $φ$, if Lily's price is more often one or the other.) Or if Lily's prices only ever rise, Travis can buy now and sell later, and by buying arbitrarily high amounts he can extract an arbitrarily high amount of money.

But also, sentences have value of themselves, which is discovered over time. Suppose someone, Dopey the **decision process**, is chugging along behind the scenes, proving theorems. As soon as Dopey proves that a sentence is a theorem (i.e. true), it's worth `$ \$1 $`. If Dopey proves that a sentence is *not* a theorem (i.e. false), it's worth `$ \$0 $`. For the rest... there's a concept of "propositionally consistent" worlds, where we look at what *might* be true given what we know plus simple Boolean algebra. If the only thing Dopey has proved is $\`\`1\text{ is odd} ∨ 2\text{ is odd}"$ then any of $\`\`1\text{ is odd} ∧ ¬(2\text{ is odd})"$, $\`\`¬(1\text{ is odd}) ∧ 2\text{ is odd}"$, $\`\`1\text{ is odd} ∧ 2\text{ is odd}"$ are p.c. A sentence is worth money according to what fraction of p.c. worlds it's true in. So $\`\`2\text{ is odd}"$ might be worth `$ \${2 \over 3} $` when Dopey proves $\`\`1\text{ is odd} ∨ 2\text{ is odd}"$, then `$ \${1 \over 2} $` when Dopey subsequently proves $\`\`1\text{ is odd}"$, then `$ \$0 $` when Dopey finally proves $\`\`¬(2\text{ is odd})"$.

(Actually, in the paper, sentences are simply worth `$ \$1 $` for each p.c. world they're "true" in - note that a theorem is "true" in *every* p.c. world. My formulation here is more complicated, but maybe gives a better intuition for what's going on?)

So if Lily doesn't change her prices at all, Travis can *still* extract money from her, by buying sentences that Dopey's proved true and selling sentences that Dopey's proved false.

We say that Travis **exploits** Lily, *relative to Dopey*, if the total value of his holdings, considered day-to-day, has a lower bound but no upper bound. For any amount of money, there's some day where his holdings are worth more than that, according to what Dopey knows (and what's p.c. with what Dopey knows) on that day. And there's some amount of money that he never dips below.

And now we can finally say what it means that Lily is a logical inductor, *relative to Dopey*. It means: Travis cannot exploit Lily (relative to Dopey), without thinking for an unreasonably long time every day. If his thinking time on day $n$ is merely polynomial in $n$, he can't exploit Lily (relative to Dopey).

(There's no such thing as simply "a logical inductor", only "a logical inductor, relative to some decision process". But if we know we're talking about Dopey, we don't need to name him every time.)

---

A trader who only sells will always have a positive dollar balance. Does that mean Lily's price for any sentence must approach either $0$ or $1$? What about self-referential sentences? Need to be careful with those but maybe there's no problem. E.g. the price for $χ_n$ from above can approach $0$ or $1$ just fine, for any $n$, because each one is only self-referential at a specific time. I'm not sure what happens if a trader sells $χ_1, χ_2, ...$. Okay, the thing I've missed up until now is that selling a true sentence gives you a positive dollar balance but a negative sentence balance.


Now suppose something is chugging along behind the scenes proving theorems, in such a way that every theorem will eventually be proved. And whenever it proves a theorem, a trader can exchange its shares in that theorem for `$ \$1 $` each, paid by the market.

We look at the set

    $$ \left\{ \mathbb{W} \left(
                 \sum_{i ≤ n} T_i( \overline{\mathbb{V}} )
               \right)
         \middle| n ∈ ℕ^+, \mathbb{W} ∈ \mathcal{PC}(D_n)
       \right\} $$

What is $T_i( \overline{\mathbb{V}} )$? $T_i$ is a trading strategy for day $i$, i.e. a combination of sentences.

$T_i( \overline{\mathbb{V}} )$ is a $ℚ$-combination, an affine combination

    $$ c + α_1φ_1 + ... α_kφ_k $$

of sentences and the amounts paid for them, where $c$ and each $α_k ∈ ℚ$

So the sum of the $T_i$ is also one of these. What does it mean to evaluate $\mathbb{W}$ on it? It's "the value of the trader's net holdings", i.e.

    $$ c + α_1\mathbb{W}(φ_1) + ... + α_k\mathbb{W}(φ_k) $$



So suppose the market has $ℙ_n(\`\`1 = 1") = 0.5$ for all $n$, and the trader buys a share of it every day. So every $T_i = -0.5 + \`\`1 = 1"$. If the decision procedure is complete, there's some least $n$ such that $\`\`1 = 1" ∈ D_n$. So for $i < n$, $\mathbb{W}(T_i(\overline{\mathbb{V}})) = -0.5$ if $\mathbb{W} ∈ \mathcal{PC}(D_i)$. And for $i ≥ n$, it's $+0.5$.

How large is $\mathcal{PC}(D_n)$? Must be finite, right? Is it just size 1?

If $\`\`φ ∨ ψ" ∈ D_n$ but neither $φ$ nor $ψ$ is, there's a $𝕎$ such that $𝕎(φ) = 1$ and one such that $𝕎(ψ) = 1$
