---
title: Specialized Labor and Counterfactual Compensation
layout: draft
---
I have three purposes in this post. The first is to review the formal game theory found in Robert Ellickson's *Order Without Law*. It's not a large part of the book, but it's the part that I'm most qualified to judge. Not that I'm a formal game theorist myself, but I'm closer to being one of them than to being any kind of social scientist, historian or lawyer. If his formal game theory is nonsense, that would suggest that I ought to discount his writing on other fields, too. (Perhaps not discount it completely, especially because formal game theory is outside his main area of study. Then again, lots of the book is outside his main area of study.)

Spoiler alert: I think he holds up reasonably well. I want to ding him a few points, but nothing too serious, and he possibly even contributes a minor original result.

My second purpose, which is valuable for the first but also valuable of itself, is to try to extend it further than Ellickson did.

My third is simply to be able to cut it from my in-progress review of the rest of the book.

Ellickson discusses two games. One is the classic Prisoner's Dilemma, in which you either Cooperate (for personal cost but social benefit) or Defect (for personal benefit but social cost[^social-cost]). Note that Ellickson specifies Cooperate/Cooperate as having more total utility than Cooperate/Defect or Defect/Cooperate; I consider this [correct](https://lesswrong.com/posts/KwbJFexa4MEdhJbs4/classifying-games-like-the-prisoner-s-dilemma#comment-xzA7K2To2N84NJgNj), but not all authors include that condition.

[^social-cost]: Strictly speaking: if you Defect, that always harms your opponent and benefits yourself, relative to you Cooperating. And if your opponent Cooperates, this will always be a *social* cost as well, harming your opponent more than it benefits you. But if your opponent is also Defecting, then the structure of a Prisoner's Dilemma is agnostic on whether your defection is a social cost; it might benefit you more than it harms your opponent.

The other he calls Specialized Labor, in which two people must choose whether to Work on some common project or Shirk their share of it. It differs from the Prisoner's Dilemma in two ways. First, it's asymmetrical; one player is a less effective worker than the other, and gets less payoff from Working while the other Shirks than does the other player. The other is that in this game, the socially optimal outcome is Work/Shirk, not Work/Work. (Many authors would consider it an asymmetrical version of the Prisoner's Dilemma. But in [my taxonomy](http://reasonableapproximation.net/2020/07/04/classifying-games-like-prisoners-dilemma.html), Prisoner's Dilemma is defined more narrowly; Specialized Labor is instead an asymmetrical version of Too Many Cooks.)

Note that payoffs aren't measured in utility. They're measured in something Ellickson calls "welfare". He doesn't really explore the formal consequences of this. But what it gives us is that, since welfare is supposed to be objective, we can sum different people's welfare; when I used the phrases "social cost" and "socially optimal" in the previous paragraphs, talking about "the sum of both players' results", that was a meaningful thing to do. I'm not sure exactly what it costs us, except that I don't expect results about mixed strategies to hold. (Someone won't necessarily prefer "50% chance of 3 welfare" to "certain chance of 1 welfare". I wasn't planning to consider mixed games anyway.) We can still assume that people prefer higher amounts of welfare to lower amounts of it.[^assume-welfare]

[^assume-welfare]: I'm not actually sure we can assume that, but that question is out of scope.

I'm going to pretend that Cooperate and Defect are also called Work and Shirk, so that I don't have to use both names when talking about both games.

In normal-form, these games look like this:

<table>
<thead>
  <tr>
    <th colspan="4" style="font-weight: bold">Prisoner's Dilemma</th>
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
    <td style="background-color: #EEE">
      <span style="color: red">$ ww_* $</span>,
      <span style="color: red">$ ww_* $</span>
    </td>
    <td>
      <span style="color: red">$ ws_* $</span>,
      <span style="color: green">$ sw_* $</span>
    </td>
  </tr>
  <tr>
    <td style="font-weight: bold">Shirk</td>
    <td>
      <span style="color: green">$ sw_* $</span>,
      <span style="color: red">$ ws_* $</span>
    </td>
    <td>
      <span style="color: green">$ ss_* $</span>,
      <span style="color: green">$ ss_* $</span>
    </td>
  </tr>
  <tr>
    <td colspan="4">$ sw_* &gt; ww_* &gt; ss_* &gt; ws_* $, and $ 2ww_* &gt; sw_* + ws_* $</td>
  </tr>
</tbody>
</table>

