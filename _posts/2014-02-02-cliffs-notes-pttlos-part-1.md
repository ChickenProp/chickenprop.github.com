---
layout: post
title: 'Cliffs Notes: "Probability Theory: The Logic of Science", part 1'
---
A book sometimes cited on LessWrong as recommended reading is E.T. Jaynes' [*Probability Theory: The Logic of Science*](http://www-biba.inrialpes.fr/Jaynes/prob.html). I intend to write a series of posts reading this book, summarizing the key points, and solving the exercises. (There are no solutions in the book.)

The book has over 750 pages. This will take me a long time, if I finish at all. I'm not committing to finishing. For example, if this turns out not to be a thing worth doing, I hope that I will notice that and stop. I'm also not committing to any particular posting rate while I continue.

## Preface

Jaynes starts by telling us the audience of his book: readers with some knowledge of applied math "at the advanced undergraduate level or preferably higher". Prior experience with statistics and probability is unnecessary and might be harmful.

Next we get a brief history of the book. The rules of probability theory have been known for centuries, but in the mid 20th century, these were discovered to be rules for statistical inference in general, unique and inescapable. You cannot violate them without producing absurdity. These discoveries interested Jaynes, and he started giving lectures on them, and eventually they turned into a book.

Jaynes contrasts his system of probability with that of Kolmogorov and de Finetti. Kolmogorov's system looks totally different, but Jaynes finds himself agreeing with it on all technical points, and considers it merely incomplete. De Finetti's system looks similar to Jaynes', but has very little agreement on technical matters. (I don't know what Kolmogorov's and de Finetti's systems actually look like.)

One point is touched on briefly, which I think will become a large theme of the book: infinite set paradoxes. Jaynes claims that these appear to come about because of failure to properly define the objects we're working with. In Jaynes' system, an infinite set can only be specified as a well-behaved limit of finite sets. Sometimes you can arrive at the same set in two different ways, and you can ask questions of it which depend on the limiting process used; but if the limiting process is specified, answers become unique and paradoxes disappear.

PTTLOS is sometimes hailed as a champion of Bayesian statistics over frequentist ones, and indeed we learn Jaynes' view on the dispute. He has always been Bayesian, but previously it was for philosophical reasons. Now he claims that theorems and worked-out examples demonstrate Bayesian superiority independent of philosophy. But he also says that neither is universally applicable, and that both methods fall out as special cases of Jaynes' approach.

Frequentist methods have certain problems; Bayesian methods correct these problems, but can only be applied with a certain amount of knowledge of the problem at hand. The "principle of maximum entropy" provides enough structure to use Bayesian methods when we lack knowledge.

Jaynes claims that probability theory also models certain aspects of human reasoning. Someone who tells the truth, and whose listeners are reasoning consistently, but who is not believed. A policy debate where discussion of the issues causes society to polarize into two camps with no middle ground, rather than to bring about a consensus as might naively be expected.

The work is not intended to be merely abstract, and Jaynes gives an example of practical applications in safety concerns. We might discover that a substance is harmful at certain doses, and it might be natural to assume a linear response curve: half the dose is half as harmful. But knowing a little about biology tells us that this will be untrue in many cases; there will be a threshold level, below which the substance is eliminated as fast as it enters the body and causes no ill effects. Using a model which ignores the possibility of threshold levels can lead to false conclusions, however good our data is.

Finally in the preface, we are told the style of presentation of the work. Most chapters in part 1 start with verbal discussion of the nature of a problem, before getting into the math (which Jaynes considers the easy part, for many students). Part 2 is more advanced, and chapters open directly with math. Jaynes places an emphasis on intuitive understanding over (but not replacing) mathematical rigor.

## Chapter 1: Plausible Reasoning

### 1.1. Deductive and plausible reasoning.

Suppose a policeman hears a burglar alarm, sees a broken shop window, and a man in a mask climbing out of that window with a bag of jewelry. The policeman will decide that the masked man is dishonest. But this cannot come from purely deductive reasoning: it may be that the man is the owner, on his way home from a masquerade party, and that someone else broke the window and he is merely protecting his own property.

Deductive reasoning follows from two familiar syllogisms: "A implies B; A; therefore B" and "A implies B; not-B; therefore not-A". We often don't have the necessary information to apply these.

There are two weaker syllogisms which we use in inferential reasoning: "A implies B; B is true; therefore A *becomes more plausible*", and symmetrically, "A implies B; A is false; therefore B *becomes less plausible*".

