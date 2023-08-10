---
title: Three configurable prettyprinters
layout: post
tags: [software]
lw_xpost: true
external_comments:
  - name: /r/haskell
    url: https://www.reddit.com/r/haskell/comments/15nr7ky/rfc_three_configurable_prettyprinters/
  - name: Haskell Discourse
    url: https://discourse.haskell.org/t/rfc-three-configurable-prettyprinters/7265
---
*I gave a [fifteen minute talk](https://www.youtube.com/watch?v=TBBHGR4ZlZM) about this at Zurihac 2023. If you read this essay, I don't think there's much point in additionally watching the video.*

I've been exploring a new-to-me approach to stringification. Except that right now it's three different approaches that broadly share a common goal. I call it/them [`pretty-gist`](https://github.com/ChickenProp/pretty-gist).

The lowest-friction way to stringify things in Haskell is usually `show`. It gives the user close to zero ability to control how the thing is rendered.

The [`Show1`](https://hackage.haskell.org/package/base-4.18.0.0/docs/Data-Functor-Classes.html#t:Show1) and [`Show2`](https://hackage.haskell.org/package/base-4.18.0.0/docs/Data-Functor-Classes.html#t:Show2) classes give some control, but only in limited ways. Importantly, they only work on parameterized values; you could use `Show2` to change how you render the keys of a `Map Int String`, but not of an `IntMap String`.

There are also things that give you some control over layout, but not much control over content. For example, [aeson-pretty](https://hackage.haskell.org/package/aeson-pretty) lets you pretty-print json data, and [pretty-simple](https://hackage.haskell.org/package/pretty-simple) can pretty-print typical output from `show`. Both let you configure indent width, and pretty-simple additionally lets you choose some different layout styles (where to put newlines and parentheses) and stuff. But they both operate by a model where you produce a relatively simple data structure that they know how to deal with, they give you a few knobs and render it in full. (For aeson-pretty the data structure is JSON, for pretty-simple it's a custom type that they parse from `show` output and that's pretty good at reproducing it.)

Here are some use cases where I've wanted more control than I can easily get:

* My test suites generate a complicated data structure. Most of the time, most of this data structure is irrelevant to the test failures and I don't want to see it.

* A complicated data structure contains JSON values, and I want them rendered as JSON rather than as a Haskell data type. Or it contains floating-point numbers, and I want them rounded to 3dp with underscore separation (`17_923.472`). Or strings, which I want printed using C-style escapes rather than Haskell-style, and with unicode rendered.

* A list might be infinite, and I only want to show the first ten elements. Or a tree might actually be cyclic, and I want to only show three levels deep.

`pretty-gist` aims to enable stuff like this. I call the rendered outputs it produces "gists" following Raku's use of that term, where I think the intention is something like "take a guess about what I'm likely to want to see here and show me that". But if `pretty-gist` guesses wrong, it lets you correct it.

I've come up with several different approaches to this, which all have different things to recommend and disrecommend them. I'm writing about three of them here.

If you're a Haskell user, I'm interested to hear your thoughts. I have some specific questions at the end.

## Design goals

* It should pretty-print, with indentation that adjusts to the available width.

* As a user, you should be able to target configurations specifically or generally. "All lists" or "all lists of Ints" or "only lists found at this specific point in the data structure". "All floating-point numbers" or "`Float` but not `Double`".

* It should be low boilerplate, both as a user and an implementer.

* You shouldn't need extra imports to configure the rendering for a type.

* If something *almost* works, you should be able to make it work. No need to throw everything out and start from scratch.

I don't know how to meet all these design goals at once, but they're things I aim for.

Also: I think there's a sort of hierarchy of demandingness for what sort of situations we expect to use the library in. From most to least demanding:

* We're generating user-facing output, and we want to specify what it looks like down to the glyph.

* We're generating debug output. We probably don't care about the exact layouting, but it would be unfortunate if we accidentally hid some data that we intended to include. We can't simply edit the config and retry.

* We're generating output for a test failure. It's not ideal if it stops doing what we expect without warning, but it's not too bad because we can just change it and rerun the test.

* We're writing debug code that we don't expect to commit.

In more demanding situations, we probably don't mind being more verbose, and updating our rendering code more often when the data structures we're working with change. In less demanding situations, we're more likely to be satisfied with an 80/20 of "not quite what I want but good enough".

I'm not personally working on anything where I care about glyph-level exactness, so that one isn't a situation I feel like optimizing for. The others are all things I'd like `pretty-gist` to help with, but of course the best design for one might not be the best design for the others.

## Example

Here's how pretty-simple would render a particular representation of a chess game. Next to it is how I'd like pretty-gist to be able to, either by default or with a small amount of configuration on the user's part.

<table>
<tr>
<th style="font-weight: bold">pretty-simple</th>
<th style="font-weight: bold">pretty-gist</th>
</tr>
<tr>
<td markdown="1">
```
GameState
  { turn = White
  , pBlackWin = 0.3463
  , pWhiteWin = 0.3896
  , nMoves = 0
  , board = Board
    [
      [ Just
        ( Piece
          { pieceType = Rook
          , owner = Black
          , lastMoved = Nothing
          }
        )
      , Just
        ( Piece
          { pieceType = Knight
          , owner = Black
          , lastMoved = Nothing
          }
      ...
```
</td>
<td markdown="1">
```
GameState { turn = White
          , pBlackWin = 35%
          , pWhiteWin = 39%
          , nMoves = 0
          , board = [ [r, n, b, q, k, b, n, r]
                    , [p, p, p, p, p, p, p, p]
                    , [_, _, _, _, _, _, _, _]
                    , [_, _, _, _, _, _, _, _]
                    , [_, _, _, _, _, _, _, _]
                    , [_, _, _, _, _, _, _, _]
                    , [P, P, P, P, P, P, P, P]
                    , [R, N, B, Q, K, B, N, R]
                    ]
          }
```
</td>
</tr>
</table>

So one difference is that I've gone with a hanging bracket style, with no newline directly after `GameState` or `board =`. I don't feel strongly about that. It would be nice to let users control this, but I haven't put much thought into it.

I've also rendered the floats as percents. I haven't put much thought into this either, and haven't implemented it. But it seems vaguely useful and easy enough to have as an option, though it usually shouldn't be default.

It's not visible here, but pretty-simple has the ability to colorize its output. That's another thing I haven't thought about, and don't currently expect pretty-gist to support any time soon.

But the most important is rendering each `Maybe Piece` as a single character. There are three parts to that: a `Nothing` is rendering as `_`; a `Just` is simply rendering the value it contains with no wrapper; and a `Piece` is rendering as a single character. The combination makes it much easier to see most of the state of the game. You can no longer see when each piece last moved. But if that's not usually useful to you, it's fine not to show it by default.

(At this point, chess pedants may be pointing out that this data type doesn't capture everything you need for chess. You can't reliably tell whether en passant is currently legal. Maybe there are other problems too. Yes, well done chess pedants, you're very clever, now shut up.)

## Possible designs

I've come up with several possible designs for this making different tradeoffs. I'm going to talk about three of them that I've actually implemented to some extent.

### Classless solution

Perhaps the very simplest solution is just to write a custom renderer every time I need one. I'm not going to do that.

A level up from that, which I've implemented in the module [`Gist.Classless`](https://github.com/ChickenProp/pretty-gist/blob/aedcfc3a8adbd0c658b1370cee25500451fe68a4/src/Gist/Classless.hs), is to write renderers for lots of different data types and combine them. We can write

```haskell
newtype Prec = Prec Int -- precedence level, 0 - 11

data ConfigMaybe = ConfigMaybe { showConstructors :: Bool }
gistMaybe :: ConfigMaybe -> (Prec -> a -> Doc) -> Prec -> Maybe a -> Doc

data ConfigList = ConfigList { showElems :: Maybe Int, ... }
gistList :: ConfigList -> (Prec -> a -> Doc) -> Prec -> [a] -> Doc

data ConfigTuple2 = ConfigTuple2 { ... }
gistTuple2
  :: ConfigTuple2
  -> (Prec -> a -> Doc)
  -> (Prec -> b -> Doc)
  -> Prec
  -> (a, b)
  -> Doc

data ConfigFloat = ConfigFloat { ... }
gistFloat :: ConfigFloat -> Prec -> Float -> Doc
```

for some data type `Doc` that supports layout. (I've been using the one from `prettprinter`, which has a type argument that I'm ignoring here for simplicity.)

The `Prec` parameters here are needed for the same reason `Show` has `showsPrec`. Sometimes we need parentheses, and this lets us choose when we have them. But they clutter things up a lot. We could imagine predence being something that gets put into config types, but then the user needs to specify it everywhere; plus, a renderer might call one of its sub-renderers at two different precedence levels under different circumstances. So that doesn't really work, so we accept the clutter.

But essentially, we've decided that one particular config parameter is important enough that every function accepts it (which means every function expects every other function to accept it). That feels kinda dirty. Is there anything else that ought to be given this treatment?

Anyway, this works, and it has some things to recommend it. It's incredibly simple, a beginner-level Haskell programmer will be able to figure out what's going on. If I, as the library author, make a decision you the library user don't like, you can just write your own function and it plugs in seamlessly. And if you have a type that can't normally be rendered, like a function, you can pick some way to render it anyway.

It also has some things to disrecommend it. Most notably, it's very verbose. You need to specify how to render every type-parameterized node of your data structure. You can have default configs, but there's no "default list renderer" because there's no "default list element renderer". `IntMap v` can have a default renderer for its keys, but `Map Int v` can't unless you write a function `gistMapInt` separate from `gistMap`.

This also means that changes to your data structure are very often going to need to be reflected in your renderers, which sounds tedious.

Another problem is, I expect consistency to be hard. Whatever design decisions I make, they're not enforced through anything. So someone who disagrees with them, or simply isn't paying attention to them, can easily make different ones, and then users need to remember things. (E.g. I had `gistList`, `gistTuple2` and `gistFloat` all take precedence parameters, but they'll completely ignore them. So maybe someone in a similar situation decides not to bother with those parameters.)

Those are problems for users. There's also a problem for implementers: roughly speaking, you're going to be allowing the user to pass a renderer for every field of every constructor of your type. For non-parameterized types (like the keys of an `IntMap`) that can be in the actual config type, and for parameterized types (like the keys of a `Map`) it comes in separate arguments later, but it's going to be there. That's going to be tedious for you.

<details markdown="1">
<summary>Implementation for <code>Maybe</code></summary>

```haskell
data ConfigMaybe = ConfigMaybe { showConstructors :: Bool }
  deriving stock Generic

defaultConfigMaybe :: ConfigMaybe
defaultConfigMaybe = ConfigMaybe { showConstructors = False }

gistMaybe :: ConfigMaybe -> (Prec -> a -> Doc ann) -> Prec -> Maybe a -> Doc ann
gistMaybe (ConfigMaybe {..}) renderElem prec = if showConstructors
  then \case
    Nothing -> "Nothing"
    Just a  -> parensIf (prec > 10) $ "Just" <+> renderElem 11 a
  else \case
    Nothing -> "_"
    Just a  -> renderElem prec a

-- Renders "()".
gistMaybe defaultConfigMaybe (\_ _ -> "()") 0 $ Just ()

-- Renders "Just ()".
gistMaybe (defaultConfigMaybe { showConstructors = True })
          (\_ _ -> "()")
          0
  $ Just ()
```

</details>

<details markdown="1">
<summary>Implementation for <code>GameState</code></summary>

```haskell
import qualified Gist
import           Gist ( Prec )
import qualified Gist as Gist.ConfigMaybe ( ConfigMaybe(..) )

data ConfigPiece = ConfigPiece
  { singleChar      :: Bool
  , renderPieceType :: forall ann . Prec -> PieceType -> Doc ann
  , renderOwner     :: forall ann . Prec -> Player -> Doc ann
  , renderLastMoved :: forall ann . Prec -> Maybe Int -> Doc ann
  }

defaultConfigPiece :: ConfigPiece
defaultConfigPiece = ConfigPiece
  { singleChar      = False
  , renderPieceType = Gist.gistShowily
  , renderOwner     = Gist.gistShowily
  , renderLastMoved = Gist.gistMaybe Gist.defaultConfigMaybe Gist.gistShowily
  }

gistPiece :: ConfigPiece -> Prec -> Piece -> Doc ann
gistPiece (ConfigPiece {..}) prec piece@(Piece {..}) = if singleChar
  then prettyPieceChar piece
  else Gist.record
    prec
    (Just "Piece")
    [ ("pieceType", renderPieceType 0 pieceType)
    , ("owner"    , renderOwner 0 owner)
    , ("lastMoved", renderLastMoved 0 lastMoved)
    ]

gistBoard :: (Prec -> [[a]] -> Doc ann) -> Prec -> Board a -> Doc ann
gistBoard renderer prec (Board a) = renderer prec a

data ConfigGameState = ConfigGameState
  { renderTurn      :: forall ann . Prec -> Player -> Doc ann
  , renderPBlackWin :: forall ann . Prec -> Float -> Doc ann
  , renderPWhiteWin :: forall ann . Prec -> Float -> Doc ann
  , renderNMoves    :: forall ann . Prec -> Int -> Doc ann
  , renderBoard     :: forall ann . Prec -> Board (Maybe Piece) -> Doc ann
  }

defaultConfigGameState :: ConfigGameState
defaultConfigGameState = ConfigGameState
  { renderTurn      = Gist.gistShowily
  , renderPBlackWin = Gist.gistShowily
  , renderPWhiteWin = Gist.gistShowily
  , renderNMoves    = Gist.gistShowily
  , renderBoard     = gistBoard
                      $ Gist.gistList Gist.defaultConfigList
                      $ Gist.gistList Gist.defaultConfigList
                      $ Gist.gistMaybe Gist.defaultConfigMaybe
                      $ gistPiece
                      $ defaultConfigPiece { singleChar = True }
  }

gistGameState :: ConfigGameState -> Prec -> GameState -> Doc ann
gistGameState (ConfigGameState {..}) prec (GameState {..}) = Gist.record
  prec
  (Just "GameState")
  [ ("turn"     , renderTurn 0 turn)
  , ("pBlackWin", renderPBlackWin 0 pBlackWin)
  , ("pWhiteWin", renderPWhiteWin 0 pWhiteWin)
  , ("nMoves"   , renderNMoves 0 nMoves)
  , ("board"    , renderBoard 0 board)
  ]

-- Renders in short form.
gistGameState defaultConfigGameState 0 startPos

-- Renders in long form.
let conf = defaultConfigGameState
      { renderBoard = gistBoard
                      $ Gist.gistList Gist.defaultConfigList
                      $ Gist.gistList Gist.defaultConfigList
                      $ Gist.gistMaybe Gist.defaultConfigMaybe
                      $ gistPiece
                      $ defaultConfigPiece { singleChar = False }
      }
in gistGameState conf 0 startPos

-- Renders in fully explicit form.
let confMaybe =
      Gist.defaultConfigMaybe { Gist.ConfigMaybe.showConstructors = True }
    conf      = CB.defaultConfigGameState
      { CB.renderBoard = CB.gistBoard
                         $ Gist.gistList Gist.defaultConfigList
                         $ Gist.gistList Gist.defaultConfigList
                         $ Gist.gistMaybe confMaybe
                         $ CB.gistPiece
                         $ CB.defaultConfigPiece
                             { CB.singleChar      = False
                             , CB.renderLastMoved = Gist.gistMaybe
                                                      confMaybe
                                                      Gist.gistShowily
                             }
      }
in gistGameState conf 0 startPos
```

</details>

### One-class solution

We can maybe-improve on this with typeclasses. We can use type families to let each gistable type have a separate config type.

```haskell
class Gist a where
  type Config a :: Type
  defaultConfig :: Config a
  gistPrec :: Prec -> Config a -> a -> Doc

data ConfigList a = ConfigList
  { showFirst :: Maybe Int
  , configElem :: Config a
  }

instance Gist a => Gist [a] where
  type Config [a] = ConfigList a
  defaultConfig = ConfigList { showFirst = Nothing, configElem = defaultConfig }
  gistPrec = ...
```

This is the foundation of the approach I've implemented in the module
[`Gist.OneClass`](https://github.com/ChickenProp/pretty-gist/blob/aedcfc3a8adbd0c658b1370cee25500451fe68a4/src/Gist/OneClass.hs).

There are a few significant complications. One is, this won't handle `String` well, because that's just `[Char]`. Other typeclasses (including `Show`) solve this by having an extra method for "how to handle lists of this type"; then you give that method a default implementation, but override it for `Char`. This seems fine as a solution, by which I mean "I hate it but I don't have any better ideas". I'm not going to bother showing it here. (Also it's not actually implemented for this approach in the code yet.)

Next: the typechecking here doesn't work very well. If we try

```haskell
gist (defaultConfig { ... }) [True] -- `gist` is `gistPrec 0`
```

we probably mean `defaultConfig` to refer to `defaultConfig @[Bool]`. But all GHC knows is that we mean `defaultConfig { ... }` to have type `Config [Bool]`. That doesn't even fully specify the type of `defaultConfig`, let alone its value. (We might be using the `defaultConfig` of some other instance that shares the same type; or that has a different type until we update it. The second possibility means injective type families wouldn't help much.) So we instead need to write

```haskell
gist ((defaultConfig @[Bool]) { ... }) [True]
```

which is no fun. That extra unnecessary-looking set of parentheses is an added kick in the teeth. So we add functions `gistF` and `gistPrecF`, which replace the `Config a` argument with a `Config a -> Config a` argument and apply it to `defaultConfig`. So now we write

```haskell
gistF (\c -> c { ... }) [True]
```

But we do keep the existing functions around for the final complication. Some things can't be rendered automatically (e.g. functions), but we sometimes want to render them anyway, or data structures containing them. Like a function `Bool -> Int` that's equivalent to a pair `(Int, Int)`. Sometimes we can use newtypes and maybe `coerce` for this, but not always, and it might be a pain even if we can.

It turns out we can handle this case. Consider the type

```haskell
data Gister a where
  FnGister :: (Int -> a -> Doc) -> Gister a
  ConfGister :: Gist a => Config a -> Gister a

runGisterPrec :: Int -> Gister a -> a -> Doc
runGisterPrec prec = \case
  FnGister   f -> f prec
  ConfGister c -> gistPrec prec c
```

A `Gister` is a renderer for any type. For types implementing `Gist`, we can create a `Gister` through `Config`, but for any other type we can still write our own rendering function.

This lets us have an instance `Gist [a]` without first requiring `Gist a`. We can't have a (useful) default config in that case, the only fully general `Gister a`s we could write would ignore the value they're passed. But we can still have a default when we do have `Gist a` (assuming it has its own default):

```haskell
class Gist a where
  type Config a :: Type
  type HasDefaultConfig a :: Constraint
  defaultConfig :: HasDefaultConfig a => Config a
  gistPrec :: Int -> Config a -> a -> Doc

data ConfigList a = ConfigList
  { showFirst :: Maybe Int
  , gistElem  :: Gister a
  }

instance Gist [a] where
  type Config [a] = ConfigList a
  type HasDefaultConfig [a] = (Gist a, HasDefaultConfig a)
  defaultConfig =
    ConfigList { showFirst = Nothing, gistElem = defaultConfig }
  gistPrec = ...
```

So now you can call `gist` on a `[Bool -> Int]`, and you need to write for yourself how to render one of those functions but you can use `gist` when you do so. There's no `defaultConfig @[Bool -> Int]`, but you can do a type-changing update of `defaultConfig @[Void]` or similar. Though this is harder than we might like, because we can't derive a `Generic` instance for `Gister a` which means we can't use generic-lens or generic-optics. Fine in this case, annoying for nested structures, might be able to improve.

And that's just about everything for this solution.

So this preserves a lot of the good stuff about the classless solution. It's still reasonably simple as Haskell code, at least according to my judgment. We can still render any type, though it would be even simpler if we removed that option. And the user can still completely override the implementer if they want, though not as seamlessly as before.

And it's usually going to be a lot less verbose, with less need to change when your data structure changes. If the bits you've configured haven't changed, you should be good.

But there's still things not to like. For one, the tedious-for-implementers thing hasn't changed.

For another, if a type shows up at multiple places in the data structure, you probably want to render it the same in all of those places; if you have a `[(Float, Float)]` you probably want to render the `fst`s the same as the `snd`s. But to do that you have to remember every place it might show up and configure them all separately; and if it starts showing up in a new place, it's probably easy for you to forget to configure that one. (Unlike with the classless solution, where you'll get type errors if you forget about it.)

You're also going to be dealing with nested record updates, which I find unpleasant and have a bunch of [questions](https://www.reddit.com/r/haskell/comments/128aifn/monthly_hask_anything_april_2023/jepke16/) about. That's somewhat the case with the classless solution too, but I think less deeply nested due to the structure of arguments and the lack of `Gister`. And here, you'll sometimes be doing type-changing record updates, and I think the future of those is uncertain (they're not supported by [`OverloadedRecordUpdate`](https://ghc.gitlab.haskell.org/ghc/doc/users_guide/exts/overloaded_record_update.html)).

<details markdown="1">
<summary>Implementation for <code>Maybe</code></summary>

```haskell
data ConfigMaybe a = ConfigMaybe
  { showConstructors :: Bool
  , gistElem :: Gister a
  }
  deriving stock Generic

instance Gist (Maybe a) where
  type Config (Maybe a) = ConfigMaybe a
  type HasDefaultConfig (Maybe a) = (Gist a, HasDefaultConfig a)
  defaultConfig = ConfigMaybe False (ConfGister $ defaultConfig @a)

  gistPrec prec (ConfigMaybe {..}) = if showConstructors
    then \case
      Nothing -> "Nothing"
      Just x  -> parensIf (prec > 10) $ "Just" <+> runGisterPrec 11 gistElem x
    else \case
      Nothing -> "_"
      Just x  -> runGisterPrec prec gistElem x

-- Renders "()". `gist_` is `gistF id`.
gist_ $ Just ()

-- Renders "Just ()".
gistF (\c -> c { showConstructors = True }) $ Just ()
```

</details>

<details markdown="1">
<summary>Implementation for <code>GameState</code></summary>

```haskell
import qualified Gist
import           Gist ( Gist(..) )
import qualified Gist as Gist.ConfigList ( ConfigList(..) )
import qualified Gist as Gist.ConfigMaybe ( ConfigMaybe(..) )

deriving via Gist.Showily Player instance Gist Player
deriving via Gist.Showily PieceType instance Gist PieceType
deriving newtype instance Gist (Board a)

data ConfigPiece = ConfigPiece
  { singleChar    :: Bool
  , gistPieceType :: Gist.Gister PieceType
  , gistOwner     :: Gist.Gister Player
  , gistLastMoved :: Gist.Gister (Maybe Int)
  }
  deriving stock Generic

instance Gist Piece where
  type Config Piece = ConfigPiece
  defaultConfig = ConfigPiece False
                              (Gist.ConfGister $ defaultConfig @PieceType)
                              (Gist.ConfGister $ defaultConfig @Player)
                              (Gist.ConfGister $ defaultConfig @(Maybe Int))

  gistPrec prec (ConfigPiece {..}) piece@(Piece {..}) = if singleChar
    then prettyPieceChar piece
    else Gist.record
      prec
      (Just "Piece")
      [ ("pieceType", Gist.runGister gistPieceType pieceType)
      , ("owner"    , Gist.runGister gistOwner owner)
      , ("lastMoved", Gist.runGister gistLastMoved lastMoved)
      ]

data ConfigGameState = ConfigGameState
  { gistTurn      :: Gist.Gister Player
  , gistPBlackWin :: Gist.Gister Float
  , gistPWhiteWin :: Gist.Gister Float
  , gistNMoves    :: Gist.Gister Int
  , gistBoard     :: Gist.Gister (Board (Maybe Piece))
  }
  deriving stock Generic

instance Gist GameState where
  type Config GameState = ConfigGameState
  defaultConfig = ConfigGameState
    { gistTurn      = Gist.defaultConfGister
    , gistPBlackWin = Gist.defaultConfGister
    , gistPWhiteWin = Gist.defaultConfGister
    , gistNMoves    = Gist.defaultConfGister
    , gistBoard     =
      let
        gPiece  = Gist.defaultConfGisterF $ \c -> c { singleChar = True }
        gMPiece = Gist.defaultConfGisterF
          $ \c -> c { Gist.ConfigMaybe.gistElem = gPiece }
        gLMPiece = Gist.defaultConfGisterF
          $ \c -> c { Gist.ConfigList.gistElem = gMPiece }
        gBoard = Gist.defaultConfGisterF
          $ \c -> c { Gist.ConfigList.gistElem = gLMPiece }
      in
        gBoard
    }

  gistPrec prec (ConfigGameState {..}) (GameState {..}) = Gist.record
    prec
    (Just "GameState")
    [ ("turn"     , Gist.runGister gistTurn turn)
    , ("pBlackWin", Gist.runGister gistPBlackWin pBlackWin)
    , ("pWhiteWin", Gist.runGister gistPWhiteWin pWhiteWin)
    , ("nMoves"   , Gist.runGister gistNMoves nMoves)
    , ("board"    , Gist.runGister gistBoard board)
    ]

-- Renders in short form. `gist_` is `gistF id`.
gist_ startPos

-- Renders in long form. This uses generic-lens to do record updates, but an
-- approach like used in `defaultConfig` would work too:
--     gistF (let ... in \c -> c { gistBoard = gBoard }) startPos
gistF
  ( setField @"gistBoard"
  $ Gist.defaultConfGisterF
  $ setField @"gistElem"
  $ Gist.defaultConfGisterF
  $ setField @"gistElem"
  $ Gist.defaultConfGisterF
  $ setField @"gistElem"
  $ Gist.defaultConfGisterF
  $ setField @"singleChar" False
  )
  startPos

-- Renders in fully explicit form. This could also be done with standard record
-- updates.
gistF
  ( setField @"gistBoard"
  $ Gist.defaultConfGisterF
  $ setField @"gistElem"
  $ Gist.defaultConfGisterF
  $ setField @"gistElem"
  $ Gist.defaultConfGisterF
  $ ( setField @"showConstructors" True
    . ( setField @"gistElem"
      $ Gist.defaultConfGisterF
      $ ( setField @"singleChar" False
        . ( setField @"gistLastMoved"
          $ Gist.defaultConfGisterF
          $ setField @"showConstructors" True
          )
        )
      )
    )
  )
  startPos
```

</details>

### Two-class solution

So here's a very different approach.

First, we find some way to store the config for every possible in a single data structure, even though we don't know all the possible configs yet.

Then we make this config store available to renderers. They look up the config that's relevant specifically to them. When rendering their contents, they simply pass down the same config store. A `MonadReader` helps here.

This makes "update the config of every occurrence of a type" easy. It makes "update the config of just this specific occurrence of a type" impossible. So we also track our location in the data structure, and in the config store we let users say "this option only applies at this location", or "at locations matching ...".

(This last bit sounds almost more trouble than it's worth. But without it, it becomes super awkward to handle things like "only show three levels deep of this self-referential data type".)

This is currently implemented in the [`Gist.TwoClass`](https://github.com/ChickenProp/pretty-gist/blob/aedcfc3a8adbd0c658b1370cee25500451fe68a4/src/Gist/TwoClass.hs) module. There's also a [`Gist.Dynamic`](https://github.com/ChickenProp/pretty-gist/blob/aedcfc3a8adbd0c658b1370cee25500451fe68a4/src/Gist/Dynamic.hs) module which has just the config-data-structure part, and is actually the implementation I've fleshed out the most. But I currently think it's not worth exploring more and not worth discussing in depth by itself.

Somewhat simplified, here's the main stuff going on with this solution:

```haskell
-- | Opaque storage of config options, implemented with existential types. Not
-- type-safe by construction, but has a type-safe interface.
newtype Config = UnsafeConfig { ... }

-- | Things that can be put into a `Config`.
class (Typeable a, Monoid (ConfigFor a), Typeable (ConfigFor a))
  => Configurable a
 where
  type ConfigFor a :: Type

-- | Tracking and matching locations in the data structure.
newtype GistPath = ...
data PathMatcher = ...

data GistContext = GistContext
  { gcPath :: GistPath
  , gcConf :: Config
  }

-- | Things that can be rendered.
class Configurable a => Gist a where
  renderM :: MonadReader GistContext m => Int -> a -> m Doc

-- | The user-facing interface.
gist :: Gist a => [Config] -> a -> Doc
config :: Configurable a => Maybe PathMatcher -> ConfigFor a -> Config
```

The separation between `Configurable` and `Gist` might seem unnecessary here - why would we configure something we can't render? The answer is that `Configurable` doesn't specify the kind of its argument. So we have all of

```haskell
instance Configurable Map
instance Typeable k => Configurable (Map k)
instance (Typeable k, Typeable v) => Configurable (Map k v)
```

and then users can add configuration for all `Map`s without needing to specify the exact types. (And they can override that config at specific types, if they want, using the `Semigroup` instance of the `ConfigFor`.) We also have `instance Configurable Floating`, and then the `Gist` instances for both `Float` and `Double` can look that up.

So the flow is that users build up a `Config` data structure, specifying "for this type, (optionally: at this location in the data structure,) set these options".

Then we walk through the structure. At each point we look up the relevant config values for the type at the current location, and possibly for other types, and combine all these in some way that users will just have to beat into submission if they're doing something complicated. And then we render, passing an updated `GistPath` and the same `Config` to any subcomponents.

This isn't very transparent to users. The `Float` instance looks up config for both `Float` and `Floating`, and the `Maybe a` instance looks it up for both `Maybe a` and `Maybe`. But to discover these you have to either try it and see, or look at the source code, or read the instance docs that someone probably forgot to write.

Also, each config option needs to have a `Monoid` instance that distinguishes between "this value hasn't been set" and "this value has been set to its default". In practice that means `Last`. But that means users don't know what the default value of any config option is.

So the actual code complexifies the implementation in a few ways, to help users. Instances have a way of specifying "these are the types I look up", as long as those types have the same `ConfigFor`. Then looking things up from the config happens automatically; and there's a separate function to set default values to what gets looked up, which users can call manually to see what's going on. Once we have the defaults we no longer need `Last`, so we change to `Identity` at that point.

We also use a custom monad class instead of `MonadReader GistContext`. For now it's no more powerful, but it would be easy to add a tracing function. Then if users had trouble figuring out what was going on, they could use that to help figure it out, with no additional work from implementers.

So the actual implementation looks more like

```haskell
class (Typeable a, Monoid (ConfigFor a Last), Typeable (ConfigFor a Last))
  => Configurable a
 where
  type ConfigFor a (f :: Type -> Type) :: Type

class (Configurable a, CanDoLookups (GistLookups a) (ConfigFor a Last))
  => Gist a
 where
  type GistLookups a
  reifyConfig :: ConfigFor a Last -> ConfigFor a Identity
  renderM :: MonadGist m => Int -> ConfigFor a Identity -> a -> m Doc

config :: Configurable a => Maybe PathMatcher -> ConfigFor a Last -> Config
```

where `CanDoLookups` roughly ensures that `GistLookups a` is a type-level list of things with a given `ConfigFor`. (But we can't use `'[]` for these type-level lists, because you can't put types of different kinds inside one of those.)

How does this fare? The big advantage over the previous solutions is the "configure every occurence of a type at once" thing. I anticipate this is usually what users want, so it's good that it's easy. Also, no nested records! And if I decide to add global config options - perhaps indent width - I just need to add them to `GistContext`.

I think the big downsides are that it's wildly complicated, and we've lost the ability to render anything we can't write a `Gist` instance for (which also means users can't override implementers' decisions). But also a bunch of other downsides. When you do want to render different occurrences of the same type differently, it's awkward. You won't get errors or warnings if your config gets out of sync with the type you're rendering. Encapsulation is tricky, internals of your types might be exposed in ways you don't want. It's not necessarily clear how you'd want newtypes to be configured, and newtype-deriving only gives you one option which might not be what you want.

<details markdown="1">
<summary>Implementation for <code>Maybe</code></summary>

```haskell
data ConfigMaybe f = ConfigMaybe { showConstructors :: f Bool }
  deriving stock Generic
instance Semigroup (ConfigMaybe Last) where
  a <> b = ConfigMaybe (showConstructors a <> showConstructors b)
instance Monoid (ConfigMaybe Last) where
  mempty = ConfigMaybe mempty

instance Configurable Maybe where
  type ConfigFor Maybe f = ConfigMaybe f
instance Typeable a => Configurable (Maybe a) where
  type ConfigFor (Maybe a) f = ConfigFor Maybe f

instance Gist a => Gist (Maybe a) where
  type GistLookups (Maybe a) = CL Maybe
  reifyConfig (ConfigMaybe {..}) =
    ConfigMaybe (Identity $ fromLast False showConstructors)
  renderM prec (ConfigMaybe {..}) = if runIdentity showConstructors
    then \case
      Nothing -> pure "Nothing"
      Just x  -> do
        renderedElem <- subGistPrec 11 Nothing x
        pure $ parensIfPrecGT 10 prec $ "Just" <+> renderedElem
    else \case
      Nothing -> pure "_"
      Just x  -> subGistPrec prec Nothing x

-- Renders "()".
gist [] $ Just ()

-- Renders "Just ()".
gist [configF @Maybe $ \c -> c { showConstructors = pure True }] $ Just ()

```

</details>

<details markdown="1">
<summary>Implementation for <code>GameState</code></summary>

```haskell
import qualified Gist
import           Gist ( Configurable(..), Gist(..), fromLast )
import qualified Gist as Gist.ConfigMaybe ( ConfigMaybe(..) )

deriving via Gist.Showily Player instance Configurable Player
deriving via Gist.Showily Player instance Gist Player

deriving via Gist.Showily PieceType instance Configurable PieceType
deriving via Gist.Showily PieceType instance Gist PieceType

-- We can't derive an instance `Configurable Board`. We have that `Board a` is
-- representation-equivalent to `[[a]]`, but `Board` itself isn't
-- representation-equivalent to anything. Anyway, even if we had an instance,
-- the instance we're deriving for `Gist (Board a)` wouldn't look at it.
deriving newtype instance Typeable a => Configurable (Board a)
deriving newtype instance Gist a => Gist (Board a)

data ConfigPiece f = ConfigPiece { singleChar :: f Bool }
  deriving stock Generic
instance Semigroup (ConfigPiece Last) where
  (ConfigPiece a1) <> (ConfigPiece a2) = ConfigPiece (a1 <> a2)
instance Monoid (ConfigPiece Last) where
  mempty = ConfigPiece mempty

instance Configurable Piece where
  type ConfigFor Piece f = ConfigPiece f

instance Gist Piece where
  type GistLookups Piece = ()
  reifyConfig (ConfigPiece a) = ConfigPiece (Identity $ fromLast False a)
  renderM prec (ConfigPiece {..}) piece@(Piece {..}) =
    if runIdentity singleChar
      then pure $ prettyPieceChar piece
      else Gist.record
        prec
        (Just "Piece")
        [ ("pieceType", Gist.subGist (Just "pieceType") pieceType)
        , ("owner"    , Gist.subGist (Just "owner") owner)
        , ("lastMoved", Gist.subGist (Just "lastMoved") lastMoved)
        ]

instance Configurable GameState where
  type ConfigFor GameState f = Proxy f

instance Gist GameState where
  type GistLookups GameState = ()
  reifyConfig _ = Proxy
  renderM prec _ (GameState {..}) =
    Gist.localPushConf
        (Gist.configF @Piece $ \c -> c { singleChar = pure True })
      $ Gist.record
          prec
          (Just "GameState")
          [ ("turn"     , Gist.subGist (Just "turn") turn)
          , ("pBlackWin", Gist.subGist (Just "pBlackWin") pBlackWin)
          , ("pWhiteWin", Gist.subGist (Just "pWhiteWin") pWhiteWin)
          , ("nMoves"   , Gist.subGist (Just "nMoves") nMoves)
          , ("board"    , Gist.subGist (Just "board") board)
          ]

-- Renders in short form.
gist [] startPos

-- Renders in long form. generic-lens could replace the record update, one of:
--     configF @Piece $ setField @"singleChar" $ pure False
--     configF @Piece $ field @"singleChar" .~ pure False
gist [Gist.configF @Piece $ \c -> c { singleChar = pure False }]
     startPos

-- Renders in fully explicit form. generic-lens would work here too, avoiding
-- the horrible import.
gist
  [ Gist.configF @Piece $ \c -> c { singleChar = pure False }
  , Gist.configF @Maybe
      $ \c -> c { Gist.ConfigMaybe.showConstructors = pure True }
  ]
  startPos
```

</details>

## Commentary

I've given three different renders for all of these `GameState` examples. "Short form" looks like the example I gave above, except I haven't configured the floats to show as percentages. (Like I said, not yet implemented.) "Fully explicit form" is similar to the pretty-simple rendering, except with a different indent style. And "long form" is in between, with abbreviated rendering for `Maybe` but everything else displayed in full - there's no ambiguity here, so it seems like a good choice even if you don't want any data missing.

In this particular case, rendering `GameState` for the classless and one-class solutions are about as verbose as each other. I think that's kind of a coincidence based on where the type variables are and what we're doing with them. For example, `GameState` has no type variables, so its renderers can be passed in `ConfigGameState`, letting them be defaulted. `Board` has a type variable, but `renderBoard` has no other config options; so there are no cases where with one-class we can say "change this option for how we render `Board`, but leave the sub-renderer alone", but with classless we can only say "change this option for how we render `Board`, and while we're at it here's the sub-renderer to use". This kind of thing does come up once, when in the fully-explicit form we want to set `showConstructors` on the `lastMoved` renderer, and have to also repeat the renderer for the `Int`. But in that case the renderer is just `gistShowily` so it doesn't hurt much.

I expect there'd be more difference in other cases. But maybe I'm wrong? Who knows.

A thing I dislike in all of them, is how I've had to do imports to handle record field updates. As of (I think) GHC 9.2, record updates combined with `DuplicateRecordFields` is [more awkward](https://www.reddit.com/r/haskell/comments/134c1kt/monthly_hask_anything_may_2023/jljjjhp/) than it used to be, at least if you don't want to get warnings about future compatibility. So when I do the awful

```haskell
import qualified Gist as Gist.ConfigMaybe ( ConfigMaybe(..) )
```

that's so I can do `val { Gist.ConfigMaybe.showConstructors = ... }` to update the field. Another option is to use [generic-lens](https://hackage.haskell.org/package/generic-lens) or [generic-optics](https://hackage.haskell.org/package/generic-optics) to do updates, which I've also demonstrated in some cases. My guess is that would be fine in a lot of application code, but many libraries won't want to depend on them.

I could also try to choose constructor names not to conflict. But I think that basically means prefixing them all, which would also be super verbose, and it would annoy users of the generic libraries.

(Given what I've implemented so far, the name conflicts only actually exist in the one-class solution, which reuses the name `gistElem`. But I expect `showConstructors` and `showFirst` to also get reused, e.g. for gisting `Either` and `Set`; and something like `countRemaining` could be useful for collections that get truncated, and so on. So it seemed more useful to write things this way.)

I haven't looked closely, but [anonymous records](https://hackage.haskell.org/package/large-anon-0.2/docs/Data-Record-Anon.html) might help here. They also might help with `Generic`-based defaulting, which is another thing I haven't looked into. But they seem like a large hammer that increases dependency footprints. And from a quick look I'm not sure they support type-changing record updates.

I'd prefer if there wasn't a single fixed indent style. But I'm not sure what to do about it. Conceivably, I could have a fixed `IndentStyle` type, and expect implementers to pay attention to it. (Similar to how precedence has been granted special status.) But I expect if I do that, there'll be situations where people wish the type was larger (because it doesn't support things they want), and others where they wish it was smaller (because implementing support for all the options is a pain). If I make it maximally small, we only have one of those problems. Similar thoughts on possible color support.

## Questions for you

One reason I wrote all this is to try to gauge enthusiasm. One possible future for pretty-gist is that I use it a small amount and in personal projects and at my job, and basically no one else uses it at all. That would be fine.

Another possible future is that it becomes a package that other people do use and that I take [responsibility](https://reasonableapproximation.net/2020/04/13/in-my-culture-responsibility-oss.html) for. But that's only going to happen if it seems like anyone cares.

So some things I'd like to know from readers:

* How cool do you think each version is?
* How likely are you to use each version?
* How annoyed would you be, for each version, if you felt obligated to implement support for it for a library you maintain or similar?
* Which version do you think is coolest / are you most likely to use / least likely to be annoyed by?
* Do you see ways to improve any of them without significant costs?
* Do any of them seem to have significant advantages or disadvantages I missed?
* What would you use them for?
* Can you think of other approaches to solving this problem that you think you might like better than any of these?

I have some opinions on these myself, but I'd prefer to wait and see what others say before revealing. I also have another possible approach vaguely in mind; but if I waited to explore it before publishing, then this would never get finished.

The canonical public place to leave comments is the reddit thread (link incoming). But I've also set up a [google form](https://forms.gle/wjW9dxr9r9qXmHLB8) you can fill in if you prefer.
