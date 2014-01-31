---
layout: draft
title: 'Cliffs Notes: "Probability Theory: The Logic of Science", part 1'
---
A book sometimes cited on LessWrong as recommended reading is E.T. Jaynes' *Probability Theory: The Logic of Science*. I intend to write a series of posts reading this book, summarizing the key points, and solving the exercises. (There are no solutions in the book.)

The book has over 750 pages. This will take me a long time, if I finish at all.

## Preface

Jaynes starts by telling us the audience of his book: readers with some knowledge of applied math "at the advanced undergraduate level or preferably higher". (At the time I write this, I've read up to part way through chapter four, and so far I think "advanced undergraduate" is more knowledge than you need.) Prior experience with statistics and probability is unnecessary and might be harmful.

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
$$
A ≡ \text{Beethoven and Berlioz never met.}\\
B ≡ \text{Beethoven's music has a better sustained quality than that of\\
          Berlioz, although Berlioz at his best is the equal of anybody.}
$$
```

Our robot can think about proposition `$A$`, although its truth or falsehood probably can't be established today. But for now, `$B$` is off-limits. Later we'll see whether this restriction can be relaxed, and our robot can help with propositions like `$B$`. ("See chapter 18 on the `$A_p$` distribution.")