(These are related to fallacies of deductive reasoning which say: "A implies B; B; therefore A" and "A implies B; not-A; therefore not-B". But deductive reasoning has only the states "certain", "impossible" and "unknown". Inferential reasoning is more subtle, and lets us say "A becomes more plausible" without saying "A becomes certain".)

The word "implies" is meant to indicate *logical* consequences, not *physical* ones. We might say: "if it will start to rain by 10 AM at the latest, then the sky will become cloudy before 10 AM". The rain at 10 AM can hardly be the cause of the clouds before 10 AM. Clouds cause rain, but uncertainly so, so we cannot say "clouds imply rain". "Rain implies clouds" is a true logical connection, but not (directly) a causal one.

And there is a still weaker syllogism which the policeman uses: "if A is true, then B becomes more plausible; B is true; therefore A becomes more plausible". Concretely, "if a man is a burglar, then it becomes more likely that he will wear a mask and climb out of a broken window carrying a bag of jewelry. He is wearing a mask and climbing out of a broken window carrying a bag of jewelry; therefore it becomes more likely that he is a burglar." The syllogism may seem weak abstractly, but we accept that the man is almost certainly a burglar.

(Jaynes does not here mention the natural sixth syllogism: "if A is true, then B becomes more plausible; A is false; therefore B becomes less plausible". But of course this is true too.)

Deductive reasoning is nice, because it never loses strength. An arbitrarily long chain of deductive inferences, if our premises are certain, will produce a certain result. Inferential reasoning does not permit this, but we will still be able to approach near-certainty in many cases, such as with the policeman and the probably-burglar.

### 1.2. Analogies with physical theories

Jaynes analogizes our study of common sense to that of physics. It's too complicated to learn everything all at once, but sometimes we produce a mathematical model that reproduces some features of our observations, and we consider this progress. We expect our models to be replaced by more complete ones in future. We don't expect that the most familiar aspects of mental activity will be the easiest to model.

### 1.3. The thinking computer

In principle, a machine can do anything that a human brain can do. Proof by existence: the human brain does it. If we don't know how to make a machine do something, it's because we don't know how to describe the thing in sufficient detail. This is also true of "thinking".

But as we study common sense, we're going to start to learn about thinking in more detail than we currently have. Whenever we make a mathematical model of some aspect of common sense, we can write a computer program to apply this model.

If we have two very different hypotheses, unaided common sense might be enough to choose one over the other. If we have a hundred similar ones, we need a computer, and we need to know how to program it. Our goal is to develop the theory that lets us program it correctly to solve such problems, in as much depth and generality as we can manage.

Talking about machines is also useful for keeping ourselves focused. The reasoning process actually used by human brains is complicated and obscure, and hard to talk about without becoming side tracked. But we're not trying to explain or emulate a human brain. We're speaking normatively, not descriptively.

Up until now we've been asking how to build a mathematical model of human common sense. A better question would be: how can we make a machine carry out plausible reasoning, following clear principles that express an idealized common sense?

### 1.4. Introducing the robot

To keep our attention focused, we're going to invent an imaginary robot. We design its brain as we see fit, and we see fit to make it reason according to definite rules. We choose the rules according to desiderata that seem like they would be desirable in human brains: if a rational person discovered that they were violating one of these desiberata, they would wish to revise their thinking.

Our robot reasons about propositions, and for now we restrict it to unambiguous true-or-false propositions. We don't require their truth or falsehood to be easy, or even possible, to establish with certainty, but it must be clear what truth and falsehood actually mean. For example, Jaynes considers both of these propositions to be true:


```
$$\begin{aligned}
A ≡ & \text{Beethoven and Berlioz never met.}\\
B ≡ & \text{Beethoven's music has a better sustained quality than that of}\\
    & \text{Berlioz, although Berlioz at his best is the equal of anybody.}
\end{aligned}$$
```

Our robot can think about proposition `$A$`, although its truth or falsehood probably can't be established today. But for now, `$B$` is off-limits. Later we'll see whether this restriction can be relaxed, and our robot can help with propositions like `$B$`. ("See chapter 18 on the `$A_p$` distribution.")

### 1.5. Boolean algebra

At this point Jaynes briefly introduces Boolean algebra. I assume the reader is familiar with it, but I note that we denote conjunction (logical AND) by `$AB$`, disjunction (logical OR) by `$A+B$`, and denial (logical NOT) by `$\bar A$`. `$≡$` means "equals by definition".

