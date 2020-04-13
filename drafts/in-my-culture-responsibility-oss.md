---
title: "In my culture: the responsibilities of open source maintainers"
layout: draft
---
If you maintain an open source project, what responsibilities do you have towards your users? Some recent drama (that I won't link to) reminded me that there are large differences in how people answer that question.

(In the drama in question, this wasn't the only thing at issue. But it was a relevant question.)

I thought I'd take a stab at describing my best guess as to how we answer it [in my culture](https://medium.com/@ThingMaker/in-my-culture-29c6464072b2): in the culture that I think (and hope) many copies of me would implement, if we had that opportunity. (That culture doesn't attempt to exclude people who *aren't* copies of me, so it does need to be robust to attack. In my culture, we do not just assume in defiance of all evidence that everyone is friendly and trustworthy.)

Some of this will probably seem obvious to many readers, like "in my culture, murder is considered bad". Probably different bits to different readers. I'm interested in discovering which bits seem obvious to almost everyone, and which bits are controversial.

A lot of it follows from how I think about responsibility in general. But if you start to think "extending this response to this other situation, you'd get this, and that's a terrible idea"... in my culture, we don't immediately assume from this that I'm endorsing a terrible idea. Instead we check. Maybe I [disagree](https://www.greaterwrong.com/posts/6ntmpCvPDh3uhAi6j/the-sally-anne-fallacy) that that's how it extends. Maybe I hadn't thought about this, and you can change my mind about the initial response. Maybe I just straightforwardly endorse a terrible idea: in that case, it'll be much easier to push back once you've gotten me to admit to it.

I do not intend, in this essay, to discuss whether any particular person or group is living up to the standards I outline here. I may do that [in future](https://www.greaterwrong.com/posts/Btdy7Fefer7S5J6qE/now-here-s-why-i-m-punching-you). But how likely that is, and what that follow-up looks like, depends on whether the responses to this essay suggest a lot of people agree with my culture.

I think there are at least three important limitations to this essay. One is that as far as I know I've never been a maintainer of an open source project that had users other than myself, though I've made small contributions to a few. As such, I don't really know what the experience is like or how my culture deals with its challenges, much like I don't really know how my culture deals with the challenges of being on a moon base. I can make educated guesses, but that's all they are. I'm not going to explicitly flag them as such in the main body. (I'm already using the words "in my culture, we..." far too much. I'm not changing it to "in my culture, my educated guess is that we...")

Another is that I don't talk at all about the responsibilities of *users*, which is also an important part of the question. I'd like to, but... this essay has been knocking around in my head for at least a year and a half, I've made at least one previous attempt to write it that I gave up on, and I'm worried that if I don't publish it quickly I never will. I hope and believe that even with this omission, it is better for this essay to be published than to not be published.

(I also omit the question "what is this responsibility thing anyway?", but that seems less important to me right now. I've probably also overlooked important parts of the things I do talk about, but that too may not be a big deal.)

And a third is that without specific examples, what I've written is less constrained than what's in my head. It may well be possible to read this and agree with what I've written, and then to discover that your culture has a much stricter or much looser conception of responsibility than mine does.

With all of that out of the way: there are three questions I'm going to be focusing on here. When is responsibility taken on; what does it entail; and how do we react if people fail at it?

### When is responsibility taken on?

In my culture, taking on responsibility requires active involvement, but not explicit consent. It's possible to take on responsibility through negligence - to draw responsibility towards yourself without realizing that's what you're doing. In my culture, we're sympathetic towards people who do that, but we don't consider that this absolves their responsibility.

In my culture, merely making something available does not make you responsible for it. If you want to put something online and ignore anyone who tries to use it, you can do that. You are allowed to [shithub](https://news.ycombinator.com/item?id=10513328).

In my culture, you take on more responsibility for a project if...

* If you start *encouraging* people to use your project. If someone happens to stumble across your repository, you have no responsibility for what they do. If you see them describe a problem they have, and you say "oh hey, I had that problem too, you might want to check out my repo" you have a little. If you create a website for your project where you describe it as "the best way to solve this problem", you have more.

* If you have *many* users, whether you encouraged them or not. If you shirk your responsibilities, most of the harm done is to your users[^other-stakeholders]. With fewer users, the harm from not-acting-responsibly is lower, and so the responsibilities themselves are lower.

* If your users are *invested* in your project. If they can't easily stop using it, you have more responsibility to treat them well.

    Your users' exit costs are probably low if you make a video game, or "libpng but 30% faster" or "`find` but with a nicer command line syntax". In that case your users can probably just play a different game, or easily replace your tool with libpng or `find`.

    They're higher if you make a programming language, where migrating away requires rewriting a codebase. Or a document editor that can only save in its native binary format or pdf, so that there's no way to edit the documents without your tool.

* If you have the *ability* to accept responsibility. Handling responsibility takes time and it takes multiple skill sets. One person hacking on their side project simply cannot act in the same ways as a team of two full-time developers plus twenty volunteers. That team can't act in the same ways as the Mozilla Foundation.

* If you *act like* you're accepting responsibility. If you have a history of ignoring issues and pull requests, people should probably pick up on this. If you tell people you're going to break backwards compatibility, they shouldn't expect you to maintain it. Words like "production ready" increase your level of responsibility. Words like "alpha" decrease it, as do version numbers below 1.0.

[^other-stakeholders]: To the extent that this isn't true, I think most of the responsibility comes from something other than "being an open source maintainer". For example, if you're making a web scraper, I would suggest you have a responsibility to make it well-behaved by default - sleep between requests, stop after a certain number of failures, and so on. But that responsibility comes from the product, not the process. You can't avoid it with a disclaimer. And so it's not the focus of this essay.

A common thread here is that responsibility is related to *justified expectations*. "Expectations" in both the moral sense and the probabilistic sense. If someone can make a compelling argument "this person *morally ought to* accept responsibility here", or a compelling argument "I predict based on past behaviour that this person *will* act as though they've accepted responsibility here", then in my culture, that person has some degree of responsibility whether they like it or not.

Accordingly, in my culture you can disclaim responsibility in advance, simply by *saying that you're doing this*. Note that a pro forma warranty disclaimer in your LICENSE file isn't sufficient here. Instead you should say it at the entry points to your project - probably the README and the website (if there is one). Something like...

> Note that while I think this project will be useful to many people, I am not devoting much attention to it, and I'm prioritizing my own use cases. Bugs may be fixed slowly if at all. Features may be removed without warning. If this isn't acceptable to you, you should probably not rely on the project; or at least you should be willing to fork it, if necessary.

Or even:

> Note that while I think this project will be useful to many people, I have no interest in accepting responsibility for other people's use of it. Feel free to submit issues and pull requests; but I may ignore them at whim, and my whim may be arbitrary and capricious.

This won't usually be necessary. But if you feel in danger of taking on more responsibility than you'd like, you can do this.

### If you have responsibility, what does that entail?

In my culture, if we've taken on responsibility and now we want to discharge it, we do so with care. We give advance notice, and we try to find replacement maintainers. If we can't find a replacement maintainer, we still get to quit. But we try.

In my culture, we acknowledge that different people have different needs and goals, and not every project will be suitable for all users. We try to help users figure out whether our projects will be suitable for them before they get invested. We're open about the limitations of our projects, and about the design goals that we explicitly reject.

In my culture, we don't need to reply to every critic. But we do try to notice common threads in criticism, and address those threads. ("Address" doesn't mean that we necessarily try to solve them in a way that will satisfy the critics. It simply means we give our thoughts about them. We try to do that in such a way that even if the critics aren't happy with what we're doing, they at least feel like we've heard them and understood them.)

In my culture, we accept that some critics will be unkind, unfair and unproductive. This sucks, but it's a reality of life right now. We distinguish these critics from others. We are free to ignore them, and to ban them and delete their posts from the spaces we control. We do not use their actions to justify shirking our responsibilities to other critics.

In my culture, we also take care to check whether we're unfairly rounding people off as being unkind, unfair and unproductive. We don't require perfection from our critics. We try to hold ourselves and our supporters to the standards we expect of our critics. We moderate our spaces, but we try not to silence all criticism from them.

In my culture, we still introduce bugs, because we're still human. We try not to, of course. But we accept fallibility. When we fail, we do our best to fix it. We put more effort into avoiding more catastrophic bugs.

In my culture, we do not accept incompetence or indifference. These are signs that a person should not have taken on responsibility in the first place. We expect people to know the limits of their ability and of how much they care.

In my culture, we can set boundaries around how our future actions are constrained. We distinguish public APIs (where we mostly try to maintain backwards compatibility) from private APIs (where we mostly don't, and if people expect us to we point to the word "private"). We may reject bugfixes that we expect to cause too much ongoing future work, in hope of finding a better fix in future.

In my culture, sometimes we hurt people deliberately because the alternatives are worse. When we do, we own it. For example, sometimes we decide to remove a feature that people were relying on. We don't make that decision lightly. When we do it, we explain why we decided to do it, and we apologize to the people who were relying on it. We don't try to minimize their pain. We try to suggest alternatives, if we can; but we try not to pretend that those alternatives are any more suitable than they actually are. We give advance notice, if we can. We can be convinced to change our minds, if new information comes to light.

Of course, the degree to which we feel bound by all of this depends on the degree to which we've actually taken on responsibility. And note that in all of this, there's very little requirement for positive action. If we don't want to include a feature, we don't need to write it, or even merge the PR if someone else writes it. If we don't want to go in the direction our users want us to, we don't have to go there. We just have to make it clear that that's what we're doing.

### What if someone fails to act responsibly?

That is, if someone has taken on responsibility, whether intentionally or not, and then has failed to act like someone who's taken on responsibility... how do we respond?

In my culture, we mostly respond by acting as though this will happen in future.

We don't treat this as an indelible black mark against all aspects of the person. We'll still accept their contributions to other open source projects, for example. (Though perhaps not technically complex contributions, that will likely need a lot of maintenance from the same person going forward.) We'll accept their conference talks. We'll stay friends with them.

But we won't rely on their projects, because we don't expect their projects to be reliable. We warn others about this, but if others decide to use their projects anyway, we consider that none of our business.

We accept that people have a right to run projects as they see fit. We acknowledge that our conception of "responsibility" is a mere social convention. But social conventions are important. We provide an opt-out for this particular social convention, but if you don't opt out *explicitly*, we'll make it explicit for you.

We give second chances. If they want to take on responsibility in future, and if they seem to understand how they failed in the past, and they say they'll try to do better, we give them a shot, because that's reason to think it won't happen in future. If they still fail, and want a third chance, we take their second failure into account too.

We may fork a project, even if the maintainer doesn't approve, but we'll rarely attempt a hostile takeover from the outside. We'll make sure our fork is clearly distinguished from the original project.
