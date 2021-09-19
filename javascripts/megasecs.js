// This creates a simple widget to calculate the time between two dates in units
// of a hundred megaseconds. Use by inserting `<script src="..."></script>` at
// the point in the document where the widget should appear.

(function () {
    function formatDate (d) {
        return (
            d.toLocaleDateString('en-US', {weekday: 'short'})
                + ', '
                + d.toLocaleDateString('en-US', {month: 'short'})
                + ' '
                + d.toLocaleDateString('en-US', {day: '2-digit'})
                + ' '
                + d.toLocaleDateString('en-US', {year: 'numeric'})
        );
    }
    function createInput (placeholder, minLength, maxLength, width) {
        var inp = document.createElement('input');
        inp.placeholder = placeholder;
        inp.minLength = minLength;
        inp.maxLength = maxLength;
        inp.pattern = '[0-9]{' + minLength + ',' + maxLength + '}';
        inp.style.width = width;
        inp.style.textAlign = 'center';
        inp.oninput = updateOutput;
        return inp;
    }

    var startYearsInput = createInput('YYYY', 4, 4, '4em');
    var startMonthsInput = createInput('MM', 1, 2, '3em');
    var startDaysInput = createInput('DD', 1, 2, '3em');
    var endYearsInput = createInput('YYYY', 4, 4, '4em');
    var endMonthsInput = createInput('MM', 1, 2, '3em');
    var endDaysInput = createInput('DD', 1, 2, '3em');

    today = new Date();
    endYearsInput.value = today.getFullYear();
    endMonthsInput.value = today.getMonth() + 1;
    endDaysInput.value = today.getDate();

    var container = document.createElement('div');
    var inputCont = document.createElement('div');
    var outputCont = document.createElement('p');

    inputCont.appendChild(startYearsInput);
    inputCont.appendChild(document.createTextNode('-'));
    inputCont.appendChild(startMonthsInput);
    inputCont.appendChild(document.createTextNode('-'));
    inputCont.appendChild(startDaysInput);

    var startText = document.createElement('i');
    startText.appendChild(document.createTextNode(' start date'));
    inputCont.appendChild(startText);

    inputCont.appendChild(document.createElement('br'));
    inputCont.appendChild(endYearsInput);
    inputCont.appendChild(document.createTextNode('-'));
    inputCont.appendChild(endMonthsInput);
    inputCont.appendChild(document.createTextNode('-'));
    inputCont.appendChild(endDaysInput);

    var endText = document.createElement('i');
    endText.appendChild(document.createTextNode(' end date'));
    inputCont.appendChild(endText);

    container.appendChild(inputCont);
    container.appendChild(outputCont);
    document.body.appendChild(container);

    function updateOutput () {
        var startYearsNum = +(startYearsInput.value || NaN);
        var startMonthsNum = +(startMonthsInput.value || NaN) - 1;
        var startDaysNum = +(startDaysInput.value || NaN);
        var endYearsNum = +(endYearsInput.value || NaN);
        var endMonthsNum = +(endMonthsInput.value || NaN) - 1;
        var endDaysNum = +(endDaysInput.value || NaN);

        if (isNaN(startYearsNum)
            || isNaN(startMonthsNum)
            || isNaN(startDaysNum)
            || isNaN(endYearsNum)
            || isNaN(endMonthsNum)
            || isNaN(endDaysNum))
        {
            return;
        }

        var startDate = new Date(startYearsNum, startMonthsNum, startDaysNum);
        var endDate = new Date(endYearsNum, endMonthsNum, endDaysNum);

        var oneMSec = 1 * 1000 * 1000 * 1000; // it's in milliseconds
        var diffMSecs = Math.floor((endDate - startDate) / oneMSec);
        var diffHMSecs = diffMSecs / 100;

        var prevHMSecs =
            new Date(+startDate + Math.floor(diffHMSecs) * oneMSec * 100);
        var nextHMSecs =
            new Date(+startDate + Math.floor(diffHMSecs + 1) * oneMSec * 100);

        outputCont.innerHTML = (
            'Between <b>'
                + formatDate(startDate)
                + '</b> and <b>'
                + formatDate(endDate)
                + '</b>,<br>there are <b>'
                + diffHMSecs.toLocaleString('en-US',
                                            { minimumFractionDigits: 2 })
                + '</b> hundred megaseconds.<br>'
                + Math.floor(diffHMSecs)
                + ' hundred megaseconds passed on <b>'
                + formatDate(prevHMSecs)
                + '</b>.<br>'
                + Math.floor(diffHMSecs + 1)
                + ' hundred megaseconds will pass on <b>'
                + formatDate(nextHMSecs)
                + '</b>.<br>'
        );
    }
})();
