
Download
--------

[Calgary Election Results Parser][dload] -- 27 Sept. 2013
[dload]: https://github.com/lucastimmons/Calgary-Election-Results-to-JSON/archive/master.zip


Introduction
------------

Calgary Election Results Parser is a simple python script to turn the City of Calgary's awful "pipe delimited" results to useable JSON.

Data format
-----------

The remaining records in the file will contain the following data:

WARD|ACCLAIMED| INCUMBENT |CANDIDATE NAME|TOTAL VOTES|LEADING BY|PERCENTAGE OF VOTES|WARD STATIONS REPORTING|TOTAL WARD STATIONS |CITY WIDE STATIONS REPORTING|TOTAL CITY WIDE STATIONS |OFFICE TYPE

Here's the actual output example:

0|||Allen, Floyd D.|0||0|0|392|0|9|1

0|||Bell, Rick (The Dinger)|0||0|0|392|0|9|1

0|||Clark, Ray|0||0|0|392|0|9|1

0|Acclaimed|Incumbant|Duerr, Al|1000|200|10|6|392|2|9|1

0|Incumbent||Jamroziak, "Yaz" Jerzyk|0||0|0|392|0|9|1

The data file will be pipe delimited (1/2).
The first record in the file will contain the date and time.
Date format will be YYYY/MM/DD. Time format will be HH:MM:SS. (24 hour clock), for example: 2010/10/181Ž218:12:24
The last record in the file will contain only EOF

[For more info][info].
[info]: http://newsroom.calgary.ca/pr/calgary/important-media-info-city-of-calgary-248275.aspx


Remember
--------
Remember to use your own username and password for the FTP. And change the filename to whatever it is when you have access or the city announces it.


<3 Lucas
