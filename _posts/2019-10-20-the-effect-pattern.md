---
title: "The Effect pattern: Transparent updates in Elm"
layout: post
lw_xpost: true
external_comments:
  - name: /r/elm
    url: https://www.reddit.com/r/elm/comments/dkou3c/the_effect_pattern_transparent_updates/
---
I don't like writing tests in Elm[^dont-like-elm]. Naively, it seems like the fact that all Elm functions are pure would make it easy. But I've still never really been able to test the things I really want to.

[^dont-like-elm]: I'm not a fan of writing Elm code in general, but that's for [mostly unrelated reasons](https://www.reddit.com/r/programming/comments/992qe5/elm_019_released/e4kncds/?context=1).

It's possible that I'm not very good at writing tests in general. But even if that's true, I don't think it's the whole story.

I have another hypothesis, which is: much of the reason is that although Elm functions are *pure*, in the sense of "given the same input, they return the same output" - they aren't necessarily *transparent*, in the sense of "you can look at the output and verify that it's correct".

To recap[^accessibility], I would describe the Elm architecture as consisting of:

[^accessibility]: I'm not going to recap in detail. This post is mostly targeted at people who already know Elm. I kind of hope others can get something from it too, but I'm not trying hard for that.

* `Model` - a type describing the data you're interested in. This is usually mostly transparent. There are some opaque blobs where components haven't exposed their internals, but I think those mostly aren't the kind of opacity that gets in the way[^philosophically-opposed].

* `Msg` - a type describing the messages your app passes around. Again, mostly transparent, with opaque blobs where components haven't exposed their messages. I feel like this opacity is maybe a bit more annoying, but still not very.

* `update : Msg -> Model -> (Model, Cmd Msg)` - a function describing the logic of your app (or whatever it is you're architecting). The `Model` and `Msg` are still transparent, but the second return value is a `Cmd Msg` which is completely opaque, and which is the main source of the problem.

* `view : Model -> Html Msg` - a function describing the rendering of your app. `Html Msg` is also arguably opaque, but you can inspect it using [elmer](https://github.com/brian-watkins/elmer)[^elmer], or (as I discovered while writing this post) the `Test.Html` modules in the [test](https://package.elm-lang.org/packages/elm-explorations/test/1.2.2/) package. I'm not sure if you can inspect it as deeply as you might want, I haven't explored these much yet.

[^philosophically-opposed]: I'm somewhat philosophically opposed to this kind of opacity, even if practically I don't think it's a big problem. But my philosophical objections aren't relevant here.

[^elmer]: I'm confused about how Elmer works. It uses kernel code, which isn't supposed to be available to mere mortals. The elm.json file says its package name is "elm-explorations/elmer", which would explain how it can use kernel code; but the name typically points at a github repository, and that repository doesn't exist. Has Elmer found some way to circumvent the kernel code restrictions? It seems to be something to do with the [elmer-test](https://www.npmjs.com/package/elmer-test) library on npm, but... maybe I'm blind, but I can't even find the source code for that online? It'll be in my filesystem at work somewhere. Maybe some day I'll investigate further.

    I wish Elmer had a README section like "oh, you thought this was impossible? Surprise, sucker! Here's how it works!" I've seen many projects that I wish had that.

Now, in my experience[^experience], a lot of the logic in an app is contained in the way the `update` function chains. "After receiving *this* message, we send a command which eventually results in receiving *that* message, and then we want to put *some value* in the model." And we can't test those chains, because `Cmd` is opaque. So that's part of why I haven't liked writing Elm tests.

[^experience]: My vast experience of writing one Elm app, in one company, mostly with other developers who have approximately the same amount of experience.

But I think I've found a method that will help, at least somewhat. You don't need to rewrite anything except your `update` function, and I actually think it's a mild improvement even if you ignore testing. I call it the Effect pattern.

We've implemented this pattern at work, in a couple of places. When I first did so, the first two tests that I wrote both revealed bugs in my code. (I think I'd known about both of those bugs but forgotten them. I wasn't consciously expecting the tests to fail.) Neither of those tests needed to be updated when I fixed the bugs. I think this is a good sign, but it's not very strong evidence. Beyond that, I mostly have theory.

### Example

I'm going to demonstrate with a simple app. It'll be buggy, and the bug will be hard to test for. Then I'm going to refactor the app to make it more testable, and write a test. Then I'm going to fix the bug, and verify that the test now passes. I think the app is too simple to make the benefits really obvious, but hopefully I can convince you anyway[^convince].

[^convince]: Or, if it happens that I'm wrong about the benefits, I hope I can explain myself well enough that someone can understand why I'm wrong, and then convince *me*.

So [here's the app](https://ellie-app.com/6XP8K8dLqZda1). It has a number, and a button to increase the number by one, and a button to multiply it by two. When you press one of those buttons, the number gets "saved to the server"; normally that would be an http request, but we emulate that by just sending a time delayed response. There's a message telling you whether the number has been successfully saved yet.

Actually, most of the app supports increasing the number by any integer, and multiplying it by any integer. That's not implemented in the view though. The [Watsonian](https://scifi.stackexchange.com/questions/109910/what-do-the-terms-doylist-doylian-and-watsonian-mean) explanation for this is that the developer has a habit of overengineering things. The Doylist explanation is that it makes the interesting bits more interesting, but not significantly more complicated; and the view code is boring.

The bug is: if you press buttons quickly, the "saved" message will temporarily be wrong. You've sent two messages to the server, and one hasn't come back yet; the number that's been saved is not the number on display. Silly, but I think it works as a demonstration.

(There are surely also bugs related to the size of numbers, but I'm not interested in those right now. Additionally, a real life server would have other problems like "sometimes requests will fail" and "sometimes requests will be handled out of order"; the second in particular is hairy, but I haven't emulated these possibilities.)

Here's the update function:

```elm
update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
    case msg of
        IncBy n ->
            ( { model | count = model.count + n, saved = False }
            , fakeSaveCount (model.count + n)
            )
        MultBy n ->
            ( { model | count = model.count * n, saved = False }
            , fakeSaveCount (model.count * n)
            )
        Saved ->
            ( { model | saved = True }, Cmd.none )

```

You can probably guess roughly what `Model` and `Msg` look like just from that.

As written, how would you test for the bug? I think the way to do it is to write a wrapper `update1 msg model = Tuple.first <| update msg model` that ignores the `Cmd`. Then test that

```elm
initialModel
    |> update1 (IncBy 1)
    |> update1 (IncBy 1)
    |> Saved
    |> .saved
```

is `False`. And that works to detect the bug, but you need to know exactly what messages get sent in response to `IncBy 1`. In this case that's easy. In more involved cases,  you'll need to know it for every `Msg` constructor, and you're going to make a mistake.

Here's how I'd rewrite for testability:

```elm
type Effect = ESaveCount Int

update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
    let (newModel, effs) = updateE msg model
    in (newModel, Cmd.batch <| List.map (\e -> runEffect e model) effs)

updateE : Msg -> Model -> (Model, List Effect)
updateE msg model =
    case msg of
        IncBy n ->
            ( { model | count = model.count + n, saved = False }
            , [ESaveCount (model.count + n)]
            )
        MultBy n ->
            ( { model | count = model.count * n, saved = False }
            , [ESaveCount (model.count * n)]
            )
        Saved ->
            ( { model | saved = True }, [] )

runEffect : Effect -> Model -> Cmd Msg
runEffect eff _ =
    case eff of
        ESaveCount n -> fakeSaveCount n
```

That is, we split it into two parts. One part updates the model, and describes the side effects transparently. The other part turns the transparent side effects into opaque ones.

Even if we're not testing this, I kind of like it. It's nice to have a complete list of possible side effects in one place, where it isn't mixed in with model updates. But I do also want to be able to test it. Obviously, now we test `updateE` instead of `update`. Is that any better? I think so.

Here's a simple example of something we can now test that we couldn't before: "whenever `update` changes `model.count`, it makes a server request to save the new value; and whenever it makes a server request to save a value, that value is now in `model.count`." (We may need to write fuzzers for our `Msg` and `Model` to do this.) To do this, we need to trust that `runEffect` works properly, that `ESaveCount` actually generates a server request; but I think that's a fairly okay thing to trust.

But that's small fry. I spoke above about chaining the update function, and that's harder. If you're going to do it properly, you still need to know what messages get sent in response to every `Effect` constructor, and you can't learn that from calling the function. But I still think this is an improvement: if done right, I would expect (and my limited experience agrees) that typically `Effect` will have many fewer constructors than `Msg`, and for each one, the transformation to messages is fairly simple.

Here's a helper function that you can use to test `updateE`:

```elm
runUpdates
    : (state -> msg -> model -> (state, (model, List effect)))
    -> (state -> effect -> model -> (state, List msg))
    -> state
    -> model
    -> List (List msg)
    -> (state, model)
runUpdates updateE runEffect initialState initialModel messages =
    let go = runUpdates updateE runEffect
    in case messages of
        [] -> (initialState, initialModel)
        [] :: moreMsgs -> go initialState initialModel moreMsgs
        (msg1 :: moreMsgs1) :: moreMoreMsgs ->
            let (newState1, (newModel, effs)) =
                    updateE initialState msg1 initialModel
                (newState2, newMsgs) =
                    List.foldl
                        (\e (s, m) -> runEffect s e newModel
                            |> Tuple.mapSecond ((++) m)
                        )
                        (newState1, [])
                        effs
            in go newState2 newModel ((moreMsgs1 ++ newMsgs) :: moreMoreMsgs)
```

On a high level, the way it works is this: you pass it your regular `updateE` function and a mocked `runEffect` function, together with an initial model and a list of messages to send. The messages get sent, one at a time, to the model. Any effects caused by `updateE` are handled by the mock `runEffect`, which returns a list of additional messages to be sent in future. We keep running until there are no more messages.

There are two complications. One is that we also thread through some arbitrary state, that can be updated both by `updateE` and `runEffect`[^updateE-state]. We'll see the value of that later, but if you don't need it,

```elm
stateless : (a -> b -> c) -> (() -> a -> b -> ((), c))
stateless f () a b = ((), f a b)
```

is a helper function that lets you forget about it.

[^updateE-state]: My initial version only exposed state to `runEffect`, because we didn't need it for `updateE` on the tests we've written so far at work. But I couldn't see a way to avoid it, or something like it, for this example.

    I weakly guess that if the state updates generated by `updateE` depend on the message, that's already a bad sign. We need it for the test I'm about to write, but that's precisely because the model doesn't keep track of everything it needs to.

The other complication is that we pass in a *nested* list of messages. That's to give us some control over timing. Any messages returned by `runEffect` will be handled after the current "batch" of messages, but before the next "batch". So if you want to test the sequency "run `msg1`, then `msg2`, then handle the results of `msg1`", you would pass in `[[ msg1, msg2 ]]`. If you want to test the sequence "run `msg1`, handle its results, then run `msg2`", you would pass in `[ [msg1], [msg2] ]`.

I have a feeling this won't always be enough control, and in future the mocked `runEffect` will need to return `List (List msg)` in place of `List msg`. (With the first item being messages to run immediately, the second being items to run between the current and the next batch, and so on. You'd get the current behaviour by returning `[ [], msgs ]`.) But it suffices for now.

And here's one way to test the app:

```elm
type alias TState = (Int, List Expectation)

testSave : Test
testSave =
    let
        mockUpdateE : TState -> Msg -> Model -> (TState, (Model, List Effect))
        mockUpdateE (n, exps) msg model =
            let (newModel, effs) = updateE msg model
                newState = case msg of
                    Saved ->
                        ( n - 1
                        , (newModel.saved |> Expect.equal (n - 1 == 0))
                            :: exps
                        )
                    _ -> (n, exps)
            in (newState, (newModel, effs))

        mockRunEffect
            : TState
            -> Effect
            -> Model
            -> (TState, List Msg)
        mockRunEffect (n, exps) eff model =
            case eff of
                ESaveCount _ -> ( (n+1, exps), [Saved] )
    in
    test "Doesn't pretend to be saved" <| \() ->
        let ((_, exps), _) =
                runUpdates mockUpdateE mockRunEffect (0, []) initialModel
                    [[IncBy 1, IncBy 1]]
        in Expect.all (List.map (\e () -> e) exps) ()
```

I admit, this is pretty ugly. But I think it's conceptually quite simple. The state keeps track of two things: how many save requests are currently "in flight", which gets updated as we step through; and a list of assertions, which we verify at the end. Every time we send a request (with `ESaveCount`), we increase the in-flight count. Every time we receive a Saved message, we decrease it, and add a new assertion to the list: `model.saved` should be `True` iff there are no requests remaining in-flight.

You can see this version of the app [here](https://ellie-app.com/6YqM2vkLWkba1). Note that to avoid the hassle of playing with `Test.Runner`, I've replaced the `Test` with an `Expectation` by commenting out the `test "..."` line (but nothing underneath), and put the result in the view. You can remove the second `IncBy` and check that it now passes (because if there's only one `IncBy`, the bug doesn't exhibit).

Now to fix the bug, and see what effect that has on the tests. If you can't fix a bug without changing the tests you wrote for it, that's a bad sign about your tests.

The test uncovered the bug by keeping track of some additional state. So the obvious thing to do is to move that state into the model. Count the number of requests in-flight, and only count as "saved" if there are none[^savedCount]. In fact, we no longer need `saved` as a field at all; as written in the test, `saved` is true iff there are no in-flight requests.

(This doesn't work in the real world, where requests can fail. I think it's fine as a demonstration.)

[^savedCount]: I had planned to take a different approach, storing both "current count" and "the count saved on the server" (which would be placed in the model through a new argument on the `Saved` constructor). But that has its own bugs: suppose the count starts at 0 and quickly goes 1, 0, 1. Then we'll get messages `Saved 1`, `Saved 0`, `Saved 1`. After the first `Saved 1`, we'll think we're saved until `Saved 0` arrives.

Removing `saved` actually does mean we need to rewrite the test. But only minorly, and we can do that before fixing the bug. All we need is to replace the reference `newModel.saved` with `isSaved newModel` where `isSaved = .saved`. Then when we fix the bug, we rewrite that as `isSaved m = m.inFlight == 0`, and the test passes with no more changes. We'll want to use that function in the `view` anyway. (Avoiding this kind of thing is one reason people like to write opaque models.)

You can see the fixed version of the app [here](https://ellie-app.com/6YqQVQSSDZ8a1).

However... now that we've put that state in the model, although the test still works, it's looking a bit silly. We've got some state in the tests that should always be identical to the state in the model; why not just test that the model is updating the state correctly?

So here are some other tests that we could write (but that I'm not going to, for time reasons):

* We could test that, given the same messages as above, the model doesn't become `isSaved` until the very end of `runUpdate`. We can still do that with `runUpdates`; our state parameter is now `List Model`, we use `mockUpdateE` to keep track of every intermediate model (and `mockRunEffect` no longer needs to deal with state at all), and then finally verify that `isSaved` is false for all but the last. (This test we could have written with the old model. As described it fails if, in future, `Saved` starts having other effects - maybe it wants to send something to a port. We can get around that by doing more bookkeeping, but we could also simply decide that `mockRunEffect` will pretend it doesn't have those effects.)

* We could test that any update which returns an `ESaveCount` also increases `inFlight`; and further, that any messages sent in response to `ESaveCount` will decrease `inFlight`. I think this test is most valuable if it uses a mocked `runEffect` that's also used in other tests.

Really though, I'm not sure what's best. I do think the Effect pattern will help.

### Further thoughts

We haven't used this much yet, so there's a lot left to explore. Here are some thoughts I've had, but not developed very far, in no particular order.

**Nomenclature.** We've gone from `update` to `update`, `updateE` and `runEffect`. I currently think `runEffect` is an okay name, but I feel like with no historical baggage, the name `update` would have gone to `updateE`. Then what would `update` be called? I left it as-is partly to avoid stepping on historical toes, and partly because I don't know. `runUpdate`? That would give us the pattern "`update` functions update the model and return some kind of what-next value, `run` functions produce `Cmd`s". (Of course, `runUpdates` violates that pattern. Maybe that should become `foldUpdate`...?)

Also, we'll want a helper function to convert `updateE` and `runEffect` into the correct form. What do we call that function? The only sensible suggestion I have is `liftUpdate`, but I'm not sure I like it.

**Randomness.** The test I've demonstrated was deterministic. So have all the tests I've written for `Effect` so far. (At least one used a fuzzed input, but that doesn't feel like it counts.) To get randomness I imagine you'd need to put a `Seed` in the state parameter of `runUpdates`, and then use [`Random.step`](https://package.elm-lang.org/packages/elm-lang/core/latest/Random#step) (maybe with [`Test.Runner.fuzz`](https://package.elm-lang.org/packages/elm-explorations/test/1.2.2/Test-Runner#fuzz) to get you the `Generator` that you need).

**Simpler test helpers.** `runUpdates` is quite complicated, and as mentioned, I suspect it'll need to be even more so. I think most tests probably won't use all of its features. What simpler variants of `runUpdates` are worth creating (and what should they be named)? An obvious candidate is a variant with no state. Maybe also a variant that returns a list of models instead of just the final model.

**Full state machine.** In Haskell we use [quickcheck-state-machine](https://github.com/advancedtelematic/quickcheck-state-machine#readme), which I really like. Could we do something similar in Elm? I think it would be possible, though probably looking quite different. Elm doesn't have all of the type-level features that QSM relies on, but it also doesn't have all of the features that QSM needs to support.

**Should `runEffect` see the model?** Reasons yes: it simplifies the `Effect` constructors; it reduces total amount of code; it allows one `stateless` function to work with both `updateE` and `runEffect`.[^avoid-old-data] Reasons no: it gives `runEffect` more rope to hang you with (more likely to be complicated, more likely to diverge in the codebase and test suite). We went with yes because in one of our components, many constructors would have needed many parameters. But we probably could have refactored a little so that many constructors would have needed only one parameter each.

[^avoid-old-data]: Update 13-Mar-2021: A coworker points out another reason yes. Often you need to update model state and send a command using the new state value - you can see this when I handle `IncBy` and `MultBy` in both versions of the app, repeating `model.count + n` and `model.count * n`. If `runEffect` sees the model, it automatically uses the new state value. Sometimes you do want to use the old value, and then you can keep passing it in the effect constructor. But now you're doing so deliberately and explicitly.

    This eliminates a subtle class of bugs where you accidentally pass in the old value, or some other incorrect value. In the first published version of this post, I had an `ESaveCount (model.count + n)` where I should have written `ESaveCount (model.count * n)`, but simply writing `ESaveCount model.count` would also have been easy, wrong, and hard to catch.

    I find this fairly compelling.

**Can you reuse mocked `runEffect` functions?** I touched on this above. That is, will you be able to write just one or two per component and use those in most of the tests for that component? (If not directly, then just wrapping them in some state-updating code that doesn't change the `Msg` they return.) Or will each test need a separate one? I certainly hope you can reuse them. If not, that might diminish a lot of the value. The fewer you have, the easier it is to keep them all correct when the real one changes.

(What if you have a potentially large number of functions, but selected by a configuration parameter? I think depending on how this is handled, it could be closer to either end of the scale.)

**Composability.** A component using this pattern can be embedded in one that doesn't, no problem. You just don't get any of the benefits in the parent.

What if you embed a non-Effect component in an Effect component? This forces you to put some `Cmd` in your `Effect` type. How do you test that? I'm not sure you reasonably can. So far I think we've just avoided testing those parts of our components.

What if you embed an Effect component in another Effect component? In the codebase, I imagine your parent's `Effect` type has a constructor `ChildEffect Child.Effect` which in turn calls `Child.runEffect`. That lets you test the parent component, but... you may need to mock `runEffect` for every child component, and that doesn't sound fun. (If the mocked functions do turn out to be fairly reusable, maybe not so bad.)

Also, if you want to provide an Effect component in a library, you may want the `Effect` type to be opaque (like `Model` and `Msg` often are today). But then if you want people to be able to test your component in theirs, maybe that makes you responsible for providing suitable mocked `runEffect` functions.

**Unconventional updates.** I've been assuming your existing `update` function has type `Msg -> Model -> (Model, Cmd Msg)`. But a lot don't. A common pattern is something like `Msg -> Model -> (Model, Cmd Msg, MsgToParent)` where `MsgToParent` is something that the parent may need to act on. (In our case, it's often just global state that needs to be sent back up in turn.) How do you handle this kind of thing?

In the codebase, I think the correct decomposition for this is still to change only the `Cmd Msg` return value, since that's the only opaque one, and for `runEffect` to be the same as it would be otherwise. (You could give it `MsgToParent` as an extra parameter, but like with `Model` that won't give you any extra power. By default I wouldn't do it, but I don't think it would be an obviously bad idea.) If you had two opaque return values... honestly I don't think I've seen this and I don't think I want to speculate about what to do in that situation.

In the test suite, you won't be able to use the existing `runUpdates` function. What to do instead? It might prove useful to have a `runUpdates3` (or something) which can handle this case, but I'm not sure exactly how that would work.

Another possibility would be using wrappers to put your `updateE` in the right shape. For example, maybe you can do `type EffectOrMsg = Effect Effect | MsgToParent MsgToParent`, and then combine the final two results of `updateE`. I don't know if that would always get you what you want.

### tl;dr

You can take your existing function `update : Msg -> Model -> (Model, Cmd Msg)`, and decompose it into two others:

* `updateE : Msg -> Model -> (Model, List Effect)`
* `runEffect : Effect -> Model -> Cmd Msg`

defining the new `Effect` type as whatever makes this decomposition work nicely. I think this is a slight improvement in the codebase; and independently of that, I think it helps you to write better tests.

### See also

Delayed update, 13-Mar-2021: A commenter on /r/elm [points out](https://www.reddit.com/r/elm/comments/dkou3c/the_effect_pattern_transparent_updates/f4kaavp/) that [elm-program-test](https://package.elm-lang.org/packages/avh4/elm-program-test/latest/) does something similar. It looks like you use it by rewriting your program in basically the same way I recommend here, and then it implements a bunch of test helpers you can use on top of that. If you're interested in this direction, I recommend checking it out.
