---
title: Keeping Code and Docs in Sync
layout: draft
---
It's widely regarded that documentation is an important task that doesn't get as much attention as it deserves.

There are a lot of proposals for how to fix this, but I think they typcially miss something. "Write the documentation before the code", for example. Sounds good, but a lot of the time, until I write the code, I don't know what it's going to do. Maybe I have a rough idea, but the details are going to evolve. And sometimes I'm just going to get things wrong. *Oh, I can't frobnicate the spam here unless I also make the user pass in an egg* - this is the sort of detail that would be easy to miss when I'm thinking about a function, but impossible to miss when I'm trying to frobnicate the spam without an egg.

And of course, having written a function and documented it (in whatever order) - you can subsequently *rewrite* the function without *redocumenting* it. This is the well-known problem where the code and the docs get out of sync.

You can't have a rule "don't edit the code unless you first edit the documentation", because a lot of code edits don't need doc changes. A more complicated rule like "don't edit the code unless you first edit the documentation, unless the documentation doesn't change" would probably just be forgotten. After a while, whenever I ask myself if the documentation is going to change, I'm just going to return the cached answer "no" without thinking. In any case it has the same problem: I don't know what I'm going to change until I change it.

---

So here's my half-baked proposal that might help to solve some of the problem of keeping code in sync with documentation:

If your code is in a git (or other VCS) repository, you can look at a function and see whether the code changed more or less recently than the docstring. It would be possible to write a tool which searches for such functions automatically.

Bam, done. The rest is just details. Edit code all you want, and if you forget to update the docs, this tool will remind you next time you run it.

Okay, some details are important. Here are some things to think about:

* Not every code edit needs you to touch the docstring, so you want a database of some sort, which can be used to mark "the docstring is up to date as of commit A, even though it hasn't been touched since commit B". Keep this database inside your repository. This is probably quite a large detail, with many details of its own.

  It might actually be better (certainly simpler) to have some way of marking this in-file. For example, in python:

  ```python
  def foo(bar):
     """Do a thing
     """ # 2014-01-07 11:25 (edit this comment to mark the docs up to date)
     pass
  ```

* Tracking a function across revision changes is probably really hard, in general. In the specific case of "the sort of revision changes that actually occur in real codebases", it might be possible most of the time.

  ((I would start by working out which lines constitute a function's code and docstring, and running `git blame` to see which was updated most recently. This might be good enough, but for example it breaks if you swap the order of two functions in the source file. One of them is going to be blamed entirely on that commit. It also breaks if you delete lines from the function body.

  A more complicated solution would be to track the function by its identifier. Look at past revisions of the file in its entirety, search for the function, and see whether it's changed. This could go wrong in *so many* ways, and even if it doesn't, it still won't catch you if you move a function from one file to another.))

* This probably works best if you run it frequently. You could have it in a hook: if there are unsynced changes, you aren't allowed to push unless you sync them (either by editing the docs, or marking them clean).

* This could be applied to classes as well as functions, but I'm not sure when you'd want to flag them. Most changes to code inside a method probably won't touch the class docstring, even if they touch the method docstring. Applying it to whole files would be even harder. In general, this will apply better to low-level documentation than high-level.

* You need custom support for each language and documentation style used, as well as for each VCS. In many cases, supporting a language will mean writing a parser for it. (In python, you can import a module and discover every class and function that it exposes, and their docstrings, but I don't know if you can find their source locations like that.)

---

Would this work? How much effort would it be to make? Would it be helpful, assuming it did work? For that matter, does something like it already exist?
