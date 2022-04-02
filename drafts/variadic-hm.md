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

* `»` and `«`, which take a function and then ≥ 2 arguments to interleave it with. Currently implemented as macros, and maybe I'd want them to be macros even if they could be functions, but that's not the point right now. Often the function will have a type like `-> $a (-> $b $a)` or `-> $b (-> $a $a)`, and then all or all-but-one of the arguments will be of the same type - this will be equivalent to using haskell's `foldr` or `foldl`. But that's not required. You could have `(» , 1 "foo" 3 "bar")` which would return `(, 1 (, "foo" (, 3 "bar")))`, the return type changing for every new argument you add.

    ```haskell
    -- e.g. in (») (+) 1 2 3
    (») :: Num a => (a -> a -> a) -> a -> a -> a -> a

    -- e.g. in (») (:) 1 2 []
    (») :: (a -> [a] -> [a]) -> a -> a -> [a] -> [a]

    -- e.g. in (») (,) 1 "foo" 3 "bar"
    (») :: (forall a b . a -> b -> (a, b))
        -> a -> b -> c -> d -> (a, (b, (c, d)))
    ```

* `sort` might have one or two optional arguments - one for a comparison function and/or one for a key function. (A key function is unnecessary if you have a comparison, but it might be convenient.)

    Actually, we can't distinguish a comparison function from a key function based on the types, here. There's nothing stopping someone from writing an `Ord` instance for `a -> Ordering`, and then `sort compare [...]` might refer to either of the two-argument forms. I'm just going to ignore that problem though.

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

* So could `zip` (`zip3`, `zip4`). Note that each of these is a partial application of a variadic `map`, but that doesn't mean variadic `map` gives us variadic `zip` for free. To define `zip` from `map` we'd presumably need a variadic tuple constructor, plus we'd need type checking to be able to combine them.

    ```haskell
    zip :: [a] -> [b] -> [(a, b)]
    zip :: [a] -> [b] -> [c] -> [(a, b, c)]
    zip :: [a] -> [b] -> [c] -> [d] -> [(a, b, c, d)]
    ```

* If we have `zip`, what about `unzip`? This isn't variadic, but it's plausible that a system allowing variadic functions would also allow it. (I think it's a harder problem, though. It seems to me that if you can get polymorphism over tuple length you essentially get polymorphism over function arity, perhaps with caveats around partial application. But I don't know if the reverse holds.)

    ```haskell
    unzip :: [(a, b)] -> ([a], [b])
    unzip :: [(a, b, c)] -> ([a], [b], [c])
    unzip :: [(a, b, c, d)] -> ([a], [b], [c], [d])
    ```

* Haskellers often find ourselves writing `f <$> a <*> b <*> c`. (`map` is a specialization of this, using the `Applicative` instance from `ZipList`.) Haskell calls these functions `fmap` (restricted to `Applicative` as `liftA`), `liftA2` and `liftA3`.

    ```haskell
    -- Realistically I expect this first would need Applicative
    appF :: Functor f => (a -> b) -> f a -> f b
    appF :: Applicative f => (a -> b -> c) -> f a -> f b -> f c
    appF :: Applicative f => (a -> b -> c -> d) -> f a -> f b -> f c -> f d
    ```

* Or we might want one for `f <*> a <*> b <*> c`. (`appF` is in turn a specialization of this, applying `pure` to its first argument.)

    ```haskell
    appA :: Applicative f => f (a -> b) -> f a -> f b
    appA :: Applicative f => f (a -> b -> c) -> f a -> f b -> f c
    appA :: Applicative f => f (a -> b -> c -> d) -> f a -> f b -> f c -> f d
    ```

* I can even imagine wanting to lift only the final result, replacing `pure $ f a b c` with `puring f a b c`. That seems kind of useless by itself, but the general pattern might not be.

    ```haskell
    puring :: Applicative f => a -> f a
    puring :: Applicative f => (a -> b) -> a -> f b
    puring :: Applicative f => (a -> b -> c) -> a -> b -> f c
    ```

