---
title: Cryptocurrency taxation in the UK
layout: draft
tags: [practical]
---
Mostly out of curiosity, I've been looking into how cryptocurrency is taxed in the UK. It's not easy to get what I consider to be a full answer, but here's my current understanding, as far as I felt like looking into it. I am not any form of accountant, I have no particular reason to trust or distrust the non-government sources I use here, and it would be surprising if I don't get anything wrong.

My impression is HMRC tends to be pretty tolerant of people making good faith mistakes? In that if they audit you and you underpaid, they'll make you pay what you owe but you won't get in any other trouble. Maybe they'd consider "I followed the advice of some blogger who explicitly said he wasn't an accountant" to be a good faith mistake? I dunno, but if you follow my advice and get audited, I'd love to hear what the outcome is.

### Capital gains tax

Very loosely speaking, capital gains is when you buy something, wait a bit, and then sell it for a different price than you bought it for. You have an allowance which [in 2023-24](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances) is £6,000, so you only pay on any gains you have above that. The [rate](https://www.gov.uk/capital-gains-tax/rates) is 10% or 20% depending on your income.

But with crypto, you might buy on multiple occasions, then sell only some of what you bought. Which specific coins did you sell? There's no fact of the matter.[^pooling] But the law has an opinion.

[^pooling]: At least not as far as I know. Like, if I have £5581.21 in my bank account, the bank doesn't keep track of each of those 558,121 individual pennies, and when I pay for something decide *which* of those pennies is leaving my account. So if my grandmother asks what I spent my birthday money on, it may (or may not) be the case that she sent me £30 and I subsequently spent £30 on a giant dildo that I don't want to talk to her about; but I can truthfully tell her "that's a meaningless question, grandma". And as far as I know crypto works the same way. But who knows, there are a lot of cryptocurrencies out there and it wouldn't shock me if some of them don't. Compare [premium bonds](https://en.wikipedia.org/wiki/Premium_Bond): NS&I keeps track of exactly which bonds you own, and when you sell them they decide exactly which bonds you no longer own.

I assume crypto works like stocks here, and for stocks HMRC explains how it works in a document titled [HS283 Shares and Capital Gains Tax (2023)](https://www.gov.uk/government/publications/shares-and-capital-gains-tax-hs284-self-assessment-helpsheet/hs284-shares-and-capital-gains-tax-2023).

The rule is that when you sell coins in a particular currency, you sell them in the following order:

* Any coins you bought that day;
* Any coins you bought in the *following* 30 days;
* Any coins you bought previously, averaged together as if you'd bought them all for the same price.

The "30 following days" thing is called the "bed and breakfasting" rule, and the point is to avoid [wash sales](https://en.wikipedia.org/wiki/Wash_sale) where you try to deliberately pull forward a loss you haven't incurred yet incurred for tax purposes. Wikipedia says "Wash sale rules don't apply when stock is sold at a profit", but that doesn't seem to be true in the UK. The rule applies regardless of if you'd be otherwise selling for profit or loss.

The third bucket is called a "section 104 holding". Every time you buy coins, if they don't offset something in one of the other buckets, they go in a big pool together. You need to track the average purchase price of the coins in that pool, and when you sell, you take the purchase price to be that average. Selling doesn't affect the average purchase price of the bucket.

If there are transaction fees, they count towards the purchase price (i.e. increase the average price in the bucket) and against the sale price (i.e. decrease the profit you made). This detail isn't in HS283, but it's in a separately linked ["example 3"](https://assets.publishing.service.gov.uk/media/641c4712ba5ac9000cb1a72d/HS284_Example_3_2023.pdf).

So suppose that at various (sufficiently distant) points in time, I

* buy 0.1 BTC for £100;
* buy 0.1 BTC for £110;
* sell 0.15 BTC for £200;
* buy 0.1 BTC for £300;
* sell 0.15 BTC for £50;

and each of these had £5 in transaction fees.

Then my section 104 holding contains:

* Initially empty.
* Then, 0.1 BTC purchased at a total of £105, average £1050/BTC.
* Then, 0.2 BTC purchased at a total of £220, average £1100/BTC.
* Then, 0.05 BTC purchased at a total of £55, average £1100/BTC.
  * Here I sold 0.15 BTC purchased at a total of £165, and I sold them for £195 after fees, so that's £30 profit.
* Then, 0.15 BTC purchased at a total of £360, average £2400/BTC.
* Then, 0 BTC purchased at a total of £0, average meaningless.
  * Here I sold 0.15 BTC purchased at a total of £360, and I sold them for £45 after fees, so that's £315 loss.

For the first two buckets, the document doesn't say what happens if you buy at two different prices in a bucket and don't sell all of the bucket. That is, suppose that the middle three events above all happened on the same day. What do I count as the purchase price of those coins? Unclear, maybe it's explained somewhere else, but my guess is I'm supposed to average them together in the same way. In that case, it would work out as:

* My section 104 holding is initially empty.
* Then, it contains 0.1 BTC purchased at a total of £105, average £1050/BTC.
* Then we have three things happening on the same day.
  * Grouping buys together, I buy 0.2 BTC for £420, average £2100/BTC.
  * I sell 0.15 BTC from that bucket, which I bought for £315.
    * Sale price is £195 so that's a loss of £120.
  * The bucket now contains 0.05 BTC bought for £105, average £2100/BTC.
* That bucket enters my section 104 holding. This now contains 0.15 BTC purchased at a total of £210, average £1400/BTC.
* I sell my remaining BTC for £45, which is a loss of £165.

In both cases my total loss is £285, which makes sense. But I might get taxed differently, if this happened over multiple tax years.

Some more edge cases:

* It's not clear what happens if there are overlapping buckets - like, I sell on September 1 and 15, and buy on September 10 and 20. If in total I buy more than I sold on September 1, then what counts for the B&B rule against the September 15 sale?
* I have no idea how these rules would apply if you're playing with options or short selling. I think those are both things you can do with crypto?
* If you receive crypto as a gift, you count it as coming in at market price on the day you recieved it. I'm not sure exactly how that's meant to be calculated (on any given day, lots of buys and sells happened for lots of different prices on various different legible exchanges; and lots also happened outside of legible exchanges) but I assume if you google "historical bitcoin prices" and use a number you find there you're probably good. So it's as if you were gifted cash and used it to buy crypto.
* Similarly, if you give it away as a gift, it's treated as disposing of it at market price on the day, as if you'd sold it for cash and gifted the cash.
* I think in both the above cases, if you buy or sell below market price as a favor (to yourself or the seller respectively) you still have to consider market price.
* If you trade one coin for another, you treat it as disposing of the first for GBP and buying the second for GBP. I assume you're supposed to use the market price in both cases, but if those don't match up I dunno what you're supposed to do. Not sure if fees are supposed to count for the sale (reducing your profit at the time) or the purchase (reducing your profit later) or what.

### Mining and staking

According to [this site](https://www.unbiased.co.uk/discover/personal-finance/savings-investing/uk-cryptocurrency-tax-guide-everything-you-need-to-know), mining and staking both count as income. (And so do capital gains, if you look like a professional trader.)

For mining, the market price at the time you recieve the coins counts as miscellaneous income. You can deduct "reasonable expenses" whatever that means. (Price of hardware? Electricity?)

For staking, you can either count it as miscellaneous income or savings income. These two have different tax-free allowances. Unclear if you can count some as miscellaneous and some as savings to use both? Again you can deduct "reasonable expenses" whatever that means.

[This reddit thread](https://www.reddit.com/r/UKPersonalFinance/comments/rb13mc/uk_tax_implications_of_crypto_staking/) suggests "savings interest or miscellaneous income?" is just a grey area, in which case I'd expect HMRC to be pretty tolerant of you choosing either but kinda ಠ_ಠ if they notice you trying to use both. It links to HMRC internal manual page [CRYPTO21200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21200) which sounds to me like it's just miscellaneous income.

I think the normal way staking works is that to get income, you need to lock your coins up for some period of time. New coins you receive are automatically locked, and when you want to do anything with them, you have to unlock them. So do you count as earning the coins when they arrive, or when you first unlock them? (When you initiate the unlocking, or when it completes?) "When they arrive" sounds like a pain in the ass, that can happen every few days with no engagement on your part and a different market price every time. But "when you unlock" has the same problem as CGT: are you unlocking coins you locked, or coins you earned, or what?

I assume it's "when they arrive" and you just gotta deal with that. [Coinbase](https://www.coinbase.com/) lets you download transaction history, including all staking rewards with market price in GBP at the time of receipt, so that's not so bad. But I've also played around with staking with [Trust Wallet](https://trustwallet.com/) and I can't immediately see a way to get staking history from that. Sadly I didn't earn enough to worry about.

For capital gains purposes, it sounds like both mining and staking count the same as if you'd bought the coins for market price at the time you received them. That would mean they can go in the same-day bucket or the B&B bucket, for matching against coins sold.

### Are stablecoins an exception?

The point of a stablecoin is to track a currency exactly. If I have 1 USDC, I should always be able to trade that for 1 USD, and vice versa. So should you treat any holdings in USDC the same as you'd treat a bank account denominated in USD?

I think this is relevant for three reasons:

* You [don't need to worry](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg78321) about capital gains tax in foreign currency bank accounts.[^s252]
* Coinbase pays interest on USDC. This isn't the same as staking, and it's not reported as staking in your transaction history. Interest in a foreign currency bank account counts as savings income, not miscellaneous income (see e.g. [this HMRC forum answer](https://community.hmrc.gov.uk/customerforums/pt/ce4ab931-49e7-ed11-913a-00155d978126)).
* I guess it also counts as [foreign income](https://www.gov.uk/tax-foreign-income)? That page isn't very clear, but I think the relevant question isn't "what currency are you getting interest in" but "what country is the bank account in". That probably depends on details of Coinbase's internal structure that I'm not familiar with; but probably they'd need to actively go to effort for UK users' USDC holdings to count as being in the UK, and probably if they did that they'd go out of their way to make sure I knew they do that, and I don't know they do it so probably they don't. If it's foreign income then it looks like that doesn't change how it's taxed, but you might need to report it differently.

[^s252]: While looking into this, I found the [Taxation of Chargeable Gains Act 1992, section 252](https://www.legislation.gov.uk/ukpga/1992/12/section/252/enacted). Section 251(1) says "if a debt is X, then it doesn't count for Y unless Z". Then when originally enacted, 252(1) said "251(1) doesn't apply to debts where..." and 252(2) said "252(1) doesn't apply to debts where...". Good grief. Parliament if you cannot use negatives responsibly we will take them away from you.

I guess this means that if exchange rates don't go your way, you might end up with less money than you started but still have to pay tax, and not be able to offset your losses against capital gains.

...but I don't think that's actually how it works. It looks to me like stablecoins just get treated like any other crypto, based on [this site](https://koinly.io/guides/hmrc-cryptocurrency-tax-guide/):

> Buying crypto with stablecoins is viewed as trading crypto for crypto, so any profits are subject to Capital Gains Tax.

and the [HMRC internal manual](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto10100), shortly after talking about stablecoins, saying:

> HMRC does not consider cryptoassets to be currency or money.

So I think that no, stablecoins are not an exception; and that coinbase's USDC interest counts as miscellaneous (and non-foreign) income, not personal savings income, unless you decide that staking income is also personal savings income.

### What if there's a fork?

Sometimes a cryptocurrency forks, and where you had one type of coin you now have two. How does that work?

Philosophically, I think the answer is: you always had both types of coin, it's just that no one was tracking the distinction between them. So on July 31 2017, I think that I have 0.1 BTC that I paid £100 for; on August 1 2017, I discover that actually I hold 0.1 BTC that I paid ??? for and 0.1 BCH that I paid ??? for, where the two ???s sum to £100.

(And when I sold 0.05 BTC for £30 a week previously, I actually sold 0.05 BTC and 0.05 BCH for amounts summing to £30, and it doesn't matter how they split at the time.)

In every case I know of, one of the split coins is considered the original and one is considered the fork. But I don't think there's a technical distinction there, it's just that there was a social (and sometimes legal) battle to decide who gets to use the original name and one group won that. ("Legal" example: when Ethereum Classic split off from Ethereum, the Ethereum Foundation had a trademark on the name. So whichever copy they endorsed was basically always going to get called "Ethereum", even if it turned out less popular.)

Of course, the outcomes of social-and-sometimes-legal battles can have important legal effects, even if there's no technical meaning to them. So one option would be to say that I paid £100 for 0.1 BTC, and £0 for 0.1 BCH. BTC has just had a drop in price (you can't reliably expect to sell 1 BTC + 1 BCH post-fork, for more than you could sell 1 BTC pre-fork), so your capital gains on BTC have gone down, but you can expect relatively high capital gains on BCH.

Another option would be to take the market price soon after they split. Suppose 1 BTC costs 9x as much as 1 BCH. Then we'd say I paid £90 for my BTC and £10 for my BCH.

[This article](https://help.recap.io/en/articles/3315653-how-do-forks-impact-cryptocurrency-tax-in-the-uk) recommends the second approach:

> HMRC does not prescribe any particular apportionment method. It is standard practice (based on the treatment of shares, because cryptoassets use the same rules) that the cost of the original cryptoasset is apportioned between the old and new cryptoasset, pro-rata in line with the respective market values of each cryptoasset the day after the hard fork. ...
>
> HMRC has the power to enquire into an apportionment method that it believes is not just and reasonable. Therefore, whichever method an individual chooses to use, they should keep a record of this and be consistent throughout their tax returns.

### Airdrops

I don't even really know what airdrops are and I don't care how they're taxed, but I suppose some readers might so [here's the HMRC internal manual page](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21250) on them.