<table>
<thead>
  <tr>
    <th colspan="4" style="font-weight: bold">Specialized Labor<br></th>
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
    <td>
      <span style="color: red">$ ww_* $</span>,
      <span style="color: red">$ ww_* $</span>
    </td>
    <td style="background-color: #EEE">
      <span style="color: red">$ ws_1 $</span>,
      <span style="color: green">$ sw_* $</span>
    </td>
  </tr>
  <tr>
    <td style="font-weight: bold">Shirk</td>
    <td>
      <span style="color: green">$ sw_* $</span>,
      <span style="color: red">$ ws_2 $</span>
    </td>
    <td>
      <span style="color: green">$ ss_* $</span>,
      <span style="color: green">$ ss_* $</span>
    </td>
  </tr>
  <tr>
    <td colspan="4">$ sw_* &gt; ww_* &gt; ss_* &gt; ws_1 &gt; ws_2 $, and $ 2ww_* &lt; sw_* + ws_1 $</td>
  </tr>
</tbody>
</table>

How to read these symbols: the subscript is the player who gets the payoff, the first letter is their move, and the second letter is the other player's move. If the subscript is `$ * $`, then this combination is symmetric.[^experimental] So `$ ws_1 $` is the payoff to Player 1, if he Works while Player 2 Shirks. `$ ws_2 $` is the payoff to Player 2, if she Works while Player 1 Shirks. `$ ws_* $` is both of these values, when they're equal to each other. And to be clear, when they're equal, `$ ws_1 $` can stand in for `$ ws_* $` just as easily as the other way around.

[^experimental]: This notation is kind of experimental on my part. Ellickson instead uses symbols `$ A, B, C, D, E $` in descending order, but that makes it hard to remember which goes where in the grid. And when I look at the Farmer's Dilemma later on, the ordering will be lost, making it even more confusing.

To help make the structure more visible, I've colored the symbols in green or red according to local incentive gradients - green for "this player prefers this outcome to the outcome they get from changing their move", red for the opposite of that. So when `$ ws_1 $` is red, that means `$ ss_1 > ws_1 $`, since `$ ss_1 $` represents Player 1's payoff if he changes his move while Player 2 keeps hers the same. A quadrant is a Nash equilibrium [iff](https://en.wikipedia.org/wiki/If_and_only_if) it has two green symbols. I've also given a slightly darker background to the socially optimal quadrants.

Comparing these games, Ellickson claims for example that norms will tend to punish someone who Shirks in a Prisoner's Dilemma, rather than rewarding those who Work, because eventually most people will Work and it's cheaper to sanction the thing that happens rarely. But in a Specialized Labor game, norms will tend to reward the efficient worker ("cheapest labor-provider") for Working, because that encourages people to obtain the skills necessary to perform this work. There's a background level of skills that everyone is expected to have, and people are punished for falling short of them and rewarded for exceeding them.

So most of the points I want to ding Ellickson here are because this is kind of a strange choice of games. For one thing, it seems to assume that: *teaming up to work is more expensive than working individually, iff players have unequal skill levels*.

Honestly I don't think that's so implausible as a heuristic. I think "most work projects have gains from working together" is a decent guess, and then one way to remove those gains could be if one player is much more skilled than the other. Still, Ellickson doesn't make this argument, or acknowledge that the assumption is kind of weird.

Another way to justify the omission is if the ommitted possibilities don't add much of interest. Prisoner's Dilemma and Specialized Labor are opposite corners in a two-by-two grid parameterized by "synergistic/discordant" (gains or no gains from cooperation) and "symmetrical/asymmetrical". If our tools for working with them can also be applied to the other corners without much extra effort, then there's no need to consider the others in detail. More on this later.

Something weird on the face of it is that in Specialized Labor, Work/Work results in the same payoff to both players. Why assume that that's symmetrical? But I don't think this is a big deal. Plausibly people can calibrate how hard they work if they think they're getting a worse result than the other. Also I suspect you just don't change much by allowing it to be asymmetrical, provided that both payoffs are in between `$ sw_* $` and `$ ss_* $`.

Similarly you might suppose that the efficient worker doesn't just pay less to Work than the inefficient worker, he also does a better job. In which case we might want to set `$ sw_1 < sw_2 $`. But again, I doubt that matters much.

Here's my largest objection: Ellickson doesn't consider that work might be worth doing selfishly. In both games, you maximize your own outcome by not working, and if that means the work doesn't get done, so be it. But that puts a narrow band on the value of a piece of work. It's not worth doing for the benefits it gives to one person, but it is worth doing for the benefits it gives to two. I think a lot of the situations Ellickson looks at don't really fit that model. For example, building a fence seems like something you'd often do of your own accord, simply for the benefits it gives to yourself, but Ellickson considers it a Prisoner's Dilemma because most people have the relevant skills. (He doesn't analyse whether fence-building is more easily done in tandem.)

