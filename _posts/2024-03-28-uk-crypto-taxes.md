---
title: Cryptocurrency taxation in the UK
layout: post
tags: [practical]
external_comments:
  - name: /r/ukpersonalfinance
    url: https://www.reddit.com/r/UKPersonalFinance/comments/1bprll5/
  - name: /r/plaintextaccounting
    url: https://www.reddit.com/r/plaintextaccounting/comments/1bsz7tr/
  - name: Plain Text Accounting forum
    url: https://forum.plaintextaccounting.org/t/repost-example-calculating-uk-capital-gains-with-ledger/227
lw_xpost: true
---
Mostly out of curiosity, I've been looking into how cryptocurrency is taxed in the UK. It's not easy to get what I consider to be a full answer, but here's my current understanding, as far as I felt like looking into it. HMRC's [internal cryptoassets manual](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual) is available but I didn't feel like reading it all, and some of it seems out of date (e.g. page [CRYPTO22110](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22110) seems to have been written while Ethereum was in the process of transitioning from proof-of-work to proof-of-stake). I also have no particular reason to trust or distrust the non-government sources I use here. I am not any form of accountant and it would be surprising if I don't get anything wrong.

My impression is HMRC tends to be pretty tolerant of people making good faith mistakes? In that if they audit you and you underpaid, they'll make you pay what you owe but you won't get in any other trouble. Maybe they'd consider "I followed the advice of some blogger who explicitly said he wasn't an accountant" to be a good faith mistake? I dunno, but if you follow my advice and get audited, I'd love to hear what the outcome is.

