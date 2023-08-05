---
layout: draft
title: Markdown testing page
---
I want footnotes[^1], including named footnotes[^here] to work[^2]. And they should have hover titles[^3].

Also, lists should work, ideally:

* Like this

* where I have two lines

* between bullets

and also

* like this
* with only one line
* between points

and the same for numbered lists:

1. two lines

2. two lines

3. two lines

and

1. one line
2. one line
3. one line

Blockquotes carry over between paragraphs. This is just one quote:

> one
>
> two

this is two:

> one

> two

Attempts at markdown in html:

<p markdown="1">
*this is how to do it using kramdown syntax*

Which [seems to be](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/setting-a-markdown-processor-for-your-github-pages-site-using-jekyll) the default
</p>

<p>

*if I switch to GFM*, this should work

</p>

<p>
*this shouldn't in either processor*
</p>

<div markdown="1">

*if it's split over multiple lines*

with surrounding whitespace

*they're paragraph broken again*

</div>

<table>
<tr>
<td markdown="1">
*in a table, it goes inside the td I think?*
</td>
</tr>
</table>

[^1]: Like this
[^here]: And this
[^2]: And this
[^3]: Which should more-or-less work work even if

    the footnote has multiple paragraphs,
    and *formatting*, and so on.
