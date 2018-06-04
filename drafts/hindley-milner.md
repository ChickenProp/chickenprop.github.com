---
title: Hindley-Milner type inference
layout: draft
---
1.

When people write software, sometimes it doesn't do exactly what we want. One way to find out is to try running it and see, but that's not ideal because any complicated program will have way too many possible inputs to test. So it would be nice if we could mathematically prove whether our software does what we want, without actually running it. Can we do that?

That's not a very well-defined question, but we can ask more precise versions of it. Here's a well-known one: we might want to prove that our software will always terminate. No matter what input it sees, eventually it will always return a result. Can we prove whether our software does that?

That question is known as the halting problem[^halting], and the simple answer is no, we can't. But the full answer is more complicated.

[^halting]: Technically the halting problem only requires you to answer for a specific input, but it's close enough enough for these purposes.

To solve the halting problem, we want a program that, when given another program as input, satisfies three different conditions:

1. It will always return an answer.
2. The answer will always be either "yes, this always terminates" or "no, sometimes this doesn't terminate".
3. The answer is always correct.

And that's not possible. But we can compromise on any of the three. We can make a program that sometimes doesn't return an answer, or one that sometimes gets the answer wrong. But most interestingly, we can make a program that sometimes says "I don't know".

And when you allow that answer, you can create a *language* on which the halting problem is tractable. You can write a program that will tell you truthfully whether any program written *in that language* will terminate; and for any other program, will say "I don't know". (Perhaps expressed in words like "syntax error on line 1".)

Now, the halting problem is tricky. It turns out that if you create a language like that, there are a lot of interesting things that programs written in that language just won't be able to do. But there are also lots of interesting things that they can do. To give three examples of such languages:

* Regular expressions are really useful for certain operations on strings, but that's about all they're good for.
* SQL is really useful for working with databases. According to someone on stack overflow, the ANSI SQL-92 standard was Turing-incomplete and the ANSI SQL-99 standard is Turing complete. (No word on the SQL-96 standard that came between these.) But I've never actually needed the feature that makes it Turing-complete; so at least for my purposes, it might as well not be.
* Coq is used for proving math theorems. It's an interesting one because when you write your program, you have to also provide a proof that your program terminates.

I'm trying to illustrate here something important, which is that there's a tradeoff between what I'll call expressiveness and legibility. A programming language is *expressive* if you can easily write many interesting programs in it; it's *legible* if you can easily say many interesting things about the programs you've written in it. And I claim that the most expressive programming languages won't be the most legible, and vice-versa; though there will certainly be languages which are neither expressive nor legible. This tradeoff seems fundamental to me, and I expect that some approximation of it has been proven as a theorem.

I haven't defined these very well, but hopefully the kinds of things that I mean will become clear. I will clarify that both of them are highly dimensional; and that "raw computational power" is one of the things that expressiveness can point at, and "human readability" is one of the things that legibility can point at, but neither of those are synonyms.

2.

So we've got this tradeoff, and in our programming language design we try to navigate it. We try to find kinds of legibility that can be bought for little cost in expressiveness. Or more precisely, we try to find kinds of legibility *that we care about*, and that can be bought for little cost in *kinds of expressiveness that we care about*.

