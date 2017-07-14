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

For that matter, sometimes I want to use currency in text, like $3 - $1. As you can see, that either does or doesn't work. Backslashes should definitely work: \$3 - \$1.
