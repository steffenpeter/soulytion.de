---
title: 'Commitment of Traders: Implications of Large Traders going short'
date: 2012-03-01
tags:
  - research
image: cot_120325.thumbnail.png
excerpt: 'Beside the various timing indicators presented on this page, I particularly have an eye on instruments describing the sentiment in the markets. One free and good source for sentiment data is the weekly Commitments of Traders report issued by the Commodity Futures Trading Commission. For several future markets it enumerates the positions of market participants grouped in Small, Large, and Commercial traders.
Frequently, two general approaches are proposed how to use the data:
1. look at the posit'
---
<p>Beside the various timing indicators presented on this page, I particularly have an eye on instruments describing the sentiment in the markets. One free and good source for sentiment data is the weekly Commitments of Traders report issued by the Commodity Futures Trading Commission. For several future markets it enumerates the positions of market participants grouped in Small, Large, and Commercial traders.<br/>
Frequently, two general approaches are proposed how to use the data:<br/>
1. look at the positions of the Commercial traders – assuming they are right<br/>
2. look at the positions of the Small traders – assuming they are wrong<br/>
That may (actually does) work for specific commodities. For stock markets, however, monitoring the position changes of the large trades seems to be a more promising approach.</p>
<p>The following chart shows the S&amp;P500 and the combined position sizes for large traders (yellow) , small traders (blue), and commercials (red).</p>
<p></p>
<p style="text-align: center"><a href='{% image "cot_120325.png", "linkonly" %}' title="cot_120325.png">{% image "cot_120325.png", "." %}</a></p>
<p>Most interesting in the chart is the second sub chart. It shows the deviation of recent activity from the normal behavior of the last half year. In this week the large traders entered many short positions so that the zscore is smaller than -2. As you can see in the chart, such readings usually come with important lows in the market. Highlighted are the low in 2010 and September 2011.</p>
<p>So, one can assume that large traders betting against the market is a good time to enter long positions. To validate this notion I wrote a small trading system, entering a long position on the Monday after the COT data is published, and exiting three weeks later.</p>
<p>The result shows that in the last 13 years we had 14 events. From these 14 trades 10 are winner and 4 lose (profit factor 3). Adding a rule only to enter in an down trend significantly improved the result. Then 10 trades remain: 9 winner and 1 lose (profit factor 12). The 4 remaining trades in a up trend (as we have it right now) only brought one winner.</p>
<p>Conclusions: Large traders exiting the market in a down trend is a strong indication for some sort of sell off, and thus it is a good time to go long. In an up trend, however, it rather indicates missing confidence in the uptrend – without delivering a true trading signal.</p>
<p>Note: One week ago the March futures expired. COT data is always a bit shuffled after future expiration. Spikes in that week have to be taken with care. Anyway,interesting in this context is the behavior of the market around these witching days.</p>
<p>The following chart shows the dates for last year</p>
<p></p>
<p style="text-align: center"><a href='{% image "expiration.png", "linkonly" %}' title="expiration.png">{% image "expiration.png", "." %}</a></p>
