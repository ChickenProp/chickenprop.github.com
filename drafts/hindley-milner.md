---
title: A reckless introduction to Hindley-Milner type inference
layout: draft
---
A few weeks ago I gave a talk at work about Hindley-Milner type inference. When I agreed to give the talk I didn't know much about the subject, so I learned about it. And now I'm writing about it, based on the contents of my talk but more fleshed out and hopefully better explained.

I call this a reckless introduction, because my main source is [wikipedia](https://en.wikipedia.org/wiki/Hindley%E2%80%93Milner_type_system). A bunch of people on the internet have collectively attempted to synthesise a technical subject. I've read their synthesis, and now I'm trying to re-synthesise it, without particularly putting in the effort to check my own understanding. I'm not going to argue that this is a good idea. Let's just roll with it.

I'm also trying to tie in some quasi-philosophy that surely isn't original to me but I don't know where or if I've encountered it before.

1.

When people write software, sometimes it doesn't do exactly what we want. One way to find out is to try running it and see, but that's not ideal because any complicated program will have way too many possible inputs to test. So it would be nice if we could mathematically prove whether our software does what we want, without actually running it. Can we do that?

That's not a very well-defined question, but we can ask more precise versions of it. Here's a well-known one: we might want to prove that our software will always terminate. No matter what input it sees, eventually it will always return a result. Can we prove whether our software does that?

That question is known as the halting problem[^halting], and the simple answer is no, we can't. But the full answer is more complicated.

[^halting]: Technically the halting problem only requires you to answer for a specific input, but my version is equivalent. If you can solve either one, you can solve the other.

To solve the halting problem, we want a program that, when given another program as input, satisfies three different conditions:

1. It will always return an answer.
2. The answer will always be either "yes, this always terminates" or "no, sometimes this doesn't terminate".
3. The answer is always correct.

And that's not possible. But we can compromise on any of the three. We can make a program that sometimes doesn't return an answer, or one that sometimes gets the answer wrong. But most interestingly, we can make a program that sometimes says "I don't know".

And when you allow that answer, you can create a *language* on which the halting problem is tractable. You can write a program that will tell you truthfully whether any program written *in that language* will terminate; and for any other program, will say "I don't know". (Perhaps expressed in words like "syntax error on line 1".)

Now, the halting problem is tricky. It turns out that if you create a language like that, there are a lot of interesting things that programs written in that language just won't be able to do. But there are also lots of interesting things that they can do. To give three examples of such languages[^nonterminating]:

[^nonterminating]: To nitpick myself: these aren't just languages for which you can prove termination, they're languages which never terminate, at least not for finite inputs. I don't offhand know any languages which are Turing-incomplete but have the ability to loop forever, though such a thing can exist.

* Regular expressions are really useful for certain operations on strings, but that's about all they're good for.
* SQL is really useful for working with databases. According to someone on stack overflow, the ANSI SQL-92 standard was Turing-incomplete and the ANSI SQL-99 standard is Turing complete. (No word on the SQL-96 standard that came between these.) But I've never actually needed the feature that makes it Turing-complete; so at least for my purposes, it might as well not be.
* Coq is used for proving math theorems. It's an interesting one because when you write your program, you have to also provide a proof that your program terminates. (I think this is slightly false, but again, good enough for the point I'm making.)

So although these languages can't do much, they can still do enough to be useful. And in the domains where they're useful, being able to prove non-termination is a useful property of the language. If you had to write a SQL query in C, it would be all too easy to write some C code that would accidentally loop forever.

