---
title: "The Farmer's Dilemma"
layout: draft
---
I could have sworn that the farmer's dilemma was a standard term in game theory, much like the [prisoner's dilemma](http://en.wikipedia.org/wiki/Prisoner%27s_dilemma). Apparently it isn't. But I think it would be a useful term to have, so I'm writing about it so that if I need to use it in future I can link people here.

Suppose you and I are farmers, owning adjacent fields. One day you have a brilliant idea. If we dig a ditch from the nearby river, between our fields, then irrigating our fields becomes a lot less work. It would cost two utils to dig the ditch - one utilon each - and we'd get five utils each from its existence.

You come to me with this suggestion. "That sounds great," I say, "but I don't think I'm going to bother."

You object that I'm being dumb not to take those four utils.

"No," I say, "I just think that if I don't help you, you'll do all the work yourself. You still get three utils if you dig it alone, so you'll do it even if I don't help you. And by not helping, I get five utils instead of four. Why would I pay a utilon to help you?"

(Unfortunately for you, I am a member of [*H. economicus*](http://en.wikipedia.org/wiki/Homo_economicus) and have a natural immunity to arguments about "fairness" and "not being a douchebag".)

---

The farmer's dilemma is game-theoretically equivalent to [chicken](http://en.wikipedia.org/wiki/Chicken_%28game%29). Both of us choose to either cooperate by digging the ditch ("swerve" in chicken), or defect by sitting at home ("straight" in chicken). If both of us cooperate ("C/C"), we both get an okay result. If both of us defect ("D/D"), we both get a terrible result. If one of us cooperates while the other defects ("C/D"), then the defector gets the best possible result for themselves, and the cooperator gets a result between C/C and D/D.

If you're cooperating and I'm defecting (or vice versa), then neither of us have any incentive to change our strategies. I could start to cooperate, but then I'd just be giving you utility. You'd like that, but I wouldn't. And you could start to defect, but then you'd be throwing away utility, neither of us would like that.

On the other hand, if we're both cooperating, then we both have an incentive to defect, as long as the other doesn't do the same; and if we're both defecting, we both have an incentive to cooperate, as long as the other doesn't do the same.

(Formally, there are two [Nash equilibria](http://en.wikipedia.org/wiki/Nash_equilibrium), at C/D and at D/C. This distinguishes it from the prisoner's dilemma, which has an equilibrium at D/D.)

(Although the games are game-theoretically equivalent, I think our intuitions about them are different. At any rate, mine are. This is at least partly because game theory defines utility only up to affine transformations. In the real world, two people crashing is a much worse outcome than two people failing to dig a ditch.)

---

There are lots of ways this story can continue.

In one of them, you dig the ditch yourself. Months later, after harvesting and selling your crop, you sit in the pub complaining that being a farmer is such hard work, you've only come out with three utils of profit this year. Nobody's very sympathetic, because they're comparing you to me, and I've made a cool five utils. Because this is a thought experiment, there's no difference between us other than how we act. So *obviously* you're doing something wrong.

In another possible continuation, you threaten to burn some of my crops if I don't help you dig. Maybe I help you, maybe not; if not, maybe you were bluffing, maybe not; if not, maybe I call the police on you and you go to jail; or maybe I do help you, but I secretly recorded the conversation and leak it to the press later on... a lot of things can happen. Even if this works out great for you, it's at least a *little* villainous.

Instead of being so blunt, you might choose to convince *everyone else* to threaten me. Perhaps you dig the ditch, and then talk to our local government and convince them that you should be allowed to extract rent on it.

Another option is to tell me that if I don't help you dig, you'll spend an extra utilon to build a brick wall on my side of the ditch, so that it doesn't do me any good. If I believe that you'll do it, I'm likely to go ahead and help.

You can also tell me that if I don't help, you're not going to dig at all. Or even that you're simply not going to dig, if I'm going to be an asshole about it I can dig the whole thing myself or go without. Once again, I'm likely to dig if I think you're not bluffing.

---

Of course there are lots of variations on the farmer's dilemma.

Maybe I have a bad back, and digging is more costly for me than for you. This may or may not change the Nash equilibria, and it may or may not change the amount of sympathy we each get in the various continuations.

Sometimes there are lots of farmers. In this case, the ditch might cost more to dig than the value it provides to any individual, so that nobody will want to dig by themselves; but little enough that you don't need literally everyone to dig before it becomes valuable, so that everyone still wants to defect individually.

Sometimes the ditch might be an agent in its own right. For example, a company might perform R&D only if someone funds them to do so; and everyone wants them to do it, but would prefer that someone else pays.

(They might not have an explicit agreement for funding with anyone, but acausal trade and early adopters and so on.)

(And having developed a super-awesome version of their product, they might also sell a cheaper version, where they've gone out of their way to disable some of the features. This is like building part of a brick wall against people who only contribute a little to the digging.)
