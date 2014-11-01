---
layout: post
title: "CAL-ACCESS in action"
deckhead: "Read the Los Angeles Times analysis that couldn't have happened without our open-source tools"
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/)"
published: true
---

Michael Finnegan and I dug deep into Gov. Jerry Brown's fundraising effort for a story [in today's Los Angeles Times](http://www.latimes.com/local/politics/la-me-pol-brown-money-20141031-story.html#page=1).

What we found is that in his drive for a fourth and final term as California governor, Brown has transformed from one of the leading critics of money in politics to the master of a machine that routinely draws on six-figure checks from lobbyists and corporations.

The story would not have been possible without [bulk data](http://www.sos.ca.gov/prd/cal-access/) from the state's CAL-ACCESS campaign finance database and CCDC's [django-calaccess-campaign-browser](http://django-calaccess-campaign-browser.californiacivicdata.org/en/latest/).

[The state's website](http://cal-access.ss.ca.gov/) offers some good options for exploring the money from outside interests that floods the statehouse in Sacramento, but if you want to conduct a sophisticated analysis it is no substitute for the raw data.

Using our tools, we were able to rapidly develop a custom application on top of CCDC's open source foundation that:

1. Discovered that nearly 20% of Brown's campaign contributions have come in large blocks of money from the state Democratic Party, blurring the original source of more than $4.7 million funding his campaign.
2. Documented that no other gubernatorial candidate of either party has had so much money passed on from a party since the CAL-ACCESS database came online.
3. Identified a series of special interests that act as "double donors," contributing hundreds of thousands of dollars more to the Democratic Party after giving the legal limit of $54,400 directly to Brown's campaign fund.

[Our story]((http://www.latimes.com/local/politics/la-me-pol-brown-money-20141031-story.html#page=1)) attempted to put all that into context and tell the story how Jerry Brown has, to use a term now en vogue in our politics, _evolved_.

In the process we contributed [dozens of incremental improvements](https://github.com/california-civic-data-coalition/django-calaccess-campaign-browser/pulse/monthly) to the underlying open-source code base that we hope others can take advantage of in the future. 

There's still a long march ahead of us before our tools make this kind of work easy, but we hope that today's story represents a first step.
