---
layout: default
title: Pluggable Data
published: true
---

# Package data like software, and the stories will flow like wine

### A proposal from the California Civic Data Coalition

By [Agustin Armendariz](mailto:aarmendariz@gmail.com), [Aaron Williams](mailto:awilliams@cironline.org) and [Ben Welsh](mailto:ben.welsh@gmail.com)

By now, the melodrama is mundane. The government is asked to release an important data set. They dither. We moan. We groan. Sometimes we sue, or even (gasp) organize. We don't always win, but more and more we do. And in the final act the government makes good. As we so procaciously demanded, they release the raw data. In our more forward-thinking precincts, they may even begin publishing bulk downloads on the Internet.

What happens next? You know the script. 

A self-taught newsroom analyst partners with an ambitious reporter to extract a story. A bored developer posts a misleading but beautifully rendered graphic on Tumblr. A data vendor with a cryptic name throws another lump into its billowing furnance.

And, almost always, all the focus, research and  

But far too often the data we use for our reporting is laboriously collected and analyzed then discarded. We move on to other stories and have to recreate that effort later should we need to use the same data source again. And our colleagues at other organizations are doing the exact same thing.
 
This has to change.
 
It’s a waste of time, effort and ultimately money. In the academic world there’s a common set of tools that community members use and members of that community collaboratively share import routines that get a particular data source ready for analysis.
 
The open source community needs to do the same.
 
Reporters, Web Developers,  Data Scientists and hobbyists that use open source tools should have access to what we’re calling “pluggable data.”
 
If you can pip install Django you should be able to pip install data to go with your Django project in the same way that there are SPSS and SAS import scripts for using education data housed in the Integrated Postsecondary Education Data System (IPEDS).
 
Access to data is increasingly important and enough people are working with the same regularly updated data sources that we believe self-sustaining communities of users can emerge to collaboratively maintain open source tools to access data quickly and easily.
 
We shouldn’t have to hand roll our own import scripts for data that’s regularly available on the web.
 
Towards that end our small group came together to liberate the State of California’s campaign finance and lobbying data housed in the CAL-ACCESS system.
 
Thanks to the efforts of the good folks at MapLight, the state committed to posting the data on the web and updating it on a regular basis. Knowing that we’d have to work with this data at some point in our reporting, we came together to collaborate on liberating it.
 
We’re calling ourselves the California Civic Data Coalition and we’d love to see similar efforts in other states and cities. Think of the insights that could be made if we had access to similar data across the 50 states and even in cities too.
 
Our effort in no way is meant to replace the valuable service that organizations like MapLight, The National Institute for Money in State Politics, The Center for Responsive Politics and the Sunlight Foundation provide. They all glean invaluable insights from the data and inform voters in a way that could never be automated.
 
We hope that they’d want to collaborate with us to ensure everyone has access to the raw data and use the open source tools we make.
 
Thanks to the generous support of the Knight-Mozilla Open News Foundation our nascent group of data liberators came together in San Francisco and put the finishing touches on a parser for the CAL-ACCESS data dump.
 
SOME STATS HERE LIKE XX MILLION RECORDS, 80 CSV FILES, ETC.  
 
And there’s more in the works. We’re well on our way to having an app that rips out the campaign finance data from the raw data dump and organizes it in a more useful way for analysis. Stay tuned in the coming weeks.

### Outline
- Define the problem
- Declare that it be destroyed
- Point to what other fields do
- Explain our solution
- Explain origin of "pluggable apps" in Django and explain the fourfold path
- Connect this idea to our work on CAL-ACCESS
-- Walk through all it takes to make it go 
-- Link to our stuff and gtfo

Things we need to reference

- David Guarino's [ETL for America](http://daguar.github.io/2014/03/17/etl-for-america/)
- Bob Lannon's [follow up](http://sunlightfoundation.com/blog/2014/03/21/data-plumbers/)
- NYT [data janitor](http://www.nytimes.com/2014/08/18/technology/for-big-data-scientists-hurdle-to-insights-is-janitor-work.html?_r=0) piece