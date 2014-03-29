---
layout: draft
title: How unbalanced is The Resistance?
---
I'm a big fan of the board/card game [The Resistance](http://en.wikipedia.org/wiki/The_Resistance_%28game%29), but I feel like the base game is massively unbalanced in favour of the spies. I think that if the spies play well, they will usually win regardless of how well the resistance plays; and I think that playing well simply involves not outing themselves.

To test this, I intend to analyse a similar, simpler game which I call Resistance-B. "B" for "brainwashed", because in this game the spies don't know they're spies, and they don't know who the other spies are either. However, any time they go on a mission, their programming takes over and they sabotage it without knowing what they're doing. If there are multiple spies on a mission, they all sabotage it.

This probably wouldn't be very fun to actually play as a group (and you'd need a GM, or some other way to find out how many spies were on a mission without the spies themselves knowing). But it seems clear that, provided all players are good at acting, this is a variant which is strictly harder for the spies to win. Their strategy in this game is available in plain Resistance (always act like a resistance member in public, but sabotage all missions), but some options have been removed, and the resistance members know that this is their strategy.

This game is also a lot easier to analyse than the original. Everyone has the same information, so there's no need to vote on missions. In fact, we can think of it as a one-player game against a random opponent; all the opponent does is pick the spies, and the player needs to pick teams to execute three successful missions.

My hypothesis is that for many game sizes, the spies will have considerably greater than even odds of winning. I'm stating this vaguely because I don't have many concrete predictions; I expect the spies to have a disadvantage in five-player games at least<sup>1</sup>, but for six I'm not sure which way it would go, and by ten I expect the spies to be usually winning.

<small><sup>1</sup> Although I don't remember specifically predicting this prior to beginning the analysis below. I got as far as "40% of the time, the resistance wins just based on the first round" before I started to write this post.</small>

Note that if I'm wrong, that doesn't mean the original Resistance is unbalanced, although it's evidence against it (strength depending on just how badly wrong I am); but if I'm right, the Resistance certainly is unbalanced.

For people not familiar with the original game, here are the rules of Resistance-B. You have a specified number of players<sup>2</sup>, some of whom are "resistance members" (good guys) and some of whom are "government spies" (bad guys). A third of the players, rounded up, are spies, but you don't know which. The game progresses in up-to-five rounds. In each round, you select a specified number of your players, and find out how many of them were spies. If none of them were spies, you win that round. If any of them were spies, you loose that round. Your goal is to win three rounds. The number of players selected in each round depends on the total number of players, and the round number ([the table is given on wikipedia](http://en.wikipedia.org/wiki/The_Resistance_%28game%29#Rounds)). In addition, for seven players and up, you win round four unless you select two or more spies, not one or more.

<small><sup>2</sup> The way I'm presenting the game, these aren't real players. You are "the player", and the game contains fictional players whom you control.</small>

Resistance-B is easy to analyse case-by-case for five players (three resistance, two spies). With no information, we select the starting team (two players) randomly. There are three equivalence classes of outcomes:

<ul>
  <li>No spies ($p = { 3 \choose 2 } / { 5 \choose 2 } = 0.3$). In this case, the resistance always wins. Mission three also only takes two members, so it's a guaranteed success. On each of missions 2, 4 and 5, take one of the remaining players until you find the one who isn't a spy.</li>

  <li>Two spies ($p = 1 / { 5 \choose 2 } = 0.1$). Now we know exactly who the spies are. Easy win.</li>

  <li>One spy ($p = 0.6$, by elimination). We have players A through E, and precisely one of A and B is a spy, and precisely one of C, D, E is a spy. For mission two, our choices are (wlog) ABC and ACD. (CDE is stupid, because we gain no information and are guaranteed the mission will fail).

    <ul>
      <li>ABC is a guaranteed fail, but

        <ul>
	  <li>If we get two failure cards (p = 1/3), we know C is a spy. We can't afford to fail any more missions, and we can't distinguish between A and B. So we send AD on mission 3; if it succeds (p = 0.5) we win, if it fails (p = 0.5) we lose.</li>

          <li>If we get one failure card (p = 2/3), we know C is not a spy. One of AB, and one of DE, is a spy; we can't afford to send any more spies on missions, so we have a 1/4 chance of winning.</li>
	</ul>

So ABC gives us a 1/3 chance of winning.</li>

      <li>ACD has a $1/2 \cdot 1/3 = 1/6$ chance of succeding, but if it does we know who the spies are and win. It has a $1/2 \cdot 2/3 = 1/3$ chance of getting two failure cards; now we know BE are good, A is bad, and have a 50/50 chance of selecting between CD to win. And there's a $1/2$ chance of getting one failure card.

In this case, $1/3$ of the time, AE are spies and BCD are not. $2/3$ of the time, the spies are B and one of CD. Again, we can't afford to fail any more missions. So we can choose either BCD or ACE to go on the remaining missions, and we'll have a $1/3$ chance of winning.

So ACD has a $1/6 + 1/3 \cdot 1/2 + 1/2 \cdot 1/3 = 1/2$ chance of winning.</li>
    </ul>

So if there's one spy amongst AB, we select team ACD for mission two, and win half the time.</li>
</ul>

In total then, we win the five-player game 70% of the time. That's not surprising.

The six-player analysis could probably be done analagously without too much trouble, since there are still only two spies. But the mission sizes go 2-3-4-3-4, which means that if we select no spies in the first mission, it's not obvious that we win, and if we select one spy we also have the choice of selecting CDE for mission two... the decision tree gets a lot more complicated, and I'd rather try to solve this problem intelligently (to work for game sizes 7+ as well). I haven't done this yet, though; it's a job for future-me.