After I published, reddit user ec265 [pointed me](https://www.reddit.com/r/UKPersonalFinance/comments/1bprll5/article_cryptocurrency_taxation_in_the_uk/kwxvv4k/) at [another article](https://recap.io/guides/crypto-tax-uk-a-comprehensive-guide) that seems more thorough than this one. I wouldn't have bothered writing this if I'd found that sooner. I didn't spot anywhere where it disagrees with me, which is good.

### Capital gains tax

Very loosely speaking, capital gains is when you buy something, wait a bit, and then sell it for a different price than you bought it for. You have an allowance which [in 2023-24](https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances) is £6,000, so you only pay on any gains you have above that. The [rate](https://www.gov.uk/capital-gains-tax/rates) is 10% or 20% depending on your income.

But with crypto, you might buy on multiple occasions, then sell only some of what you bought. Which specific coins did you sell? There's no fact of the matter.[^pooling] But the law has an opinion.

[^pooling]: At least not as far as I know. Like, if I have £5581.21 in my bank account, the bank doesn't keep track of each of those 558,121 individual pennies, and when I pay for something decide *which* of those pennies is leaving my account. So if my grandmother asks what I spent my birthday money on, it may (or may not) be the case that she sent me £30 and I subsequently spent £30 on a giant dildo that I don't want to talk to her about; but I can truthfully tell her "that's a meaningless question, grandma". And as far as I know crypto works the same way. But who knows, there are a lot of cryptocurrencies out there and it wouldn't shock me if some of them don't. Compare [premium bonds](https://en.wikipedia.org/wiki/Premium_Bond): NS&I keeps track of exactly which bonds you own, and when you sell them they decide exactly which bonds you no longer own.

Crypto works like stocks here. For stocks HMRC explains how it works in a document titled [HS283 Shares and Capital Gains Tax (2023)](https://www.gov.uk/government/publications/shares-and-capital-gains-tax-hs284-self-assessment-helpsheet/hs284-shares-and-capital-gains-tax-2023), and there's also manual page [CRYPTO22200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto22200) which agrees.

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

For the same-day bucket, all buys get grouped together and all sells get grouped together. For the 30-day bucket, you match transactions one at a time, the earliest buy against the earliest sell. (Unclear if you get to group them by day; I don't see anything saying you do, but if you don't then interactions with the same-day rule get weird.)

So for example, suppose the middle three events above all happened on the same day. In that case, it would work out as:

* My section 104 holding is initially empty.
* Then, it contains 0.1 BTC purchased at a total of £105, average £1050/BTC.
* Then we have three things happening on the same day.
  * Grouping buys together, I buy 0.2 BTC for £420, average £2100/BTC.
  * I sell 0.15 BTC from that bucket, which I bought for £315.
    * Sale price is £195 so that's a loss of £120.
  * The bucket now contains 0.05 BTC bought for £105, average £2100/BTC.
* That bucket enters my section 104 holding. This now contains 0.15 BTC purchased at a total of £210, average £1400/BTC.
* I sell my remaining BTC for £45, which is a loss of £165.

And if the middle three all happened within 30 days of each other, then:

* My section 104 holding is initially empty.
* Then, it contains 0.1 BTC purchased at a total of £105, average £1050/BTC.
* Then, 0.2 BTC purchased at a total of £220, average £1100/BTC.
* The subsequent buy and sell get matched:
  * I buy 0.1 BTC for £305 and sell it for £130, making a loss of £175.
  * I also sell 0.05 BTC for £65, that I'd bought at £55, making a profit of £10.
  * So in total that sale makes me a loss of £165, and the 30-day bucket contains -0.05 BTC purchased at £55.
* That bucket enters my section 104 holding. This now contains 0.15 BTC purchased at a total of £165, average £1100/BTC.
* I sell my remaining BTC for £45, which is a loss of £120.

In all cases my total loss is £285, which makes sense. But I might get taxed differently, if this happened over multiple tax years.

Some more edge cases:

* I have no idea how these rules would apply if you're playing with options or short selling. I think those are both things you can do with crypto?
* If you receive crypto as a gift, you count it as coming in at market price on the day you recieved it. I'm not sure exactly how that's meant to be calculated (on any given day, lots of buys and sells happened for lots of different prices on various different legible exchanges; and lots also happened outside of legible exchanges) but I assume if you google "historical bitcoin prices" and use a number you find there you're probably good. So it's as if you were gifted cash and used it to buy crypto.
* Similarly, if you give it away as a gift, it's treated as disposing of it at market price on the day, as if you'd sold it for cash and gifted the cash.
* I think in both the above cases, if you buy or sell below market price as a favor (to yourself or the seller respectively) you still have to consider market price.
* If you trade one coin for another, you treat it as disposing of the first for GBP and buying the second for GBP. Mark both the sell and the buy at the market price of the second, so that if you're somehow trading £1000 of one coin for £1200 of another, £200 of profits is taxable now. I assume you also count fees for the sell, reducing your profit now.

### Mining and staking

According to [this site](https://www.unbiased.co.uk/discover/personal-finance/savings-investing/uk-cryptocurrency-tax-guide-everything-you-need-to-know), mining and staking both count as income. (And so do capital gains, if you look like a professional trader.)

For mining, the market price at the time you recieve the coins counts as miscellaneous income. You can deduct "reasonable expenses" whatever that means. (Price of hardware? Electricity?)

For staking, you can either count it as miscellaneous income or savings income. These two have different tax-free allowances. Unclear if you can count some as miscellaneous and some as savings to use both? Again you can deduct "reasonable expenses" whatever that means.

[This reddit thread](https://www.reddit.com/r/UKPersonalFinance/comments/rb13mc/uk_tax_implications_of_crypto_staking/) suggests "savings interest or miscellaneous income?" is just a grey area, in which case I'd expect HMRC to be pretty tolerant of you choosing either but kinda ಠ_ಠ if they notice you trying to use both. It links to manual page [CRYPTO21200](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21200) which sounds to me like it's just miscellaneous income. ec265 agrees.

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

and manual page [CRYPTO10100](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto10100), shortly after talking about stablecoins, saying:

> HMRC does not consider cryptoassets to be currency or money.

So I think that no, stablecoins are not an exception. And I weakly guess that coinbase's USDC interest counts as miscellaneous (and non-foreign) income, not personal savings income, unless you decide that staking income is also personal savings income.

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

### Airdrops and NFTs

I don't even really know what airdrops are and I don't care how they're taxed, but I suppose some readers might so manual page [CRYPTO21250](https://www.gov.uk/hmrc-internal-manuals/cryptoassets-manual/crypto21250) talks about them.

I don't care about NFTs either and didn't see a manual page on them, so ¯\\\_(ツ)\_/¯.

### Ledger

I like to track my finances with [ledger](https://ledger-cli.org), which means I want some way to encode these rules in that.

I think I have something that works decently, which I demonstrate in a sample file that you can see here.

I think it's mostly fairly standard outside of the `Holdings` top-level account. You can do e.g. `ledger bal not Holdings` to hide that. It doesn't make use of lot dates or prices to do matching (that's not how the UK needs you to do things). It doesn't use virtual postings.

It doesn't work in hledger because that doesn't support posting cost expressions like `0.01 ETH @ (£300 / 0.01)`. If you replace those with their calculated value it seems fine.

It should work fairly straightforwardly with stocks as well as crypto, with the caveat that I'm not sure how to encode stock splits and don't know if there are other fiddly details to complicate matters.

The things I'm most unhappy about are that it doesn't balance to 0, and that there's no help with average prices of Section 104 holdings.

<details markdown="1">
<summary>Example ledger file</summary>

```ledger
;; This ledger demonstrates calculating capital gains on cryptocurrency for UK
;; taxes. For more info see:
;; https://reasonableapproximation.net/2024/03/28/uk-crypto-taxes.html

2020/01/01 Buy
    ; When we buy an asset, we record it in two places. `Assets` holds what we
    ; currently own, grouped in some way that's convenient for general use (by
    ; which account they're in, currency, whatever). `Holdings` holds the same,
    ; but grouped by capital gains buckets.
    ;
    ; Annoyingly, they don't balance, since for capital gains purposes the price
    ; includes transaction fees. So the total ETH balance comes to 0 but the £
    ; balance comes to `Expenses:Fees`.
    ;
    ; The `@` and `@@` ensure the ETH and GBP amounts balance with each other.
    ; But the `Holdings` exchange rate is wrong, so we use `(@@)` to avoid that
    ; getting put in the price database.
    ;
    ; S104 is "Section 104". That's the technical term for that bucket.
    Assets:ETH                                  0.13 ETH @ £765.38
    Assets:GBP                              £-100.00
    Expenses:Fees                              £0.50
    Holdings:S104:ETH                          -0.13 ETH (@@) £100.00
    Holdings:S104:ETH                        £100.00

2020/01/10 Buy
    ; So after this, the "Holdings:S104:ETH" account records that we own 0.21
    ; ETH, that we paid £200.00 for.
    Assets:ETH                                  0.08 ETH @ £1243.75
    Assets:GBP                              £-100.00
    Expenses:Fees                              £0.50
    Holdings:S104:ETH                          -0.08 ETH (@@) £100.00
    Holdings:S104:ETH                        £100.00

2020/01/31 Staking
    ; When we get staking income, we can either record it as Income in ETH or £.
    ; Recording it as ETH seems more powerful, since it lets us answer all of:
    ;
    ; * "how much ETH have I got from staking?" (`ledger bal`)
    ; * "how much £ is that worth now?" (`ledger bal -X £`)
    ; * "how much was it worth when I got it?" (`ledger bal -X £ --historical`)
    ;
    ; Recording in £ would mean `ledger bal` fully balances in ETH (at least all
    ; buys and sells do), and total balance in £ equals `Expenses:Fees`. That
    ; seems like a potentially useful sanity check. We can at least check that
    ; non-staking transactions balance like that with
    ;
    ;     ledger bal not @Staking
    ;
    ; Still, I'm not sure this is better than just recording in £.
    ;
    ; We don't need to add every staking distribution individually. We can group
    ; several together and add them all at once, as long as they don't need to
    ; be distinguished for capital gains or income tax reasons or something. But
    ; then the price isn't accurate, so we probably want to follow it with an
    ; explicit entry for the price on the final day.
    Assets:ETH                                0.0014 ETH
    Income:Staking:ETH                       -0.0014 ETH
    Holdings:S104:ETH                        -0.0014 ETH (@) £942.86
    Holdings:S104:ETH                          £1.32

; This gives the actual price at the time we most recently received staking
; income. Price database entries given by `@` and `@@` are saved at midnight, so
; might as well use that time here too. We could equivalently leave out the
; time, `P 2020/01/31 ETH £981.38`.
P 2020/01/31 00:00:00 ETH £981.38

2020/02/05 Sell
    ; At this point, S104 holds 0.2114 ETH bought for a total of £201.32,
    ; average £952.32. That means 0.0514 ETH was bought for £48.95. I don't know
    ; if there's a way to have ledger help with that calculation or enforce that
    ; we did it right.
    Assets:ETH                               -0.0514 ETH @ £1578.97
    Assets:GBP                                £80.66
    Expenses:Fees                              £0.50
    Income:Capital Gains:ETH                 £-31.71
    Holdings:S104:ETH                         0.0514 ETH (@@) £80.66
    Holdings:S104:ETH                        £-48.95

2020/03/01 Sell
    ; Now a more complicated sell that we'll match with some non-S104 buys.
    ;
    ; When we buy, we know by the end of the day which Holdings bucket(s) it
    ; needs to go in. But when we sell, any buys or other acquisitions in the
    ; next 30 days affect which bucket(s) we're drawing from. So we won't be
    ; able to complete this transaction until April. (The bed-and-breakfasting
    ; bucket for this sell runs March 2-31 inclusive.) Until we do we might
    ; choose to just write the Assets and Expenses postings, leaving the
    ; transaction not to balance in ETH until we come back and fill in the rest.
    ;
    ; This counts as a capital loss (positive income), since after transaction
    ; fees, we buy it back in future for slightly more than we sell it for now.
    ;
    ; The three +ETH and the three -£ in Holdings empty out those buckets, and
    ; in this case there's none left over to take from the S104 bucket. The
    ; `(@)`s ensure that if we get cap gains wrong, the whole thing won't
    ; balance.
    Assets:ETH                                 -0.08 ETH @ £1635.90
    Assets:GBP                               £130.37
    Expenses:Fees                              £0.50
    Income:Capital Gains:ETH                   £1.06
    Holdings:SameDay:20200301:ETH               0.01 ETH (@) (£130.37 / 0.08)
    Holdings:SameDay:20200301:ETH            £-16.71
    Holdings:BnB:20200301:ETH                   0.05 ETH (@) (£130.37 / 0.08)
    Holdings:BnB:20200301:ETH                £-80.45
    Holdings:BnB:20200301:ETH                   0.02 ETH (@) (£130.37 / 0.08)
    Holdings:BnB:20200301:ETH                £-34.27
    ; Suppose that the Mar 31 buy below didn't happen. Then the last 0.02 ETH
    ; here would come from the S104 bucket. At this point the bucket contains
    ; 0.16 ETH bought for £114.72, average £952.31. (It changed slightly in the
    ; last transaction because of rounding errors.) So 0.02 ETH was bought for
    ; £19.05. In that case the Income posting and the last two Holdings postings
    ; would be replaced with:
    ;
    ; Income:Capital Gains:ETH               £-14.16
    ; Holdings:S104:ETH                         0.02 ETH (@) (£130.37 / 0.08)
    ; Holdings:S104:ETH                      £-19.05

2020/03/01 Buy
    ; We buy some back on the very same day. This is within 30 days after the
    ; Feb 5 sell, but the sell from today takes precedence. If we bought more
    ; than 0.08 ETH here, then the remainder would go in a BnB bucket to match
    ; against that. After today, the `SameDay:20200301` account is empty.
    Assets:ETH                                  0.01 ETH @ £1620.81
    Assets:GBP                               £-16.71
    Expenses:Fees                              £0.50
    Holdings:SameDay:20200301:ETH              -0.01 ETH (@@) £16.71
    Holdings:SameDay:20200301:ETH             £16.71

2020/03/07 Buy
    ; We buy some more back within 30 days after selling, so this is also
    ; matched against the Mar 1 buy. It's 31 days after Feb 5, so it doesn't
    ; get matched against that.
    Assets:ETH                                  0.05 ETH @ £1599.01
    Assets:GBP                               £-80.45
    Expenses:Fees                              £0.50
    Holdings:BnB:20200301:ETH                  -0.05 ETH (@@) £80.45
    Holdings:BnB:20200301:ETH                 £80.45

2020/03/31 Buy
    ; And more on the final day in the BnB window. Only 0.02 ETH gets matched
    ; against the previous sale, the rest goes into the S104 bucket. After
    ; today, the `BnB:20200301` account is empty.
    Assets:ETH                                  0.05 ETH @ £1703.67
    Assets:GBP                               £-85.68
    Expenses:Fees                              £0.50
    Holdings:BnB:20200301:ETH                  -0.02 ETH (@) (£85.68 / 0.05)
    Holdings:BnB:20200301:ETH                 £34.27
    Holdings:S104:ETH                          -0.03 ETH (@) (£85.68 / 0.05)
    Holdings:S104:ETH                         £51.41
```

</details>
