---
title: Variadic functions in Hindley Milner
layout: draft
---
I [previously mentioned](http://reasonableapproximation.net/2021/03/14/haskenthetical-update-macros.html) an interest in adding variadic functions to Haskenthetical, the "Haskell with a Lisp syntax" I'm vaguely working on.

It sounds difficult. This is an attempt to figure out just how difficult, partly by looking at the state of the art.

A variadic function is one which can accept argument lists of different length. A well-known example in many languages is [printf](https://en.wikipedia.org/wiki/Printf_format_string#Programming_languages_with_printf). Here are a bunch of functions I might want to be variadic in Haskenthetical, along with examples in Haskell of types I might want to use them as:

* `+`, accepting any number ≥ 2 of numbers and returning a number of the same type.

    ```haskell
    (+) :: Num a => a -> a -> a
    (+) :: Num a => a -> a -> a -> a
    ```

* Similarly, `-`, `*` and `/`. `-` and maybe `/` could reasonably accept ≥ 1 input, but that would be inconsistent and disallow `(- 3)` as a partial application. `-` and `/` would be left associative, i.e. `(- 5 1 2)` would be `(- (- 5 1) 2)`.

* `list`, accepting any number of arguments of the same type and returning a `List` of that type. (An empty `(list)` would have type `List $a`, the same as `Nil`.) There's a related function that I'll call `list'` for now, where the final argument has to be a `List` and the other arguments are prepended to it.

    ```haskell
    list :: [a]
    list :: a -> [a]
    list :: a -> a -> [a]

    list' :: [a] -> [a]
    list' :: a -> [a] -> [a]
    list' :: a -> a -> [a] -> [a]
    ```

* I already mentioned `printf`. Haskell's implementation is in the [Text.Printf module](https://hackage.haskell.org/package/base-4.15.0.0/docs/Text-Printf.html):

    ```haskell
    printf :: String -> IO ()
    printf :: PrintfArg a => String -> a -> IO ()
    printf :: (PrintfArg a, PrintfArg b) => String -> a -> b -> IO ()
    -- Also: all of the above, with `-> String` instead of `-> IO ()`. But
    -- that's not super relevant here.
    ```

* `»` and `«`, which take a function and then ≥ 2 arguments to interleave it with. Currently implemented as macros, and maybe I'd want them to be macros even if they could be functions, but . Often all or all-but-one of the arguments will be of the same type, such as you could use with Haskell's `foldr` and `foldl`. But they don't have to be. You could have `(» , 1 "foo" 3 "bar")` which would return `(, 1 (, "foo" (, 3 "bar")))`, the return type changing for every new argument you add.

    ```haskell
    -- e.g. in (») (+) 1 2 3
    (») :: Num a => (a -> a -> a) -> a -> a -> a -> a

    -- e.g. in (») (:) 1 2 []
    (») :: (a -> [a] -> [a]) -> a -> a -> [a] -> [a]

    -- e.g. in (») (,) 1 "foo" 3 "bar"
    (») :: (forall a b . a -> b -> (a, b))
        -> a -> b -> c -> d -> (a, (b, (c, d)))
    ```

* `sort` might have one or two optional arguments - one for a comparison function and/or one for a a key function. (A key function is unnecessary if you have a comparison, but it might be convenient.)

    ```haskell
    sort :: Ord a => [a] -> [a]
    sort :: (a -> a -> Ordering) -> [a] -> [a]
    sort :: Ord b => (a -> b) -> [a] -> [a]
    sort :: (a -> b) -> (b -> b -> Ordering) -> [a] -> [a]
    ```

* Similarly, lots of functions could take an optional config argument.

    ```haskell
    renderCsv :: [[String]] -> String
    renderCsv :: RenderCsvOpts -> [[String]] -> String
    ```

* `map` could take arbitrarily many lists. Haskell has separate functions for these, named `map`, `zipWith` and `zipWith3`.

    ```haskell
    map :: (a -> b) -> [a] -> [b]
    map :: (a -> b -> c) -> [a] -> [b] -> [c]
    map :: (a -> b -> c -> d) -> [a] -> [b] -> [c] -> [d]
    ```

* Similarly for `unzip`. This isn't variadic, but it's plausible that a system allowing variadic functions would also allow it. (I think it's a harder problem, though. It seems to me that if you can get polymorphism over tuple length you also get polymorphism over function arity. But I don't know if the reverse holds.)

    ```haskell
    unzip :: [(a, b)] -> ([a], [b])
    unzip :: [(a, b, c)] -> ([a], [b], [c])
    unzip :: [(a, b, c, d)] -> ([a], [b], [c], [d])
    ```

* Haskellers often find ourselves writing `f <$> a <*> b <*> c`. (`map` is a specialization of this, using the Applicative instance from ZipList.)

    ```haskell
    -- Realistically I expect this first would need Applicative
    appF :: Functor f => (a -> b) -> f a -> f b
    appF :: Applicative f => (a -> b -> c) -> f a -> f b -> f c
    appF :: Applicative f => (a -> b -> c -> d) -> f a -> f b -> f c -> f d
    ```

* Or we might want one for `f <*> a <*> b <*> c`

    ```haskell
    appA :: Applicative f => f (a -> b) -> f a -> f b
    appA :: Applicative f => f (a -> b -> c) -> f a -> f b -> f c
    appA :: Applicative f => f (a -> b -> c -> d) -> f a -> f b -> f c -> f d
    ```

* Haskell offers an impure function `trace` which is useful in debugging. We might want something similar, wrapping around a function to log every time it's called:

    ```haskell
    -- The first argument would be the function name or other identifier.
    trace :: String -> (a -> b) -> a -> b
    trace :: String -> (a -> b -> c) -> a -> b -> c
    trace :: String -> (a -> b -> c -> d) -> a -> b -> c -> d
    ```

(I'm using Haskell syntax for the types partly because Haskenthetical has no concept of typeclasses or rank-2 types, which some of the examples use. But also partly because it's probably easier to read. Which you might think would be a reason not to make Haskenthetical, but here we are.)

I'm not, to be clear, saying that all or even any of these are good ideas. I mostly don't miss variadic functions in Haskell; they can be implemented hackily like in Text.Printf linked above, but I'm not sure I've ever felt the need to, and I've rarely-if-ever used its `printf`. But it seems worth exploring the space of the sorts of things I might want to consider trying to support, before making any decisions.

Actually, I'm sure this doesn't fully explore the space. But I am going to leave it there for now.

---

The first paper I'm going to look at is the most recent one I've found:  Strickland, Tobin-Hochstadt and Felleisen, [Practical Variable-Arity Polymorphism](https://www2.ccs.neu.edu/racket/pubs/esop09-sthf.pdf) (2009, doi:[10.1007/978-3-642-00590-0_3](https://doi.org/10.1007/978-3-642-00590-9_3)). I linked this in my previous post. It implements typechecking for variadic functions in Typed Scheme, I think specifically meaning Typed [Racket](https://en.wikipedia.org/wiki/Racket_%28programming_language%29)? I'm not familiar with the language (I have done a little untyped Racket in the past), but from the sounds of things, its type system is fundamentally different from Hindley-Milner, and the implementation won't easily transfer. (Both compile to [System F](https://en.wikipedia.org/wiki/System_F), but I don't think that helps.)

But it does help me make sense of the space. It divides the functions it can type into two: uniform and non-uniform. Let's call the optional arguments the "rest parameter", as in the parameter which holds "the rest of the parameters". Uniform functions are those whose rest parameter is a homogeneous list, such that they could be replaced (at cost to ergonomics) with a function accepting a list. In my above examples, that's the arithmetic functions plus `list` and `list'`. In Typed Racket [syntax](https://docs.racket-lang.org/ts-guide/types.html), the types of these functions would be

```
(: + (-> Number Number Number * Number)) # also -, *, /
(: list (All (a) (-> a * (Listof a))))
(: list' (All (a) (-> a * (Listof a) (Listof a))))
```

With the `*` indicating "zero or more of the preceding type". These seem simple enough. (Though `list'` takes an argument after the variadic part, which makes things more complicated. Racket calls that function `list*` but I couldn't find a type declaration for it to be sure it's actually valid.)

Then the other other functions handled by the paper are "non-uniform". Of my examples, I think that's just `map`, `trace` and maybe `unzip` natively.

```
(: map (All (a b ...) (-> (-> b ... b a) (Listof b) ... b (Listof a))))
(: trace (All (a b ...)) (-> String (-> b ... b a) b ... b a))
(: unzip (All (a ...)) (-> (Listof (Tuple a ... a)) (Tuple (Listof a) ... a)))
```

For `unzip`, I'm inventing the type `Tuple` here to refer to a collection with known size and types. `(Tuple Number String Bool)` would be equivalent to Haskell's `(Number, String, Bool)`. I don't know if anything like it actually exists, or can exist, in Typed Racket already.

These are a bit more involved. The `...` is doing two related but syntactically different things.[^ellipsis] In the variable list of `All` (the `(a b ...)` and `(a ...)`) it says the preceding variable corresponds to a list of types. In the body of `All`, it combines with both the preceding and following variables. `t ... b` means: "`b` was followed by `...` in the type signature, so it corresponds to a list of types. Use a copy of `t` for each one of those types, and inside each copy, substitute `b` with the corresponding type from the list".

[^ellipsis]: It also makes it really hard to write code outlines while omitting certain parts.

So if `b ...` corresponds to `Integer String Number`, then `(Listof b) ... b` corresponds to `(Listof Integer) (Listof String) (Listof Number)`.

I don't know if we strictly need the trailing variable in the body. You're only allowed one `...` in the variable list (right at the end), and the trailing variable is required to have been in the variable list followed by a `...`, so as far as I can tell it's unambiguous. (At least as long as there are no higher-rank types, which I don't think I've seen mentioned yet.)

`printf`, `appF` and `appA` would also fit into this schema if it weren't for the constraints. But as far as I know Typed Racket has nothing analagous to Haskell's constraints. I don't know how much they complicate matters.

That leaves four examples. `sort` and `renderCsv` don't fit the scheme because they can only accept one or two optional arguments, not an arbitrary number. (Typed Racket [does support optional arguments](https://docs.racket-lang.org/ts-guide/types.html#%28part._.Types_for_.Functions_with_.Optional_or_.Keyword_.Arguments%29), they're just not covered by this paper.)

`»` and `«` don't fit because the type of each argument can depend on the type of the preceding one. For example, we might call

```haskell
(«) (&) 1 (+ 1) Just (fmap (* 3)) (: [])
(») ($) (: []) (fmap (* 3)) Just (+ 1) 1
```

There's a pattern to the types, but not the pattern we need.

So: this paper describes a way of typechecking a few of the functions we might like to typecheck, in a completely different type system than the one we want to use. What can we do in Hindley-Milner?

There's a brief discussion of that, mostly of the form "here's another paper that made some progress in an HM system. It's not as powerful as what we have here". But those other papers fully exhaust what I've managed to find on the subject, so let's take a look.

---

First up: Dzeng and Haynes, [Type reconstruction for variable-arity procedures](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.40.3560&rep=rep1&type=pdf) (1994, doi:[10.1145/182590.182484](https://doi.org/10.1145/182590.182484)). This uses a thing called "infinitary tuples" to handle optional arguments and both uniform and non-uniform variadic functions. Practical Variable-Arity Polymorphism lists some limitations:

> Most importantly, since their system does not support first-class polymorphic functions, they are unable to type many of the definitions of variable-arity functions, such as *map* or *fold*. Additionally, their system requires full type inference to avoid exposing users to the underlying details of row types, ...

I don't understand this first one: `map` is explicitly given as an example, with type

    $$ (\mathit{pre} · ((γ∘δ) → α) :: (γ ∘ (\underline{\mathtt{list}}\ δ)))
       → \mathtt{list}\ α $$

But this might help illustrate the second problem, which I think is saying that type annotations are complicated.

(Note that I've swapped from a postfix `$ α\ \mathtt{list} $` syntax to a prefix `$ \mathtt{list}\ α $` that I'm more used to. Also the `$ \underline{\mathtt{list}} $` was originally rendered `$ \underline{\mathit{list}} $` but I think that was a mistake.)

What's not allowed is to pass in a variadic function and apply it with two different argument counts: `((λ (f) (+ (f 1) (f 2 3))) +)` is forbidden, even though `(+ 1)` and `(+ 2 3)` are both okay. (I'm inclined to forbid `(+ 1)` but that's not important.) Combining this system with higher-rank types might avoid this limitation, but I don't know if they're compatible. The authors list two other ways to potentially avoid it, but both would need more investigation.

The other limitation I notice is: there's only one thing you can do with a "rest argument" (i.e. the collection of the arbitrarily-many arguments at the end), and that's to use it as another rest argument. There's even special syntax for that: you'd define a variadic function as `(λ (x &rest xs) ...)` (i.e. taking one required argument and arbitrarily many following that), and inside the body you'd call some other variadic function with `(g a b c &rest xs)`. So variadic functions need to be either built-in or defined in terms of other variadic functions.

How big a problem is this? I have no idea; the paper talks about type-checking, it contains zero implementations of variadic functions.

Ignoring that problem for now, and considering whether we can type the example functions from above:

* `+`, `list` and `map` are given as examples. The other arithmetic functions would be fine, and I'm fairly confident `trace` would be too.

* I think `list'` is not allowed, since it has an extra argument after the variadic part.

* I dunno about `printf`. I'd need to figure out how typeclasses fit in.

* I presented both `sort` and `renderCsv` with the optional arguments before the required ones. I think that rules them out.[^opt-before-req] `renderCsv` would be fine if we swap the arguments, but `sort` also has typeclass stuff going on. Even ignoring *that*, I'm not sure if "explicit comparison function with optional key function" is as polymorphic as we'd like. That is, we could write a function that can be accepted at types

    ```haskell
    sort :: [a] -> (a -> a -> Ordering) -> [a]
    sort :: [a] -> (a -> a -> Ordering) -> (a -> a) -> [a]
    ```

    with the third argument, the key function, defaulting to the identity. But I'm not sure if we could also accept

    ```haskell
    sort :: [a] -> (b -> b -> Ordering) -> (a -> b) -> [a]
    ```

    with the third argument taking a default type as well as a default value.

[^opt-before-req]: I'm not sure. It looks like there's nothing stopping us from constructing types corresponding to optional-before-required. But the paper describes a language syntax that forbids it. My weak guess is such types would break the inference algorithm.

* `appF` and `appA` seem likely, the typeclass stuff is simpler than either `printf` or `sort`.

* `unzip` might be feasible. We'd need some way to interpret a row (see below) as a proper type. I don't know how difficult that would be.

* I think `«` and `»` are right out.

So how does it work? It's based on extensible records, which I haven't yet looked at in depth. ([Extensible records with scoped labels](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/scopedlabels.pdf) is the paper I was planning to look into if I tried to add them to Haskenthetical, but it might not take a compatible approach.) A *row* is an infinite sequence of (mark, type) pairs, where a *mark* is either "present", "absent" or a mark variable. Rows can be equivalently constructed as pairs of (mark row, type row), where those are infinite sequences of the respective things. At some point all the marks become "absent", and then the types don't matter. Recall the type of `map` from above,

    $$ (\mathit{pre} · ((γ∘δ) → α) :: (γ ∘ (\underline{\mathtt{list}}\ δ)))
       → \mathtt{list}\ α $$

This is quantified over three type variables. $γ$ is quantified over mark rows, and $δ$ over type rows, with $γ∘δ$ combining them into a row. And $α$ is quantified over proper types.

Everything before the outermost `$ → $` is a row. (Functions in this system are of kind "row → type", not kind "type → type".) It has `$\mathit{pre} · ((γ∘δ) → α)$` as its head, a single field marked present with type `$ (γ∘δ) → α $`.
`$ γ∘δ $` is itself a row. Then for the outer row, the tail `$ γ ∘ (\underline{\mathtt{list}}\ δ) $` has the same sequence of marks as the argument to its head, meaning the same number of arguments. `$ \underline{\mathtt{list}}\ δ $` is a type row of "apply `list` to the types in `$ δ $`".

Then we might instantiate `$γ$` at `$ \mathit{pre} :: \mathit{pre} :: \underline{\mathit{abs}} $`, i.e. "two present fields and then nothing". And we might instantiate `$δ$` at `$ \mathtt{int} :: \mathtt{string} :: δ' $`, i.e. "an int, then a string, then another type row", and `$α$` at `$ \mathtt{bool} $`. Then we'd have something like the Haskell type

```haskell
(Int -> String -> Bool) -> [Int] -> [String] -> [Bool]
```

but it would be rendered in this type system as

    $$ (\mathit{pre}
        · ((\mathit{pre} · \mathtt{int}
            :: \mathit{pre} · \mathtt{string}
            :: \underline{\mathit{abs}} ∘ δ')
           → \mathtt{bool})
       :: \mathit{pre} · \mathtt{list\ int}
       :: \mathit{pre} · \mathtt{list\ string}
       :: \underline{\mathit{abs}} ∘ (\underline{\mathtt{list}}\ δ'))
    → \mathtt{list\ bool}
    $$

Which, let us say, I do not love. And this kind of thing infects all functions, not just variadic ones! And I don't know how it interacts with partial application. Still, maybe it can be made ergonomic. I think this paper deserves further study, though of course I don't know if I'll be doing it myself.

I still don't know what infinitary tuples actually are.

---








Resources:

[Practical Variable-Arity Polymorphism](https://www2.ccs.neu.edu/racket/pubs/esop09-sthf.pdf) (2009?) Works with Typed Scheme. Compiles to System F, which GHC does too, but I think that's not very helpful. (But maybe I should be doing the same?) Gives examples of variable arity functions.

"The Zip Calculus" (2000) - behind a paywall.

[Type reconstruction for variable-arity procedures](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.40.3560&rep=rep1&type=pdf) (1994) Extends an ML. Haven't read yet.

[Faking It: Simulating Dependent Types in Haskell](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.22.2636&rep=rep1&type=pdf) (2002)

"Arity polymorphism and dependent types" (2000) - haven't found a pdf yet





Ideally we maybe want types for

+ - 2 or more numbers
- - 1 or more numbers
list - any number of values of the same type

^ These are uniform. Might be most of the value?

map : (a -> b -> ... -> z) -> list a -> list b -> ... -> list z

^ does this generalize to fmap? It's already awkward with lists of different lengths. Plausibly we can generalize to fmap only for applicatives - though the list generalization is using the ZipList applicative, I think

unzip : list (a, b) -> (list a, list b)
      : list (a, b, c) -> (list a, list b, list c)
      : list (a, b, ..., z) -> (list a, list b, ..., list z)

^ is this possible in PVAP's scheme? Same question about generalizing to other functors

But we also need things like (foldl +) i.e. using + as (Float -> Float -> Float). Still want to type (+ 1) as (Float -> Float), except ideally (?) (foldl (+ 1)) will type (+ 1) as (Float -> Float -> Float).

And we want to be able to do something like ((+ 1 2) 3 4). I actually don't expect that to work at all, but ((partial + 1 2) 3 4) maybe?

Certainly I think it's fine to treat (a b c d) different from ((((a) b) c) d). Haskell is looking at this too, "a quick look at impredicativity".


Uniform types: we'd have something like

(def (: + (» -> Float Float (… Float) Float))
  (λ (x1 x2 (… xs)) (...)))


Somehow we need (-> (… Float) Float) to be able to be instantiated as any of

Float
(-> Float Float)
(-> Float (-> Float Float))
(-> Float (-> Float (-> Float Float)))

If we see (+ 1 2 3) we know to instantiate it as (» -> Float Float Float Float)

But we also need to be able to instantiate

(foldl + 0 (list 1 2 3))
(zip-with + (list 1 2 3) (list 4 5 6))
(zip-with-3 + (list 1 2 3) (list 4 5 6) (list 7 8 9))

Maybe we need

(-> (… Float) Float)

to be a specific kind of mtype, `TUniVarFn Float Float` that we handle in matching/unification and substitution, somehow?