And Hindley-Milner type systems are a tradeoff that's proved fairly successful, both in direct use and as inspiration. At my company[^my-company], we use Elm, which runs on a HM type system. (Elm might need minor extensions to HM, to deal with extensible record types; I'm not sure. With that one possible extension, I think all of Elm's types can be expressed in an HM system.) We also use Haskell, which runs on a type system that extends HM in many directions. Haskell's system is more expressive and less legible, but still successful. (I'll mostly be using Elm for examples in this post, and not extensible records.)

[^my-company]: "My company" is a phrase which sometimes means "the company I own or run" and sometimes "the company I work for". Here it means the latter. I don't know an unambigous way to phrase that which I don't find slightly awkward, so instead I'm using a super-awkward footnote. But, y'know. Ironically, or something.

The legibility HM offers is, roughly, the ability to prove that a program typechecks. What exactly that means I'll get to later, but we probably all have a decent idea. It's the thing that lets the Elm compiler say "no, that program is trying to add a string to an int, bad program", while the python interpreter doesn't know that's going to happen until it's too late. The Elm compiler will refuse to compile your program unless it can logically prove that it will typecheck.

More precisely, what HM offers isn't type *checking* but the more general type *inference*. (And beyond that, type inference *in roughly linear time*.) Type inference doesn't just tell you *whether* a program typechecks, but *what* its type is; a program fails to typecheck iff no type can be inferred for it.

What this means is that there's no need to supply type annotations. And indeed, in Elm you can get away without them, except I think for extensible records[^extensible-records]. In Haskell you sometimes can't, because Haskell loses some of the legibility that HM offers.

We typically do supply type annotations, but that's because they're useful. Partly as documentation for humans, partly to help pinpoint errors in typechecking.

And so in an HM system you get no runtime type errors. Elm goes further, and tries to promise no runtime errors, period. One one level, I think that's something you get "for free" once you have typechecking, by deciding that none of the built-in functions you provide will ever throw a runtime error. On another level, it seems completely impractical to decide that `cons` will return a meaningful value if it can't allocate more memory. I'm not aware that Elm even tries to handle those errors.

Haskell doesn't try to promise the ssame thing, and allows functions to return `undefined`. This is another legibility-expressiveness tradeoff.

[^extensible-records]: There's some tension here. I said above that I'm not sure whether extensible records need an extension to HM, but now I'm saying that they need type annotations. My answer is that I suspect a compiler could turn extensible records into something that pure HM would support, but that type annotations would be needed to tell the compiler to do that. Again, I'm unsure.

    Also, even if it's *possible*, I suspect that's not how elm actually does it.

So the legibility gain is: type inference, no runtime type errors, optionally no runtime errors at all. It's good.

Meanwhile, the expressiveness cost is that you need to write your programs in ways that the type inference algorithms can work with, which forbids some things that you might like to do.

For example, suppose you want to clamp a number to between -1 and +1. In haskell, you could write that like

```haskell
clamp x = sort [-1, x, 1] !! 1
```

and as long as `sort` always returns a list of the same length it started with, that works fine. But it only works because the Haskell compiler allows the `!!` operator to crash if it goes out of range. For comparison, the Elm compiler attempts to offer "no runtime errors", and so Elm has no equavalent operator. If you tried to write the same function in the same way in Elm, the result in the compiler's eyes would not be a number but a `Maybe` number - AKA "either a number or `Nothing`". (`Nothing` is roughly equivalent to `None` in python or `null` in many other languages.) When you actually run the program, you will always get a number and never `Nothing`. But the compiler can't prove that.

(Again, I stress that you will never get `Nothing` *as long as* `sort` always returns a list of the same length it started with. That's something you can prove for yourself, but it's not something the compiler can prove. It's not even the sort of thing the compiler knows can be proven.)

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

but impossible in Elm[^het-list]. You can *sort of* get the same effect by creating a type with many constructors

```elm
type HeteroType = HTInt Int
                | HTString String
                | HTBool Bool
                | HTList (List HeteroType)
                | ...
```

but it's not quite the same, because it can only accept types you know about in advance. Also, it's a massive pain to work with[^htfunc].

[^htfunc]: Also, suppose you want to include functions. You can add the constructor `HTFunc (HeteroType -> HeteroType)`, but it's not clear how to turn a function `Int -> String` into an "equivalent" function `HeteroType -> HeteroType` - the `String` can be wrapped in `HTString`, but the `Int` can't be safely unwrapped. So you need `HTFuncInt (Int -> HeteroType)`, `HTFuncString (String -> HeteroType)` and so on. The number of constructors needed grows at least as O(n²).

For a third example: Haskell is known for its monads. But Elm has no equivalent, because an HM type system can't support generic monad programming. You can implement the generic monad functions for specific caes, so there's `Maybe.map` and `List.map`, but there's no equivalent of Haskell's `fmap` which works on all monads.

3.

So I've talked about the tradeoffs that HM type systems offer, but not what HM type systems actually are. So here is where I get reckless.

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

And type specialisation, denoted $⊑$, is the process of replacing quantified variables with specific ones. So for example the type `∀a b. a -> b -> a` can be specialized to $∀b. Int -> b -> Int` and then to `Int -> String -> Int`.

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

This introduces the syntax $\bar{μ}$, which generalises a monotype to a polytype. How it works is: if $μ$ mentions a type variable $a$, and $a$ isn't quantified over in the surrounding context, then $\bar{μ}$ contains a "$∀a$".

Thus: we can infer `(\x -> x) ~ a -> List a`, where `a` is a type variable unused in the surrounding context. That type generalises to `∀a. a -> List a`. And given the declaration `f : ∀a. a -> List a`, we can infer `(f "", f True) ~ (List String, List Bool)`. So in total, we can infer `let f x = [x] in (f "", f True) ~ (List String, List Bool)`.

(It seems a little strange to me that the approach here is to first construct a meaningless type, and then quantify over it. Still, that's my understanding. It's of course possible I'm mistaken.)

Why do we need both `let` and lambda? Well, we can't replace lambda expressions with let expressions: they're not re-usable. (When you translate a let expression into a lambda expression, you actually generate a lambda *applied to an argument*. There's no way to translate a lambda expression by itself into a let expression.) Meanwhile, I'm not entirely sure why we can't make lambdas polymorphic in the same way let expressions are. I assume the answer is that if we tried it, we'd lose some of the legibility that HM offers, but I'm not sure exactly what. Let can be more powerful in the type system because it's less powerful in the language.
