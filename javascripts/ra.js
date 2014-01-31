var disqus_shortname='reasonableapproximation';
$(function () {
    $('code').each(function () {
        var html = $(this).html().replace(/\n$/, '');
        if (html[0] == '$' && html[html.length-1] == '$')
            MathJax.Hub.Queue(['Typeset', MathJax.Hub, this]);

        // MathJax and pygments interfere with each other, and the markdown
        // interpreter wraps code blocks in a pygments div. This is a hacky way
        // to remove pygment highlighting from mathjax.
        if ($(this).parent().prop('tagName') == 'PRE'
            && $(this).parent().parent().prop('tagName') == 'DIV')
        {
            $(this).parent().parent().removeClass('highlight');
        }
    });
});