Also, a brief reminder of certain identities:

* **Idempotence**: `$AA = A+A = A$`.
* **Commutativity**: `$AB = BA$`; `$A+B = B+A$`.
* **Associativity**: `$A(BC) = (AB)C = ABC$`; `$A+(B+C) = (A+B)+C = A+B+C$`.
* **Distributivity**: `$A(B+C) = AB + AC$`; `$A + (BC) = (A+B)(A+C)$`.
* **Duality**: `$\overline{AB} = \bar A + \bar B$`; `$\overline{A+B} = \bar A \bar B$`.

If `$A=B$`, by which we mean that `$A$` and `$B$` are logically equivalent, then `$A$` and `$B$` must also be equally plausible. This seems obvious, but Jaynes notes that Boole himself got it wrong.

As usual, `$A ⇒ B$` means "`$A$` implies `$B$`", i.e. `$A+\bar B$`. Remember that this is a much narrower statement than it would be in ordinary language; it doesn't mean that there is any actual connection between `$A$` and `$B$`.

### 1.6. Adequate sets of operations

We have four operations (AND, OR, NOT and IMPLIES) that we can apply to propositions. We can use these to generate many new propositions, but two questions occur to us. Firstly, are there propositions defined from `$A$` and `$B$` that we can't represent using these operations? Secondly, can we reduce the number of operations without losing any propositions that we can currently generate?

We answer the first question no: any logical function on `$n$` variables (of which there are `$2^{2^n}$`) can be written as a disjunction of conjunctions of arguments and their negations. Each conjunction includes every argument precisely once, either purely or negated, and is true at precisely one point of its domain. For example, `$AB\bar C + \bar A \bar B C + \bar A B \bar C$`. There is one semi-exception, where we have zero conjunctions (the function which is constantly false), and this can be written `$A\bar A$`.

We answer the second question yes: it is clear from the previous answer that IMPLIES is unnecessary, and from duality that we can do away with either (but not both) of AND and OR. We can't reduce either of the sets (AND, NOT) or (OR, NOT), but there are two operators which suffice by themselves: NAND, `$A↑B = \overline{AB}$`, and NOR, `$A↓B = \overline{A+B}$`.

### 1.7. The basic desiderata

We now move on to our extension of logic. This will follow from the conditions to be discussed in this section. We don't call them "axioms" because we're not asserting that they're true, just that they appear to be desirable goals. In chapter 2 we'll discuss whether the goals are contradictory, and whether they determine any unique extension of logic.

Our robot must assign a degree of plausibility to each proposition that it thinks about, based on the evidence it has available. When it collects new evidence, it must update these degrees of plausibility. To store these plausibility assignments in the brain, they have to be associated with some physical quantity, such as a voltage level. This means there must be some kind of association between degrees of plausibility and real numbers. Thus we have

* **Desideratum (I)**. Degrees of plausibility are represented by real numbers.

This is motivated by physical necessity, but appendix (A) shows that it's also a theoretical necessity.

Being more specific, two other properties of this representation will be useful. Firstly, that a greater degree of plausibility is represented by a greater real number. And secondly, continuity; this is difficult to state precisely yet, so we say it intuitively: an infinitesimally greater plausibility should correspond to an infinitesimally greater number.

The plausibility assigned to a proposition will often depend on whether some other proposition is true. We use the symbol `$A|B$` to denote "the conditional plausibility that `$A$` is true, given that `$B$` is true", or "`$A$` given `$B$`". We also have, for example, `$A | BC$`, the plausibility of `$A$` given that `$B$` and `$C$` are true; and `$A+B \mid CD$`, the plausibility that at least one of `$A$` and `$B$` is true, give that both of `$C$` and `$D$` are true; and so on.

(I mildly dislike this notation, myself, but we're stuck with it. I think the problem is spacing: the way it's usually typeset, `$A + B | CD$` looks like it should be parethesised `$A + (B|(CD))$` rather than `$(A+B)|(CD)$`. I prefer to have more whitespace around operators with low precedence.)

We're not going to attempt to define constructions like `$A|B$` when `$B$` is impossible; for example, if we write `$A|BC$`, we are implicitly assuming that `$B$` and `$C$` are compatible.

We want our robot to think in a way which is qualitatively like the way humans try to reason, as described by the above weak syllogisms and similar ones. So suppose the robot has prior information `$C$` which gets updated to `$C'$` such that the plausibility for `$A$` is increased, but the plausibility of `$B$` given `$A$` does not change:

    $$ A|C' > A | C; \\
       B|AC = B|AC'. $$

