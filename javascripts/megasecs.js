// This creates a simple widget to calculate the time between two dates in units
// of a hundred megaseconds. Use by inserting `<script src="..."></script>` at
// the point in the document where the widget should appear. It probably won't
// work if you try to load it asynchronously.

(function () {
    function fmtDate(d, opts) {
        return d.toLocaleString('en-US', opts);
    }
    function twoDigit(n) {
        return n.toLocaleString('en-US', {minimumIntegerDigits: 2});
    }

    function prettyDate (d, precise) {
        var dPart = (
            fmtDate(d, {weekday: 'short'})
                + ', '
                + fmtDate(d, {month: 'short'})
                + ' '
                + fmtDate(d, {day: '2-digit'})
                + ' '
                + fmtDate(d, {year: 'numeric'})
        );
        if (!precise)
            return dPart;

        var tPart =
            fmtDate(d, {hour: '2-digit', minute: '2-digit', second: '2-digit',
                        hourCycle: 'h23', timeZoneName: 'short'});
        return dPart + ' ' + tPart;
    }

    function secsToHMS (secs) {
        // Format the time by getting a date which has it as the time part.
        // Assumes the seconds are fewer than one day.
        var midnight = Date.UTC(2000, 0, 1);
        return fmtDate(new Date(+midnight + secs * 1000),
                       {hour: '2-digit', minute: '2-digit', second: '2-digit',
                        hourCycle: 'h23', timeZone: 'UTC'});
    }

    function yearsAndDaysBetween(startDate_, endDate_) {
        // Calculate the number of years-and-days between two dates.
        var startDate = startDate_ < endDate_ ? startDate_ : endDate_;
        var endDate = startDate_ < endDate_ ? endDate_ : startDate_;

        var nYears = endDate.getFullYear() - startDate.getFullYear();
        var startDateThatYear = new Date(startDate);
        startDateThatYear.setFullYear(endDate.getFullYear());

        if (startDateThatYear > endDate) {
            nYears--;
            startDateThatYear.setFullYear(endDate.getFullYear() - 1);
        }

        return { years: nYears,
                 days: Math.floor((endDate - startDateThatYear)
                                  / (86400 * 1000)) };
    }

    function createInput (value, placeholder, minLength, maxLength, width) {
        var inp = document.createElement('input');
        inp.placeholder = placeholder;
        inp.minLength = minLength;
        inp.maxLength = maxLength;
        inp.pattern = '[0-9]{' + minLength + ',' + maxLength + '}';
        inp.style.width = width;
        inp.style.textAlign = 'center';
        inp.oninput = updateOutput;
        inp.value = value;
        return inp;
    }
    function createSimpleElement (tagName, textContent) {
        var elt = document.createElement(tagName);
        elt.appendChild(document.createTextNode(textContent));
        return elt;
    }

    var now = new Date()
    var startDateInputs = {
        y: createInput('', 'YYYY', 4, 4, '4em'),
        m: createInput('', 'MM', 1, 2, '3em'),
        d: createInput('', 'DD', 1, 2, '3em')
    };
    var endDateInputs = {
        y: createInput(fmtDate(now, {year: 'numeric'}), 'YYYY', 4, 4, '4em'),
        m: createInput(fmtDate(now, {month: '2-digit'}), 'MM', 1, 2, '3em'),
        d: createInput(fmtDate(now, {day: '2-digit'}), 'DD', 1, 2, '3em')
    };

    var startTimeInputs = {
        h: createInput('00', 'HH', 1, 2, '3em'),
        m: createInput('00', 'MM', 1, 2, '3em'),
        s: createInput('00', 'SS', 1, 2, '3em')
    }
    var endTimeInputs = {
        // toLocaleString doesn't work with 2-digit for minutes and seconds.
        // Firefox and chrome both buggy. Hours seem to work, but needs
        // hourCycle too. This way is fine.
        h: createInput(twoDigit(now.getHours()), 'HH', 1, 2, '3em'),
        m: createInput(twoDigit(now.getMinutes()), 'MM', 1, 2, '3em'),
        s: createInput(twoDigit(now.getSeconds()), 'SS', 1, 2, '3em')
    }

    var container = document.createElement('div');
    var inputCont = document.createElement('div');
    var outputCont = document.createElement('p');

    function createDateCont(inputs, name) {
        var dateCont = document.createElement('div');
        dateCont.appendChild(inputs.y);
        dateCont.appendChild(document.createTextNode('-'));
        dateCont.appendChild(inputs.m);
        dateCont.appendChild(document.createTextNode('-'));
        dateCont.appendChild(inputs.d);
        dateCont.appendChild(createSimpleElement('i', ' ' + name + ' date'));
        return dateCont;
    }
    var startDateCont = createDateCont(startDateInputs, 'start')
    var endDateCont = createDateCont(endDateInputs, 'end')

    function createTimeCont(inputs, name) {
        var timeCont = document.createElement('div');
        timeCont.style.display = 'none';
        timeCont.appendChild(inputs.h);
        timeCont.appendChild(document.createTextNode(':'));
        timeCont.appendChild(inputs.m);
        timeCont.appendChild(document.createTextNode(':'));
        timeCont.appendChild(inputs.s);
        timeCont.appendChild(createSimpleElement('i', ' ' + name + ' time'));
        return timeCont;
    }
    var startTimeCont = createTimeCont(startTimeInputs, 'start');
    var endTimeCont = createTimeCont(endTimeInputs, 'end');

    inputCont.appendChild(startDateCont);
    inputCont.appendChild(startTimeCont);
    inputCont.appendChild(endDateCont);
    inputCont.appendChild(endTimeCont);

    var precisionLabel = document.createElement('label');
    var precision = document.createElement('input');
    precision.type = 'checkbox';
    precision.onchange = updateOutput;
    precisionLabel.appendChild(precision);
    precisionLabel.appendChild(document.createTextNode(' precision mode'));
    inputCont.appendChild(document.createElement('br'));
    inputCont.appendChild(precisionLabel);

    container.appendChild(inputCont);
    container.appendChild(outputCont);
    // This will be the currently running script, if it wasn't loaded async.
    var thisScript = document.scripts[document.scripts.length - 1];
    thisScript.parentElement.insertBefore(container, thisScript);

    function updateOutput () {
        startTimeCont.style.display = precision.checked ? 'block' : 'none';
        endTimeCont.style.display = precision.checked ? 'block' : 'none';

        var startDateNums = {
            y: +(startDateInputs.y.value || NaN),
            m: +(startDateInputs.m.value || NaN) - 1,
            d: +(startDateInputs.d.value || NaN)
        }
        var endDateNums = {
            y: +(endDateInputs.y.value || NaN),
            m: +(endDateInputs.m.value || NaN) - 1,
            d: +(endDateInputs.d.value || NaN)
        }

        var nullTime = { h: 0, m: 0, s: 0 };
        var startTimeNums = precision.checked ? {
            h: +(startTimeInputs.h.value || NaN),
            m: +(startTimeInputs.m.value || NaN),
            s: +(startTimeInputs.s.value || NaN)
        } : nullTime;
        var endTimeNums = precision.checked ? {
            h: +(endTimeInputs.h.value || NaN),
            m: +(endTimeInputs.m.value || NaN),
            s: +(endTimeInputs.s.value || NaN)
        } : nullTime;

        if ([startDateNums.y, startDateNums.m, startDateNums.d,
             endDateNums.y, endDateNums.m, endDateNums.d,
             startTimeNums.h, startTimeNums.m, startTimeNums.s,
             endTimeNums.h, endTimeNums.m, endTimeNums.s
            ].find(isNaN) !== undefined)
        {
            return;
        }

        function mkDate(d, t) {
            return new Date(d.y, d.m, d.d, t.h, t.m, t.s);
        }
        var startDate = mkDate(startDateNums, startTimeNums);
        var endDate = mkDate(endDateNums, endTimeNums);

        var oneMSec = 1000 * 1000 * 1000; // one megasec in millisecs
        var diffMSecs = Math.trunc((endDate - startDate) / oneMSec);
        var diffHMSecs = diffMSecs / 100;

        var prevHMSecs =
            new Date(+startDate + Math.floor(diffHMSecs) * oneMSec * 100);
        var nextHMSecs =
            new Date(+startDate + Math.floor(diffHMSecs + 1) * oneMSec * 100);

        var precisionDetail = '';
        if (precision.checked) {
            var diffSecs = Math.floor((endDate - startDate) / 1000);
            var diffDays = Math.floor(Math.abs(diffSecs) / 86400);
            var diffSecsRem = Math.abs(diffSecs) % 86400;
            var yearsAndDays = yearsAndDaysBetween(startDate, endDate);

            precisionDetail = (
                'To be precise, <b>'
                    + diffSecs.toLocaleString('en-US')
                    + "</b> seconds.<br>That's <b>"
                    + diffDays.toLocaleString('en-US')
                    + '</b> days (<b>'
                    + yearsAndDays.years
                    + '</b> years, <b>'
                    + yearsAndDays.days
                    + '</b> days), and <b>'
                    + secsToHMS(diffSecsRem)
                    + '</b>.<br>'
            );
        }

        outputCont.innerHTML = (
            'Between <b>'
                + prettyDate(startDate, precision.checked)
                + '</b> and <b>'
                + prettyDate(endDate, precision.checked)
                + '</b>,<br>there are <b>'
                + diffHMSecs.toLocaleString('en-US',
                                            { minimumFractionDigits: 2 })
                + '</b> hundred megaseconds.<br>'
                + precisionDetail
                + '<b>'
                + Math.floor(diffHMSecs)
                + '</b> hundred megaseconds passed on <b>'
                + prettyDate(prevHMSecs, precision.checked)
                + '</b>.<br><b>'
                + Math.floor(diffHMSecs + 1)
                + '</b> hundred megaseconds will pass on <b>'
                + prettyDate(nextHMSecs, precision.checked)
                + '</b>.<br>'
        );
    }
})();
