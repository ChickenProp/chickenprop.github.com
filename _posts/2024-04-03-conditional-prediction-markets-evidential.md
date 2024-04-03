---
title: "Conditional prediction markets are evidential, not causal"
layout: post
tags: [math, rationality]
external_comments:
  - name: LessWrong
    url: https://www.lesswrong.com/posts/vrEA6taJZtSoQbyPA/
---
Quick note about a thing I didn't properly realize until recently. I don't know how important it is in practice.

tl;dr: Conditional prediction markets tell you "in worlds where *thing* happens, does *other-thing* happen?" They don't tell you "if I make *thing* happen, will *other-thing* happen?"

Suppose you have a conditional prediction market like: "if Biden passes the DRESS-WELL act, will at least 100,000 Americans buy a pair of [Crocs](https://en.wikipedia.org/wiki/Crocs#Products) in 2025?" Let's say it's at 10%, and assume it's well calibrated (ignoring problems of liquidity and time value of money and so on).

Let's even say we have a pair of them: "if Biden doesn't pass the DRESS-WELL act, will at least 100,000 Americans buy a pair of Crocs in 2025?" This is at 5%.

This means that *worlds where Biden passes the DRESS-WELL act* have a 5pp higher probability of the many-Crocs event than worlds where he doesn't. (That's 5 [percentage points](https://en.wikipedia.org/wiki/Percentage_point), which in this case is a 100% higher probability. I wish we had a symbol for percentage points.)

It does not mean that *Biden passing the DRESS-WELL act* will increase the probability of the many-Crocs event by 5pp.

I think that the [usual notation](https://en.wikipedia.org/wiki/Causal_model#Intervention) is: prediction markets tell us

    \[ P(\text{many-Crocs}\, | \,\text{DRESS-WELL}) = 10\% \]

but they don't tell us

    \[ P(\text{many-Crocs}\, | \mathop{do}(\text{DRESS-WELL})) = \, ?\% \]

One possibility is that "Biden passing the DRESS-WELL act" might be correlated with the event, but not causally upstream of it. Maybe the act has no impact at all; but he'll only pass it if we get early signs that Crocs sales are booming. That suggests a causal model

    \[   \text{early-sales}
       → \text{many-Crocs}
       → \text{DRESS-WELL}
       ← \text{early-sales}
    \]

with

    \[ P(\text{many-Crocs}\, | \mathop{do}(\text{DRESS-WELL}))
       = P(\text{many-Crocs})
    \]

(I don't know if I'm using causal diagrams right. Also, those two "early-sales"es are meant to be the same thing but I don't know how to draw that.)

But here's the thing that triggered me to write this post. **We can still get the same problem if the intervention is upstream of the event.** Perhaps Biden will pass the DRESS-WELL act if he thinks it will have a large effect, and not otherwise. Let's say the act has a 50% chance of increasing the probability by 3pp and a 50% chance of increasing it by 5pp. Biden can commission a study to find out which it is, and he'll only pass the act if it's 5pp. Then we have

    \[   \text{size-of-impact}
       → \text{many-Crocs}
       ← \text{DRESS-WELL}
       ← \text{size-of-impact} \\
    
       P(\text{many-Crocs}\, | \mathop{do}(\text{DRESS-WELL})) = \, 9\%
    \]

I expect that sometimes you want to know the thing that prediction markets tell you, and sometimes you want to know the other thing. Good to know what they're telling you, whether or not it's what you want to know.

Some other more-or-less fictional examples:

* If Disney sues Apple for copyright infringement, will they win? A high probability might mean that Disney has a strong case, or it might mean that Disney will only sue *if* they decide they have a strong case.
* If the Federal Reserve raises interest rates, will inflation stay below 4%? A high probability might mean that raising interest rates reliably decreases inflation; or it might mean that the Fed won't raise them *except in the unusual case* that they'll decrease inflation.
* If I go on a first date with this person, will I go on a second? A high probability might mean we're likely to be compatible; or it might mean she's very selective about who she goes on first dates with.
