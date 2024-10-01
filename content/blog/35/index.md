---
title: 'How to add future dates and gaps for weekends, holidays in TradeStation'
date: 2009-03-01
tags:
  - tradestation
excerpt: 'One problem I’ve always had is that TS can perfectly show data and indications for everything what happened in history, but there is no convenient way to show predictions in the future. This is particulary annoying if it’s about astro-indications.'
---

<p>One problem I’ve always had is that TS can perfectly show data and indications for everything what happened in history, but there is no convenient way to show predictions in the future. This is particulary annoying if it’s about astro-indications.</p>
<p>Ok, now I found a way to extend the time axis of TS so that it can process data for weekends (yes, planets eevn move on weekends) and holidays - and even for the future.</p>
<p>The basic idea is to add an instrument that� contains a data entry for every day. So all needed is a csv-file that looks like that:</p>
<p>1980-01-01,1,<br/>
1980-01-02,1,<br/>
1980-01-03,1,<br/>
…</p>
<p>Such a filewith data from 1980 to 2020� can be downloaded here: <a href="/wp-content/uploads/2009/03/calendar.zip" title="calender.zip">calendar.zip</a></p>
<p>Just extract the zip, add corresponding directory to the 3rd party data in TS.</p>
<p>Then add the symbol (CALENDAR) as first symbol to a new chart. Add the actual symbol ($DJI or $INX or whatever) as second symbol, and finally add some days or years to the data range (set last date).</p>
<p>Here is a small tutorial video - hope it helps…</p>
<p>tutorial video (flash): <a href="/wp-content/uploads/2009/03/calendar.swf" title="calendar.swf">calendar.swf</a></p>