To model this possibility, we'd set `$ ws_1 > ss_* $`, and maybe `$ ws_2 > ss_* $` as well. This gives the game that I like to call the [Farmer's Dilemma](http://reasonableapproximation.net/2015/05/05/farmers-dilemma.html) and others call Chicken, Hawk/Dove or Snowdrift. ([Here's why I call it that.](https://lesswrong.com/posts/KwbJFexa4MEdhJbs4/classifying-games-like-the-prisoner-s-dilemma#comment-aEC8trK7f3uczsXvM)) Normally I think of the Farmer's Dilemma as symmetrical, but the asymmetrical case seems fine to count as an instance of it, at least right now.

The tricky thing about this game is that even though you'd be willing to do the work yourself if no one else benefitted, the fact that someone else *does* benefit makes you want them to join in and help with the work. If they decline,
your only in-game way to punish them is not to do the work, which hurts you too - but if you don't punish them, you're a sucker. This is fundamentally different from the tricky thing with Prisoner's Dilemma and Specialized Labor, which in both cases is simply that people have no selfish incentive to work. So it seems like an important omission. Especially because depending on the exact payoffs, it may be that "one player is a sucker while the other makes off like a bandit" is both a Nash equilibrium and socially optimal.

---

The thesis of the book is to propose a certain hypothesis. Roughly speaking, and for the purpose of this essay, we can assume the hypothesis says: norms will evolve to maximize the aggregate welfare of the players.

(And so Farmer's Dilemmas might be a good place to look for failures of the hypothesis. When the socially optimal result is for one player to be a sucker, and that's also a Nash equilibrium, the hypothesis thinks this is fine. Humans might not think that, and norms might evolve that the hypothesis would have ruled out. But note that this is only the case in the *Discordant* Farmer's Dilemma - when there are no gains from cooperation. In the Synergistic Farmer's Dilemma, the socially optimal result is for both players to Work. The Discordant Farmer's Dilemma might be rare in practice - I wouldn't expect it with fence-building, for example.)

Let's pretend we're creating a system of norms for these games. Something we can do is mandate transfers of welfare between players. In each quadrant, we can take some of one player's payoff and give it to the other. Total payoff stays the same, and so the socially optimal outcome stays in the same place. But the distribution of welfare changes, and the Nash equilibria might move.

How do we encourage the socially optimal result by doing this? This is Ellickson's possible minor contribution. He points out that we can do it by introducing a debt from those who Shirk to those who Work, and that the value `$ ww_* - ws_1 $` works in both these games.

He calls this the "liquidated-Kantian formula" but doesn't explain the name, and I have only the vaguest understanding of where he might be going with it. Since the name hasn't caught on, I'm going to propose my own: *counterfactual compensation*. If I Shirk, I compensate you for your losses compared to the world where I worked.

(To compare: actual compensation would be compensating you for the losses you actually suffered from working, `$ ss_* - ws_1 $`. Actual restitution would be handing over to you the gains I got from your work, `$ sw_* - ss_* $`. Counterfactual restitution would be handing over to you the gains I got from not working myself, `$ sw_* - ww_* $`. Each of these takes one player's payoff in one quadrant, and subtracts the same player's payoff in an adjacent quadrant. The actual variants are about differences between the world where no one worked and the worlds where one of us worked; they're about the effects of work that actually happened. The counterfactual variants are about the differences between the worlds where only one of us worked and the world where we both worked; they're about the effects of work that didn't happen.)

(Also: yes, obviously there are caveats to apply when bringing this formula to the real world. Ellickson discusses them briefly. I'm going to ignore them.)

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
    <td style="background-color: #EEE">
      <span style="color: green">$ ww_* $</span>,
      <span style="color: green">$ ww_* $</span>
    </td>
    <td>
      <span style="color: green">$ ww_* $</span>,
      <span style="color: red">$ sw_* + ws_* - ww_* $</span>
    </td>
  </tr>
  <tr>
    <td style="font-weight: bold">Shirk</td>
    <td>
      <span style="color: red">$ sw_* + ws_* - ww_* $</span>,
      <span style="color: green">$ ww_* $</span>
    </td>
    <td>
      <span style="color: red">$ ss_* $</span>,
      <span style="color: red">$ ss_* $</span>
    </td>
  </tr>
  <tr>
    <td colspan="4">$ sw_* &gt; ww_* &gt; ss_* &gt; ws_* $, and $ 2ww_* &gt; sw_* + ws_* $</td>
  </tr>
</tbody>
</table>

Since `$ ww_* > sw_* + ws_* - ww_* $`, this puts the incentives in the correct place. The Nash equilibrium is now for both players to Work, which is socially optimal.

(In my taxonomy, depending on whether `$ sw_* + ws_* - ww_* ≷ ss_* $`, this new game is at the point where The Abundant Commons meets either Cake Eating or Studying For a Test. It's not unique in either case, because there are at most three distinct payout values.)

Specialized Labor is more complicated. There are three ways we might decide to apply counterfactual compensation. We could say that the Shirker compensates the Worker for the Worker's costs, either `$ ww_* - ws_1 $` or `$ ww_* - ws_2 $` depending on who Worked. Or we could say that the Shirker compensates the Worker for what the *efficient* Worker's costs would have been, `$ ww_* - ws_1 $` regardless of who Worked. Or we could say that the efficient worker never owes anything to the inefficient worker; he gets to just say "sorry, I'm not going to pay you for work I could have done more easily". Lets call these approaches "actual-costs", "efficient-costs" and "substandard-uncompensated"

Ellickson doesn't discuss these options, and I ding him another point for that. He just takes the substandard-uncompensated one. Here's what it looks like.

<table>
<thead>
  <tr>
    <th colspan="4" style="font-weight: bold">Specialized Labor with counterfactual compensation (substandard-uncompensated)</th>
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
    <td>
      <span style="color: red">$ ww_* $</span>,
      <span style="color: red">$ ww_* $</span>
    </td>
    <td style="background-color: #EEE">
      <span style="color: green">$ ww_* $</span>,
      <span style="color: green">$ sw_* + ws_1 - ww_* $</span>
    </td>
  </tr>
  <tr>
    <td style="font-weight: bold">Shirk</td>
    <td>
      <span style="color: green">$ sw_* $</span>,
      <span style="color: red">$ ws_2 $</span>
    </td>
    <td>
      <span style="color: red">$ ss_* $</span>,
      <span style="color: green">$ ss_* $</span>
    </td>
  </tr>
  <tr>
    <td colspan="4">$ sw_* &gt; ww_* &gt; ss_* &gt; ws_1 &gt; ws_2 $, and $ 2ww_* &lt; sw_* + ws_1 $</td>
  </tr>
</tbody>
</table>

Player 2 has no incentive to Work, regardless of what Player 1 does, because `$ ss_* > ws_2 $` and (unlike in the Prisoner's Dilemma) `$ sw_* + ws_1 - ww_* > ww_* $`. And given that Player 2 is Shirking, Player 1 has incentive to Work. So again, we've moved the Nash equilibrium to the socially optimal quadrant.

This isn't, like, a mind-shattering result that's going to blow open the field of game theory. But I don't remember seeing it before, and Ellickson doesn't attribute it to anyone else. I'm inclined to give him some credit for it. Even if others have had the insight before - which I expect they have - it seems like he's still doing competent work in a field outside his own. Not amazing work, not particularly difficult work, but competent.

One objection: the inefficient worker gets a better result than the efficient worker. That seems bad to me, because it discourages people from becoming the efficient worker. I don't think this is a big deal, though. For one thing, acquiring skills probably does increase your own payoff; your skills will feed into `$ ww_* $`, not just your `$ ws $`. (So it directly increases your payoff in Work/Work, and reduces your debt in Shirk/Work.) *Someone else* acquiring skills will increase your payoff even more, perhaps, but that's not a big problem. For another thing, such incentives can be handled out-of-game. I do think Ellickson should have acknowledged this issue, and I ding him a point for not doing so. But a brief note would have been fine.

What happens if we apply counterfactual compensation in the other possible ways? The only difference is in the bottom left quadrant, which becomes either `$ sw_* + ws_2 - ww_* $`, <code style="color: green">$ ww_* $</code> (actual-costs) or <code style="color: green">$ sw_* + ws_1 - ww_* $</code>, `$ ww_* + ws_2 - ws_1 $` (efficient-costs). The problem with both of these is that that quadrant might now be a Nash equilibrium. In the first case, Player 1 might prefer that quadrant over Work/Work, depending on `$ 2ww_* ≷ sw_* + ws_2 $`, and Player 2 will certainly prefer it over Shirk/Shirk. In the second case, Player 1 will certainly prefer that quadrant over Work/Work, and Player 2 might prefer it over Shirk/Shirk, depending on `$ ww_* + ws_2 - ws_1 ≷ ss_* $`. That's not great, we only want a Nash equilibrium in the socially optimal quadrant.

On the other hand, I note that if `$ ws_1 - ws_2 $` is small, then the social cost is low; and if it's large, then (except perhaps with some fairly specific payoff values?) that quadrant isn't a Nash equilibrium. Meanwhile, if payoffs are uncertain - if people might disagree about who the more efficient worker is - then either of the other choices seems more robust. And this is more of an aesthetic judgment, but it feels like the kind of aesthetic judgment that sometimes hints at deeper problems: there's something a bit weird about how substandard-uncompensated is discontinuous. A small change in Player 2's skills lead to a small change in her compensation in each quadrant, until she gets equally skilled as Player 1, at which point there's a large change in the Shirk/Work quadrant.

On the other other hand, a feature of how these games translate to the real world is that players encourage each other to discuss in advance. Someone building unilaterally may not get to claim this debt. So if they disagree about who the efficient worker is, that's unlikely to cause much grief.

What about measures other than counterfactual compensation? Actual compensation (`$ ss_* - ws_1 $`) doesn't work. If a player expects the other to Shirk, they'd be indifferent to Working; and in a Prisoner's Dilemma, if they expect the other to Work, they might prefer to Work or not depending on `$ ww_* ≷ sw_* + ws_1 - ss_* $`. (In Specialized Labor, that inequality always resolves as `$ < $` which gives the incentives we want.)

Actual restitution (`$ sw_* - ss_* $`) is sometimes okay in a Prisoner's Dilemma, but if `$ ws_* + sw_* < 2ss_* $` then Shirk/Shirk remains a Nash equilibrium; players will only want to Work if they expect the other to also Work. In Specialized Labor it has the problem that players would prefer to Work than to pay restitution, and so Work/Shirk cannot be a Nash equilibrium.

Counterfactual restitution (`$ sw_* - ww_* $`) has much the same problem in a Prisoner's Dilemma; if `$ ws_* + sw_* < ww_* + ss_* $` then Shirk/Shirk is a Nash equilibrium. And in both games, a player who expects the other to Work will be indifferent to Working.

There are other options for payment one might consider; I haven't even looked at all of them of the form "one raw payoff minus another raw payoff". But so far, counterfactual compensation seems like the best option.

(We could even consider values of the debt based on information outside of the original payoff matrix. But Ellickson points out that when deciding how to act in the first place, players will already want to figure out what the payoff matrix looks like. If the debt was based on other information, there'd be a further cost to gather that information.)

While we're here, let's look at the other games implied by Prisoner's Dilemma and Specialized Labor. "Asymmetrical synergistic games" have `$ ws_1 ≠ ws_2 $` but `$ 2ww_* > ws_1 + sw_* $`. In this case, counterfactual compensation does exactly what we want it to do, just like in the symmetrical Prisoner's Dilemma; we can choose any of the three ways to apply it. "Symmetrical discordant games" have `$ ws_1 = ws_2 $` but `$ 2ww_* < ws_* + sw_* $`. The difficulty here is that there's no way to break the symmetry. Any of the three ways to apply counterfactual compensation will be equivalent, and leave us with two Nash equilibria in the two socially equal quadrants. The "discuss in advance" feature saves us again, I think; players don't need to somehow acausally cooperate to select one to Work and one to Shirk, they can just, like, talk about it. And so I think it was basically fine for Ellickson to not consider these games, though it would have been worth a couple of sentences on why.

---

How does this work in the Farmer's Dilemma? First we need to clarify exactly what set of games that refers to. In symmetrical games, I think of it as having `$ sw_* > ww_* > ws_* > ss_* $`; that is, each player would prefer the other to do all the work, or failing that to help; but they'd still rather do it all themselves than for the work not to get done.

I'm going to break symmetry by separating `$ ws_1 $` from `$ ws_2 $` as before. Without loss of generality, we can specify `$ ws_1 > ws_2 $`, but I'm not going to decide whether `$ ws_2 ≷ ss_* $`. It might be that only one player is skilled enough to benefit from Working alone.

So in normal form, the Farmer's Dilemma looks like this:

<table>
<thead>
  <tr>
    <th colspan="4" style="font-weight: bold">Farmer's Dilemma</th>
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
    <td style="background: repeating-linear-gradient(-45deg, #EEE 0 10px, transparent 10px 20px)">
      <span style="color: red">$ ww_* $</span>,
      <span style="color: red">$ ww_* $</span>
    </td>
    <td style="background: repeating-linear-gradient(-45deg, #EEE 0 10px, transparent 10px 20px)">
      <span style="color: green">$ ws_1 $</span>,
      <span style="color: green">$ sw_* $</span>
    </td>
  </tr>
  <tr>
    <td style="font-weight: bold">Shirk</td>
    <td>
      <span style="color: green">$ sw_* $</span>,
      $ ws_2 $
    </td>
    <td>
      <span style="color: red">$ ss_* $</span>,
      $ ss_* $
    </td>
  </tr>
  <tr>
    <td colspan="4">$ sw_* &gt; ww_* &gt; ws_1 &gt; ss_*$, and $ ws_1 &gt; ws_2 $</td>
  </tr>
</tbody>
</table>

Either of the top two quadrants could be socially optimal, depending whether the game is synergistic or discordant (that is, whether `$ 2ww_* ≷ sw_* + ws_* $`). Shirk/Work may or may not be a Nash equilibrium, depending whether `$ ws_2 ≷ ss_* $`. So how does it look with counterfactual compensation? I'll consider the synergy and discord cases separately.

<table>
<thead>
  <tr>
    <th colspan="4" style="font-weight: bold">Synergistic Farmer's Dilemma with counterfactual compensation (substandard-uncompensated)</th>
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
    <td style="background: #EEE">
      <span style="color: red">$ ww_* $</span>,
      <span style="color: green">$ ww_* $</span>
    </td>
    <td>
      <span style="color: green">$ ww_* $</span>,
      <span style="color: red">$ sw_* + ws_1 - ww_* $</span>
    </td>
  </tr>
  <tr>
    <td style="font-weight: bold">Shirk</td>
    <td>
      <span style="color: green">$ sw_* $</span>,
      $ ws_2 $
    </td>
    <td>
      <span style="color: red">$ ss_* $</span>,
      $ ss_* $
    </td>
  </tr>
  <tr>
    <td colspan="4">$ sw_* &gt; ww_* &gt; ws_1 &gt; ss_*$, $ ws_1 &gt; ws_2 $, and $ 2ww_* &gt; sw_* + ws_1 $</td>
  </tr>
</tbody>
</table>

Oh dear. Substandard-uncompensated compensation is clearly not going to work; Shirk/Work might still be a Nash equilibrium. In Specialized Labor it was fine that the efficient Worker would prefer the inefficient Worker to do all the work, because the inefficient worker would say "nuts to that". In a Farmer's Dilemma she might continue to Work, which we don't want. Even if we specified `$ ws_2 < ss_* $`, we'd simply have no Nash equilibrium; one player would always get a better result by changing their move.

Fortunately, either of the others seems fine. The payoffs for these are the same as in Specialized Labor, but their comparative values have changed. Actual-costs gives us <code style="color: red">$ sw_* + ws_2 − ww_* $</code>, <code style="color: red">$ ww_* $</code> in that quadrant, which isn't a Nash equilibrium because `$ ww_* > sw_* + ws_2 − ww_* $`. (Compared to this quadrant, Player 1 would rather Work and Player 2 would rather Shirk.) And efficient-costs again gives us <code style="color: red">$ sw_* + ws_1 − ww_* $</code>, `$ ww_* + ws_2 - ws_1 $`, which isn't a Nash equilibrium because `$ ww_* > sw_* + ws_1 − ww_* $`. (Player 1 would still rather Work. Player 2 may or may not prefer to Shirk; if `$ ws_2 > ss_* $` she'll certainly prefer this quadrant, might prefer it even if not, but it's not a problem either way.)

What about the discordant case? If `$ ws_2 < ss_* $` we actually already have the desired result. The only Nash equilibrium is Work/Shirk which is socially optimal. But as discussed above, it's a crap result for Player 1, and my sense is that the "no incentive to become the efficient worker" problem now becomes a lot more of an issue. Let's see what happens with counterfactual compensation.

<table>
<thead>
  <tr>
    <th colspan="4" style="font-weight: bold">Discordant Farmer's Dilemma with counterfactual compensation (substandard-uncompensated)</th>
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
    <td>
      <span style="color: red">$ ww_* $</span>,
      <span style="color: red">$ ww_* $</span>
    </td>
    <td style="background: #EEE">
      <span style="color: green">$ ww_* $</span>,
      <span style="color: green">$ sw_* + ws_1 - ww_* $</span>
    </td>
  </tr>
  <tr>
    <td style="font-weight: bold">Shirk</td>
    <td>
      <span style="color: green">$ sw_* $</span>,
      $ ws_2 $
    </td>
    <td>
      <span style="color: red">$ ss_* $</span>,
      $ ss_* $
    </td>
  </tr>
  <tr>
    <td colspan="4">$ sw_* &gt; ww_* &gt; ws_1 &gt; ss_* $, $ ws_1 &gt; ws_2 $, and $ 2ww_* &lt; sw_* + ws_1 $</td>
  </tr>
</tbody>
</table>

Again, substandard-uncompensated doesn't really help; Shirk/Work will be a Nash equilibrium iff it was one before. But at least Player 1 gets a less-bad result from Work/Shirk. (Player 2 still does better than him.)

Actual-costs might also be a Nash equilibrium in that quadrant, if `$ ww_* < sw_* + ws_2 − ww_* $`. And so might efficient-costs, if `$ ww_* + ws_2 - ws_1 > ss_* $`. (Again, this always holds if `$ ws_2 > ss_* $`, so looking only at the Nash equilibria, this is strictly worse than having no compensation.)

So this is unfortunate. We can't reliably remove that Nash equilibrium with counterfactual compensation. Depending how we apply it, we might even make it an equilibrium when it wasn't before.

(Actual restitution also works in the synergistic game, but moves the Nash equilibrium to Work/Work in the discordant game. Counterfactual restitution makes players indifferent to Working if they expect their partner to Work, so in practice I guess Work/Work is the Nash equilibrium there, too. And actual compensation would be negative, which is silly.)

---

Summing up, counterfactual compensation:

* Gives people good incentives in Prisoner's Dilemma.
* Gives people good incentives in Specialized Labor, using substandard-uncompensated. Mostly-good incentives using the other implementations.
* Gives people good incentives in the Synergistic Farmer's Dilemma, except that substandard-uncompensated only works sometimes.
* Maybe kinda sorta helps a bit in the Discordant Farmer's Dilemma. Maybe not.

So that's not amazing. I do think the Discordant Farmer's Dilemma is just fundamantally, in technical terms, a real bastard of a game. But even in the synergistic variant, the way we calibrate it to get the best incentives is different from the way we calibrate it for the best incentives in Specialized Labor.

So I appreciate Ellickson's contribution, and I think it's a real one. But it's not as much as we might have hoped. I think he had a blind spot about the Farmer's Dilemma, and his tools don't really work against it.

---

With counterfactual compensation in mind, Ellickson proposes a variant Iterated Prisoner's Dilemma tournament, and a strategy for it that he calls "Even-Up". Even-Up takes advantage of features of the tournament that make it more realistic, and is modelled on real-world behaviours that he describes elsewhere in the book.

The tournament has rounds of both Prisoner's Dilemma and Specialized Labor, and payoffs for them can vary considerably. He suggests that perhaps one in five rounds might have each payoff increased twentyfold. Additionally, in between rounds, players can unilaterally choose to make a side payment to their partner.

To apply the Even-Up strategy, a player would use an internal balance to keep account of standing with their partner. Whenever counterfactual compensation would be owed, according to the analysis above, they'd adjust the balance by its value. (Ellickson doesn't specify, but presumably they'd also adjust whenever their partner makes a payment to them.) Whenever the balance was close to zero, they'd play the socially optimal strategy. If they were in debt, they'd make a side payment. And if they were in credit, they'd "exercise self-help": Shirk when they'd otherwise Work.[^even-up-tit-for-tat] (But only if the debt owed was more than half the value of the compensation, so that the balance would become closer to zero.)

[^even-up-tit-for-tat]: Incidentally, in in a typical IPD tournament, with only Prisoner's Dilemmas and no variance in payoffs, Even-Up plays identically to Tit-for-Tat. An Even-Up player would never be in debt in such a tournament, since they'd never Shirk except to correct a balance, and doing so would either leave the balance unchanged (if their partner also Shirked) or bring it to exactly zero.

There are three parameters I might be inclined to play with. One: which variant of counterfactual compensation should we use? (Ellickson's wording doesn't make it clear which he intends. Above he took substandard-uncompensated for granted, but here he sort of hints ambiguously at efficient-costs, without noting or justifying the change if there is one.) As noted, substandard-uncompensated gives the right incentives where the other options sometimes don't. Still, I wouldn't be surprised if the other options sometimes helped to avoid a feud.

Related, two: suppose we do use substandard-uncompensated. When in credit, and facing a Specialized Labor game as the efficient worker, should we Shirk? (Since we'd never Work as the inefficient worker, this is the only time the choice of counterfactual compensation variants is relevant.) Regardless of the other player's move, no compensation is owed. So Shirking will destroy communal resources, but not bring players' standings back in balance. On the other hand, it does stop us from extending more credit that may never be paid back. It may be worth having a higher threshold for this than for Shirking in a Prisoner's Dilemma, but I'd say never Shirking in this case would be a mistake.

And three: is "brings the balance closer to zero" the optimal condition to use for when to exercise self-help? If we exercise it more readily, others may be more inclined to cooperate with us in the first place, but that effect is probaby minor - there's only so much we can be exploited for, over the whole game. On the other hand, we're also destroying more total payoff, per round. It may be worth only exercising self-help if our credit is more than say three-quarters the value of counterfactual compensation.

(If we're looking at modfications to the tournament: as well as tweaking the probability distribution of the various possible payoff matrices, I'd be interested to see what changes if you add a small or large transaction fee to the side payments. Naturally I'd also like to see what happens if you add the possibility of Farmer's Dilemmas, but then Even-Up needs to be altered to account for it. Of other games in the genre, a Discordant Abundant Commons (`$ ws_1 > ww_* > {sw_*, ss_*} $`, `$ 2ww_* < ws_1 + sw_* $`, and I'm not sure what the constraints on `$ ws_2 $` should be) would also be a good addition. Maybe an asymmetrical Anti-Coordination variant, with a single socially optimal outcome so as not to confuse SociallyOptimalOutcomeBot. The others don't seem like they'd add much; they all have `$ ww_* $` as the highest payoff, so their socially optimal outcomes are also individually optimal. That doesn't mean there's no reason not to play Work, but the reasons mostly boil down to "I'm willing to hurt myself to threaten or punish you" and you already get that from the Farmer's Dilemma. So I'm not convinced the other games add much strategic depth, and they do add noise.)

Ellickson predicts that Even-Up would do well in this tournament, and I agree. It's inexploitable, rewards its partners for cooperating, forgives past transgressions, and plays well against itself. I'd be concerned about what happens if it plays against some similar strategy with different ideas of fairness - might you get into a situation where only one of them is ever satisfied at a time, leading to alternating defections? More generally I just don't trust either myself or Ellickson to have especially reliable intuitions about this.

Ellickson also says that if Even-Up turns out not to be evolutionary stable - that is, if a society of Even-Up players can be exploited by other strategies, or wouldn't be able to enter groups currently dominated by other strategies - his hypothesis would no longer be credible. I think it would be stable, but even if not, I'd be somewhat forgiving. I'd want to know why not, before deciding how it reflects on the hypothesis.

---

The relevance for all of this to the rest of the book, is that he also says Even-Up is a decent model of how people sometimes act in the real world:

> Many Shasta County residents appear to follow something like an Even-Up strategy. Their live-and-let-live approach calls for them to put up with minor matters. As we have seen, when a nontrivial loss arises from a failure to supervise cattle or contribute to boundary-fence maintenance, residents mentally adjust interneighbor accounts and then usually repay the debt (or, conversely, avenge its nonpayment) in a measured way. For example, a ranchette owner in Shasta County used the phrase "get even" in predicting how he would respond to a neighbor's refusal to share appropriately in the costs of a boundary fence.
>
> More generally, the familiarity of the phrase "get even," the biblical remedy of an eye for an eye, the norm of reciprocity that George Homans calls one of the world's most common, anthropologists' findings of gift exchange, friends' tendencies to alternate in hosting social events - all these hint at the pervasiveness of something like an Even-Up approach to social interactions. [Footnotes removed.]

Seems fair. I don't think I have much to say about it.
