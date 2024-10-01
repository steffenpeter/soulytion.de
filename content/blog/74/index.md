---
title: 'Easy Language Programming Interface for Planetary Data'
date: 2000-01-01
tags:
  - planetaryindicators
  - tradestation
excerpt: 'The ephemeris data as it is basis for the planetary indicators can be accessed directly within any Easy Language code. The interface is the function named $pi_ephem. It is part of the planetaryindicators package and can be used for Indicators, Signals, or Strategies.'
---
<p>The ephemeris data as it is basis for the planetary indicators can be accessed directly within any Easy Language code. The interface is the function named <strong>$pi_ephem</strong>. It is part of the <a href="/archives/category/planetaryindicators/">planetaryindicators package </a>and can be used for Indicators, Signals, or Strategies.</p>
<p><strong>$pi_ephem</strong> provides geocentric and heliocentric data for planetary longitude, latitude, declination (only geocentric) and distance.</p>
<p>Syntax of the function is:</p>
<p><strong><span style="font-family: 'Courier New'">$pi_ephem (</span></strong><span style="font-family: 'Courier New'"><span> </span>planet (numeric),</span><span style="font-family: 'Courier New'"><span> </span>date (numeric),</span><span style="font-family: 'Courier New'"><span> </span>time (numeric),</span><span style="font-family: 'Courier New'"><span> </span>type (numeric),</span><span style="font-family: 'Courier New'"><span> </span>heliocentric (truefalse),</span><span style="font-family: 'Courier New'"><span> </span>sidereal (truefalse),</span><span style="font-family: 'Courier New'"><span> </span>timeZone(string))</span><span style="font-family: 'Courier New'"> </span></p>
<p><strong><span style="color: red">Parameters:</span></strong></p>
<p><span id="more-74"></span></p>
<p><strong><span style="color: red"></span></strong><strong><span style="font-family: 'Courier New'">Planet</span></strong> is the number of the planet (or element) for which the data is requested. It is recommended to use following constants:</p>
<p><span style="font-family: 'Courier New'">vars: </span><span style="font-family: 'Courier New'">P_SUN(3),</span><span style="font-family: 'Courier New'">P_MOON(0),</span><span style="font-family: 'Courier New'">P_MERCURY(1),</span><span style="font-family: 'Courier New'">P_VENUS(2),</span><span style="font-family: 'Courier New'">P_EARTH(3),</span><span style="font-family: 'Courier New'">P_MARS(4),</span><span style="font-family: 'Courier New'">P_JUPITER(5),</span><span style="font-family: 'Courier New'">P_SATURN(6),</span><span style="font-family: 'Courier New'">P_URANUS(7),</span><span style="font-family: 'Courier New'">P_NEPTUNE(8),</span><span style="font-family: 'Courier New'">P_PLUTO(9),</span><span style="font-family: 'Courier New'">P_NNODE(10),</span><span style="font-family: 'Courier New'">P_SNODE(11);</span><span style="font-family: 'Courier New'"> </span></p>
<p><span style="font-family: 'Courier New'"></span><strong><span style="font-family: 'Courier New'">Date</span></strong> and <strong><span style="font-family: 'Courier New'">Time</span></strong> are date and time (in normal EL format) of the requested data.</p>
<p><strong><span style="font-family: 'Courier New'">Type</span></strong> is an integer that defines the type (planetary longitude, latitude, declination or distance) of the requested item. The following constants apply:</p>
<p><span style="font-family: 'Courier New'">Vars: </span><span style="font-family: 'Courier New'">D_LONGITUDE(0),</span><span style="font-family: 'Courier New'">D_LATITUDE(1),</span><span style="font-family: 'Courier New'">D_DECLINATION(2),</span><span style="font-family: 'Courier New'">D_DISTANCE(3);</span></p>
<p><span style="font-family: 'Courier New'"></span><strong><span style="font-family: 'Courier New'">heliocentric</span></strong> has to be true if heliocentric data is required. For geocentric data the parameter has to be false</p>
<p><strong><span style="font-family: 'Courier New'">sidereal</span></strong> has to be true if sidereal coordinates of the geocentric longitude are required.</p>
<p><strong><span style="font-family: 'Courier New'">Timezone</span></strong> is a string that defines the timezone of the chart. It should be either the time zone in hours (e.g. â€œ+5â€, â€œ-2â€) of the market relative to Greenwich, or â€œautoâ€ if market time and computer system time are the same. If â€œautoâ€ is set the function will automatically use the time zone of the computer.</p>
<p><strong><span style="color: red"></span></strong></p>
<p><strong><span style="color: red">Return:</span></strong></p>
<p><strong><span style="color: red"></span></strong>The requested value as floating point number. Based on the requested type the return value is:</p>
<p>D_LONGITUDE: the position of the selected planet in degrees (0-360) as seen from Sun (heliocentric) or Earth (geocentric)</p>
<p>D_LATITUDE: latitude of the selected planet degrees as seen from Sun (heliocentric) or Earth (geocentric)</p>
<p>D_DECLINATION: declination of the selected planet in degrees to the Earth Equator</p>
<p>D_DISTANCE: distance of the selected planet in AUs (astronomic unit) to Sun (heliocentric) or Earth (geocentric)</p>
<p><strong><span style="color: red"></span></strong></p>
<p><strong><span style="color: red">Example:</span></strong></p>
<p><strong><span style="color: red"></span></strong>Plot geocentric longitude of Mars:</p>
<p><span style="font-family: 'Courier New'">Plot1 ($pi_ephem(P_MARS, d, t, D_LONGITUDE, false, false, â€œautoâ€));</span><span style="font-family: 'Courier New'"> </span></p>
<p><span style="font-family: 'Courier New'"></span><span style="font-family: 'Courier New'"></span><br/>
Plot Distance of Jupiter to the Sun:</p>
<p><span style="font-family: 'Courier New'"></span><span style="font-family: 'Courier New'">Plot2 ($pi_ephem(P_JUPITER, d, t, D_DISTANCE, true, false, â€œautoâ€));</span><span style="font-family: 'Courier New'"> </span></p>
<p><span style="font-family: 'Courier New'"></span></p>
<p>Please check the Indicator [PI] Sample (also part of the PI package) for a practical example.</p>
