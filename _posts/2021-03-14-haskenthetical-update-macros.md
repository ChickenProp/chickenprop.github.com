---
title: "Haskenthetical update: user-defined macros"
layout: post
lw_xpost: true
---
A while back I [wrote](http://reasonableapproximation.net/2020/05/19/haskenthetical.html) about Haskenthetical, a language that I'm implementing for fun. I'm still working on it, at least from time to time.

The thing I'm pleased to have implemented recently is user-defined macros. This makes it potentially a lot more ergonomic.

(You still can't do anything with it, really. It has no I/O except for printing a single value at the end, and that's in a constrained format. It's beyond the reach even of [sysfuck](https://github.com/ChickenProp/sysfuck). But, like. If you could do things with it, user-defined macros would make it nicer to do those things.)

These aren't hygienic macros, partly because when I used Racket a little at my old job I never really got my head around those, but also because they would have been more work. I'm more inclined to go for Clojure's approach of [namespace qualifying](http://clojure-doc.org/articles/language/macros.html#macro-hygiene-and-gensym), but since I don't have any kind of namespaces yet it seems premature to think of that.

### Quasiquote

The biggest test of Haskenthetical yet has been using these macros to [implement](https://github.com/ChickenProp/haskenthetical/blob/master/examples/quote.hth) <sup><small>[¶](https://github.com/ChickenProp/haskenthetical/blob/e2a0472d72df7134f5729db27b373e499d834186/examples/quote.hth)</small></sup> quoting (`quote`, like a standard lisp `'`) and quasiquoting (`qq`, like `` ` ``, using `↑` and `↑↑` for splicing). Quasiquoting in particular was one of the hardest pieces of code I think I've ever written, and it's only 100 lines in the end. Some of the things that made it difficult:

* Haskenthetical is deficient. Pattern-matching causes deep nesting and the chance of forgetting a case, while type eliminators are hard to read and flow poorly. (It's deficient in many many ways, but those are the ones that seem particularly relevant here.)

* More importantly, the current implementation of Haskenthetical is deficient. The error messages are completely unhelpful, telling you that two types didn't unify but not where they occured. Both the debugging output and the output from the program itself are hard to read. I also uncovered one straight-up bug in the process, which was [easy to fix](https://github.com/ChickenProp/haskenthetical/commit/6231daa08dbad745a0427342d8306ae16eb2c32f#diff-7c3aa97781f37aaf206a0ea06a8d0953d13944309c2e3ed289997630749de32a) when I tracked it down but hard to track down because the error messages are completely unhelpful.

* Also, I'm deficient as a thinker. I have a brain architecture that can't easily distinguish between the object and the meta levels, or the meta and the meta-meta levels. Wtf, who designed this piece of shit?

* The problem itself is well-targeted to hit those last two deficiencies. The quasiquote function simply converts syntax trees to syntax trees, but some of the trees in question represent Haskenthetical expressions of certain types, and some of the transformations need to preserve or manipulate those types. The type checker could tell me "you're passing a list of trees somewhere you should be passing a single tree", but since everything is either a tree or a list of trees that doesn't narrow things down much. And it couldn't tell me "you're trying to convert this list-of-trees to a tree-evaluating-to-a-list but you've actually created a tree-evaluating-to-a-type-error".

Eventually I simplified the problem by first parsing a syntax tree into a new datatype, and then converting that new datatype into another syntax tree, giving slightly more type information. That also made it easier to perform some simplifications in the parsing step, which made the output simpler and easier to check. Ultimately this brought it to a level that my brain could handle.

The result is that you can implement macros by describing the shape of the code they could generate, rather than implementing something that evaluates to that shape. Here are two ways to write an if-elsif-else macro (technically only the "else" is necessary):

```
(defmacro if
  (λ ts
    (if~ ts (Cons $else Nil)
      else
      (if~ ts (Cons $cond (Cons $then $rest))
        (STTree (» Cons (STBare "if~")
                        cond
                        (STBare "True")
                        then
                        (STTree (Cons (STBare "if") rest))
                        Nil))
        (error! "`if` must have an odd number of args")))))

(defmacro if-qq
  (λ ts
    (if~ ts (Cons $else Nil)
      else
      (if~ ts (Cons $cond (Cons $then $rest))
        (qq (if~ (↑ cond) True (↑ then) (if-qq (↑↑ rest))))
        (error! "`if` must have an odd number of args")))))
```

In the first, we manually construct a `SyntaxTree` with the `STTree` constructor (which represents syntax like `(...)`), passing it an argument of type `List SyntaxTree`. In the second, we construct the same `SyntaxTree` using quasiquoting, with splices `↑` and `↑↑` to indicate where the input parameters go. `↑` expects its parameter to be a `SyntaxTree`, which gets interpolated directly, while `↑↑` expects its parameter to be a `List SyntaxTree`, each element of which gets interpolated. So `(if-qq a b c d e)` macroexpands once to `(if~ a True b (if-qq c d e))`, and ultimately to `(if~ a True b (if~ c True d e))`.

There's another macro I use in the first definition: `»` and `«` can be used to "make functions variadic" by threading them in between other parameters like a fold. We have

```
(» f a b c d) === (f a (f b (f c d)))
(« f a b c d) === (f (f (f a b) c) d)
```

These are built-in, but they don't need to be. It's partly a matter of convenience, and partly because I implemented them to test macroexpansion before I implemented user-defined macros.

### Implementation

There's a circularity problem when defining macros. Sometimes you'll want to do so using functions you've previously defined. And sometimes you'll want to use a macro to help define a function. Allowing either one of these seems easy enough, but how do you do both?

I don't know how lisps handle this problem. I don't remember it ever tripping me up when I used them (I have some experience with Common Lisp, Clojure and Racket), but that was years ago and maybe I just didn't stress test them properly.

Haskell solves it with modules. You can't call a macro in the same module you define it. In Haskell's case that also means not in the same file you define it. That's fine for Haskell I guess, but I wouldn't want it for Haskenthetical.

But getting rid of one-module-per-file, this seemed like a reasonable solution. So I added a new top-level form, `(declarations ...)`. With this, the order of events is:

1. Parse the input file into a list of `SyntaxTree` (trees whose leaves are barewords, floats and strings). Separate trees into those of the form `(declarations ...)` and all others.

2. For each `(declarations ...)` block,

    1. Parse its children into statements (`(def ...)`, `(type ...)`, `(defmacro ...)`) and expressions (underneath `def` and `defmacro`). In this step, we have a list of macros available in the environment, and recognize when those are being called, declining to parse the arguments to macros.

    2. Recursively macroexpand the result, evaluating macros (which can be builtins written in Haskell or Haskenthetical closures) on their arguments. Since macros convert SyntaxTrees directly to SyntaxTrees, we have to parse the result of each expansion.

    3. Add all the type declarations (`(type ...)`) to the environment, along with their constructors and eliminators. We have to do this simultaneously, because types can be mutually recursive.

    4. Type check all the value definitions. This has to be simultaneous too, for the same reason. If type checking passes, add them to the environment, which doesn't strictly need to be simultaneous but is forced to be by my implementation. (Every defined value is a thunk storing a copy of the environment at the time it was defined. These environments do need to be mutually recursive.)

    5. Type check the macro declarations, and add them to the environment. The type of a macro is `-> SyntaxTree SyntaxTree`, I think it's pretty okay for macros to be impure but in future they'll need to be augmented with some way for macros to consult the environment. We can do these one at a time, because macros declared in the same block can't reference each other directly. (They can generate references to each other.)

3. Treat the remaining top-level trees as another `(declarations ...)` block, and go through the same process. But this block is required to also contain a single top-level expression, after macroexpansion.

4. Type check that expression. If type checking passes, evaluate it in the environment we've been building up.

I don't know if this approach is standard. It seems to work. It doesn't allow macros to expand to `declarations` blocks, which is a shame. In future, if I implement importing from other files, I might figure out how to allow macros defined in other files to expand to those blocks. On the other hand, once I have IO it would be interesting to see if I can implement importing from other files purely in Haskenthetical, and use `declarations` blocks as the only built-in form of module. That would be great and terrible.

### Other things

I've added comments now. `#` is a comment to end of line, but it has to be surrounded by whitespace[^surrounded], because I don't want to eliminate the possibility of using that character in combination with other things. `#!` works the same, to allow shebang lines. I don't yet have multiline comments, or single-form comments.

[^surrounded]: Writing that I wasn't sure if it needed whitespace in front. Turns out it does. I didn't deliberately write it that way, I didn't think about the question at the time, but I think I prefer it.

I also have an emacs major mode, which parses comments badly because emacs' easy-mode syntax highlighting only supports fairly specific kinds of syntax. But it's better than nothing.

I discovered two bugs writing the previous post. The type checker was ignoring type annotations on λ parameters. I've fixed that. It also wasn't giving an error if a type annotation in a pattern match was more general than the type it matched. I've [only partly](https://www.reddit.com/r/ProgrammingLanguages/comments/k7cj7e/resources_on_typechecking_hindleymilner_with/gfgmgio/) fixed that. I think to fix it more thoroughly I'd need to implement constraints and constraint solving. I might also decide to eliminate that feature - GHC is [going in that direction](https://github.com/ghc-proposals/ghc-proposals/pull/128).

### What's next?

(Assuming I continue at all, that is. This is fun, but it's not the only fun thing.)

I dunno. The test suite is looking a bit embarrassing, I've only added a handful of new tests since I first wrote about this project. At first I wanted them to be nicely grouped, tests about type checking and type declaration and evaluation, but there's no clear division and I shouldn't try for it. Instead I think I'll just have one big file with lots of examples and some metadata.

One thing is that macros can't currently be used in types or patterns. So you can write `(list a b c)` instead of `(Cons a (Cons b (Cons c Nil)))` when constructing a list, but not when destructing it. And you can't write a three-argument function type as `(» -> a b c d)`. This should be some fairly low-hanging fruit.

Writing the quasiquoter made me want better error messages. That's definitely not low-hanging fruit though. Especially with macros in play - how do you give the location of an error in the file when any given piece of syntax might not have been in the original file? There are options here but also, annotating everything with a source location sounds boring even if I didn't have to worry about macros.

Another possibility is to look at the type checker only. [Write You a Haskell](http://dev.stephendiehl.com/fun/006_hindley_milner.html) implements it in two different ways in the same chapter. I followed the second approach, section "constraint generation", because Diehl says it "becomes easier to manage as our type system gets more complex and we start building out the language". But it means that by the time I get a type error, I've lost all context. The types `String` and `Float` should unify but don't, great, but I have no idea why I'd expect either of those. And I'm not convinced it accomplishes its goal - the point is to separate constraint solving from traversing the tree, but you still need to solve constraints when you generalize a variable during traversal (the implementation on the page is buggy).

I think the first approach in WYAH is also used by [Typing Haskell in Haskell](http://web.cecs.pdx.edu/~mpj/thih/thih.pdf), where you solve constraints as you traverse the program. Then the context is still there when you encounter a type error, which might make it easier to report a helpful error message.

Half the macros I've written so far (`»`, `«`, `list`) could simply be functions, except Hindley-Milner doesn't have variadic functions. Can it be expanded to have them? The paper [practical variable-arity polymorphism](https://www2.ccs.neu.edu/racket/pubs/esop09-sthf.pdf) looks interesting on this question, though I haven't looked closely or thought deeply. I'd be going even further out of my comfort zone, but that's not a bad thing.

I've been thinking about nomenclature a bit. Right now the `Either` type is called `+`, which might make sense if the `,` type was called `*` but it's called `,`. `List` and `Maybe` aren't built-in, but when I've been defining them I've been calling them `List` and `Maybe` with constructors `Nil` `Cons` `Nothing` `Just`. I'm thinking I might go with regex-inspired names,

* The unit type becomes `ε`, with constructor also `ε`.
* `+ $a $b` becames `|| $a $b`. Constructors `_| $a` and `|_ $b`, perhaps.
* `Maybe $a` becomes `?? $a`. Constructors `ι $a` and `?ε`. (`ι` is the [inclusion map](https://en.wikipedia.org/wiki/Inclusion_map) `-> $a (?? $a)`.)
* `List $a` becomes `** $a`. Constructors `:: $a (** $a)` and `*ε`, but I'm not sold on `::`.

This seems pretty terrible, how do you pronounce any of that? But it also seems kind of fun.
