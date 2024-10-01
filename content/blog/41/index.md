---
title: 'New Version of astro lib for TradeStation'
date: 2009-03-01
tags:
  - tradestation
  - astro
image: astro0903.thumbnail.png
excerpt: 'With this post I present a new version of the astro library for TradeStation. The new version allows to compute so many cool things around the planets, with much higher precision than previous version.'
---

<p>With this post I present a new version of the astro library for TradeStation. The new version allows to compute so many cool things around the planets, with much higher precision than previous version.</p>
<p>I also updated the indicators for Ephemeris and Bradley.</p>
<p>Most important changes (beside some fixes):</p>
<p>[SOULY] Ephemeris:<br/>
onexone is now called multiplier. It still determines the vertical scaling - but now it has an additional setting 0 (default) that is an auto-scale.<br/>
added option for sidereal geocentric computation (relative to vernal point). Some background info here: <a href="http://www.lunarplanner.com/siderealastrology.html">here</a></p>
<p>[SOULY] Bradley<br/>
now in an extra window<br/>
if applied to the calendar symbol (see <a href="/archives/35">previous post</a> ) you can study the Bradley from 1995 to 2010.</p>
<p>The new version including all required files can be downloaded from:<br/>
<a href="/upload/astro090319.zip" title="Astro Package for TradeStation Mar/09">Astro Package for TradeStation Mar/09 (ZIP, 2.2MB)</a><br/>
Copy embedded dll to your windows\system32 directory (there are alternatives, but that’s the easy way) and import both ELS-files in Tradestation. It’s tested with TS8 and TS2000i</p>
<p>The screen below shows the dow jones with ephemeris plots (geocentric and sidereal enabled, default multiplier), and the default geocentric Bradley. I applied ephemeris to the $DJI and the Bradley to CALENDAR (invisible DATA1).<br/>
</p>
<p style="text-align: center">{% image "astro0903.png", "." %}</p>
<p></p>
