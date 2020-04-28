---
title: "Chris Masterjohn on Coronavirus, Part 2"
layout: draft
---
Background on this in [part one](http://reasonableapproximation.net/2020/03/29/chris-masterjohn-on-coronavirus-part-1.html).

### General info: Interferon

[Interferon](https://en.wikipedia.org/wiki/Interferon) is an antiviral that our immune system naturally releases when it detects invasion. But SARS-CoV and MERS-CoV (the virus that causes MERS) manage to avoid this response. The trigger is the presence of double-stranded RNA, which viruses need but our own cells don't. (We make single-stranded RNA from DNA, and then proteins from single-stranded RNA. We never need to copy our RNA. But viruses do need to copy their RNA, and apparently that means viral RNA needs to be double-stranded.) SARS-CoV and MERS-CoV hide their double-stranded RNA inside "double-membrane vesicles" to avoid detection.

They also have a bunch of other ways to limit production of interferon, and on top of that they limit the response to the interferon that does get produced.

This all sounds like "so we should ramp up interferon". But that's probably a bad idea. During early stages of the virus, interferon is suppressed, so the virus can replicate quickly. But when the infection is established, macrophages generate a lot of interferon, leading to a [cytokine storm](https://en.wikipedia.org/wiki/Cytokine_release_syndrome). In a mouse trial, deleting the genes for the main interferon receptor made the subjects very resistant to SARS-CoV, but very vulnerable to mouse hepatitis virus and influeza A, compared to normal mice. (0% died to a dose of SARS-CoV[^mouse-trial-sars-cov] that killed 85% of normal mice; but 100% died to a dose of the other viruses that killed 10-20% of normal mice.)

[^mouse-trial-sars-cov]: In the first reference to this study, Chris says this was a dose of SARS-CoV-2. I think that was just a typo/brain fart. He later refers to it as if it was SARS-CoV, and the reference is from 2016.

(Question: "During the replication of the virus, macrophages are recruited to the lung". These are what release the interferon. What is a macrophage and what is recruiting them and why?)

We don't yet know that any of this applies to SARS-CoV-2 as well, but it seems likely. So high levels of interferon might be slightly helpful in early stages, but make later stages much worse. Thus, Chris recommends avoiding them.

(Question: LW user CellBioGuy [is bullish on](https://www.lesswrong.com/posts/nRX7uwT2wNvvmd2Yd/coronavirus-justified-key-insights-thread#comment-hRzw8sejgnb5C8C7B) inhaled interferon pretreatment, which I take it means "inhaling interferon before the disease gets bad". Does this square with Chris' recommendations? It wouldn't surprise me if inhaling interferon increases your levels in the short term but not the long term, which is exactly what we want. On the other hand, he links a paper whose abstract says SARS-CoV-2 "is much more sensitive [than SARS-CoV] to type I interferon pretreatment", so maybe this is just a case of "generalizing from SARS-CoV didn't work here".)

On April 25, Chris [wrote more about this](https://chrismasterjohnphd.com/covid-19/new-evidence-that-interferon-can-be-harmful-in-covid-19) on his mailing list. My own summary: in hamsters with their native ACE2 (which is similar enough to human ACE2 that they can get infected), eliminating the type 1 interferon response increased the amount of virus in various body parts including the lungs; but dramatically reduced lung damage. Chris notes that this is a bit weird, but takes it as supporting his hypothesis, and I'm inclined to agree.

### Every-day optional add-on: Garlic or stabilized allicin

[Allicin](https://en.wikipedia.org/wiki/Allicin) is the thing we care about here, garlic is just one way to get it. Garlic doesn't actually contain any, though. Garlic contains alliin. Alliin is converted to allicin when the garlic is crushed and left at room temperature in the open air for ten minutes.

(Who decided to name those things with an edit distance of one, and how do we stop them from naming anything ever again?)

Alternatively, we can mix garlic powder with water, and let that sit at room temperature in the open air for ten minutes. That gives us a more reliable dose, since garlic cloves vary in size. Or we can just take stabilized allicin supplements, which is a still more reliable dose. Most garlic extract won't work, and "potential allicin" is unreliable. Meals containing garlic won't work, because allicin isn't robust to heat or acids.

180mg allicin daily makes people [less likely to get colds](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6465033/). (I note that Chris here seems more confident than the authors of that review, who only found one study matching their inclusion criteria and who say at different times that the evidence is "poor-quality" and "moderate". Looking at the excluded studies, two seem worth noting. Both were excluded because they grouped colds and influenza together. [Andrianova 2003](https://www.ncbi.nlm.nih.gov/pubmed/12718222) found that a specific brand of garlic tablets "allicor" reduced morbidity from acute respiratory diseases 1.7-fold. So that seems to support Chris' recommendation. [Nantz 2012](https://www.ncbi.nlm.nih.gov/pubmed/22280901) used aged garlic extract, and found that it didn't reduce the incidence of (colds + flu) but did reduce the number and severity of symptoms. It's not clear to me whether aged garlic extract even contains allicin, but these results seem a little confusing to me whether it does or not.)

We also see antiviral effects in vitro against six different viruses: "herpes simples virus type 1, herpes simplex virus type 2, parainfluenza virus type 3, vaccinia virus, vesicular stomatitis virus, and human rhinovirus type 2". It seems to work by damaging the lipid envelope of those viruses. So it might also work against coronaviruses, which also have a lipid envelope.

Separately, allicin has antibacterial effects, which work by the same mechanism as zinc and copper inhibit SARS-CoV enzymes, so maybe it also inhibits those enzymes. (Note, this is not the same mechanism as how copper surfaces destroy SARS-CoV.) And it inhibits papain, so maybe it also inhibits papain-like proteases. (It sounds like papain-like protease 2 could be targeted by both these effects, and there are other papain-like proteases that could only get targeted by the second?)

Chris recommends this as an optional daily add-on, because although it's never been tested directly against coronaviruses, it's plausible and seems to be safe.

### If you get sick optional add-on: Echinacea

I've never heard of this. Apparently [it's a herb](https://en.wikipedia.org/wiki/Echinacea). It "[has been used for the common cold](https://www.ncbi.nlm.nih.gov/pubmed/16678640)", which isn't saying much (what hasn't?) but the citation suggests it was also at least somewhat effective. Wikipedia is skeptical, and this seems to be the only evidence Chris provides that it has any positive effects at all.

The mechanism of its effect seems to be boosting the immune system, so we might worry that it does so by increasing interferon. But instead it seems to work by increasing "inducible nitric oxide synthase" (iNOS). That doesn't seem to be protective against contracting SARS, but in mice it helps protect against the long-term damage that SARS does to the lungs.

Chris thinks this is less important than all of the preceding compounds, because "there is no clear evidence echinacea will offer specific protection against COVID-19". He no longer thinks it's safe long-term (though he hasn't updated the in-depth section of his report to reflect that), so he recommends only taking it when you get sick.

### Everyday optional add-on: Vitamin C

Vitamin C supplements seem to prevent colds, but not necessarily cure them. Intravenous vitamin C reduced mortality of acute respiratory distress syndrome by half; but none of those patients had SARS. Studies have shown conflicting effects of vitamin C on interferon levels, variously increasing and decreasing it.

Chris recommends getting enough vitamin C "to support normal immune function", which means taking supplements if and only if you don't get enough from your diet. He thinks the chance of it increasing interferon is too risky to take high doses.

### No longer recommended? N-Acetyl-Cysteine

In the first version of the report, Chris considered this an optional add-on. He no longer includes it in his list of recommendations, but the sections where he explained his recommendation are still in the report, unchanged. I'm not sure what's up with that.

Another thing that I'm not sure what's up with: In one section, Chris says: Normally we get cysteine by eating protein. [NAC](https://en.wikipedia.org/wiki/Acetylcysteine) helps us get more [cysteine](https://en.wikipedia.org/wiki/Cysteine) into our cells, and the extra cysteine is good for the immune system and lung health. In another section, he says NAC "is a precursor to [glutathione](https://en.wikipedia.org/wiki/Glutathione), which is critical for lung function." He's not very detailed about either of these claims, so I'm not sure how to put them together, and a quick glance at wikipedia doesn't really help. (There's totally room in my lack-of-understanding for them both to be true, it's just a bit weird that we have two different descriptions of its effects.)

Apart from being generally good for the lungs, the reason for recommending it - if he does recommend it - seems to be a single case where large amounts of NAC helped someone to recover from pneumonia caused by H1N1. There's no reason to think it might help prevent COVID-19, but it might help mitigate the damage.

### Limit: Vitamin A

Vitamin A is vital to the immune system, and you shouldn't get deficient. But its active metabolite is all-trans retinoic acid. In many rat studies, that's increased ACE2: "in the heart of rats whose blood pressure was raised by constricting their aortas, in the heart and kidney of spontaneously hypertensive rats, in the kidney of rats with glomerular sclerosis (to much higher levels than even healthy control rats), and in rat tubular epithelial cells subject to hypoxia-repurfusion." Since that effect seems fairly consistent, there's a significant risk that increased levels of vitamin A would increase levels of ACE2, which (as discussed in part 1) seems likely bad. So Chris recommends getting only enough vitamin A to avoid deficiency.

(Question: how easy is it to avoid publication bias / confirmation bias / etc. here? If some people found situations where ACE2 didn't get raised by Vitamin A, would that result have been published and would Chris have found it? He does mention studies like that for vitamin D, so that's at least evidence for yes and yes.)

### Limit: Vitamin D

Like vitamin A, vitamin D runs the risk of increasing ACE2 levels. We have three rat studies supporting this, two rat studies contradicting it, and one human study contradicting it.

The supporting rat studies show that: "Calcitriol, the active metabolite of vitamin D, increases ACE2 mRNA and protein in rat pulmonary microvascular endothelial cells treated with lipopolysaccharide, synergizes with diabetes to increase ACE2 protein in the renal tubules of rats, and in the brains of both hypertensive and healthy rats."

Of the contradicting evidence, the human study and one of the rat studies looked at serum ACE2, i.e. ACE2 which has been shed from cells and is circulating (I guess in the bloodstream). Serum ACE2 won't help the virus gain entry to cells, and might help protect against it. (No citation or explanation for this, but I guess the reasoning is that if the relevant part of the virus binds to serum ACE2, it won't subsequently be able to bind to ACE2 on the cell wall.) Serum ACE2 might not correlate with docked ACE2. Additionally, the rat study showed that vitamin D depletion had no effect on serum ACE2, but that doesn't mean an abundance of vitamin D would also have no effect; and the human study only showed a statistically significant difference in people with stage 5 kidney disease (with less severe kidney disease, the difference wasn't statistically significant; in healthy controls there was no difference).

The final rat study was looking at injury response of rat kidneys; the injury in question would normally increase ACE2 levels but vitamin D (or at least calcidiol, its partially activated metabolite) reduces that effect. But this seems to be caused by vitamin D making the kidneys more resilient to injury, not by directly suppressing ACE2. So it probably isn't relevant here.

Weighing up, vitimin D seems likely to increase ACE2, and Chris recommends against supplementing it (but still against becoming deficient).

**Except that** based on a more recent study, Chris [now recommends](https://chrismasterjohnphd.com/covid-19/update-on-vitamin-d-and-covid-19-using-the-first-observational-study-released) supplementing "to shoot for a 25(OH)D of 30 ng/mL" (more info at the link). He still recommends not going higher than that. He sent that to his mailing list on April 24th, and said he'd update the report "tomorrow"; as of this writing he has not done so.

(Note: He says 900 IU/day is sufficient for the average person to reach that level. By comparison, different institutions generally recommend daily intakes around [600 IU/day](https://en.wikipedia.org/wiki/Vitamin_D#Recommended_levels), and for the past few years I've been supplementing with 3000 IU on weekdays.)

### Limit: Calcium

And balance it with phosphorus. There's a complex system keeping them balanced in the blood, and they often have opposite effects. Notably, a high calcium:phosphorus ratio suppresses [fibroblast growth factor 23](https://en.wikipedia.org/wiki/Fibroblast_growth_factor_23), and a low calcium:phosphorus ratio increases it. FGF23 suppresses ACE2, so a high calcium:phosphorus ratio might increase ACE2. Chris recommends limiting calcium supplements to 1000 mg/day, and matching supplemental calcium with supplemental phosphorus 1:1.

### Avoid: Pelargonium Sidoides

[This](https://en.wikipedia.org/wiki/Pelargonium_sidoides) is also called Umcka. I don't think I've previously heard of it under either name. It has many of the same components as elderberry, but only a small amount of caffeic acid. Caffeic acid was what gave us most reason to think elderberry would work, so Umcka seems inferior to elderberry.

Umcka does have some antiviral effects, including against [HCoV-229E](https://en.wikipedia.org/wiki/Human_coronavirus_229E), but the mechanism for that is unclear. In cell cultures it increaes iNOS like echinacea; but also interferon, so if that generalizes it would be risky to take. It also increases [neutrophil](https://en.wikipedia.org/wiki/Neutrophil) activity; those are part of the immune system, so naively we might think that was a good thing, but high neutrophil counts seem to make SARS worse.

So basically this seems like it offers nothing we can't get from elderberry and echinacea, and is too risky. So Chris recommends avoiding it.

### Avoid: Honeybee Propolis

This hasn't been found to have significant direct antiviral properties against any viruses. It increases interferon responses in mice and chickens, so it may be somewhat helpful against some viruses, but it's too risky to use here. Chris recommends avoiding it.

### Avoid: Monolaurin

Monolaurin seems to damage lipid envelopes, as well as the membrane of cells without cell walls, so SARS-CoV-2 is probably vulnerable to it. But so are human T cells. The risk of impairing those seems unacceptably high, and Chris recommends avoiding monolaurin.

There's an argument that it "only [hurts] pathogenic organisms because it is effective against yeast and the bacteria that cause bacterial vaginosis, but not against lactobacillus", but Chris thinks that's just because [lactobacillus](https://en.wikipedia.org/wiki/Lactobacillus) has a cell wall, and there are probiotics which don't have anything like that which would probably be vulnerable too.

(I think the idea that this would only hurt pathogens seems absurd, but what do I know. The [citation](https://www.ncbi.nlm.nih.gov/pubmed/20008774) for that clause doesn't seem to present the argument, so I'm not sure who's making it or if Chris is representing it accurately, but people have been to occasionally say absurd things.)