This can never decrease the plausibility that both `$A$` and `$B$` are true:

    $$ AB | C' ≥ AB | C $$

This doesn't say anything about *how much* the plausibilities change, but it gives a sense of direction. These qualitative requirements will be stated explicitly in chapter 2; for now we sum them up as

* **Desideratum (II)**. Qualitative correspondance with common sense.

Finally, we wish our robot to reason consistently. By this we mean

* **Desideratum (IIIa)**. If a conclusion can be reasoned out in more than one way, then every possible way must lead to the same result.
* **Desideratum (IIIb)**. The robot always takes into account all of the evidence it has relevant to a question. It does not arbitrarily ignore some of the inormation, basing its conclusions only on what remains. In other words, the robot is completely nonideological.
* **Desideratum (IIIc)**. The robot always represents equivalent states of knowledge by equivalent plausibility assignments. That is, if in two problems the robot's state of knowledge is the same (except perhaps for the labeling of the propositions), then it must assign the same plausibilities in both.

Desiderata (I), (II) and (IIIa) are structural requirements on the robot's brain, while (IIIb) and (IIIc) show how the robot should relate to the outside world.

It turns out that these are all the desiderata we need. There is only one set of mathematical operations for manipulating plausibilities which satisfies all of them; they uniquely determine the rules by which our robot must reason. These rules will be deduced in chapter 2.

### 1.8. Comments

Our robot's mental state about any proposition is going to be represented by a real number. A human's mental state is much more complicated: we judge propositions as being plausible, desirable, amusing, etc. A human's mental state might be better represented as a many-dimensioned vector of real numbers.

Unemotional propositions like "the refractive index of water is less than 1.3" can be represented with fewer dimensions than propositions like "your mother-in-law just wrecked your new car". The situations we encounter in real life are often the ones requiring many coordinates. This may help explain why human reasoning about such situations is hard to model; and why math and science (dealing with propositions that generate simple mental states) are so successful.

Many of these coordinates are not useful to us. We don't want our robot to get bored with a lengthy problem, or to get confused by emotional factors. But there is a large unexplored area of possible generalizations of the theory that we'll be developing, which could more accurately model actual human brains.

#### 1.8.1. Common language vs. formal logic

Ordinary language, if used carefully, does not need to be less precise than formal logic. But it's more complicated, giving it richer possibilities of expression. In particular, it has many ways to imply something without saying it, which are lost on formal logic. The claim "I believe what I see" and the retort "he doesn't see what he doesn't believe" would have the same meaning in formal logic, but convey opposite meanings in common language.

Another example is that the word "is" is not commutative in common language. This example is taken from a math textbook: consider a straight line in the plane, and an infinite set of points in the plane, and the projections of the points onto the line. Then the statements

* The projection of the limit is the limit of the projections
* The limit of the projections is the projection of the limit

Are not considered equivalent. The projections may have a limit while the points themselves do not (but not vice versa). The first statement implicitly asserts that the points have a limit, and is true conditional on that premise; the second implicitly asserts only that the projections have a limit, and is false.

We can also distinguish between two different senses of the word "is". The epistemological sense, "the room is noisy", expresses something about the speaker's perception. The ontological sense, "there is noise in the room", asserts the physical existence of something. Mistaking one's thoughts and sensations for external realities is called the "mind projection fallacy", and causes much trouble in probability theory and elsewhere.

(This is Jaynes' way of reminding us that [the map is not the territory](http://en.wikipedia.org/wiki/Map%E2%80%93territory_relation). It is not meant to imply that one's thoughts and sensations are completely unrelated to the real world.)

We will not attempt to make our robot grasp common language.

#### 1.8.2. Nitpicking

Sometimes people question the second strong syllogism, "A implies B; not-B; therefore not-A". But Jaynes is happy to use it, noting among other things that if we exhibit a counterexample to a supposed theorem, then the supposed theorem is considered disproved. A new logic might lead to results which Aristotelian logic can't talk about, and that's just what we're trying to create here. But if a new logic was found to disagree with Aristotelian logic, then we would consider that a fatal flaw in the new logic.

There are attempts to develop multiple-value logics. But arguments presented in appendix A suggest that there is no new content in these. An `$n$`-valued logic applied to a set of propositions is equivalent to a two-valued logic applied to a larger set; or it is inconsistent.
