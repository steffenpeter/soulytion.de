---
title: 'Tradestation indicator for Delta Phenomenon'
date: 2009-08-01
tags:
  - tradestation
image: delta_dji0908.thumbnail.png
excerpt: 'In â€œThe Delta Phenomenonâ€ Welles Wilder described something he believes is the â€œhidden order in all marketsâ€.Â  Now 26 years later the idea has been published in a lot of books and papers, and is no secret anymoreBasically the idea is that market vibration repeats'
---
<p>In â€œThe Delta Phenomenonâ€ Welles Wilder described something he believes is the â€œhidden order in all marketsâ€.<span>Â  </span>Now 26 years later the idea has been published in a lot of books and papers, and is no secret anymoreBasically the idea is that market vibration repeats</p>
<p>– Every 4 days (Short Term Delta),<br/>
– Every 4 lunar months (itâ€™s called Intermediate Term Delta â€“ I call it IMT)<br/>
– Every 12 lunar months (Medium Term Delta – MTD)<br/>
– Every 4 years (Long Term Delta – LTD)<br/>
– Every 19 years (Super Long Term Delta)</p>
<p>Each period consists of a well-defined -but market specific- series. A series are usually 10 to 14 points that define times for highs and lows. Highs and lows alternate strictly, but in a special time window once in the period (Inversion Time window). In this window inversions are allowed â€“ with all the implications for the rest of the cycle, because after the window the market is supposed to rotate strictly again until the next ITW. Once a series for a market is found, it can be applied until the end of all times â€“ at least thatâ€™s the notion.</p>
<p>Ok, so I made an indicator implementing the simple framework for IMT and MTD for now. The indicator can be downloaded <a href="/wp-content/uploads/2009/08/s09_delta.eld" title="Delta Indicator for Tradestation">here (Delta Indicator for Tradestation 8.x)</a>. The imported indicator is [S09] Delta.</p>
<p>The indicator draws dashed lines for each full moon. I saw it in some publications that the first moon in the series is colored red, the second blue, the third orange and the fourth is green â€“ so I use the coding here as well. The dashed line series is the IMT-sequence. Each third full moon is partially a solid line. That is one of the four anchor points of the IMT-cycle. Here I use the same color code. The first in the series is red.</p>
<p>Starting from the red anchors IMT counts the days and marks the days listed in the input â€œMarkDaysAfterRedMoonâ€. These marked days are counted subsequently starting from 1. Following the rotation rule, a high is followed by a low and a low is followed by a high. On the next red moon they start again from 1 â€“ and they rotate until the end of all times. Then all additionally needed are inversions. Currently the indicator does not care for ITW. You can invert whenever you want. To make it easier you just define additional highs and lows (using inputs IMT.High.Dates and IMT.Low.Dates). So for example you think there is an inversion (double high) early June 2009, then add the date 1090601 to the IMT.Low.Dates-List. Then the next point in the series following the date will be forced to be a high. After that it will continue with alternation. For MTD itâ€™s basically the same. The only difference is that for definition of the series you donâ€™t need to count days, but weeks.</p>
<p>In the chart, IMT points are marked with small white dashed lines. The MTD points are yellow horizontal lines over two weeks. It allows fast and easy testing of the “Phenomenon”.<br/>
The picture shows the default settings in todays DJI chart.<br/>
<a href='{% image "delta_dji0908.png", "linkonly" %}' title="My Delta for Dow Jones, August 2009">{% image "delta_dji0908.png", "." %}</a></p>
<p>I think the default settings work fine for most stock markets. If you have better parameters for some markets, it would be great you leave a comment.</p>
