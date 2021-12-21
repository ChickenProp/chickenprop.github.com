---
layout: draft
title: "Walkthrough: Filing a UK self-assessment tax return"
---

The gov.uk [page on filing](https://www.gov.uk/log-in-file-self-assessment-tax-return) says you have to register first unless you sent a tax return last year. I've sent tax returns for several years running now, and I don't remember what registering was like.

<a href="/images/uk-self-assessment/01-personal-tax-account.png"><img src="/images/uk-self-assessment/01-personal-tax-account.png" style="max-width: 100%" alt="screenshot"></a>

Logging in I get sent to my "personal tax account" page. It tells me I paid the right amount of tax for 2019-2020, but that has to be based on guesswork because they don't know how much I donated to charity or put into pensions.[^charity-pensions] I click that box and another page tells me how much they think I paid and that they think it was right, but they don't explain either number. According to my own records[^ledger] I think I paid about £230 more than they think I paid.

[^charity-pensions]: For charity, they ask each time you file a return how much you expect to donate next year, so they have a decent guess for that. For pensions you'd think they have some idea, because they give me money every time money goes into my pensions. But also they ask later in the process how much money went into my pensions. So I'm not sure if they've taken it into account here.

[^ledger]: I track my finances with [Ledger](https://en.wikipedia.org/wiki/Ledger_%28software%29), so this is fairly easy for me to calculate. There's a caveat that I got a tax rebate in January 2021 for apparently overpaying in tax year 2019-2020. I marked that as coming out of the same account that I mark the tax deductions on my payslip as going in to. Since it arrived in tax year 2020-2021, I need to add that amount back in to get the amount I paid in that tax year. I could also mark it as "it arrived in my current account on this date but came out of my tax account on that date".

So I click the "complete your tax return" link in the top right box. I swear that was harder to find in the past. It explains who can and can't file a return, I assume I read that in a previous year and could then and still can, and I click 'start now'.

The first page has a bunch of stuff filled in for me, mostly accurate. The all-caps HAZELDEN seems unnecessary, you don't need to worry about my handwriting.

<a href="/images/uk-self-assessment/02.01-about-you-name.png"><img src="/images/uk-self-assessment/02.01-about-you-name.png" style="max-width: 100%" alt="screenshot"></a>

"P J" is my first two initials, not my first name, but nice try.

<a href="/images/uk-self-assessment/02.02-about-you-id.png"><img src="/images/uk-self-assessment/02.02-about-you-id.png" style="max-width: 100%" alt="screenshot"></a>

These say 'optional', which sounds like I don't need to give them if I don't want to. But up above it says

> 'Optional' indicates only complete if relevant to you

So maybe that means "give us this if you have one"? I'm probably safe to leave out my phone number, I don't want them calling me and I don't know what "STD" means.[^std] I'll grudgingly give them my email address I guess.

[^std]: In this context.

<a href="/images/uk-self-assessment/02.03-about-you-address.png"><img src="/images/uk-self-assessment/02.03-about-you-address.png" style="max-width: 100%" alt="screenshot"></a>

For years I've been using my parents' address for all official stuff, which is easier than telling banks and the like every time I move house. But some time this year I got a scary letter telling me I had to register for the electoral roll in my current place, which meant I got removed from it back in Bristol. So probably I have to give my current address here too.

(I don't see why it's any of the government's business where I live. Unfortunately they disagree, and they have all the power in this relationship.)

<a href="/images/uk-self-assessment/02.04-about-you-address-date.png"><img src="/images/uk-self-assessment/02.04-about-you-address-date.png" style="max-width: 100%" alt="screenshot"></a>

Well this is awkward. I moved in here in 2019, but I wouldn't have given this address when filling in my 2019-2020 tax return. Will they get pissy with me if I give the date I moved in? Eh, probably not.

Almost every address form I've filled in for the past several years has let me give my postcode and then select my exact address from a short dropdown, or enter it manually. This address form does not offer that.

The help for the country selector says

> Select the country where the income was earned from the drop-down menu.

But there's no dropdown box (just radio buttons for UK/Abroad), and "where the income was earned" is not very clear and I feel like it might not always agree with one's address? Fortunately I have never lived or earned income outside the UK.

In the help for the postcode box, they have a note

> Important: when entering your UK postcode the letters within the postcode must be in capitals.

Well done for finding and documenting a bug, HMRC, but this sounds like it should be an easy one to fix.

<a href="/images/uk-self-assessment/02.05-residency-dob.png"><img src="/images/uk-self-assessment/02.05-residency-dob.png" style="max-width: 100%" alt="screenshot"></a>

Residency is "based on whether you lived in England and Northern Ireland, Scotland or Wales for the majority of the tax year". I assume they mean "plurality", but maybe if you spent less than half the year in any of these, you don't pay tax at all. (Tax collectors hate him! Nonlocal man discovers one weird trick...)

That's not what "e.g." means, but the date is correct.

<a href="/images/uk-self-assessment/02.06-marital-status.png"><img src="/images/uk-self-assessment/02.06-marital-status.png" style="max-width: 100%" alt="screenshot"></a>

This is 'optional', so maybe there are people who don't have a marital status, as distinct from having the marital status 'single'? Or maybe, contra what they said above, it means I don't have to tell them, and then probably they'll treat me as single if I don't specify?

The options are: Single, Married, In Civil Partnership, Divorced, Civil Partnership dissolved, Widow, Widower, Surviving Civil Partner, Separated. Obviously you can be more than one of these in any given tax year, or even more than one of them simultaneously, so the help text is not very helpful. I guess the idea is you give the most specific version of the most recent change as of the end of the tax year? I don't know who would ever pick "separated". Luckily for me, the government hasn't decided it cares about long-term cohabiting relationships until we actively make them legible, at least not for tax purposes. So I get to just say "single" and not worry about it.

This is the only part of the page (maybe of the whole tax return?) where your gender becomes relevant, and then only for widows and widowers.

<a href="/images/uk-self-assessment/02.07-blind.png"><img src="/images/uk-self-assessment/02.07-blind.png" style="max-width: 100%" alt="screenshot"></a>

If they're assuming I didn't move house, you'd think they could assume I didn't go blind or get a blind spouse or civil partner.

I wonder what counts as an "other register". I think it's a crime to lie on my tax return, and quite possibly a crime to lie to my local authority about being blind. But it might not be a crime to lie on Honest Joe's Register Of Definitely Actually Blind People, and then to truthfully tell HMRC that I'm on that register. (This sounds like the sort of thing that you [patiently explain](https://xkcd.com/651/) to a judge and then the judge adds a little extra to your fine for being a smartarse. You try to appeal and the appeals court rejects with the comment "lolno". If you're going to try this, I think the funniest way would be to borrow a guide dog to take to court with you but make no other pretense at blindness. Maybe carry a cane slung over your shoulder.)

<a href="/images/uk-self-assessment/02.08-student-loan.png"><img src="/images/uk-self-assessment/02.08-student-loan.png" style="max-width: 100%" alt="screenshot"></a>

There's nothing here telling you how to figure out if you're on plan 1 or plan 2, but I am indeed on plan 1. The Student Loan Company told them that (according to the help text), but apparently didn't tell them enough to know that I do not have and am not repaying a postgrad loan.

---

The next page helps figure out which other pages should be included in the rest of the form, and which ones can be skipped.

In my case, I was an employee (or director or office-holder) during the tax year, so I answer yes and tell them how many employments (or directorships) I had (one) and the name of the employer.

I wasn't self-employed or in a partnership, but if I was I'd need to tell them how many of those I had and their names, too. I didn't get income from UK land or property over £1,000 (or indeed at all), I didn't receive any foreign income, and I don't need to complete the capital gains section.

For capital gains it's not entirely obvious that the answer is no. Here's the advice:

> You must report your capital gains and attach your computations if in the tax year either:
>
> * you disposed of chargeable assets which were worth more than £49,200
> * your chargeable gains, before the deduction of any losses, are more than £12,300
> * you have gains in an earlier year taxable in this period
> * you want to claim an allowable capital loss or make any other capital gains claim or election for the year
>
> In working out if the assets you disposed of were worth more than £49,200 use the market value of any assets you gave away or sold for less than full value and ignore disposals of:
>
> * exempt assets such as private cars, shares held within Individual Savings Accounts
> * assets to your spouse or civil partner, if you were living together at some time during the tax year
> * your own home where: [omitted a sub-list because I don't even own a home]
>
> In working out your total chargeable gains include any gains attributed to you, for example, because you're a settlor or beneficiary of a trust, or in certain cases where you're a member of a non-resident company.

This is fairly readable, but it keeps using words like "chargeable" and "allowable". Those sound like they have important technical definitions. Are we given the important technical defintions? Ha, no.

So here's my current understanding. I have shares in some index funds in ISAs and pensions, but I'm pretty sure I should ignore those. And I own a handful of individual stocks and cryptocurrencies, that I shouldn't ignore.

But so far all I've done is buy things and let their values go up or down. I haven't "disposed of" any of them: sold, traded or given away.[^trade-crypto] That means I don't need to worry about it. When I dispose of something, I'll need to work out how how much profit or loss I made on it, and also (as a separate question) how much it was worth at the time. If those amounts go over certain thresholds in total for the year (£12,300 and £49,200 respectively), then I need to fill in the capital gains section. And there's also another two reasons I might need to, but I'm confident I can ignore them too.

[^trade-crypto]: In the current tax year I've done a small amount of trading, because I couldn't directly buy the thing I wanted to. My vague impression is that because I bought and traded on the same day I can ignore this? (I'm not sure where I heard that, and I feel like high-frequency traders probably can't get away with that.) But also we're talking amounts small enough that I'm not going to reach either threshold this tax year, whether I can ignore this or not.

So I can answer "no" to capital gains because I haven't disposed of anything. Also, outside of ISAs and pensions I had less than £49,200 and my on-paper gains for the year were less than £12,300, so I could answer "no" even if I'd sold everything at the end of the year.

(Also, something unclear: to calculate gains, the obvious thing is to take "price when disposed of" and subtract "price when bought". And we're calculating "price when disposed of" anyway. But we're told to ignore certain disposals when calculating the total disposal price. Do we also ignore those disposals when calculating gains? I would guess so, but mostly I'm glad I don't have to worry about it.)

---

The next page is the same sort of thing, but in my case less clear.

<a href="/images/uk-self-assessment/04.01-interest.png"><img src="/images/uk-self-assessment/04.01-interest.png" style="max-width: 100%" alt="screenshot"></a>

An important detail here is that you can omit interest earned in an ISA. Nothing on the page says so. You might think that if you only earned interest in an ISA, you say here that you earned interest, and later you tell them it was only in an ISA. At any rate, that's what I thought the first time. But then they told me I owed tax on all that interest, so I decided to go back and tell them I didn't earn any interest.

I guess that was lying on my tax return, and I just admitted to a crime? Thanks, HMRC.

<a href="/images/uk-self-assessment/04.02-dividends.png"><img src="/images/uk-self-assessment/04.02-dividends.png" style="max-width: 100%" alt="screenshot"></a>

Similarly, dividends earned in an ISA don't count here. I did not earn any dividends outside of an ISA last tax year. (This tax year I've earned about £1.50 of them so far.)

<a href="/images/uk-self-assessment/04.03-pension.png"><img src="/images/uk-self-assessment/04.03-pension.png" style="max-width: 100%" alt="screenshot"></a>

Ever get the feeling that someone said "every question needs help text" and the person writing the help text was phoning it in?

<a href="/images/uk-self-assessment/04.04-child-benefit.png"><img src="/images/uk-self-assessment/04.04-child-benefit.png" style="max-width: 100%" alt="screenshot"></a>

I don't know how Child Benefit works. Is anyone in the position of "I got it during the tax year starting on 6 April 2020, but the payments had stopped before 6 April 2020"?

<a href="/images/uk-self-assessment/04.05-covid.png"><img src="/images/uk-self-assessment/04.05-covid.png" style="max-width: 100%" alt="screenshot"></a>

This seems to be an "if you made a mistake, that's fine, you can correct it now" thing. I appreciate that.

<a href="/images/uk-self-assessment/04.06-other-income.png"><img src="/images/uk-self-assessment/04.06-other-income.png" style="max-width: 100%" alt="screenshot"></a>

This help text is long so I'm not including it. This includes casual earnings, and I might have had some of those? Certainly I have in other years, like the money I sometimes got for getting my brain scanned. But it says I don't need to report if the total from this plus self employment is less than £1,000, which it is for me.

They don't mention gambling income, and mine isn't that high anyway, but I think that should be excluded.

<a href="/images/uk-self-assessment/04.07-income-tax-losses.png"><img src="/images/uk-self-assessment/04.07-income-tax-losses.png" style="max-width: 100%" alt="screenshot"></a>

I don't know what these are and the help text doesn't help much, but probably not.

<a href="/images/uk-self-assessment/04.08-pension-savings-tax-charges.png"><img src="/images/uk-self-assessment/04.08-pension-savings-tax-charges.png" style="max-width: 100%" alt="screenshot"></a>

Again, long help text. But the gist seems to be that if I have more than £1,073,100 in pensions in total (5 significant digits! Impressive precision), or if I (or my employer) put more than £40,000 into pensions this year, I need to worry about this. Neither is the case for me. (Yet! Growth mindset.)

---

One more page of basically the same thing, but this one is easy again. Yes, I contributed to a personal pension. Yes, I gave to charity (and claimed gift aid). My partner and I are ineligible for married couple's allowance (we are neither married nor in a civil partnership, and anyway we were both born after 6 April 1935). Nor can I transfer 10% of my personal allowance to them (we are neither married nor in a civil partnership). I don't want to claim other tax reliefs. I don't have a tax adviser. I... think I haven't used any tax avoidance schemes, but that probably relies on distinguishing between schemes that HMRC thinks are legit (like giving to charity) and schemes that HMRC thinks are kinda sus. I haven't used any disguised remuneration avoidance schemes. I am not acting in capacity or on behalf of anyone else.

There is one interesting one here.

<a href="/images/uk-self-assessment/05.01-tax-refunded.png"><img src="/images/uk-self-assessment/05.01-tax-refunded.png" style="max-width: 100%" alt="screenshot"></a>

I got a tax rebate in tax year 2020-2021 from 2019-2020, and then another in tax year 2021-2022 from 2020-2021. I think neither of these is what it's asking about. Rather, I think this is asking about rebates in tax year 2020-2021 from tax already paid in that tax year.

---

Having filled in those three pages, I get an overview page listing what I've filled in so far and what I still need to do. The first thing to do is income. I only had one employer this year, so I only have one section for that.

The first three questions are answered by my P60, which I was able to find because my employer emailed it to me. They want to know my employer's PAYE reference, my pay before tax taken off, and my tax taken off. (My P60 agrees with my own records about how much tax I paid.)

These last two are "optional". First time I did this, I thought that meant "we have a copy of your P60 too, so if you don't fill this in we'll fill it in for you". Nope, it means "if you don't fill this in we'll think it's 0".

Then they want to know if I got any tips or other payments not on my P60, which I didn't. This one is optional too - if I try to enter 0 it complains and tells me to leave it blank.

Also, some helpful Javascript on the page makes sure your numbers are given to two decimal places, i.e. pounds and pennies. You can't enter pennies, they'll be truncated (£567.89 becomes £567.00), but it makes sure to show you them.

They also want to know if I was a director (no) and something about "inside off-payroll working engagements" (not entirely clear what this is, but no).

I did have benefits, medical insurance. The value of that will be on my P11D, not my P60, but they don't ask for it here. That's on the next page, which I guess I won't get shown if I didn't have any?

The final question almost caught me out:

<a href="/images/uk-self-assessment/06.01-expenses.png"><img src="/images/uk-self-assessment/06.01-expenses.png" style="max-width: 100%" alt="screenshot"></a>

I don't normally think of myself as having employment expenses. But I've been working from home, and this is how I claim back some of my utility bills.

---

My answers to that question added two new pages that weren't listed on the overview before. First for taxable benefits and expenses, listed on my P11D. I have an email copy of that too, I just copy the amount listed for medical insurance on that into the "private medical or dental insurance" box on the page.

They even tell me which number to use. (I have three, "cost to employer", "amount made good or from which tax deducted" and "cash equivalent". The middle one is £0 and the others are equal, so it's not hard for me. But if the middle one wasn't £0, I wouldn't be sure whether to use "cost to employer" or "cash equivalent" - but the latter is the one labeled with an "11", so that's the one to use.)

Then there's a page for expenses not reimbursed, of which WFH costs fall in "Other expenses and capital allowances".

The help text doesn't make it clear how much I can claim, but the [link](https://www.gov.uk/tax-relief-for-employees/working-at-home) mostly does. I can claim for gas, electricity, metered water, business phone calls and dial-up internet; but only the amount of them that's related to my work. (Strictly it sounds like this would exclude things like the week when my ISP failed to connect me and I had to use mobile data for internet. As it happens I didn't use enough to pay extra, but if I had... I guess I'd be able to claim for some of it, even though this page only mentions dial-up?)

I can claim up to £6/week without evidence, or more with evidence. (I don't have evidence.) I can only claim if I have to work from home, not if I do so by choice. I had to look this up, but there were four months where my office was closed (April, May, June and November), so call it 16 weeks. It's also not entirely clear whether that's "£6/week no matter how much I had to work from home that week" or whether I should think of it as £1.20/day, but that doesn't affect me personally. I assume I shouldn't count any holidays I took, but I don't think I took any in those months.

Following this page there's one for providing any more information.

<a href="/images/uk-self-assessment/07.01-other-information.png"><img src="/images/uk-self-assessment/07.01-other-information.png" style="max-width: 100%" alt="screenshot"></a>

I'm not sure what kind of thing I'd need to use it for, but I don't have anything to add. Which is good because it's kind of embarrassingly limited. I'm not allowed to use multiple lines or most punctuation?!

---

Next up is pensions. I have two pensions that I contributed to this year, my employer one and an SIPP. I'm not aware of having a retirement annuity contract whatever one of those is, and I don't have any overseas pensions, so there are only one or two questions relevant to me. Still, this page is frankly confusing.

<a href="/images/uk-self-assessment/08.01-pension-tax-relief.png"><img src="/images/uk-self-assessment/08.01-pension-tax-relief.png" style="max-width: 100%" alt="screenshot"></a>

I have a standing order to deposit into my SIPP every month, and then about 11 weeks later, 25% of that amount gets added as tax relief. (It's supposed to be 6-8 weeks, but it's not.) So do I count the tax relief in the tax year when it arrived, or the tax year when I deposited the money? So far I've been doing when I deposited, and that's what they suggest by telling me to multiply the amount I contributed by 1.25. On the other hand, if that calculation is always correct, why don't they save me the trouble and do it for me? In any case, there's nothing saying explicitly what to do. It probably doesn't make that much difference as long as I'm consistent year-on-year, so let's stick with "deposited".

<a href="/images/uk-self-assessment/8.02-no-relief-given.png"><img src="/images/uk-self-assessment/8.02-no-relief-given.png" style="max-width: 100%" alt="screenshot"></a>

Meanwhile, my employer pension has two sources of contributions. There's the stuff "my employer pays", doesn't get written on my payslip, and the stuff "I pay", which does. These are both part of my compensation package, but I guess some people don't realize money is fungible or something? So as far as I can tell, what's happening is we pretend that if my employer doesn't write it on my payslip it's not coming out of my salary, and we make things more complicated and less transparent in service of this fiction.

Anyway, the stuff "my employer pays" I think isn't relevant here. The stuff "I pay" is. In my case, this is also paid relief at source, meaning it's deducted after I've paid tax on it. So that sounds like it matches "Payments to your employer's scheme which were not deducted from your pay before tax". Buuut... I *think* that question is trying to ask about payments which were *expected* to be deducted before tax. At my previous job that's how it happened, and it sounds like under certain circumstances that could have gone wrong and then I'd use this question to correct that.

So I think contributions "I paid" to my employer pension actually go along with my SIPP contributions as the answer to the first question, and I leave this one blank. (It's not marked optional, but it doesn't accept 0.)

---

For charity, there's three questions that look maybe relevant.

<a href="/images/uk-self-assessment/09.01-gift-aid.png"><img src="/images/uk-self-assessment/09.01-gift-aid.png" style="max-width: 100%" alt="screenshot"></a>

For pensions I needed to figure out my contribution plus what was added, for charity I just need to give my own contribution. Obviously. Still, this number is easy to find in my records. (I tag all gift aided contributions in my ledger.)

<a href="/images/uk-self-assessment/09.02-one-off.png"><img src="/images/uk-self-assessment/09.02-one-off.png" style="max-width: 100%" alt="screenshot"></a>

I think this is a roundabout way of asking how much gift aid I expect to donate in tax years 2021-22 and/or 22-23? They'll assume it's the amount I donated this year, minus whatever I put here. And then they'll adjust my tax code for that, to reduce overpayments.

Most of my charity donations were monthly recurring, but that left me slightly below my "10% of take-home" target, so I did do a one-off donation on top of that which I don't particularly expect to repeat. (But I haven't checked how far below my target I am right now.) But I do expect to donate more in total this year, so I'm going to leave this blank.

<a href="/images/uk-self-assessment/09.03-foreign.png"><img src="/images/uk-self-assessment/09.03-foreign.png" style="max-width: 100%" alt="screenshot"></a>

Not much help about what specific countries count as "certain" here, or what the definition of charity is for tax purposes. Some of the money I donate goes to [MIRI](https://intelligence.org/), which is not a UK charity. But it goes via [EA Funds](https://funds.effectivealtruism.org/), which is. So I'm pretty sure I haven't officially done this.

For the rest: I'm not asking to treat any payments as being made in a year other than they were actually made. And I haven't given any shares, securities, land or buildings to charity, so I can ignore these.