I'm trying to illustrate here something that seems to me important, which is that there's a tradeoff between what I'll call expressiveness and legibility. A programming language is *expressive* if you can easily write many interesting programs in it[^expressive]; it's *legible* if you can easily say many interesting things about the programs you've written in it. And I claim that the most expressive programming languages won't be the most legible, and vice-versa; though there will certainly be [languages](https://en.wikipedia.org/wiki/Malbolge) which are neither expressive nor legible. This tradeoff seems fundamental to me, and I expect that some approximation of it has been proven as a theorem.[^zfpa]:

[^expressive]: I've subsequently discovered that wikipedia uses [the same name](https://en.wikipedia.org/wiki/Expressive_power_\(computer_science\)) for this concept.

[^zfpa]: I think this is related to the way that ZF set theory can encode Peano arithmetic. Thus, ZF is more expressive than PA. But because ZF allows you to construct objects that PA doesn't, there are more things you can say about "all objects in PA" than about "all objects in ZF". So PA is more legible than ZF.

I haven't defined these very well, but hopefully some examples will help. I will also clarify that both of them are highly dimensional; and that "raw computational power" is one of the things that expressiveness can point at, but not the only thing; and "human readability" is not really one of the things that legibility points at.

* [Perl-compatible regular expressions](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) can classify sets of strings that normal regular expressions can't. But they're harder to make time and space guarantees about. And it's possible to prove whether two regular expressions are equivalent, but that's not possible in general for PCREs (proof: [PCREs can encode CFGs](https://nikic.github.io/2012/06/15/The-true-power-of-regular-expressions.html); [CFGs can't be proved equivalent](https://math.stackexchange.com/questions/231187/an-efficient-way-to-determine-if-two-context-free-grammars-are-equivalent)).

* Under certain assumptions, Haskell's monadic IO lets you look at the type of a piece of code and know that it won't depend on external state. In return, a function can only bring in external state if its caller allows it to (which requires having permission from its own caller, and so on).

  The assumptions in question are false (partly because `unsafePerformIO` exists), but I've been able to get away with pretending they're true (partly because `unsafePerformIO` is punishable with excommunication).

* Custom operators don't gain or cost much in terms of legibility and expressivity, since they're equivalent to function calls. They simply make code more or less readable. But operator overloading, at least when combined with dynamic typing, gains expressivity at the cost of legibility (you no longer know that `a + b` will do anything remotely like an addition).

* Macros make it easier to do things like create DSLs, reduce boilerplate, and set compile-time config options. But they mean that a function call might not look like one, or vice-versa; expressions might get evaluated many times, or not at all; and the code might perform differently depending on the phase of the moon when it was compiled.


2.

So we've got this tradeoff, and in our programming language design we try to navigate it. We try to find kinds of legibility that can be bought for little cost in expressiveness. Or more precisely, we try to find kinds of legibility *that we care about*, and that can be bought for little cost in *kinds of expressiveness that we care about*.

And Hindley-Milner type systems are a tradeoff that's proved fairly successful, both in direct use and as inspiration. At my company[^my-company], we use Elm, which runs on an approximately HM type system. (I don't think it's pure HM, due to extensible record types.) We also use Haskell, which runs on a type system that extends HM in many directions. Haskell's system is more expressive and less legible, but still successful. (I'll mostly be using Elm for examples in this post, and not extensible records.) ML and OCaml are other notable languages based on HM, though I haven't used either.

[^my-company]: "My company" is a phrase which sometimes means "the company I own or run" and sometimes "the company I work for". Here it means [the latter](https://proda.ai). I don't know an unambigous way to phrase that which I don't find slightly awkward, so instead I'm using a super-awkward footnote. But, y'know. Ironically, or something.

The legibility HM offers is, roughly, the ability to prove that a program typechecks. What exactly that means I'll get to later, but we probably all have a decent idea. It's the thing that lets the Elm compiler say "no, that program is trying to add a string to an int, bad program", while the python interpreter doesn't know that's going to happen until it's too late. The Elm compiler will refuse to compile your program unless it can logically prove that it will typecheck.

More precisely, what HM offers isn't type *checking* but the more general type *inference*. (And beyond that, type inference *in roughly linear time*.) Type inference doesn't just tell you *whether* a program typechecks, but *what* its type is; a program fails to typecheck iff no type can be inferred for it.

What this means is that there's no need to supply type annotations. And indeed, in Elm you can get away without them, except I think for extensible records. In Haskell you sometimes can't, because Haskell loses some of the legibility that HM offers.

(We typically do supply type annotations, but that's because they're useful. Partly as documentation for humans, partly to help pinpoint errors in typechecking.)

And so in an HM system you get no runtime type errors. And although not all runtime errors are type errors, in many cases they could be. For example, an array out-of-bounds exception isn't a type error. But when designing a language, you can decide that array out-of-bounds exceptions won't exist, any array lookup will return either a value from the array or `null`. If type errors are possible, you've just eliminated one source of errors by pushing them somewhere else, and possibly somewhere harder to debug. But in HM, you've eliminated one source of errors by pushing them somewhere more visible, where they can be ruthlessly executed.

Elm actually tries to promise no runtime errors, period, provided you stay inside Elm. On one level, I think that's a fairly minor imposition on language design, something you get "for free" by deciding that none of the built-in functions you provide will ever throw a runtime error. On another level, it seems completely impractical to decide for example that `cons` will return a meaningful value if it can't allocate more memory. I'm not aware that Elm even tries to handle those errors.

(Haskell doesn't try to promise the same thing, and allows functions to return `undefined`. This is another legibility-expressiveness tradeoff.)

So HM's legibility gain is: type inference, powerful type system, no runtime type errors, optionally no runtime errors at all. It's good.

Meanwhile, the expressiveness cost is that you need to write your programs in ways that the type inference algorithms can work with, which forbids some things that you might like to do.

For example, suppose you want to clamp a number to between -1 and +1. In Python, you could write that like

```python
def clamp(x): sorted([-1, x, 1])[1]
```

and as long as `sorted` always returns a list of the same length it started with, that works fine. But it only works because the Python interpreter allows array indexing to crash if it goes out of range. For comparison, the Elm compiler attempts to offer "no runtime errors", and so Elm has no equavalent operator. If you tried to write the same function in the same way in Elm, the result in the compiler's eyes would not be a number but a `Maybe` number - AKA "either a number or `Nothing`". (`Nothing` is roughly equivalent to `None` in python or `null` in many other languages, but you have to explicitly flag when it's allowed.) When you actually run the program, you will always get a number and never `Nothing`. But the compiler can't prove that.

(Again, I stress that you will never get `Nothing` *as long as* your sort function always returns a list of the same length it started with. That's something you can prove for yourself, but it's not something the compiler can prove. It's not even the sort of thing the compiler knows can be proven.)

And then the Elm compiler would force you to account for the possibility of `Nothing`, even though there's no way that possibility could occur at runtime. One option is to pick an arbitrary result that will never be exposed - until the code goes through several layers of changes, an assumption that used to be true is now violated, and suddenly that arbitrary result is wreaking havoc elsewhere. Or in Haskell, your program is crashing at runtime.

...or you can rewrite your function to avoid indexing into a list. The point isn't that you can't do the thing. The point is that (a) even if the thing is safe, the compiler might not know that, and (b) if you decide it's safe anyway and find some way to work around the compiler, you're in dangerous territory.

For another example, HM type systems can't implement heterogenous lists. So this is really easy in python:

```python
def stringify_list(l):
    return [ repr(x) for x in l ]

stringify_list(["hello",
                0,
                ["here's a", "nested list", {"and": "maybe", "a": "dict"}],
                "it can even be passed itself, like so:",
                stringify_list])
```

but impossible in Elm. You can *sort of* get the same effect by creating a type with many constructors

```elm
type HeteroType = HTInt Int
                | HTString String
                | HTBool Bool
                | HTList (List HeteroType)
                | ...
```

but it's not quite the same, because it can only accept types you know about in advance. Also, it's a massive pain to work with.

For a third example: Haskell is known for its monads. But Elm has no equivalent, because an HM type system can't support generic monad programming. You can implement the generic monad functions for specific cases, so there's `Maybe.map` and `List.map`, but there's no equivalent of Haskell's `fmap` which works on all monads.

3.

So I've talked about the tradeoffs that HM type systems offer, but not what HM type systems actually are. So here is where I get particularly reckless. Also, this part is likely to make more sense if you're familiar with at least on HM-based language.

You need types, you need a language, and you need a way to relate the two.

3.1.

**Types** come in a conceptual hierarchy which starts with type constants. That's things like, in Elm, `Int`, `Float`, `Bool`, `String`, `Date`, `()`. It also includes type variables, which in Elm are notated with initial lower-case, like `a` and `msg`. (Though the type variables `number`, `comparable` and `appendable` are special cases that I won't cover here.)

Next in the type hierarchy is applied types like `List Int`, `Maybe (List Float)`, `a -> String` and `Result () Date`. (`->` is the only type that HM specifically requires.) Notably, an applied type *must* have a specific named "root"; you can't have `m Int`, which you would need for generalised monads. The "leaves" in an applied type can be any type constants or applied types.

Type constants and applied types are *monotypes*. You get a *polytype* by optionally sticking one or more "∀"s in front of a monotype. So for example `a -> Int` is a monotype, but `∀a. a -> Int` is a polytype. `∀b. a -> Int` is also a polytype, and so is `∀a. ∀b. Int` (which I'll write equivalently as `∀a b. Int`). As a degenerate case, all monotypes also count as polytypes.

Type signatures in Elm typically have an implied "∀" over whichever variables it makes sense to quantify. So the type of `List.map` would be written

```elm
map : (a -> b) -> List a -> List b
```

but I'll be writing

```elm
map : ∀a b. (a -> b) -> List a -> List b
```

for clarity. Because there's one place where Elm *doesn't* give an implied ∀, which is when you have scoped types. To demonstrate by example,

```elm
const : ∀a b. a -> b -> a
const x = let foo : b -> a
              foo y = x
           in foo
```

`const` has a polytype here, but `foo` has a monotype, because (in context) its argument type and return type are constrained. If you tried to swap `a` and `b` in the type signature for `foo`, or rename either of them, the Elm compiler would complain.

3.2.

The **language** has four kinds of expression, and each has a rule relating it to the type system. You need variables and constants, function calls, lambda expressions, and let statements.

3.2.1.

Variables and constants are things like `True`, `0.2`, `Just`, `"Hello"`, `[]`, `()`, `List.map`. Each of these has a declared type, which in Elm is notated with `:`. So `True : Bool`, `0.2 : Float`, `Just : ∀a. a -> Maybe a`, `"Hello": String`, `[] : ∀a. List a`, `() : ()`, `List.map : ∀a b. (a -> b) -> List a -> List b`.

The rule that relates these to the type system is that *type declarations imply type judgments*. Mathematically it looks like

    $$ \frac{x : π \quad π ⊑ μ}{x \sim μ}. $$

Reading clockwise from top left, this says: if you have a variable $x$ declared to have some polytype $π$, and if the monotype $μ$ is a specialisation of $π$, then $x$ can be judged to have type $μ$. ($π$ always denotes a polytype, and $μ$ always denotes a monotype.)

A type *judgment*, as opposed to a declaration, provides a type that an expression can be used as. A judgment is always as a monotype.

And type specialisation, denoted $⊑$, is the process of replacing quantified variables with less-quantified ones. So for example the type `∀a b. a -> b -> a` might be specialized to `∀a. a -> String -> a`, or to `∀b. Int -> b -> Int`; and from either of those, it could be further specialised to `Int -> String -> Int`. Of course `String -> Int -> String` and `List Float -> (Float -> String) -> List String` are valid specialisations too.

Thus: we have the type declaration `[] : ∀a. List a`, and we have `∀a. List a ⊑ List Int`, and so we can form the type judgment `[] ~ List Int`. We also have `∀a. List a ⊑ List String`, and so `[] ~ List String`. And `[] ~ List (List (Maybe Bool))`, and so on.

3.2.2.

Function calls are things like `not True`, `(+ 1)`, `List.Map Just`. And the rule relating them to the type system is that *function calls consume function types*. This is the simplest of the rules. Mathematically it looks like

    $$ \frac{f \sim μ → μ' \quad v \sim μ}{f v \sim μ'}. $$

Or: if $f$ can be judged to have a function type $μ → μ'$, and $v$ can be judged to have type $μ$, then the function call $fv$ can be judged to have type $μ'$.

Thus: we can infer the type judgment `toString ~ Int -> String`, and we can infer `3 ~ Int`, and so we can infer `toString 3 ~ String`.

And we can infer `List.map ~ (Int -> Maybe Int) -> (List Int -> List (Maybe Int))`, and we can infer `Just ~ Int -> Maybe Int`. So we can infer `List.map Just ~ List Int -> List (Maybe Int)`

3.2.3.

Lambda expressions are things like `\x -> Just x`, and in Elm they're used implicitly when something like `const x y = x` is turned into `const = \x -> \y -> x`. The type system rule is that *lambda expressions produce function types*. Mathematically:

    $$ \frac{x : μ ⇒ e \sim μ'}{λx.e \sim μ → μ'}. $$

Or: suppose that the type declaration $x : μ$ would allow us to infer the judgment $e \sim μ'$. In that case, we could judge that $λx.e \sim μ → μ'$.

Typically $e$ would be some expression mentioning the variable $x$, but it's no problem if not. In that case, if you can get $e \sim μ'$ at all, you can get it assuming any $x : μ$, and so you have $λx.e \sim Int → μ'$ and $λx.e \sim String → μ'$ and $λx.e \sim Result String (List (Maybe Float)) → μ'$ and so on.

Thus: given the declaration `x : Int`, we can infer the judgment `[x] ~ List Int`. And so we can infer the judgment `(\x -> [x]) ~ Int -> List Int`.

3.2.4.

Let expressions read like `let x = y in a`. Semantically, this is very similar to using a lambda expression, `(\x -> a) y`. But HM treats them differently in the type system, allowing a let expression to introduce polytypes. That permits code like

```elm
let f x = [x]
in (f "", f True)
-- returns ([""], [True])
```

If you tried to rewrite this as a lambda, you would get

```elm
(\f -> (f "", f True))(\x -> [x])
```

But type inference fails here, because there's no monotype declaration for `f` that allows a type judgment for `(f "", f True)`. So the precondition for the lambda rule never obtains, and so in turn, no type judgment can be made for the expression `\f -> (f "", f True)`.

Let expressions compensate for this deficiency, with the rule *let expressions are like polymorphic lambda applications*. Mathematically:

    $$ \frac{a \sim μ \quad x : \bar{μ} ⇒ b \sim μ'}
            {(\mathtt{let}\ x = a\ \mathtt{in}\ b) \sim μ'} $$

Or: suppose that $a$ can be judged to have type $μ$, and that the declaration $x : \bar{μ}$ would allow us to infer the judgment $b \sim μ'$. In that case, we could judge that $(\mathtt{let}\ x = a\ \mathtt{in}\ b)$ has type $μ'$.

This introduces $\bar{μ}$, which generalises a monotype to a polytype. How it works is: if $μ$ mentions a type variable $a$, and $a$ isn't quantified over in the surrounding context, then $\bar{μ}$ contains a "$∀a$".

Thus: we can infer `(\x -> x) ~ a -> List a`, where `a` is a type variable unused in the surrounding context. That type generalises to `∀a. a -> List a`. And given the declaration `f : ∀a. a -> List a`, we can infer `(f "", f True) ~ (List String, List Bool)`. So in total, we can infer `let f x = [x] in (f "", f True) ~ (List String, List Bool)`.

(It seems a little strange to me that the approach here is to first construct a meaningless type, and then quantify over it. Still, that's my understanding. It's of course possible I'm mistaken.)

Why do we need both `let` and lambda? Well, we can't replace lambda expressions with let expressions: they're not re-usable. (When you translate a let expression into a lambda expression, you actually generate a lambda *applied to an argument*. There's no way to translate a lambda expression by itself into a let expression.) Meanwhile, I'm not entirely sure why we can't make lambdas polymorphic in the same way let expressions are. I assume the answer is that if we tried it, we'd lose some of the legibility that HM offers, but I'm not sure exactly what. Let can be more powerful in the type system because it's less powerful in the language.

3.3.

There's an interesting thing about the system I just described: it may or may not be Turing complete.

The problem is that there's no specified way of doing recursion. A function can't call itself, and it can't call any other function that can call it.

But a [fixed-point combinator](https://en.wikipedia.org/wiki/Fixed-point_combinator) allows recursion, and might be included in the initial set of variables. Failing that, the proper recursive types can be used to define one. (Elm and Haskell [allow us](http://rosettacode.org/wiki/Y_combinator) to define such types[^brag].)

[^brag]: Minor brag: I myself contributed the Elm implementation on that page.

Failing both of those, we can introduce a new kind of expression

    $$ \frac{x : μ ⇒ a \sim μ \quad x : \bar{μ} ⇒ b \sim μ'}
            {(\mathtt{letrec}\ x = a\ \mathtt{in}\ b) \sim μ'}. $$

This is much the same as `let`, but makes the variable `x = a` available when evaluating `a`. It's only available as a monotype when evaluating `a`, and still doesn't get generalised to a polytype until evaluating `b`.

(Elm and Haskell provide `letrec` as `let` and don't provide simple `let` at all.)

But if an HM language doesn't provide the appropriate variables or types, and doesn't implement `letrec` or something similar, it won't be Turing complete. Legibility gain, expressivity cost.

4.

And modulo some small details, that's the entirety of a Hindley-Milner type system. If you have a language with those features, and a suitable set of types, you can perform type inference.

What we have is a set of rules that allows us to construct proofs. That is, if we look at a program written in this language, we would be able to construct a proof of its type (or lack thereof). But I already said HM is better than that: it lets us *mechanically* construct a proof, in (roughly) linear time.

I confess, I'm not entirely sure how to do that. The outline is obvious, recurse down the parse tree and at each step apply the appropriate rule. But since a constant can be judged as one of many types, you need to keep track of which types are acceptable. Wikipedia hints at how it works, but not in a way that I understand particularly well.

(Here I just start to infer things for myself.)

Elm and Haskell both support many things not covered so far. To look at some of them briefly,

* It seems obvious, but both allow you to evaluate the language, something I haven't touched on much. Their evaluation models are different though - Haskell is lazy, Elm is eager.

* Both have ways to introduce new types. That doesn't change what we've seen, but it does separate the languages into two parts. One part describes the types used in a program and one part implements the semantics of a program.

* Both also support case statements along with destructuring, like

  ```elm
  mHead : Maybe (List a) -> Result Bool a
  mHead ml = case ml of
      Just (a::_) -> Ok a
      Just _ ->     Err True
      Nothing ->    Err False
  ```

  To implement these, you'd want to add a fifth class of language expression. But I think it would be possible in theory to write a "thin" first-pass compiler to translate these statements into the existing language. By "thin" I mean to do this in such a way that we don't lose any of the legibility guarantees we care about.[^case-compiled] (For example, if this compiler turned $n$ bytes of code in a case statement into more than $O(n)$ bytes of code in the base language, or if it ran in more than O(n) time, this condition would fail.)

  If I'm right about that, then case statements neither make the language more expressive nor less legible, at least in one important sense. (But not the only important sense. They do make the language easier to read and write for humans.)

[^case-compiled]: I think it might look something like this:

    ```elm
    mHead ml =
        if *isJust ml && (*fromJust ml (\_x -> *isCons _x)) then
            *fromJust ml (\_x -> *fromCons _x (\a _ -> Ok a))
        else if *isJust ml then
            *fromJust ml (\_ -> Err True)
        else if *isNothing ml then
            Err False
        else
            *fail
    ```

    functions marked with a `*` can be hidden from the language user. Additionally, `*fromJust`, `*fromCons` and `*fail` would be able to throw runtime errors. These don't violate Elm's "no runtime errors" policy, because the compiler would only generate them in contexts where it could prove they wouldn't throw. (In the case of `*fail`, when it could prove that code branch was unreachable, so it could also just not bother.)

    I'm very much spitballing here. I wouldn't be surprised to discover that the approach I've described is completely unworkable.

* (By comparison, if-then-else statements are also another class of language expression, but one which can obviously be thinly compiled down to the existing ones.)

* In the type system, Elm supports record types, which are a lot like tuples but with nicer syntax. I believe these too could be thinly compiled down. But it also supports *extensible* records, which are more complicated. On one level you can think of a type like `{a | x : Int, y : Int}` like a tuple `∀a. (a, Int, Int)`. But then this tuple needs to be unpacked and manipulated when you pass it into a function expecting an `{a | x : Int}`.

  I suspect this is unresolvable, and extensible records represent an extension of Elm from HM, to become more expressive and less legible.

* Haskell supports typeclasses, which are a way of allowing functions to operate on multiple different types. (For example, the `show` function can be applied to a `String`, an `Int`, a `()`, a `[Float]`, ....) Elm doesn't, but simple typeclasses can be emulated with only a little added verbosity.

Another thing I'll say is that I've been talking about legibility and expressivity of a language. But a type system is itself a language, and may be more or less legible and expressive. I don't have a strong intuition for how these interact.

There's a lot more I could add to this post. Some things that I omitted for brevity, some that I omitted because I don't know enough about them yet[^enough], and some that I omitted because I don't know about them at all. I don't know what a sensible cutoff point is, so I'm just going to end it here.

[^enough]: Not that that stopped me from writing this entire post.

From writing my original talk, and subsequently this blog post, I think I understand HM type systems much better than I used to. Hopefully you think the same. Hopefully we're both correct. If you see any inaccuracies, please point them out.
