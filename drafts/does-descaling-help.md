---
title: Does descaling a kettle help? Theory and practice
layout: draft
---
I've heard that descaling a kettle makes it more efficient, and can save me time and money.

Okay, but how much? For some reason my my intuition says it'll be basically unnoticable. Let's try to figure it out, and then actually try it.

### The Models

There's a first-order approximation which says this should be impossible: heating things up is 100% efficient. What's the limescale going to do, convert some electricity into forms of energy other than heat?

No, but it might cause the heat to go to the wrong places. I think there are two ways that could happen. The first is if the limescale itself has a high [heat capacity](https://en.wikipedia.org/wiki/Heat_capacity), meaning it takes a lot of energy to heat up. That doesn't seem likely to me; I think there's likely less than 10 g of it, and I think it probably has less heat capacity than the same mass of water (because I think water's is higher than most other things). I don't think adding 10 ml water (weighing 10 g) to my kettle will significantly effect the boiling time.

Spot check: water's specific heat capacity is about 4 J/K·g. So to heat 10 g water by 100 K needs about 4000 J. My kettle is 2200 W according to the email I got when I bought it, so an extra 10 ml should take about 2 s longer to boil.

Also, I normally boil about 500 ml of water, so we'd expect 10 ml extra to make about a 2% difference. (I don't have a strong intuition for how long my kettle normally takes to boil. 1-3 minutes? The above calculation suggests it should be around 100 s.)

The second way the limescale could matter is if it's a good thermal insulator. Then the metal heating element gets significantly above 100°C before the water boils. And from my googling, it seems like this is the reason people give that descaling a kettle is helpful. How much effect would this have?

