---
layout: draft
title: 'Cliffs Notes: "Probability Theory: The Logic of Science", part 2'
---
A book sometimes cited on LessWrong as recommended reading is E.T. Jaynes' [*Probability Theory: The Logic of Science*](http://www-biba.inrialpes.fr/Jaynes/prob.html). I intend to write a series of posts reading this book, summarizing the key points, and solving the exercises. (There are no solutions in the book.)

The book has over 750 pages. This will take me a long time, if I finish at all. I'm not committing to finishing. For example, if this turns out not to be a thing worth doing, I hope that I will notice that and stop. I'm also not committing to any particular posting rate while I continue.

## Chapter 2: The Quantitative Rules

In [chapter 1](/2014/02/02/cliffs-notes-pttlos-part-1.html), we formulated our problem. In this chapter, we deduce the quantitative rules for inference that follow from  ouur desiderata. To recap, the desiderata can be broadly stated as:

* (I) Representation of degrees of plausibility by real numbers;
* (II) Qualitative correspondance with common sense;
* (III) Consistency.

### 2.1. The product rule

First, let's find a consistent rule relating the plausibility of $AB$ to the separate plausibilities of $A$ and $B$. In particular, let's find $AB|C$.

We should be able to calculate $AB|C$ given $B|C$ and $A|BC$. If our robot thinks about $B$, and decides that it's true, then it will further need $A|BC$ to determine that $A$ is also true. But knowing $B|C$ and $A|BC$, we will not need $A|C$; that wouldn't provide useful information that we don't already know about $AB$. Similarly, we don't need $A|B$ or $B|A$: since we know $C$ is true, it doesn't do us any good to consider what we would know about $A$ and $B$ if $C$ were unknown.

So we should be able to write

    $$ (AB|C) = F[(B|C), (A|BC)] $$

Of course, since $AB = BA$, then we should also be able to use $A|C$ and $B|AC$; and by desideratum (IIIa), using either of these methods should give the same results. Thus we have

    $$ (AB|C) = F[(B|C), (A|BC)] = F[(A|C), (B|AC)]. $$

We can approach this from another direction. For example, suppose instead that

    $$ (AB|C) = F[(A|C), (B|C)]. $$

We can easily see that this fails desideratum (II). Consider the propositions $A$, that the left eye of the next person I meet will be blue; $B$, that her right eye will be blue; and $B'$, that her right eye will be brown. $B$ and $B'$ are both fairly plausible given $C$, my knowledge of the human eye; but $AB|C$ is also fairly plausible, and $AB'|C$ is very implausible.

We are trying to find $AB|C$ as a function of the plausibilities $A|C$, $B|C$, $A|BC$ and $B|AC$. There are $11$ combinations of two or more of these; for nine of them we can find an example where desideratum (II) fails. The two that survive are the ones we already found.

(Jaynes doesn't carry out this analysis himself, but refers us to [Tribus (1969)](http://www.amazon.com/Rational-descriptions-decisions-Pergamon-engineering/dp/0080063934/ref=la_B001HP9MS8_1_1?s=books&ie=UTF8&qid=1394285981&sr=1-1), which I haven't looked up. It's not obvious to me how this process can eliminate certain combinations. For example, there is certainly a function $G[ (A|C), (B|C), (A|BC) ]$ which gives the correct answer merely by ignoring $B|C$. We can present a situation in which $B|C$ changes, the other two remain fixed, and $AB|C$ also remains fixed; but that doesn't tell us that ignoring $B|C$ is *always* correct.)

Following desiderata (I) and (II), we require that $F(x,y)$ is continuous and monotonically increasing in both $x$ and $y$.

Now consider the plausibility $(ABC|D)$. By associativity, we can consider this as either $A(BC)|D = F[ (BC|D), (A|BCD) ]$ or as $(AB)C|D = F[ (C|D), (AB|CD) ]$. By desideratum (III), these two calculations must give the same result. Expanding $(BC|D)$ and $(AB|CD)$ in terms of $F$, we see that

    $$ F[ F[ (C|D), (B|CD) ], (A|BCD) ] = F[ (C|D), F[ (B|CD), (A|BCD) ] ]. $$

