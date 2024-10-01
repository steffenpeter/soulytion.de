---
title: 'Simple TradeStation Strategy based on Planetary Indicators'
date: 2010-01-01
tags:
  - astro
  - planetaryindicators
  - tradestation
image: pi_trade_jan10.thumbnail.png
excerpt: 'PlanetaryIndicators can be used to create trading systems working on planetary data.'
---
<p>PlanetaryIndicators can be used to create trading systems working on planetary data.</p>
<p>For the beginning I show a simple one. In two weeks (Jan 24th) Sun will be Trine to Saturn. Visual investigation (with [PI] Planet Pair) showed that the event often comes with a temporary top in stock markets. So how can we verify the observation? I create a Trading System that enters a long position one week before the event, turns it the day before the Trine and closes the Short a week later.</p>
<p>The screen shot shows the setup and the result (click on the figure to zoom in).</p>
<p></p>
<p style="text-align: center">{% image "aspect_strat.png", "." %}</p>
<p><br/>
The applied strategy ([PI] PlanetPairStrat) is a general strategy for planet aspects. Just enter the aspect (in this case 3 for Sun and 6 for Saturn and 120 degrees) and the relative offset in days for the market action. For the buy rule the offset is -8 so we enter 7 days before the event (the enter rule is next bar at market).</p>
<p>[PI] PlanetPairStrat is not yet part of the PI package, but it can be downloaded here:<br/>
<a href="/wp-content/uploads/2010/01/pi_strategy1001.ZIP" title="pi_strategy1001.ZIP">pi_strategy1001.ZIP (4kB)<br/>
</a>(The PI package has to be installed.)</p>
<p>EDIT February:<br/>
This time the strategy was not so much a success: The BUY part had -37 Points and the SELL part had +8 Points. Maybe next time (Mid May)<br/>
<a href='{% image "pi_trade_jan10.png", "linkonly" %}' title="Trade Jan 2010, 120degree Earth/Saturn">{% image "pi_trade_jan10.png", "." %}</a></p>
