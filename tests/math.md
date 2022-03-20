---
layout: draft
title: Math test page
---
Some things that I want to work include: math inline like $\sin(A)$, and inside backquotes like `$\sum_{n=1}^∞ a_n$`; also note the unicode in that one. And code blocks, like:

    $$ f(x) = x^3 - 2x^2 + 1. $$

Then I want equations to be numbered:

    $$ \begin{equation}
        f'(x) = 3x^2 - 4x
    \end{equation} $$

And if I include a label tag \eqref{testlabel}, I should be able to reference it both before...

    $$ \begin{equation}
        f''(x) = 6x - 4 \label{testlabel}
    \end{equation} $$

...and after (\ref{testlabel}).

But I don't want most code blocks to process math, so `$foo - $bar` should be clean, and so should

    $foo - $bar.

For that matter, sometimes I want to use currency in text, like $3 - $1. But that doesn't work. Backslashes work, but they need to be doubled up for markdown: \\$3 - \\$1.

And sometimes I want dollars in math. I need to use backquotes or code blocks for that. `$ $0 $` backslashes. `$ \$1 $` backslashes. `$ \\$2 $` backslashes. `$ \\\$3 $` backslashes.

And there's something funky going on with fractions after dollars? First, without a space. `$ ${0 \over 3} $` backslashes. `$ \${1 \over 3} $` backslashes. `$ \\${2 \over 3} $` backslashes. `$ \\\${3 \over 3} $` backslashes.

And now including a space. `$ $ {0 \over 3} $` backslashes. `$ \$ {1 \over 3} $` backslashes. `$ \\$ {2 \over 3} $` backslashes. `$ \\\$ {3 \over 3} $` backslashes.

And I want to be able to use `\(` and `\)` delimiters too. Inline needs some backslashes to be doubled like \\( \sin(A) \\). In code there's `\( \sin(A) \)`. And blocks:

    \[ f(x) = x^3 - 2x^2 + 1. \]

<p>
If I want to disable markdown without code blocks, e.g. to get consumed by LW, that seems impossible in only part of a line. But I can do it on a full line, like \( \sum_{n=1}^∞ a_n \). Or on a full block, like
</p>

<div>
\[ f(x) = \sin( x_1^3 - 2x_2^2 + 1 ). \]
</div>
