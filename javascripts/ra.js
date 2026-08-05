var disqus_shortname='reasonableapproximation';
$(function () {
    $('code').each(function () {
        var html = $(this).html().replace(/\n$/, '');
        var isMath =
            (html.startsWith('$') && html.endsWith('$'))
            || (html.startsWith('\\(') && html.endsWith('\\)'))
            || (html.startsWith('\\[') && html.endsWith('\\]'));
        if (isMath) {
            $(this).html(html);
            $(this).addClass('do-math');

            // MathJax and pygments interfere with each other, and the markdown
            // interpreter wraps code blocks in a pygments div. This is a hacky
            // way to remove pygment highlighting from mathjax.
            if ($(this).parent().prop('tagName') == 'PRE'
                && $(this).parent().parent().prop('tagName') == 'DIV')
            {
                // Both PRE and DIV have the class, we don't want either.
                $(this).parent().removeClass('highlight');
                $(this).parent().parent().removeClass('highlight');
            }
        }
        else {
            $(this).addClass('no-math');
        }
    });

    MathJax.Hub.Queue(['Typeset', MathJax.Hub]);

    // Add title text to footnotes. Very dependent on how the markdown compiler
    // handles them. If the same footnote is referenced multiple times, the
    // first is given a `↩` link, the second a `↩2` link, and presumably so on.
    $('a.footnote').each(function () {
        var id = $(this).attr('href').substr(1);
        var text = $('[id="' + id + '"]').text();
        text = $.trim(text.replace(/( ↩\d*)+\s*$/, ''));
        $(this).attr('title', text);
    });
});