* Haskell offers an impure function `trace` which is useful in debugging. I could imagine wanting something similar, wrapping around a function to log every time it's called. The variadic part of the type here is equivalent to `puring` specialized to `Identity`, but not having to worry about typeclasses might make things simpler.

    ```haskell
    -- The first argument would be the function name or other identifier.
    trace :: String -> (a -> b) -> a -> b
    trace :: String -> (a -> b -> c) -> a -> b -> c
    trace :: String -> (a -> b -> c -> d) -> a -> b -> c -> d
    ```

(I'm using Haskell syntax for the types, rather than Haskenthetical syntax. Partly because Haskenthetical has no concept of typeclasses or rank-2 types, which some of the examples use. But also partly because it's probably easier to read. Which you might think would be a reason not to make Haskenthetical, but here we are.)

I'm not, to be clear, saying that all or even any of these are good ideas. I mostly don't miss variadic functions in Haskell; they can be implemented hackily like in Text.Printf linked above, but I'm not sure I've ever felt the need to, and I've rarely-if-ever used that `printf`. But it seems worth starting to explore the space of the sorts of things I might want to consider trying to support, before making any decisions.

### Not Hindley-Milner

The first paper I'm going to look at is the most recent one I've found:  Strickland, Tobin-Hochstadt and Felleisen, [Practical Variable-Arity Polymorphism](https://www2.ccs.neu.edu/racket/pubs/esop09-sthf.pdf) (hereafter PVAP; 2009, doi: [10.1007/978-3-642-00590-0_3](https://doi.org/10.1007/978-3-642-00590-9_3)). I linked this in my previous post. It implements typechecking for variadic functions in Typed Scheme, I think specifically meaning Typed [Racket](https://en.wikipedia.org/wiki/Racket_%28programming_language%29)? I'm not familiar with the language (I have done a little untyped Racket in the past), but from the sounds of things, its type system is fundamentally different from Hindley-Milner, and the implementation won't easily transfer. (Both compile to [System F](https://en.wikipedia.org/wiki/System_F), but I don't think that helps.)

But it does help me make sense of the space. It divides the functions it can type into two: uniform and non-uniform. Let's call the optional arguments the "rest parameter", as in the parameter which holds "the rest of the parameters". Uniform functions are those whose rest parameter is a homogeneous list, such that they could be replaced (at cost to ergonomics) with a function accepting a list. In my above examples, that's the arithmetic functions plus `list` and `list'`. In Typed Racket [syntax](https://docs.racket-lang.org/ts-guide/types.html), the types of these functions would be

```
(: + (-> Number Number Number * Number)) # also -, *, /
(: list (All (a) (-> a * (Listof a))))
(: list' (All (a) (-> a * (Listof a) (Listof a))))
```

With the `*` indicating "zero or more of the preceding type". These seem simple enough. (Though `list'` takes an argument after the variadic part, which makes things more complicated. Racket calls that function `list*` but I couldn't find a type declaration for it to be sure it's actually valid.)

Then the other other functions handled by the paper are "non-uniform". Of my examples, I think that's just `map`, `trace`, and maybe `zip` and `unzip` natively.

```
(: map (All (a b ...) (-> (-> b ... b a) (Listof b) ... b (Listof a))))
(: trace (All (a b ...)) (-> String (-> b ... b a) b ... b a))
(: zip (All (a ...)) (-> (Listof a) ... a (Listof (Tuple a ... a))))
(: unzip (All (a ...)) (-> (Listof (Tuple a ... a)) (Tuple (Listof a) ... a)))
```

For `zip` and `unzip`, I'm inventing the type `Tuple` here to refer to a collection with known size and types. `(Tuple Number String Bool)` would be equivalent to Haskell's `(Number, String, Bool)`. I don't know if anything like it actually exists, or can exist, in Typed Racket already.

These are a bit more involved. The `...` is doing two related but syntactically different things.[^ellipsis] In the variable list of `All` (the `(a b ...)` and `(a ...)`) it says the preceding variable corresponds to a list of types. In the body of `All`, it combines with both the preceding and following syntax elements. `t ... b` means: "`b` was followed by `...` in the type signature, so it corresponds to a list of types. Use a copy of `t` for each one of those types, and inside each copy, substitute `b` with the corresponding type from the list".

[^ellipsis]: It also makes it really hard to write code outlines while omitting certain parts.

So if `b ...` corresponds to `Integer String Number`, then `(Listof b) ... b` corresponds to `(Listof Integer) (Listof String) (Listof Number)`.

I don't know if we strictly need the trailing variable in the body. You're only allowed one `...` in the variable list (right at the end), and the trailing variable is required to have been in the variable list followed by a `...`, so as far as I can tell it's unambiguous. (At least as long as there are no higher-rank types, which I don't think I've seen mentioned in this context.)

`printf`, `appF`, `appA` and `puring` would also fit into this schema if it weren't for the constraints. But as far as I know Typed Racket has nothing analagous to Haskell's constraints. I don't know how much they complicate matters.

That leaves four examples. `sort` and `renderCsv` don't fit the scheme because they can only accept one or two optional arguments, not an arbitrary number. (Typed Racket [does support optional arguments](https://docs.racket-lang.org/ts-guide/types.html#%28part._.Types_for_.Functions_with_.Optional_or_.Keyword_.Arguments%29), they're just not covered by this paper.)

`»` and `«` don't fit because the type of each argument can depend on the type of the preceding one. For example, we might call

```haskell
(«) (&) 1 (+ 1) Just (fmap (* 3)) (: [])
(») ($) (: []) (fmap (* 3)) Just (+ 1) 1
```

There's a pattern to the types, but not the pattern we need.

So: this paper describes a way of typechecking a few of the functions we might like to typecheck, in a completely different type system than the one we want to use. What can we do in Hindley-Milner?

There's a brief discussion of that, mostly of the form "here's another paper that made some progress in an HM system. It's not as powerful as what we have here". But those other papers fully exhaust what I've managed to find on the subject, so let's take a look. I can't find Moggi, Arity polymorphism and dependent types (2000), which leaves three to look at.

### Infinitary Tuples

First up: Dzeng and Haynes, [Type reconstruction for variable-arity procedures](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.40.3560&rep=rep1&type=pdf) (1994, doi: [10.1145/182590.182484](https://doi.org/10.1145/182590.182484)). This uses a thing called "infinitary tuples" to handle optional arguments and both uniform and non-uniform variadic functions. PVAP lists some limitations:

> Most importantly, since their system does not support first-class polymorphic functions, they are unable to type many of the definitions of variable-arity functions, such as *map* or *fold*. Additionally, their system requires full type inference to avoid exposing users to the underlying details of row types, ...

I don't understand this first one: `map` is explicitly given as an example, with type[^type-edit]

<div>
\[ (\mathit{pre} · ((γ∘δ) → α) :: (γ ∘ (\underline{\mathtt{list}}\ δ)))
→ \mathtt{list}\ α \]
</div>

[^type-edit]: Note that I've swapped from a postfix \\( α\ \mathtt{list} \\) syntax to a prefix \\( \mathtt{list}\ α \\) that I'm more used to. Also the \\( \underline{\mathtt{list}} \\) was originally rendered \\( \underline{\mathit{list}} \\) but I think that was a mistake.

But this might help illustrate the second problem, which I think is saying: type annotations are complicated, users won't want to deal with them.

I do notice two limitations myself. One is that you're not allowed to pass in a variadic function and apply it with two different argument counts: `((λ (f) (* (f 1) (f 2 3))) -)` is forbidden, even if `(- 1)` and `(- 2 3)` are both okay. Combining this system with higher-rank types might avoid this limitation, but I don't know if they're compatible. The authors list two other ways to potentially avoid it, but both would need more research. I don't know how big a deal this would be, but it feels minor. It's similar to (perhaps the same as) the restriction that lambda bindings are monomorphic, and I don't know if I've ever had a problem with that in practice.

The other is: there's only one thing you can do with a "rest argument" (i.e. the collection of the arbitrarily-many arguments at the end), and that's to use it as another rest argument. There's even special syntax for that: you'd define a variadic function as `(λ (x &rest xs) ...)` (i.e. taking one required argument and arbitrarily many following that), and inside the body you'd call some other variadic function with `(g a b c &rest xs)`. So variadic functions need to be either built-in or defined in terms of other variadic functions.

This feels like a bigger limitation, but again I don't really know. The paper only talks about type-checking - it contains zero implementations of variadic functions. Maybe a small handful of built-in ones would let us define everything we want.

Ignoring that problem for now, and considering whether we can type the example functions from above:

* `+`, `list` and `map` are given as examples. The other arithmetic functions would be fine, and I'm fairly confident `trace` would be too.

* I think `list'` is not allowed, since it has an extra argument after the variadic part.

* I dunno about `printf`. I'd need to figure out how typeclasses fit in.

* I presented both `sort` and `renderCsv` with the optional arguments before the required ones. I think that rules them out.[^opt-before-req] `renderCsv` would be fine if we swap the arguments, but `sort` also has typeclass stuff going on. Even ignoring *that*, I'm not sure if we can make the "explicit comparison function with optional key function" as polymorphic as we'd like. That is, we could write a function that can be accepted at types

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

* `appF`, `appA` and `puring` seem likely, the typeclass stuff is simpler than either `printf` or `sort`.

* `zip` and `unzip` might be feasible. We'd some way to interpret a row (see below) as a proper type. I don't know how difficult that would be.

* I think `«` and `»` are right out.

So how does it work? It's based on extensible records, which I haven't yet looked at in depth. ([Extensible records with scoped labels](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/scopedlabels.pdf) is the paper I was planning to look into if I tried to add them to Haskenthetical, but it might not take a compatible approach.) A *row* is an infinite sequence of (mark, type) pairs, where a *mark* is either "present", "absent" or a mark variable. Rows can be equivalently constructed as pairs of (mark row, type row), where those are infinite sequences of the respective things. At some point all the marks become "absent", and then the types don't matter. Recall the type of `map` from above,

<div>
\[ (\mathit{pre} · ((γ∘δ) → α) :: (γ ∘ (\underline{\mathtt{list}}\ δ)))
→ \mathtt{list}\ α \]
</div>

<p>
This is quantified over three type variables. \(γ\) is quantified over mark rows, and \(δ\) over type rows, with \(γ∘δ\) combining them into a row. And \(α\) is quantified over proper types.
</p>

<p>
Everything before the outermost \(→\) is a row. (Functions in this system are of kind "row → type", not kind "type → type".) It has \(\mathit{pre} · ((γ∘δ) → α)\) as its head, a single field marked present ("pre") with type \((γ∘δ) → α \). \(γ∘δ\) is itself a row. Then for the outer row, the tail \(γ ∘ (\underline{\mathtt{list}}\ δ)\) has the same sequence of marks as the argument to its head, meaning the same number of arguments. \(\underline{\mathtt{list}}\ δ\) is a type row of "apply <code>list</code> to the types in \(δ\)".
</p>

<p>
Then we might instantiate \(γ\) at \(\mathit{pre} :: \mathit{pre} :: \underline{\mathit{abs}}\), i.e. "two present fields and then nothing". And we might instantiate \(δ\) at \(\mathtt{int} :: \mathtt{string} :: δ'\), i.e. "an int, then a string, then another type row", and \(α\) at \(\mathtt{bool}\). Then we'd have something like the Haskell type
</p>

```haskell
(Int -> String -> Bool) -> [Int] -> [String] -> [Bool]
```

but it would be rendered in this type system as

<div>
\[
  (\mathit{pre}
   · ((\mathit{pre} · \mathtt{int}
       :: \mathit{pre} · \mathtt{string}
       :: \underline{\mathit{abs}} ∘ δ')
      → \mathtt{bool})
  :: \mathit{pre} · \mathtt{list\ int}
  :: \mathit{pre} · \mathtt{list\ string}
  :: \underline{\mathit{abs}} ∘ (\underline{\mathtt{list}}\ δ'))
→ \mathtt{list\ bool}
\]
</div>

Which, let us say, I do not love.[^indentation] And this kind of thing infects all functions, not just variadic ones! And I don't know how it interacts with partial application. Still, maybe it can be made ergonomic. I think this paper deserves further study, though I'm unlikely to do it myself.

[^indentation]: Sorry it's not indented nicely, I'm not sure how to make Mathjax do that. I wouldn't love it however nicely laid out, though.

### The Zip Calculus

Next is Tullsen, [The Zip Calculus](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.37.2645&rep=rep1&type=pdf) (2000, doi: [10.1007/10722010_3](https://doi.org/10.1007/10722010_3)). This extends typed lambda calculus to get variadic tuples.

This paper seems to come out of the "program transformation community", which I'm not familiar with. I suspect it's talking about things I know a little about in ways I don't recognize.

The specific typed lambda calculus it extends is "\\(\mathrm{F}\_ω\\)". Fortunately I recently came across the [lambda cube](https://en.wikipedia.org/wiki/Lambda_cube) so I know how to find out what that means. It's System F, which (as above) is what GHC compiles to as an intermediate step, plus the ability for the user to define their own types, which... I'd always assumed GHC's intermediate System F also had that, but maybe not, or maybe GHC actually compiles to \\(\mathrm{F}\_ω\\)? But... later in the paper it talks about dependent typing, which \\(\mathrm{F}\_ω\\) doesn't have, so maybe the paper is using nonstandard terminology? Argh.

Anyway, I think of System F as a more powerful version of Hindley-Milner, but too powerful to automatically type check, so you need lots of type annotations. If we're making it more powerful I guess we're still going to need those.

I confess I have trouble figuring out what this paper offers in any detail. I think I'd be able to eventually, but I'd need to put in more effort than I felt like right now.

It does give us a short list of functions that, if the language defines them built-in, we can build other functions out of. These are `list` and what it calls `seqTupleL` and `seqTupleR`. These aren't described except for their (identical) type signatures

<div>
\[ \mathtt{Monad\ m}
   ⇒ ×⟨^{i} \mathtt{a}_{.i} → \mathtt{m\ b}_{.i}⟩
   → ×\mathtt{a} → \mathtt{m}(×\mathtt{b}) \]
</div>

which I think in Haskell correspond to the types

```haskell
seqTuple_ :: Monad m => (a1 -> m b1) -> a1 -> m b1
seqTuple_ :: Monad m => (a1 -> m b1, a2 -> m b2) -> (a1, a2) -> m (b1, b2)
seqTuple_
  :: Monad m
  => (a1 -> m b1, a2 -> m b2, a3 -> m b3)
  -> (a1, a2, a3)
  -> m (b1, b2, b3)
```

If I'm right about that, I'm pretty sure the semantics are "zip the tuple of functions with the tuple of parameters, apply them each in turn and sequence the effects (left-to-right / right-to-left)".

Given these functions, we're specifically told we can implement `zip`, `unzip`, `map`[^zip-calculus-map] and `appF`[^appf-monadic]. I'm pretty sure arithmetic, `list'`, `appA`, `puring` and `trace` will be possible, and I weakly guess that `printf` will be as well, while `«` and `»` won't be. I'm not sure about `sort` or `renderCsv`.

[^zip-calculus-map]: Like with the previous paper, PVAP said `map` wouldn't be possible: "The presented limitations of the Zip Calculus imply that it cannot assign a variable-arity type to the definition of `zipWith` (Haskell's name for Scheme’s *map*) without further extension". As far as I can tell it was simply wrong.

[^appf-monadic]: `appF` is described with `Monad` constraints, but I gather the `Applicative` typeclass wasn't [introduced](https://www.staff.city.ac.uk/~ross/papers/Applicative.html) at the time. I expect the `seqTuple_` functions could take `Applicative` instead of `Monad`, and then so could `appF`.

One thing is that all of these functions are defined with variadic tuples, so that e.g. `map` would actually be accepted at types like

```haskell
map :: (a -> b) -> [a] -> [b]
map :: ((a, b) -> c) -> ([a], [b]) -> [c]
map :: ((a, b, c) -> d) -> ([a], [b], [c]) -> [d]
```

which I assume leaves no room for partial application. It might also be awkward when the final argument needs to be handled separately; I'm not sure if we could get

```haskell
list' :: [a] -> [a]
list' :: (a, [a]) -> [a]
list' :: (a, a, [a]) -> [a]
```

or if we'd be stuck with

```haskell
list' :: () -> [a] -> [a]
list' :: a -> [a] -> [a]
list' :: (a, a) -> [a] -> [a]
```

Given this limitation, it would be convenient to have variadic `curry` and `uncurry` functions,

```haskell
curry :: (a -> b -> c) -> (a, b) -> c
curry :: (a -> b -> c -> d) -> (a, b, c) -> d
curry :: (a -> b -> c -> d -> e) -> (a, b, c, d) -> e

uncurry :: ((a, b) -> c) -> a -> b -> c
uncurry :: ((a, b, c) -> d) -> a -> b -> c -> d
uncurry :: ((a, b, c, d) -> e) -> a -> b -> c -> d -> e
```

but no such luck. We're specifically told `curry` can't be typed, that's an area for future research. And `uncurry` would break us out of the variadic-tuple paradigm entirely.

I'd be really interested to see a more approachable-to-me version of this paper.

### Typeclasses

Finally McBride, [Faking It: Simulating Dependent Types in Haskell](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.22.2636&rep=rep1&type=pdf) (2002, doi: [10.1017/S0956796802004355](https://doi.org/10.1017/S0956796802004355)).

I'm happy to say I understand (the relevant parts of) this paper. It adds variadic `map` directly to Haskell using typeclasses. It then explores further in directions I'm going to ignore. The downside, as PVAP correctly notes, is that you need to explicitly pass in the number of variadic arguments as an initial argument.

The code is simple enough. It felt a bit dated to me: in the past twenty years GHC has added a bunch of new features that seemed like they'd help make it more ergonomic. But I [couldn't find](https://www.reddit.com/r/haskell/comments/sqnjsq/whats_the_modern_idiomatic_way_to_write_this/) a much better way to write it using those, so whatever.

The original is (equivalent to):

```haskell
{-# LANGUAGE FunctionalDependencies, FlexibleInstances, UndecidableInstances #-}

data Zero = Zero
data Suc n = Suc n

one = Suc Zero :: Suc Zero
two = Suc one :: Suc (Suc Zero)

class ManyApp n fst rest | n fst -> rest where
  manyApp :: n -> [fst] -> rest

instance ManyApp Zero t [t] where
  manyApp Zero fs = fs

instance ManyApp n fst rest => ManyApp (Suc n) (t -> fst) ([t] -> rest) where
  manyApp (Suc n) fs xs = manyApp n (zipWith ($) fs xs)

nZipWith :: ManyApp n fst rest => n -> fst -> rest
nZipWith n f = manyApp n (repeat f)
```

Here `manyApp` is the version where instead of just one function, we provide a list of them. The instances give us

```haskell
manyApp Zero :: [t]           -> [t]
manyApp one  :: [s -> t]      -> [s] -> [t]
manyApp two  :: [r -> s -> t] -> [r] -> [s] -> [t]
--      ^ n     ^ fst            ^ rest
```

We define it recursively, in terms of its simpler definitions. Then `nZipWith` is easy to define in terms of `manyApp`, where it's not easy to define recursively in terms of itself.

So what else can we already implement in Haskell with typeclasses? I think most of my original list of functions, and for several of them I think explicitly specifying the variadic count would be unnecessary.

I tried out a few of them, [see here](https://gist.github.com/ChickenProp/2f56ce8b2d056534fa9a049359a17af8). It's possible there are ways to improve on what I found, but my current sense is:

* Arithmetic, `list`, `printf`: work mostly fine with no variadic count, fine with it.
* `list'`: works poorly with no variadic count, fine with it.
* `zip`, `unzip`: need nested tuples, `((a, b), c)` rather than `(a, b, c)`. Given that, both work fine with variadic count. `zip` works poorly without, `unzip` doesn't for reasons related to the next section.
* `renderCsv`: works (mostly?) fine with no variadic count.
* `sort`: works okay with one optional argument and no variadic count. With two optional arguments, works fine with something specifying which form you want. (If they're independently optional, there are two two-argument forms, so it wouldn't necessarily be a "variadic count".) But at that point, really, just have different functions.
* `map`, `appF`, `appA`, `puring`, `trace`: work fine with variadic count.
* `»`, `«`: do not work.

Here, I consider something to "work" if you can make it do what you want, and work "better" if it doesn't need much type hinting. "works fine" means you don't need type hinting in any places I wouldn't normally expect it in Haskell, and I think the error messages might even be pretty normal?

So I think that with explicit counts, most of these work fine. Without the explicit counts, several of them work pretty okay, but they'll have difficulty if you use them in a weakly-constrained context. Like, `print (list "a" "b" "c")` won't work because it doesn't know if you want the `Show` instance on `[String]` or on `String -> [String]` or.... (Probably only one of these instances exists, but we can't rely on that.) But then you just need to add a type annotation, `print (list "a" "b" "c" :: [String])`. `list'` and `zip` need a lot more type annotations than is normal, for reasons I maybe have a shallow understanding of but not a deep one.

### Partial application

Here's something I think I was vaguely aware of before I started this, but it's clearer now: partial application makes this harder.

Consider the Haskell code

```haskell
zipWith (\a b c -> a + b + c) [1,2] [3,4]
```

That uses the existing 2-ary `zipWith` function, which means it has type `[Int -> Int]`[^int-literals]. (Its value is `[(+ 4), (+ 6)]`.) We could instead have used the existing 3-ary `zipWith3`, and then it would have type `[Int] -> [Int]`. If we used a variadic function, what type would it have? All the papers I looked at had some way of answering the question.

[^int-literals]: Pedantic note: I'm pretending here that integer literals have type `Int`, not type `Num a => a`.

In Racket, as far as I know there's no partial application. A function that takes two arguments is different from a function that takes one argument and returns a function that takes one argument. So under PVAP, to choose between the two interpretations, you'd need something like:

```racket
(map (λ (a b) (λ (c) (+ a b c))) '(1 2) '(3 4)) ; [Int -> Int]
(λ (cs) (map (λ (a b c) (+ a b c)) '(1 2) '(3 4) cs)) ; [Int] -> [Int]
```

The Zip Calculus preserves partial application for fixed-arity functions, but not variadic ones. (More precisely, it has partial application for functions but not for variadic tuples.) The two interpretations would be written as

```haskell
nZipWith (\(a, b) c -> a + b + c) ([1,2], [3,4]) -- [Int -> Int]
\cs -> nZipWith (\(a, b, c) -> a + b + c) ([1,2], [3,4], cs) -- [Int] -> [Int]
```

Which is basically the same as the Racket version, apart from syntax.

And "infinitary tuples" has to do something similar. For the list of functions, we'd pass "a function taking a row with two variables and returning a function" as the first argument. For the function on lists we'd pass "a function taking a row with three variables". I guess the system must lose Haskell's equivalence between `\a b -> ...` and `\a -> \b -> ...`.

The typeclass solution to this is completely different. The inner function is the same for both interpretations, what changes is the initial "number of variadic arguments" argument.

```haskell
nZipWith two (\a b c -> a + b + c) [1,2] [3,4] -- [Int -> Int]
nZipWith three (\a b c -> a + b + c) [1,2] [3,4] -- [Int] -> [Int]
```

This feels to me like the cleanest of the bunch. I introduced this initial argument as a downside before, but that might be kind of unfair - like, maybe it's only a downside compared to an imaginary world that I [hadn't yet realized was impossible](https://www.lesswrong.com/posts/gNodQGNoPDjztasbh/lies-damn-lies-and-fabricated-options).

How else might we solve this problem?

One option is to assume that `nZipWith` will never want to return a list of functions. I don't love that solution, but [here's someone implementing it](https://github.com/effectfully-ou/sketches/tree/master/avoid-overlapping-recursive) for `appF` (which they call `liftAn`).

Something else that might work is to wrap the return value of the initial function in some singleton type.

```haskell
nZipWith (\a b -> Solo $ \c -> a + b + c) [1,2] [3,4] -- [Int -> Int]
nZipWith (\a b c -> Solo $ a + b + c) [1,2] [3,4] -- [Int] -> [Int]
```

This is kind of similar to "no partial applications", except you can still do partial applications everywhere else.

And I don't know if this would be possible, but I could imagine using a type annotation to distinguish. If you need to annotate every call to the function, I think I'd rather just specify the number of arguments or something. But if you only need them when it's ambiguous that could be neat.

As I mentioned in the last section, this isn't a problem for every variadic function. I think PVAP's uniform variadic functions don't have it. Beyond that I don't currently have a good sense of which functions will and won't.

### Conclusion

The main thing I take away from this is that I'm basically going to drop variadic functions from my radar for Haskenthetical. Infinitary tuples and the zip calculus don't feel like directions I want to go in. This might affect whether, when and how I add support for typeclasses and various surrounding machinary.
