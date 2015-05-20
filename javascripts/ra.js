var disqus_shortname='reasonableapproximation';
$(function () {
    $('code').each(function () {
        var html = $(this).html().replace(/\n$/, '');
        if (html[0] == '$' && html[html.length-1] == '$') {
            $(this).html(html);
            $(this).addClass('do-math');

	    // MathJax and pygments interfere with each other, and the markdown
	    // interpreter wraps code blocks in a pygments div. This is a hacky
	    // way to remove pygment highlighting from mathjax.
	    if ($(this).parent().prop('tagName') == 'PRE'
		&& $(this).parent().parent().prop('tagName') == 'DIV')
	    {
		$(this).parent().parent().removeClass('highlight');
	    }
        }
        else {
            $(this).addClass('no-math');
        }
    });

    MathJax.Hub.Queue(['Typeset', MathJax.Hub]);

    // Add title text to footnotes. Very dependent on how the markdown compiler
    // handles them.
    $('a[rel=footnote]').each(function () {
        var text = $($(this).attr('href')).text();
        $(this).attr('title', text.slice(1, -3)); // strip whitespace and "↩"
    });
});
