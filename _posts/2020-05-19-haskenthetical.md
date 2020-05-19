---
title: Haskenthetical
layout: post
lw_xpost: true
---
This is a toy language I've been designing, or at least implementing, for about a year.

It's another take on "Haskell with a Lisp syntax". I'm aware of prior art: [Hackett](https://lexi-lambda.github.io/hackett/), [Axel](https://axellang.github.io/) and [Liskell](https://github.com/haskell-lisp/liskell). I haven't looked closely at any of them, because doing that seemed like it might make me less likely to keep working on Haskenthetical.

I call it "toy" in the sense of... well, right now it's a toy like an RC plane is a toy. But my vague goal is to make it into a toy like the Wright flyer would have been a toy if it had been built in 2003. I'd like to get it, say, 80% of the way to being a "real" language. I have no intention or expectation of taking it the other 800% of the way. I have no intention or expectation of taking on [responsibility-according-to-me](http://reasonableapproximation.net/2020/04/13/in-my-culture-responsibility-oss.html) here.

(And honestly, even the first 80% is super ambitious. I don't *expect* to get that far, it would just be nice to. If I never touch the project again after this, I won't consider my time wasted.)

If you're curious, [the source code is available here](https://github.com/ChickenProp/haskenthetical)<sup><small>[¶](https://github.com/ChickenProp/haskenthetical/tree/54d7571f1662af68418840645435ab7d0e719003)</small></sup>[^permalinks]. If you have [stack](https://en.wikipedia.org/wiki/Stack_\(Haskell\)), `stack build --fast` should suffice to build and then `stack exec -- haskenthe -h` to run the executable.

[^permalinks]: I'm using ¶ to indicate links to the state of the repository as of this writing.

So far I've implemented basic [Hindley-Milner type inference](http://reasonableapproximation.net/2019/05/05/hindley-milner.html), the ability to define new types, and pattern matching. The only built-in types are `->`, `Float` (which is a Haskell `Double` under the hood), and `String` (a Haskell `Text`). Builtin functions are `+`, `-` and `*` (all of type `-> Float (-> Float Float)` and `err!` (of type `-> String $a`). I don't yet have division because I haven't decided how I want to handle division by 0. I don't expect I'll come up with anything particularly exciting there, but also I haven't felt the need for division yet.

(Actually, the types `Either` and `,` are also builtin, along with functions to work with them: constructors `Left`, `Right` and `,`, and destructors `either`, `car` and `cdr`. But that's just because I added them before I added custom types, and I haven't bothered to remove them yet.)

I have a long list of things I'd like to include in future. Probably the ones that interest me most right now are macros[^hygenic], [extensible records](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/scopedlabels.pdf), and compilation. I don't know how macros and compilation are supposed to fit together, but I have some vague ideas in my head. And clearly it's been done in the past, so I assume I can find out how.

[^hygenic]: I don't think I'll try for hygienic macros, despite [recent events](https://en.wikipedia.org/wiki/Severe_acute_respiratory_syndrome_coronavirus_2#/media/File:SARS-CoV-2_without_background.png). My only experience with those has been in the small amount of Racket I've worked on, and I didn't manage to get my head around them.

Other things include IO, comments, imports, exhaustiveness checking and FFI. Maybe typeclasses, but I'm curious whether macros and lazy evaluation can make those less useful. Maybe lazy evaluation, but I'm on the fence about that.

Open variants (the sum-type version of extensible records) might be on that list too, but I'm not familiar with any prior uses of them so I guess there's probably something that makes them difficult? Maybe they're just not very ergonomic in actual use, in which case cool, they'll fit right in.

What I have so far isn't very interesting as a language, but it might be interesting enough to be worth writing about.

### General language overview

There are seven types of expression right now. I'm going to assume you'll understand most of them just by name.

Literal values are Strings and Floats. Variables are bare words with very few restrictions. (Right now they can contain any combination of printable characters other than whitespace, `"`, `(` and `)`; except that they can't start with something that would parse as a Float.) Lambdas have the syntax `(λ (arg1 arg2 ...) expr)`, or if there's only one argument, `(λ arg expr)` is also acceptable[^unicode]. Function calls, unsurprisingly, look like `(func arg1 arg2 ...)`, where all of those are expressions.

[^unicode]: I want unicode in languages to be more mainstream. There are good reasons why it's not, but at least some of those are chicken-egg problems. For example, most people aren't set up to easily write in unicode, but that's partly because most people never have to. Fortunately, I'm in a position where I can ignore all the good reasons not to do something.

There are two forms of let-binding. Syntactically they're similar: `([let/letrec] ((name1 expr1) (name2 expr2) ...) body-expr)`. `let` is nonrecursive, so that `exprN` can only refer to `nameM` for M < N. (You can reuse names, e.g. `(let ((a 1) (a (+ 1 a))) a)` gives 2.) `letrec` is recursive, so that any `exprN` can refer to any `nameM`. (I haven't implemented any checks to forbid you from reusing names here, but probably only the first or last use of a name would have any effect.)

Finally there's pattern binding with `(if~ val pat if-match else)`. Pattern `pat` can be a literal string or float, or a variable name prefixed with `$`, or a constructor name possibly with other patterns as arguments. If the value matches the pattern, `if-match` gets evaluated, with any variables bound to the relevant parts of the pattern. Otherwise, `else-match` gets evaluated. For example:

```
(if~ 0 0 "zero" "nonzero") # "zero"
(if~ 1 0 "zero" "nonzero") # "nonzero"
(if~ (Just 3) Nothing "Nothing" "Just") # "Just"
(if~ (Just 3) (Just $x) x 0) # 3
(if~ Nothing (Just $x) x 0) # 3
(if~ (, 1 2) (, $a $b) (+ a b) (err! "impossible")) # 3
```

(I'm leaning towards `#` for comments when I get around to that. Also, I'm assuming here that the `Maybe` type has been defined.)

There's no equivalent of a `case` statement that matches the same thing against multiple patterns. For that you'd need nested `if~`, and there's no exhaustiveness checking (i.e. nothing that would say "you missed a possibility").

This is all typechecked, so that you get a compilation error if you try to multiply a string by a float or whatever.

You can add explicit type declarations to expressions, or to parts of patterns or to the variables in `let` or `letrec` bindings.[^no-lambda] A type declaration looks like `(: expr type)` and a type is either a bare name for a type constructor, or a `$name` for a type variable, or a type application like e.g. `Maybe $a` or `-> (Maybe Float) String`. The root of a type application has to be a constructor, not a variable.

[^no-lambda]: While writing this I realized that while you can attach them to `λ` params as well, those currently aren't typechecked at all.

```
(: 0 Float)
(: (λ x (+ x 1)) (-> Float Float))
(if~ (Just 3) (Just (: $x Float)) x 0)
(if~ (Just 3) (: (Just $x) (Maybe Float)) x 0)
(let (((: id (-> $a $a)) (λ x x))) (id 3))
```

If a type declaration is more specific than it could be, it constrains the type of the expression; if it's more general, that's an error[^too-general-pattern]:

[^too-general-pattern]: But the error doesn't seem to work for type declarations in pattern bindings. That's another thing I noticed while writing this.

```
(let (((: x (Maybe $a)) Nothing)) x) # valid, (Maybe $a) is the inferred type
(let (((: x (Maybe Float)) Nothing)) x) # valid, Float is more specific than $a
(let (((: x (Maybe Float)) (Just "foo"))) x) # not valid, Float /= String
(let (((: x (Maybe $a)) (Just "foo"))) x) # not valid, $a is more general than String
```

Apart from expressions, the statements I've implemented so far are `def` for global definitions, and `type` to declare a new type.

Currently all the `def` statements get pulled together and brought into a single `letrec` around the top-level expression. (Each program currently is required to have exactly one of those.) So

```
(def foo ...)
(foo bar)
(def bar ...)
```

is sugar for

```
(letrec ((foo ...)
         (bar ...))
  (foo bar))
```

Type declaration introduces new types, constructors, and eliminator functions. For example,

```
(type (Maybe $a) Nothing (Just $a))
```

introduces three values into the environment: `Nothing` of type `Maybe $a`; `Just` of type `(-> $a (Maybe $a))`; and `elim-Maybe` of type `(-> $a (-> (-> $b $a) (-> (Maybe $b) $a)))`[^infix]. This last is the standard Haskell `maybe` function, but you get one for free whenever you declare a type.

[^infix]: Gee, you ever think maybe there's a reason Haskell doesn't use Lisp syntax? I feel like Lisp syntax kind of needs variadic applications to be readable, but Haskell semantics don't go well with those. I'm hoping to solve this disconnect with macros.

Other type declarations would look like:

```
(type Bool False True)
(type (List $a) Nil (Cons $a (List $a)))
(type (, $a $b) (, $a $b))
(type (Either $a $b) (Left $a) (Right $b))
(type Unit Unit)
(type (Proxy $a) Proxy)
(type Void)
```

(I'm tempted to name the standard unit type and its value `∅` instead. That's a bad name for the type, which is not an empty set, but it's a decent name for the value. It would be a fine name for the void type, but that type isn't useful enough to deserve such a concise name.)

`letrec` has something that's either a bug or, generously, a "missing feature that looks an awful lot like a bug when you don't realize that you're expecting it to be there". The way the typechecking works, inside the bindings for `letrec`, you can only use each bound variable at a single type. So you can't do

```
(letrec ((id (λ x
               (let ((a (id 3))
                     (b (id "foo")))
                 x))))
  ...)
```

because that uses `id` at types `-> Float Float` and `-> String String`. (Never mind that if you could it would be an infinite loop.) Haskell has this limitation too, though I'm not sure I've ever run into it naturally; I couldn't think of a non-contrived example.

In Haskenthetical, this applies across an entire binding group. So you also can't do this:

```
(letrec ((id (λ x x)))
         (some-float (id 3))
         (some-str (id "foo")))
  ...)
```

But that example would work if you translated it to Haskell. What gives?

Well, since `id` doesn't depend on `some-float` or `some-str`, you could easily rewrite that example as

```
(letrec ((id (λ x x))))
  (letrec ((some-float (id 3))
           (some-str (id "foo")))
    ...))
```

And it turns out that Haskell just does that transformation for you automatically. It figures out what depends on what and groups them in such a way as to impose the fewest possible restrictions. If you make that impossible by adding some contrived mutual references, you can make Haskell fail in the same way:

```haskell
let id_ x = const (const x someFloat) someStr
    someFloat = id_ (3 :: Int)
    someStr = id_ ("foo" :: String)
in ...
-- error: Couldn't match type ‘[Char]’ with ‘Int’
```

(You actually only need to reference one of `someFloat` or `someStr`, because once `id_` is used at a specific type, it no longer generalizes to `a -> a` in the body of the `let`.)

I haven't implemented this in Haskenthetical yet.

### Implementation

I don't think there's anything particularly exciting about the implementation, if you're familiar with such matters. But for those who aren't, and who want to hear about them from me, read on.

I [parse](https://github.com/ChickenProp/haskenthetical/blob/master/src/Parser.hs)<sup><small>[¶](https://github.com/ChickenProp/haskenthetical/blob/54d7571f1662af68418840645435ab7d0e719003/src/Parser.hs)</small></sup> the input text into a list of syntax trees using [Megaparsec](https://markkarpov.com/tutorial/megaparsec.html). The syntax tree only knows about a few types of token:

```haskell
data SyntaxTree
  = STString Text
  | STFloat Double
  | STBare Text
  | STTree [SyntaxTree]
```

Then I parse each tree into a statement (or expression, but that's just a type of statement) by recognizing specific `STBare` values (at the head of an `STTree`) as needing special handling and passing everything else through to "assume this is a function getting called".

[Typechecking](https://github.com/ChickenProp/haskenthetical/blob/master/src/TypeCheck.hs)<sup><small>[¶](https://github.com/ChickenProp/haskenthetical/blob/54d7571f1662af68418840645435ab7d0e719003/src/TypeCheck.hs)</small></sup> is [Hindley-Milner](http://reasonableapproximation.net/2019/05/05/hindley-milner.html). When I wrote that essay, I said I didn't know how to implement HM typechecking. I have some idea now, and would describe it vaguely like this:

> Recurse down the parse tree. At each step there are a few relevant types that you get to say "unify" with each other, roughly meaning "these are two different ways of writing the same type". Sometimes you look those types up in the environment, sometimes you just generate fresh type variables, and sometimes you generate fresh type variables and then add them to the environment. But as you go, you're building up a big list of *constraints*, pairs of types that unify. Also, each node gets a specific type assigned to it, which will generally be placed in a constraint. This stage is called "unification". For example, if you see the function call `(foo bar)`, you'll recurse down to get types `t1` for `foo` and `t2` for `bar`, and you'll generate a fresh type variable `t3` for the result. Then you'll say that `t1` unifies with `-> t2 t3`.
>
> When you've finished, you loop back over the list of constraints, and build up a *substitution*. Any time you see "this type variable should be the same as this other type", you add that to the substitution, and you make that substitution in the remaining constraints before looking at them. If you see two types that should be the same but the non-variable parts of them don't match up, that indicates a type error in the program. This stage is called "solving". For example, if we have the constraint that types `-> $a String` and `-> (Maybe Float) String` unify, then whenever we see type variable `$a` in future we can replace it with `Maybe Float`; if the second one had instead been `-> (Maybe Float) Float`, then those don't match up and the program doesn't typecheck.
>
> In the end, you apply your substitution to the type of the program as a whole that you got from unification, and that's the ultimate type inferred for the program. If there are any type variables left, the program doesn't fix them. (An example of this would be if the program was simply `Nothing`.)

Of course it's more complicated than that. For example, `let` and `letrec` need you to run solving during the unification phase. Also, declared types need to be treated specially so that you can reject if the user declares `Just 3` as `Maybe $a`.

Aside, a thing I don't fully understand: I haven't tried timing it, but this implementation looks to me like it's something like O(n²) in the size of the input. It's supposed to be roughly linear. I'm not sure if I'm missing something or if there's just a more efficient algorithm.

Anyway, that's roughly how I do it. I take this approach mostly from [Write You a Haskell](http://dev.stephendiehl.com/fun/) (notably chapter 7, section "constraint generation"[^chapter-7], but also other chapters were useful for other parts of Haskenthetical). But I had to figure out how to handle `letrec` myself, because the language implemented there uses `fix` instead[^fix]. I also took a lot from [Typing Haskell in Haskell](http://web.cecs.pdx.edu/~mpj/thih/thih.pdf), especially pattern matching. (I hadn't discovered it by the time I implemented `letrec`.) Neither source implements explicit type declarations[^h98], so I had to figure out those for myself too. I'm not convinced I did a very good job.

[^chapter-7]: Be aware that the implementation of let on that page [doesn't work](https://github.com/sdiehl/write-you-a-haskell/pull/89). It's been fixed in the repository, but not on the website.

[^fix]: It's [possible](https://github.com/ChickenProp/haskenthetical/blob/master/examples/fix-factorial.hth)<sup><small>[¶](https://github.com/ChickenProp/haskenthetical/blob/54d7571f1662af68418840645435ab7d0e719003/examples/fix-factorial.hth)</small></sup> to implement `fix` in Haskenthetical without `letrec`, so maybe I didn't need to figure it out. I could have just waited until I get macros and then implemented `letrec` in terms of `fix`.

[^h98]: THIH does have them for binding groups (like found in `let` and at the top level), but not expressions. That made me wonder if those weren't in the [Haskell 98 report](https://www.haskell.org/definition/haskell98-report.pdf), like how Elm doesn't have them. But they're there: §3.16, "Expression Type-Signatures".

Finally, [evaluation](https://github.com/ChickenProp/haskenthetical/blob/master/src/Eval.hs)<sup><small>[¶](https://github.com/ChickenProp/haskenthetical/blob/54d7571f1662af68418840645435ab7d0e719003/src/Eval.hs)</small></sup>: for the most part that's fairly straightforward. For example, when we evaluate a variable, we look up its value in the environment. When we evaluate a `let`, we evaluate something, add it to the environment under the relevant name, and go on to the next thing. There are a few [types of values](https://github.com/ChickenProp/haskenthetical/blob/master/src/Syntax.hs#L128)<sup><small>[¶](https://github.com/ChickenProp/haskenthetical/blob/54d7571f1662af68418840645435ab7d0e719003/src/Syntax.hs#L128)</small></sup> that we need only when evaluating:

* A closure is the thing that gets returned when we evaluate a `λ` expression. It captures a snapshot of the current environment, the name of the argument, and the body expression. If a λ has multiple arguments, it returns nested closures.
* A builtin is a regular Haskell function of type `Val -> Either Text Val` (plus a name to distinguish them). Builtins and closures are ultimately the only things that can be called as functions.
* A Thunk is an unevaluated expression, with a copy of its environment. They get evaluated as soon as anything returns them. Currently they're used in two places. `letrec` needs them because we can't evaluate bindings before adding them to the environment or we'd get infinite recursion. Type eliminators are builtin values, but the `Val` they return is a Thunk (with empty environment) to avoid the Haskell file Env.hs from having to reference Eval.hs.
* A tag is just a symbol (a Haskell `Text` under the hood) paired with a list of other values. Constructors wrap their arguments in a tag, and eliminators and pattern matching compare those symbols. There's no way to look at or manipulate the symbol directly in Haskenthetical, but I'd be curious to explore that direction.

I'll mention a couple other things that might be of note. These probably require more background knowledge of Haskell to make sense.

Firstly: I have the data type

```haskell
data Pass = Parsed | Typechecked
type Ps = 'Parsed
type Tc = 'Typechecked
```

which some types use as a parameter, like

```haskell
data TVar (p :: Pass) = TV !(XTV p) Name
type family XTV (p :: Pass)
type instance XTV Ps = NoExt -- data NoExt = NoExt
type instance XTV Tc = Kind  -- the kind of a Haskenthetical type
```

This lets us use a slightly different type `TVar` in different parts of the codebase. When we've merely parsed the program, we have no way to tell the kind of a type variable, so we have `NoExt` there. When it's been typechecked, the kind is known, so we include it. If there was a pass in which type variables simply shouldn't exist, we could write

```haskell
type instance XTV NoTVarPass = Void
```

and we wouldn't be able to use a `TVar` in that pass at all.

This technique is called "trees that grow", and I copied it directly from GHC. I'm not currently using it everywhere I could, for no principled reason that I can recall. There's a chance it'll be more trouble than it's worth at the level I'm working at. An annoying thing about it is that you can't use a regular `deriving` clause, so I have

```haskell
deriving instance Eq (TVar Ps)
deriving instance Eq (TVar Tc)
deriving instance Show (TVar Ps)
deriving instance Show (TVar Tc)
deriving instance Ord (TVar Ps)
deriving instance Ord (TVar Tc)
```

which kind of sucks[^undecidable-instances].

[^undecidable-instances]: If it annoys me too much, I can enable `UndecidableInstances` and do

    ```haskell
    deriving instance Eq (XTV p) => Eq (TVar p)
    deriving instance Show (XTV p) => Show (TVar p)
    deriving instance Ord (XTV p) => Ord (TVar p)
    ```

Secondly: builtin functions are kind of a pain to write manually. For example, `either` was previously defined as `Builtin $ Builtin' "either" heither` where

```haskell
rbb :: Name -> (Val -> Either Text Val) -> Either Text Val
rbb name func = Right $ Builtin $ Builtin' name func

heither :: Val -> Either Text Val
heither l = rbb "either.1" $ \r -> rbb "either.2" $ \case
  Tag "Left" [v] -> call l v
  Tag "Right" [v] -> call r v
  _ -> Left "final argument of either must be an Either"
```

(`Builtin` is a constructor of type `Val` containing a `Builtin`, and `Builtin'` is the only constructor of type `Builtin`. These names do not spark joy.)

It works, but it always felt like I should be able to do better. I spent a while [trying to figure that out](https://www.reddit.com/r/haskell/comments/ewrfaw/monthly_hask_anything_february_2020/fg7n07m/) and [now](https://github.com/ChickenProp/haskenthetical/commit/e1ee65de57090f2f8393fd2124f10d8a5ca21413#diff-e755bad193d9db7eb765fba628323325) the value is simply `heither` where

```haskell
heither :: Val
heither = mkBuiltinUnsafe $ do
  l <- getArg "either"
  r <- getArg "either.1"
  e <- getArg "either.2"
  pure $ case e of
    Tag "Left" [v] -> call l v
    Tag "Right" [v] -> call r v
    _ -> Left "final argument of either must be an Either"
```

I dunno if this is much better, honestly, but there we are. It needs `ApplicativeDo`; I never managed to either figure out a Monad that could do this, or prove that no such monad exists. (There's no Monad instance for the specific type that I use to implement this, because to write `join` for that monad you'd need to be able to extract the inner `[w]` from `([w], r -> ([w], r -> a))` without having an `r` to pass to the outer function, and that's not a thing that even makes sense to be able to do[^monad-instance]. But there might be a different type that enables what I'm trying to do and does admit a Monad instance.)

[^monad-instance]: You could actually get somewhere by passing in `undefined`, as long as the inner `[w]` doesn't depend on the outer `r` and everyone involved is careful about strictness. I don't recommend this.

---

So that's where it's at right now. Feel free to point out ways that it sucks, although not-sucking isn't the point. I'm also interested in pointers to how I might implement some of the things on my future list (I'm aware of [Implementing a JIT Compiled Language with Haskell and LLVM](http://www.stephendiehl.com/llvm/)), or other cool things I may like to put on that list, or even things you might happen to like about Haskenthetical.