So if our robot will reason consistently, $F$ must follow the *associativity equation*

    $$ F( F(x,y), z) = F(x, F(y, z)). $$

At this point, Jaynes proves that there is a function $w$ such that

    $$ w(F(x,y)) = w(x)w(y), \\
       w(AB|C) = w(A|BC)w(B|C) = w(B|AC)w(A|C) $$

which we call the "product rule". You're probably familiar with it already. (It's usually written with a $p$, not a $w$. More on that later.)

I [don't understand the proof](http://math.stackexchange.com/questions/721178/how-do-we-make-this-integration-rigorous): it looks to me like when Jaynes defines $w$, he uses notation that makes it look like a function $ℝ → ℝ$, but it's actually a function $ℝ × (ℝ → ℝ) → ℝ$. (That is, $w$ pretends to turn real numbers into real numbers, but in reality, for $w$ to work you also need to give it another function which *does* turn real numbers into real numbers.) The linked post on math.stackexchange has more detail (and an answer which agrees with me, but no resolution).

However, I shall proceed under the assumption that I have not uncovered a hole in the very foundations of probability theory, and that $w$ is a well-defined function $ℝ → ℝ$.

We now show that if $A|C$ is certain, we must have $w(A|C) = 1$: because in this case $A|BC = A|C$, and $AB|C = B|C$; so we get $w(B|C) = w(A|C)w(B|C)$ for any value of $B|C$. Similarly, if $A|C$ is impossible, we must have either $w(A|C)
= 0$ or $∞$; WLOG we choose by convention that it is $0$.

To clarify what's happened up to this point: we know that the plausibility $AB|C$ can be determined as $AB|C = F(A|BC, B|C)$, where $F$ is some function that we don't actually know. For that matter, we don't even know the values of $A|BC$ or $B|C$, we just decided it would be a good idea for them to be real numbers.

We know that $F$ satisfies certain properties, notably associativity; and it turns out that as long as it does so, its precise definition doesn't matter. Instead of using $F$ directly, we can define a function $w$ in terms of $F$, and if we work with $w$ we have the product rule. $w$ also gives us the familiar rules that $w$ of certainty is $1$, and $w$ of impossibility is $0$.

From now on, there is little or no reason to use bare symbols like $A|C$. Instead we work with $w(A|C)$, and (spoiler alert) soon we'll replace that with the familiar $p$.

### 2.2. The sum rule

Since propositions are always true xor false, we must have that $A\bar A$ is always false, and $A + \bar A$ is always true. The plausibility that $A$ is false must depend on the plausibility that it is true. So there must be some function $S$

    $$ w(A|B) = S(w(\bar A | B)). $$

By common sense, $S$ must be continuous, monotonically decreasing on `$[0,1]$`, and have extreme values $S(0) = 1, S(1) = 0$. Further, $S$ must be consistent with the product rule. We have $w(A\bar B | C) = w(A|C)w(\bar B | AC)$, and $w(B|AC) = S(w(\bar B|AC))$, and it follows that

    $$ w(AB|C) = w(A|C)S(w(\bar B|AC)) = w(A|C)S\left({ w(A\bar B|C) \over w(A|C) }\right). $$

But by symmetry, we must also have

    $$ w(AB|C) = w(BA|C) = w(B|C)S\left({ w(B\bar A|C) \over w(B|C) }\right). $$

This holds for all possible values of $A, B, C$.

Choose some arbitrary proposition $D$, and set $B = \overline{AD}$. Thus, $A\bar B = \bar B$, so $w(A\bar B|C) = S(w(B|C))$; and $B\bar A = \bar A$, so $w(B\bar A|C) = S(w(A|C))$. Substitute $x = w(A|C), y = w(B|C)$ and we get the equation

    $$ xS\left({ S(y) \over x }\right) = yS\left({ S(x) \over y }\right). $$

From this, Jaynes proves that $S$ must have the form

    $$ S(x) = (1-x^m)^{1/m}, $$

for some $m > 0$. (Unlike for the product rule, I confess that I haven't made a proper attempt to follow this proof.)

This was derived using the choice of $B = \overline{AD}$. Thus, this form of $S$ is necessary for our theory to be consistent; but it may be that other choices of $B$ would impose further conditions on $S$. We show that this is not so: substituting into our general equation,

    $$ w(A|C)S\left({ w(A\bar B|C) \over w(A|C) }\right)
           = w(B|C)S\left({ w(B\bar A|C) \over w(B|C) }\right) \\
       w(A|C) \left(1 - { w(A\bar B|C)^m \over w(A|C)^m } \right)^{1/m}
           = w(B|C) \left(1 - { w(B\bar A|C)^m \over w(B|C)^m } \right)^{1/m} \\
       w(A|C)^m \left(1 - { w(A\bar B|C)^m \over w(A|C)^m } \right)
           = w(B|C)^m \left(1 - { w(B\bar A|C)^m \over w(B|C)^m } \right) \\
       w(A|C)^m - w(A \bar B|C)^m = w(B|C)^m - w(B \bar A|C)^m.
    $$

Jaynes says this identity is trivial by virtue of the product rule. I disagree about "trivial". But to continue,

    $$ w(A|C)^m - w(A|C)^m w(\bar B|AC)^m = w(B|C)^m - w(B|C)^m w(\bar A|BC)^m \\
       w(A|C)^m (1 - w(\bar B|AC)^m) = w(B|C)^m (1 - w(\bar A|BC)^m) \\
       w(A|C)^m w(B|AC)^m = w(B|C)^m w(A|BC)^m \\
       w(AB|C)^m = w(BA|C)^m, $$

where the third line follows from the second by applying $S$ again to get $w(X|Y)^m = 1 - w(\bar X|Y)^m$.

That is: $S$ must follow the form that we derived for it, or our general equation fails; and as long as it does follow this form, our general equation holds true. So this form of $S$ is both necessary and sufficient for our theory.

Now, we have already implicitly used an equivalent form of the product rule $w(AB|C)^m = w(A|C)^m w(B|AC)^m$; and we have that $w(A|C)^m + w(\bar A|C)^m = 1$. Thus, we may define $p = w^m$, and we get the familiar forms of the product rule,

    $$ p(AB|C) = p(A|C) p(B|AC), $$

and of a specific case of the sum rule,

    $$ p(\bar A|C) = 1 - p(A|C). $$

In part 1, we noted that conjunction and negation were sufficient to construct any boolean function. Thus, these two rules allow us to calculate the plausibility of any logical proposition. For example, we can calculate the general form of the sum rule:

    $$\begin{equation}
        p(A+B|C) = p(A|C) + p(B|C) - p(AB|C). \label{sumrule}
    \end{equation}$$

If we have four basic propositions `$\{A_1, \ldots, A_4\}$`, there are `$2^4 = 16$` basic conjunctions (such as `$A_1A_2\bar{A_3}A_4$`). If the background knowledge is enough to determine the plausibilities of these conjunctions, repeated application of the sum rule allows us to determine the plausibility of any of the `$2^{16} = 65536$` propositions generated by the `$A_i$`. We'll rarely need that much information, though; knowing the plausibility of just a few basic conjunctions may be enough for our purposes in any given calculation.

---

**Exercise 2.1.** Is it possible to find a general formula for $P(C|A+B)$, analogous to (\ref{sumrule}), from the product and sum rules? If so, derive it; if not, explain why this cannot be done.

**Answer.**

There's no particular reason we would expect one, since the $|$ notation isn't symmetrical. And it intuitively feels unfair to ask someone, "either it is raining or my sprinkler is on. How plausible is it that the sun is shining?" In one case, it is implausible; in another case, it is quite plausible; but without knowing which case we are in, how can we answer?

Still: suppose that despite our intuition, we could find a general formula. This formula would have to work for any values of $A$, $B$ and $C$. In particular, it would have to work in the case $B = \bar A$. But then $A+B$ gives us no information at all, and $P(C|A+B)$ is simply asking "how plausible is C, given no knowledge at all?" We have no way to answer this question, so the general formula cannot exist.

---

**Exercise 2.2.** Now suppose we have a set of propositions `$\{A_1, \ldots, A_n\}$` which on information $X$ are mutually exclusive: `$p(A_iA_j|X) = p(a_i|X)\delta_{ij}$`. Show that `$p(C|(A_1 + A_2 + \ldots + A_N)X)$` is a weighted average of the separate plausibilities `$p(C|A_iX)$`:

    $$ p(C|(A_1 + \ldots + A_n)X) = p(C|A_1X + \ldots + A_nX)
        = { \sum_i p(A_i|X)p(C|A_iX) \over \sum_i p(A_i|X) } $$

**Answer.**

(To come later.)

---

### Qualitative properties

We started with two syllogisms of deductive logic. These can be written in our new notation. For example, consider the syllogism: "$A$ implies $B$; $A$; therefore $B$". Let $C$ stand for the background knowledge $A \Rightarrow B$. Then we have the premise $AC$, and by the product rule,

    $$ p(B|AC) = { p(AB|C) \over p(A|C) } $$

But $C$ says that $p(AB|C) = p(A|C)$, and so we have $p(B|AC) = 1$. That is, the deductive syllogism follows as a specific case of our rules for plausible reasoning. Similarly, $p(A|\bar{B}C) = 0$, corresponding to the other deductive syllogism.

We can also express the weak syllogisms, but now we have quantitative forms of them. For example, we have

    $$ p(A|BC) = p(A|C) { p(B|AC) \over p(B|C) } $$

where $p(B|AC) = 1$ and $p(B|C) \le 1$, so that

    $$ p(A|BC) \ge p(A|C) $$

corresponding to the weak syllogism "$A$ implies $B$; $B$; therefore $A$ becomes more plausible".

The policeman's still-weaker syllogism was: "if $A$ is true, $B$ becomes more plausible; $B$; therefore $A$ becomes more plausible". $C$ now becomes background information, and we have the premise $p(B|AC) > p(B|C)$. This once again gives us $p(A|BC) > p(A|C)$.

But now we can quantify how much effect $B$ has on $A$. Our policeman made a large update, from $A|C$ being very implausible to $A|BC$ being very implausible. This can only happen when $p(B|AC) / p(B|C)$ is large, which in turn requires $p(B|C)$ to be small.

### Numerical values

We've found the most general consistent rules for manipulating plausibilities that our robot might use. But our job is not yet finished.

For starters, the product and sum rules limit how plausibilities must be related to each other. We have found that a function $p$ exists relating the plausibilities $A|C, B|C, A+B|C, AB|C$, etc. in a certain way. But it seems that we haven't found any unique rules. The values of $A|C$ etc. are still undetermined; whatever they happen to be (subject to desideratum (II)), we can find a continuous monotonic $p$ to relate them, and vice versa. So for every possible such $p$, it seems that there is a different set of rules for plausible reasoning.

Secondly, we can find plausibilities *in terms of others*, but we have no way to get started with a problem by assigning plausibilities based on the background knowledge.

We begin to solve the second problem as follows: suppose we have propositions `$A_1, \ldots, A_n$` which are mutually exclusive and exhaustive given background knowledge $B$. That is, precisely one of the `$A_i$` must be true. It follows easily that

    $$ p(A_1 + \ldots + A_n|B) = \sum_{i=1}^n p(A_i|B) = 1. $$

We now see that if $B$ is indifferent between the `$A_i$` - that is, if anything $B$ says about one, it says about the others, so that the robot has no reason to prefer one over the others - then all the `$A_i$` must be equal. (This seems intuitively obvious, but Jaynes warns us to avoid intuition, and constructs an actual argument.) Thus,

    $$ p(A_i | B) = { 1 \over n } $$

giving us our first set of definite numerical values. This is called the *principle of indifference*.

This also solves our first problem. The information given to the robot determines the value `$p(x) = p(A_i|B)$`, not the value `$x = A_i|B$`. Whatever the value of $x$, we shall find $p(x)$ to be the same. Until now, we have considered $p$ to be an arbitrary monotonic function of $x$; but instead, we can say that $x$ is an arbitrary monotonic function of $p$, where $0 \le p \le 1$. Since the values of $p(x)$ are fixed by the data, there is only one set of consistent rules to reason by.

Having discovered this, we finally apply the name *probability* to the quantities $p(x)$. The word has an imprecise colloquial meaning, but we use it in a technical sense; and we can only justify that now, having determined that the $p(x)$ have a precise meaning.

