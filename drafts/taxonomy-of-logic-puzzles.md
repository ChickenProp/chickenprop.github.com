---
title: Towards a Taxonomy of Logic Puzzles
layout: draft
---
(Content note: minor untagged spoilers for the solutions to certain logic puzzles. No major spoilers.)

(Epistemy note: It’s impossible to talk about how easy/hard a puzzle is that I discovered the answer to years ago, sometimes without working it out for myself. I’m about to do that anyway.)

There seems to be some kind of taxonomy for logic puzzles and how hard they are and the sort of strategies that are needed to solve them.

This might be too subjective to be worth talking about, but I suspect not, and the way to find out is to talk about it and see if people understand me, so without further ado:

Let's vaguely pretend that logic puzzles have a sort of fundamental particle which is the *insight*. You collect insights, and then you use insights to collect other insights, and eventually you win.

Now I'm going to describe five types of puzzle.[^types]

**Deep**: For example, the [blue eyes puzzle](https://xkcd.com/blue_eyes.html). I consider this one to be actually pretty easy. You ask what happens with one blue-eyed person, then two, then three, and just proceed by induction. (Even if you don’t know the terms *common knowledge* and *mutual knowledge* and the difference between them, in the two-person case you can say “she tells Alice that Bob can see blue eyes” and in the three-person case you can say “she tells Alice that Bob knows that Carol can see blue eyes” and so on.) There's only one real insight, which you apply lots of times. Or just a couple of times until you get bored and assume/prove the pattern continues.

(I feel like there's a lot of similarity between solving a logic puzzle and proving a math theorem. Here, the math equivalent is proof by induction.)

**Wide**: [Cheryl’s birthday](http://en.wikipedia.org/wiki/Cheryl%27s_Birthday) is also quite easy, but what difficulty it has lies in breadth rather than depth. Every line tells you something new, and you need to extract a different insight from each of them.

(Math equivalent: a theorem with a complicated statement but a proof where every line just reads "because X, Y".)

**Trivial** puzzles are the limiting case of either of the above. I don't know any famous ones, but the blue-eyed puzzle with one blue-eyed person would count.

(Math equivalent: modus ponens.)

**Verify**: Then there are problems where as far as I know you kind of just have to intuit (or guess) the solution, and then demonstrate that it works. (The demonstration is a recursive problem that deserves its own classification, or possibly doesn't even count as a logic puzzle. Often it is just math.[^lmdiff]) The key insight is hidden away, with no hints as to what it might be. The [fork in the road](http://en.wikipedia.org/wiki/Knights_and_Knaves#Fork_in_the_road) is a good example of this, I think, where the demonstration has reasonable claim to being trivial.

It’s a very fuzzy and personal category, because there are patterns that you may be able to recognize which would move it towards **wide**.

(Math equivalent: a proof which introduces some new device that you don't know where it came from, but it turns out to be exactly what you need.)

**Learn**: And there are probably also problems where, if you happen to know the right *thing* and it comes to mind at the right time, this will be **trivial** (or **wide** or...). Otherwise you’ll have to deduce *thing* for yourself, good luck with that. I can’t offhand think of any canonical examples.

This category may be even fuzzier and more personal, and probably overlaps a lot with **verify**, and is hard to detect except in hindsight. (If you can work out what you need to know, it moves towards **wide** or **verify**.)

Of course every puzzle has a *thing* which is the solution to that particular puzzle; and many puzzles rely on the ability to do basic arithmetic or other such skills. Those obviously "shouldn't count" to clasify a puzzle as **learn**, but I don't have a principled way to distinguish them from things that should.

(Math equivalent: a proof in complex analysis that relies on an obscure theorem from number theory.)

---

I don't intend for these descriptions to be fully general. I think that they're pointing at real clusters in puzzlespace, but don't fully capture the essences of those clusters.

Even if they did, I expect these clusters are going to fail to capture a lot of variation, and attempting to shove things into them will sometimes be a silly thing to do. But let's make a start with them, and try to classify some problems that come to mind:

This [transfinite epistemic logic puzzle challenge](http://jdh.hamkins.org/transfinite-epistemic-logic-puzzle-challenge/) is mostly a combination of deep and wide I think, but also some learn because I wouldn't recommend attempting it if you don't know about order types. I didn't find it overly challenging. (Except that reading the solution, I no longer remember if I got the answer exactly correct. I might have made a fencepost error.)

I haven't solved the [sum and product puzzle](http://en.wikipedia.org/wiki/Sum_and_Product_Puzzle), but [as far as I've got](http://lesswrong.com/lw/m1p/open_thread_apr_13_apr_19_2015/c9od) has been a wide. I'm pretty sure I could finish it with brute force,[^brute] but I suspect there's an elegant way to do it which is either a verify or a learn, possibly involving number theory.

[The hardest logic puzzle ever](http://en.wikipedia.org/wiki/The_Hardest_Logic_Puzzle_Ever) is the fork in the road on steroids. Given the solution, proving that that solution works would be a moderately challenging wide puzzle. Generating it from scratch seems to require multiple levels of verify and wide.

The [hundred prisoners problem](http://en.wikipedia.org/wiki/100_prisoners_problem) is very verify. The verification step is a combinatorics problem. (I feel like there are a lot of problems based on having a hundred prisoners and an intellectually peverse gatekeeper, and I feel like most of them are verify. [Here's another example.](http://www.cut-the-knot.org/Probability/LightBulbs.shtml))

[This card trick/puzzle](https://news.ycombinator.com/item?id=9030899) is a verify. (I'm pretty sure I have a solution, but I've only verified it in my head, and I didn't fully work out the details. My solution is very different to the posted one. Arguably, the posted solution has a learn on the pigeonhole principle and mine doesn't.)

The [pirate game](http://en.wikipedia.org/wiki/Pirate_game) is a little deep and not much else.

[Logic grid puzzles](http://www.logic-puzzles.org/) are wide. They differ from Cheryl's birthday in that every clue needs to get used multiple times, but each clue-application is still straightforward. That doesn't mean they're easy.

---

Here are some other features that we might want to talk about.

Logic puzzles often (not always) have a number of characters. Sometimes you know more than/just as much as the characters, and need to work out how each of them will act. Sometimes you know less, and need to work out what they know from how they act.

Sometimes you need to come up with a strategy rather than a specific answer. Sometimes there are multiple strategies. Sometimes there's a foolproof strategy, other times you just need to find one as effective as possible. If that's the case, then it might be difficult to work out exactly how effective it is, even if it seems obviously more effective than the naive strategy; and proving that it's optimal might be harder again. It took three years to prove optimality on the hundred prisoners.

Different puzzles require different "levels" of theory of mind, and I suspect there's a lot of variation in how well people can keep track of those without accidentally collapsing them. "Alfred knows that Bernard doesn't know" might become just "Bernard doesn't know"; and "Alice doesn't know that Bob knows that Carol can see blue eyes" might become just "I have no idea what's going on".

---

Another future direction to explore might be a taxonomy of video game puzzles. I think there'd be some similar themes, but for example, video games can have progression in a sense that doesn't exist in most of the puzzles I've described so far.

Two senses, in fact. You can progress within a level, when you change the board state.[^progress] Different games/levels have different attitudes to (a) how many ways you can do this at any given moment, and (b) whether it's possible to make a level unsolvable.

But also a level can teach you something by holding your hand, and in future levels you can use that without having your hand held. So level ten would have seemed impossible if you'd started with it, but after levels one through nine it's just challenging enough to be fun. Logic puzzles can have this: the fork in the road teaches you a tool to apply to THLPE. But the level order in video games gets to be designed deliberately. Whereas in real life, I mostly encounter logic puzzles by accident, with no guarantee that I've already encountered any precursors.

(When I was playtesting [Sokobond](http://www.sokobond.com/), Alan said that I approach puzzles differently to most people. I think I was thinking along the lines of: "okay, the target molecule will only fit *here*, which means that I need to move into place from *there* which means...". This kind of thinking comes naturally to me, and I think it serves me well, most of the time - though I have known myself to occasionally prove that this particular level can't *possibly* have a solution. It seems well-suited to puzzles with predictable mechanics and clear unwinnable states.)

[^types]: I'm really describing types of *solution*, but I think I can get away with that for the most part.
[^lmdiff]: Though I'm not sure what the difference is.
[^brute]: Brute force seems like it could fit as either verify or deep, or just as a separate category.
[^progress]: For current purposes, not all progress takes you in the right direction.
