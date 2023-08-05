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

Blockquotes ideally should carry over between paragraphs, but I don't think that's possible with kramdown. What I want:

> one
>
> two

what I get:

> one

> two

I think this needs to be fixed in my posts, as long as I'm stuck with kramdown.

Attempts at markdown in html:

<div>
*this shouldn't work*
</div>

<div>

*this should*

</div>

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
