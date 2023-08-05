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

<p>
*this shouldn't work*
</p>

<p>

*this should but seems not to*

</p>

<p markdown="1">

*this probably shouldn't but seems worth trying*

</p>

<table>
<tr>
<td>

*does this?*

</td>
</tr>
</table>

<table>
<tr>

<td>

*how about this?*

</td>

</tr>
</table>

[^1]: Like this
[^here]: And this
[^2]: And this
[^3]: Which should more-or-less work work even if

    the footnote has multiple paragraphs,
    and *formatting*, and so on.
