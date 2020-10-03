---
title: Specialized Labor and Counterfactual Compensation
layout: draft
---
I have two purposes in this post. The first is to review the formal game theory found in Robert Ellickson's *Order Without Law*. It's not a large part of the book, but it's the part that I'm most qualified to judge. Not that I'm a formal game theorist myself, but I'm closer to one of them than any kind of social scientist, historian or lawyer. If his formal game theory is nonsense, that would suggest that I ought to discount his writing on other fields, too. (Perhaps not discount it completely, especially because formal game theory is outside his main area of study. Then again, lots of the book is outside his main area of study.)

Spoiler alert: I think he holds up reasonably well. I want to ding him a few points, but nothing serious, and he possibly even contributes a minor original result.

My second purpose, which is valuable for the first but also valuable of itself, is to try to extend it further than Ellickson did.

Ellickson discusses two games. One is the classic Prisoner's Dilemma, in which you either Cooperate (for personal benefit but social cost) or Defect (for personal cost but social benefit). Note that Ellickson specifies Cooperate/Cooperate as having more total utility than Cooperate/Defect or Defect/Cooperate; I consider this [correct](http://reasonableapproximation.net/2020/07/04/classifying-games-like-prisoners-dilemma.html), but not all authors include that condition.

The other he calls Specialized Labor, in which two people must choose whether to Work on some common project or Shirk their share of it. It differs from the Prisoner's Dilemma in two ways. First, it's asymmetrical; one player is a less effective worker than the other, and gets less payoff from Working while the other Shirks than does the other player. The other is that in this game, the socially optimal outcome is Work/Shirk, not Work/Work. ("Socially optimal" means maximizing the sum of the players' results. That's not a meaningful thing to do if the results are measured in utility, but it is if they're measured in welfare.)

I'm going to pretend that Cooperate and Defect are also called Work and Shirk, so that I don't have to use both names when talking about both games.

In normal-form, these games look like this:

<table>
<thead>
  <tr>
    <th colspan="4" style="font-weight: bold">Prisoner's Dilemma</th>
    <th></th>
    <th colspan="4" style="font-weight: bold">Specialized Labor<br></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td></td>
    <td></td>
    <td colspan="2" style="font-weight: bold">Player 2</td>
    <td></td>
    <td></td>
    <td></td>
    <td colspan="2" style="font-weight: bold">Player 2</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td style="font-weight: bold">Work</td>
    <td style="font-weight: bold">Shirk</td>
    <td></td>
    <td></td>
    <td></td>
    <td style="font-weight: bold">Work</td>
    <td style="font-weight: bold">Shirk</td>
  </tr>
  <tr>
    <td rowspan="2" style="font-weight: bold">Player 1</td>
    <td style="font-weight: bold">Work</td>
    <td>$ ww_=, ww_= $</td>
    <td>$ ws_=, sw_= $</td>
    <td></td>
    <td rowspan="2" style="font-weight: bold">Player 1</td>
    <td style="font-weight: bold">Work</td>
    <td>$ ww_=, ww_= $</td>
    <td>$ ws_1, sw_= $</td>
  </tr>
  <tr>
    <td style="font-weight: bold">Shirk</td>
    <td>$ sw_=, ws_= $</td>
    <td>$ ss_=, ss_= $</td>
    <td></td>
    <td style="font-weight: bold">Shirk</td>
    <td>$ sw_=, ws_2 $</td>
    <td>$ ss_=, ss_= $</td>
  </tr>
  <tr>
    <td colspan="4">$ sw_= &gt; ww_= &gt; ss_= &gt; ws_= $, and $ 2ww_= &gt; sw_= + ws_= $</td>
    <td></td>
    <td colspan="4">$ sw_= &gt; ww_= &gt; ss_= &gt; ws_1 &gt; ws_2 $, and $ 2ww_= &lt; sw_= + ws_1 $</td>
  </tr>
</tbody>
</table>

How to read these symbols: the subscript is the player who gets the payoff, the first letter is their move, and the second letter is the other player's move. If the subscript is =, then this combination is symmetric. So `$ ws_1 $` is the payoff to Player 1, if he Works while Player 2 Shirks. `$ ws_2 $` is the payoff to Player 2, if she Works while Player 1 Shirks. `$ ws_= $` is both of these values, when they're equal to each other. And to be clear, when they're equal, `$ ws_1 $` can stand in for `$ ws_= $` just as easily as the other way around.

This notation is kind of experimental on my part. Ellickson instead uses symbols `$ A, B, C, D, E $` in descending order, but that makes it hard to remember which goes where in the grid. And when I extend it, the ordering will be lost, making it even more confusing.

Comparing these games, he claims for example that norms will tend to punish someone who Shirks in a Prisoner's Dilemma, rather than rewarding those who Work, because eventually most people will Work and it's cheaper to sanction the thing that happens rarely. But in a Specialized Labor game, norms will tend to reward the efficient worker ("cheapest labor-provider") for Working, because that encourages people to obtain the skills necessary to perform this work. There's a background level of skills that everyone is expected to have, and people are punished for falling short of them and rewarded for exceeding them.

So most of the points I want to ding Ellickson here are because this is kind of a strange choice of games. For one thing, it seems to assume that: *teaming up to work is more expensive than working individually, if and only if players have unequal skill levels*.

Honestly I don't think that's so implausible as a heuristic. I think "most work projects have gains from (little-C) cooperation" is a decent guess, and then one way to remove those gains could be if one player is much more skilled than the other. Still, Ellickson doesn't make this argument, or acknowledge that the assumption is kind of weird. And I do think it would be worth looking, at least briefly, at "symmetrical games with no gains from cooperation" and "asymmetrical games with gains from cooperation".

Something weird on the face of it is that in Specialized Labor, Work/Work results in the same payoff to both players. Why assume that that's symmetrical? But I don't think this is a big deal. Plausibly people can calibrate how hard they work if they think they're getting a worse result than the other. But also I suspect you just don't change much by allowing it to be asymmetrical, provided that both payoffs are in between `$ sw_= $` and `$ ss_= $`.

Similarly you might suppose that the efficient worker doesn't just pay less to Work than the inefficient worker, he also does a better job. In which case we might want to set `$ sw_1 &lt; sw_2 $`. But again, I doubt that matters much.

More seriously, Ellickson's choice ignores the possibility that work might be worth doing selfishly. In both games, you maximize your own outcome by not working, and if that means the work doesn't get done, so be it. But that puts a narrow band on the value of a piece of work. It's not worth doing for the benefits it gives to one person, but it is worth doing for the benefits it gives to two. I think a lot of the situations Ellickson looks at don't really fit that model. For example, building a fence seems like something you'd often do of your own accord, simply for the benefits it gives to yourself, but Ellickson considers it a Prisoner's Dilemma.

To model this possibility, we'd set `$ ws_1 > ss_= $`, and maybe `$ ws_2 > ss_= $` as well. This gives the game that I like to call the [Farmer's Dilemma](http://reasonableapproximation.net/2015/05/05/farmers-dilemma.html) and others call Chicken, Hawk/Dove or Snowdrift. ([And here's why I call it that.](https://www.greaterwrong.com/posts/KwbJFexa4MEdhJbs4/classifying-games-like-the-prisoner-s-dilemma#comment-aEC8trK7f3uczsXvM)) Normally I think of the Farmer's Dilemma as symmetrical, but the asymmetrical case seems fine to count as an instance of it, at least right now.

The tricky thing about this game is that even though you'd be willing to do the work yourself if no one else benefitted, the fact that someone else *does* benefit makes you want them to join in and help with the work. If they decline,
your only in-game way to punish them is not to do the work, which hurts you too - but if you don't punish them, you're a sucker. This is fundamentally different from the tricky thing with Prisoner's Dilemma and Specialized Labor, which in both cases is simply that people have no incentive to work. So it seems like an important omission. Especially because depending on the exact payoffs, it may be that "one player is a sucker while the other makes off like a bandit" is both a Nash equilibrium and socially optimal.

The thesis of the book is to propose a certain hypothesis. (Not going into more detail here.) The hypothesis has no problem with that result, but humans often do. So Farmer's Dilemmas may be a fruitful place to look for failures of the hypothesis. But it may be that the relevant payoff structure is rare, in which case we wouldn't find much. (I wouldn't expect it with fence-building for example.)

How do we get the socially optimal result in Prisoner's Dilemma and Specialized Labor? We introduce debts owed from those who Shirk to those who Work. Ellickson's possible minor original contribution is to point out that the value `$ ww_= - ws_1 $` works in both these games.

He calls this the "liquidated-Kantian formula" but doesn't explain the name, and I have only the vaguest understanding of where he might be going with it. Since the name hasn't caught on, I'm going to propose my own: *counterfactual compensation*. If I Shirk, I compensate you for your losses compared to the world where I worked.

(To compare: regular compensation would be compensating you for the losses you actually suffered from working, `$ ss_= - ws_1 $`. Restitution would be handing over to you the gains I got from your work, $ ss_= - sw_2 $. Counterfactual restitution would be handing over to you the gains I got from not working myself, $ ww_= - sw_2 $. Each of these takes one player's payoff in one quadrant, and subtracts the same player's payoff in an adjacent quadrant. The factual variants are about differences between the world where no one worked and the worlds where one of us worked; they're about the effects of work that actually happened. The counterfactual variants are about the differences between the worlds where only one of us worked and the world where we both worked; they're about the effects of work that didn't happen.)

If we apply this formula to the Prisoner's Dilemmma, we get this:

<table>
<thead>
  <tr>
    <th colspan="4" style="font-weight: bold">Prisoner's Dilemma with counterfactual compensation</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td></td>
    <td></td>
    <td colspan="2" style="font-weight: bold">Player 2</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td style="font-weight: bold">Work</td>
    <td style="font-weight: bold">Shirk</td>
  </tr>
  <tr>
    <td rowspan="2" style="font-weight: bold">Player 1</td>
    <td style="font-weight: bold">Work</td>
    <td>$ ww_=, ww_= $</td>
    <td>$ ww_=, sw_= + ws_= - ww_= $</td>
  </tr>
  <tr>
    <td style="font-weight: bold">Shirk</td>
    <td>$ sw_= + ws_= - ww_=, ww_= $</td>
    <td>$ ss_=, ss_= $</td>
  </tr>
  <tr>
    <td colspan="4">$ sw_= &gt; ww_= &gt; ss_= &gt; ws_= $, and $ 2ww_= &gt; sw_= + ws_= $</td>
  </tr>
</tbody>
</table>

Since `$ ww_= > sw_= + ws_= - ww_= $`, this puts the incentives in the correct place. The socially optimal outcome hasn't changed - total welfare in each quadrant is the same as before - but now the Nash equilibrium is for both players to Work.

(In [my previous classification](http://reasonableapproximation.net/2020/07/04/classifying-games-like-prisoners-dilemma.html), depending on whether `$ sw_= + ws_= - ww_= ≷ ss_= $`, it hits the point where The Abundant Commons meets either Cake Eating or Studying For a Test. It's not unique in either case, because there are at most three distinct payout values.)

Specialized Labor is more complicated. There are three ways we might decide to apply counterfactual compensation. We could say that the Shirker compensates the Worker for the Worker's costs, either `$ ss_= - ws_1 $` or `$ ss_= - ws_2 $` depending on who Worked. Or we could say that the Shirker compensates the Worker for what the *efficient* Worker's costs would have been, `$ ss_= - ws_1 $` regardless of who Worked. Or we could say that the efficient worker never owes anything to the inefficient worker; he gets to just say "sorry, I'm not going to pay you for work I could have done more easily".

Ellickson doesn't discuss these options, he just takes the last one. Here's what it looks like.

<table>
<thead>
  <tr>
    <th colspan="4" style="font-weight: bold">Prisoner's Dilemma with counterfactual compensation</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td></td>
    <td></td>
    <td colspan="2" style="font-weight: bold">Player 2</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td style="font-weight: bold">Work</td>
    <td style="font-weight: bold">Shirk</td>
  </tr>
  <tr>
    <td rowspan="2" style="font-weight: bold">Player 1</td>
    <td style="font-weight: bold">Work</td>
    <td>$ ww_=, ww_= $</td>
    <td>$ ww_=, sw_= + ws_1 - ww_= $</td>
  </tr>
  <tr>
    <td style="font-weight: bold">Shirk</td>
    <td>$ sw_=, ws_2 $</td>
    <td>$ ss_=, ss_= $</td>
  </tr>
  <tr>
    <td colspan="4">$ sw_= &gt; ww_= &gt; ss_= &gt; ws_1 &gt; ws_2 $, and $ 2ww_= &lt; sw_= + ws_= $</td>
  </tr>
</tbody>
</table>

The debt is only owed from the inefficient worker to the efficient one; if the inefficient worker Works while the efficient worker Shirks, presumably the efficient worker just gets to say "sorry, I'm not going to pay you for work I could have done more easily". So the inefficient worker has no incentive to Work if the efficient worker Shirks. And if the efficient worker Works, the inefficient worker also has no incentive to Work, because by Shirking they get (A+D-B > B). And given that the ineffecient worker is Shirking, the efficient worker has incentive to Work (ending with B if they do, or C if they don't). Ellickson doesn't use the term "Nash equilibrium", but: in both cases, this B-D payment results in a single Nash equilibrium at the single socially optimal result.

This isn't, like, a mind-blowing result that's going to blow open the field of game theory. But I don't remember seeing it before, and Ellickson doesn't attribute it to anyone else. I'm inclined to give him some credit for it. Even if others have had the insight before - which I expect they have - it seems like he's still doing competent work in a field outside his own.

But then I do dock him a point because he doesn't comment on the fact that the inefficient worker gets a better result than the efficient worker. That seems bad to me, because it discourages people from becoming the efficient worker.

(Obviously there are caveats to apply when bringing this formula to the real world. Ellickson discusses them.)

How does this work in the Farmer's Dilemma? There's more cases to consider there, and I haven't looked in detail yet, but I think it mostly either improves the incentives or at least doesn't hurt them? So that's kind of a point to Ellickson, too.

It's nice that the payment is based only on the players' possible outcomes, because they'll have to figure those values out anyway when deciding how to act. Other possible damage formulas (like C-D and A-C) apparently don't set up correct incentives, but Ellickson doesn't go into much detail on that.

With this payment in mind, Ellickson proposes a variant Iterated Prisoner's Dilemma tournament, and a strategy for it that he calls "Even-Up". The tournament has rounds of both Prisoner's Dilemma and Specialized Labor, and payoffs for them can vary considerably. In between rounds, players can unilaterally choose to make a side payment to their partner. To apply the Even-Up strategy, a player would keep account of standing with their partner. They'd adjust that balance by B-D in the circumstances described above. Whenever the balance was close to zero, they'd play the socially optimal strategy. If they were in debt, they'd make a side payment. And if they were in credit, they'd Defect or Shirk when they'd otherwise Cooperate or Work. (But only if that would bring the balance closer to zero, i.e. if the debt owed was more than half of B-D. Though it's not clear to me why they wouldn't do it for any debt and then just make a side payment if appropriate. I suspect Ellickson is implicitly assuming transaction costs that he didn't bake into the tournament rules.) Note that Even-Up falls through to Tit-for-Tat in a normal IPD tournament.

Ellickson predicts that Even-Up would do well in this tournament, which seems plausible to me. He says that if Even-Up turns out not to be evolutionary stable - if a society of Even-Up players can be exploited by other strategies, or wouldn't be able to enter groups currently dominated by other strategies - the hypothesis would no longer be credible. (I'd be more forgiving of the specific strategy described, but I think it would be evolutionary stable anyway.)

He also says it carries through to the real world:

> Many Shasta County residents appear to follow something like an Even-Up strategy. Their live-and-let-Iive approach calls for them to put up with minor matters. As we have seen, when a nontrivial loss arises from a failure to supervise cattle or contribute to boundary-fence maintenance, residents mentally adjust interneighbor accounts and then usually repay the debt (or, conversely, avenge its nonpayment) in a measured way. For example, a ranchette owner in Shasta County used the phrase "get even" in predicting how he would respond to a neighbor's refusal to share appropriately in the costs of a boundary fence.
>
> More generally, the familiarity of the phrase "get even," the biblical remedy of an eye for an eye, the norm of reciprocity that George Homans calls one of the world's most common, anthropologists' findings of gift exchange, friends' tendencies to alternate in hosting social events - all these hint at the pervasiveness of something like an Even-Up approach to social interactions. [Footnotes removed.]
