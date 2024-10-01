---
title: 'On the Compatibility of the Planetary Indicators to MultiCharts'
date: 2011-10-01
tags:
  - planetaryindicators
excerpt: 'The Plantary Indicators have been developed in Easy Language (EL) for Tradestation (TS) platforms. Multicharts (MC) is somewhat compatible to the EL intepretation of TS. And to the best of my knowledge they comile and run without errors on MC starting from version 6.'
---
<p>The Plantary Indicators have been developed in Easy Language (EL) for Tradestation (TS) platforms. Multicharts (MC) is somewhat compatible to the EL intepretation of TS. And to the best of my knowledge they comile and run without errors on MC starting from version 6.</p>
<p>However, one function that does not work for most indicators is the forward projection. That means when the indicators are applied to a chart the results are fine up to the last bar on the chart. But MC stops drawing there. As an example see the chart below: The planetary ingresses are shown correctly – but no information on the future.</p>
<p></p>
<p style="text-align: center"><a href="" title="PI ingresse multichart"></a></p>
<p>Â <span id="more-92"></span></p>
<p>ReasonÂ  is the different interpretation of the following code:</p>
<blockquote>
<blockquote><p>Â if lastbaronchart then begin<br/>
print (“last bar is “,d,t);<br/>
value89 = TL_new(d,t,c,d,t+1,c);<br/>
value53 = TL_GetEndDate(value89);<br/>
value54 = TL_GetEndTime(value89);<br/>
print (“first future bar is “,value53,value54);</p>
<p>tl_setend(value89, value53, value54+1, c);<br/>
value53 = TL_GetEndDate(value89);<br/>
value54 = TL_GetEndTime(value89);<br/>
print (“second future bar is “,value53,value54);</p>
<p>TL_delete(value89);<br/>
end;</p></blockquote>
</blockquote>
<p>While TS delivers the correct date for the following bars, MC just delivers some garbage. If someone knows a simple workaround that works on all time frames please let me know.</p>