[This page](https://www.comsol.com/paper/influence-of-limescale-on-heating-elements-efficiency-15419) says the [thermal conductivity](https://en.wikipedia.org/wiki/Thermal_conductivity) is 2.2 W/m·K. I don't remember studying this in school, and I don't find that wikipedia page very clear. But I think maybe this means: the rate of energy transfer (W) from the heating element is 2.2 W/m·K, multiplied by the surface area of the heating element (m²), divided by the thickness of the limescale (m), multiplied by the temperature difference (K) between the heating element and the water. The units check out at least.

This implies, if there's no limescale, that the power transfer should be infinite, regardless of the size of the heating element. That's clearly not how things work. Still, it seems fine to have as a model, it just means that the water and heating element will stay the same temperature.

But doing some field research (i.e. looking at my kettle) makes me think it's a bad model in this case. Here's what it looks like:

<a href="//reasonableapproximation.net/images/does-descaling-help/before.jpg"><img src="//reasonableapproximation.net/images/does-descaling-help/before.jpg" height="500"></a>

(This kettle was last descaled around August 2020. I know because I bought vinegar for it, and thanks to online shopping the receipt is in my email.)

It seems that I have some limescale over some of the heating element (bits of the metal plate at the bottom, and the tube around where it passes through the plate), and zero limescale over some of it. The "no limescale gives ∞ W/K" model is going to give ∞ W/K no matter how small the no-limescale area is. So scratch that model.

I don't feel like trying to model the rate of power transfer from an un-limescaled heating element to water. I don't know what material it's made of (some kind of steel I suppose?), and I don't know what property of that material to look up. Plus it probably depends on how fast water convects.

Here's another way to think about it: assume that the amount of metal the manufacturer used is roughly as small as possible without compromising too much on boiling speed.

When we turn the kettle on, we start putting 2200 W into the heating element, and the heating element starts putting some of that into the water. When the heating element is sufficiently hot, it can pour 2200 W into the water, and we're at 100% efficiency.

(Except that as it heats up the water, it needs to get hotter itself to maintain that 2200 W rate. So we'll never actually be putting 2200 W into the water. But I'm gonna guess that we can ignore this effect for current purposes. Also, if the heating element has enough thermal mass, we might boil the kettle before it gets hot enough to pour 2200 W into the water. I'm gonna guess this isn't the case.)

Energy used to heat the heating element is essentially wasted. I don't know if other kettle designs could do away with one entirely, but as long as we have a heating element there's going to be some wastage. We can minimize the wastage by having the heating element be low-volume (so not much energy needed to heat it) but high surface area (so high rate of energy transfer to the water).

If the rate of energy transfer is 1 W/K, then we reach 100% efficiency when the heating element is 2200 K hotter than the water. But long before you reach that point you're going to melt the plastic of the kettle, which would be bad. (The highest melting temperature of any plastic listed on [this page](https://plasticranger.com/melting-point-of-plastics/) is 390°C.)

If it's 10 W/K, then we reach 100% efficiency at 220 K hotter than the water. Some plastics can survive 320°C, but idk, it still seems bad.

But at 100 W/K, we only need to get 22 K hotter than the water. That seems like it should be fine?

Let's assume that under optimal conditions, the heating element reaches $x$ K hotter than the water. That suggests the rate of energy transfer is $2200/x$ W/K.

Now suppose that some fraction $f$ of the heating element is covered in limescale, and that the rate of energy transfer through the limescale is essentially 0 W/K. Then the heating element will instead reach $x/f$ K hotter than the water. The energy needed to heat it that extra $x{1 - f \over f}$ K, is extra energy wasted.

...but I actually expect the energy needed to heat the heating element to be pretty low? According to [this page](https://www.engineersedge.com/materials/specific_heat_capacity_of_metals_13259.htm) the specific heat capacity of steels tends to be about 0.5 J/K·g. If the heating element is 100 g of steel, and we heat it an extra 50 K, we waste an extra 2500 J which costs us a bit over a second.

So I'm not super confident in this, but: I don't have a model which suggests descaling a kettle (similar to mine) will have particularly noticeable effects. If it gets sufficiently scaled it'll self-destruct, but I expect this to be very rare. (I don't have a model for how much scaling it takes to reach that point, it's just that I don't remember ever hearing a friend, family member or reddit commenter say they destroyed their kettle by not descaling.)

### The Setup

It's almost time for some empiricism! I'm going to see how quickly my kettle boils currently (average of three observations), then I'm going to descale it, and then I'm going to see how quickly it boils after that.

My immediate temptation is to boil a large amount of water, so that the effect is most noticeable. A 10% difference is easier to notice if it's going from 500 s to 550 s, than from 100 s to 110 s. But my models (such as they are) predict that scale decreases initial efficiency but not eventual efficiency; it would be a fixed cost, not a percent cost. And a 10s difference is easier to notice if it's going from 100 s to 110 s, than from 500 s to 510 s.

I don't trust my models, so I'm going to try both small and large amounts. For small amounts, I'm going to fill the kettle to the "2 cup" line. I'm in the UK so that ought to be 568 ml, but most of my mugs are only 500 ml and it's not quite enough to fill one of them. Checking in a measuring jug, it's somewhere between 450 and 500 ml, so likely a US pint, 473 ml. There's some noise here because the kettle has a wide diameter, so we only get small differences in the water level for the volume poured in. My rough guess without measuring is a 5 ml difference between runs is plausible. For large amounts, I'm just going to empty my entire 1.5 l bottle of fridge-water into the kettle. There's some noise here because the bottle doesn't have markings at all and I don't bother to fill it right to the brim, but I do try to get it to roughly the same place. A 5 ml difference between runs seems plausible here too.

I'll use water from the fridge, to mostly control for initial temperature (my guess is it'll start around 3°C). I'm not going to bother trying to control for room temperature or for where in the fridge I keep the water or what phase of the cooling cycle the fridge is in at the time. I'm going to assume that the kettle cuts off when all the water is at 100°C. I'll only measure the first boil of the day, and that way the kettle has definitely had time to cool down overnight. (In hindsight:) I didn't control for whether the kettle had had water sitting in it overnight; that could plausibly make the heating element a few degrees below room temperature.

There's one more calculation to do first, and that's to figure out how quickly it would boil assuming no energy wasted. Then I can make some predictions; do the pre-descaling boils; possibly adjust my predictions; descale; do the post-descaling boils; and compare.

But I'm writing this post out of order, and I've already got the numbers for pre-descaling, without having calculated the maximum efficiency and made predictions based on that. I could make predictions knowing the numbers but not having calculated max efficiency, that seems mostly fine, except that rereading through this I saw that I did do a rough calculation above.

### The Prediction

Still, for what it's worth: my current guess is indeed that the effect will be pretty similar in absolute time for both small and large boils; and less than a 10s difference in both cases.

So, is that worth it? In terms of money, obviously not. I don't remember how much I pay for electricity, but it's less than £0.50/kWh. Multiplied by 2.2 kW for 10 s gives about £0.003, I'll save less than £3/year. Definitely not worth paying attention to that kind of money, which is what I expected. (It's even less when you consider the cost of the water and electricity and vinegar I use to descale.)

As for the time... ten seconds isn't much, but the time cost of boiling a kettle isn't how long it takes to boil. It's how long it takes to fill and turn on, plus how long I wait for it after I'm ready for boiling water. (That depends a lot on what I'm making. When I boil it for food, it usually finishes before I'm ready for it, but when I boil it for tea I usually have to wait.) Knocking ten seconds off the waiting could make it more pleasant to use, even if the actual time saving is minimal. I don't think I particularly expect to notice a difference, especially because 10s is the upper range of my prediction, but I won't be shocked if I do. I'm not going to give a numeric probability because I don't want my subjective judgment to be influenced by how it affects my predictive score.

(We don't get to count "time spent writing this post" against descaling. I'm not writing it to save myself time, I'm writing it to practice my sience skills and have fun doing so.)

Okay, actual calculations: we're making a 97 K difference in water temperature. The specific heat capacity [is](https://en.wikipedia.org/wiki/Specific_heat_capacity) 4.184 J/K·g, and the density is 1 g/ml. The power transfer at 100% efficiency is 2200 W. So for $x$ ml of water, we need a minimum of ${97 · 4.184 \over 2200} x$ s to boil. For 473 ml that's 87.3 s, and for 1500 ml that's 276.7 s.

If you want to make some predictions before you see the actual times, here's some space for you to do so.

...

...

...

...

...

### The results

The actual pre-descaling times: for small I measured 103, 105 and 107 s, average 105. That's 17.7 s or 20% higher than theoretical minimum. For large I measured 296, 290 and 300 s, average 295.3. That's 18.7 s or 7% higher than minimum.

I think this is looking pretty good for the "initial efficency, not eventual efficiency" models. I still expect descaling to make less than a 10 s difference in both.

If you want to change your predictions, here's some space for that.

...

...

...

...

...

I had to descale twice, the first time I don't think I put in enough vinegar relative to water. Here's what it looked like after the second attempt:

<a href="//reasonableapproximation.net/images/does-descaling-help/after.jpg"><img src="//reasonableapproximation.net/images/does-descaling-help/after.jpg" height="500"></a>

Now I measured 103, 104 and 104 s for small, average 103.7, 1.3 s faster than before. And 298, 296, 293 s for large, average 295.7, 0.3 s slower than before.

I assume these results aren't statistically significant, and I'm sure they're not practically significant. Descaling my kettle basically just doesn't speed it up unless it's much more scaly than it was this time. You know your kettle better than I do, but my guess is it won't speed up yours either. Don't be fooled by big vinegar.

I should have given a numeric probability for "no detectable difference". (The probability I was reluctant to give was for "I notice a difference when I'm not measuring".) Thinking back, I think that just before descaling I would have given this... something like 30-50% probability?

### The caveats

There may be other reasons to descale your kettle. Some friends mentioned flavor; I don't remember hearing that as a reason before, and I didn't notice a difference, but I'm the opposite of a supertaster. One mentioned getting scum on top of tea when a kettle is too scaly; I haven't noticed that either, but I'm probably also the opposite of a super-scum-noticer.

Also, my partner pointed out that post-descaling, the 2-cup mark holds slightly more water than it used to. I think this is less than the uncertainty in my measurements anyway, and in practice I use those markings to decide how much to fill my kettle so maybe it's correct not to control for this effect. Still, I'm a little embarrassed I didn't think of it in advance.
