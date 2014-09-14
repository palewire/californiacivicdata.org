---
layout: default
title: Pluggable Data
published: true
---

# Package data like software, and the stories will flow like wine

### A proposal from the California Civic Data Coalition

By [Agustin Armendariz](mailto:aarmendariz@gmail.com), [Aaron Williams](mailto:awilliams@cironline.org) and [Ben Welsh](mailto:ben.welsh@gmail.com)

By now, the melodrama is mundane. The government is asked to release an important data set. They dither. We moan. We groan. Sometimes we sue, or even (gasp) organize. 

We don't always win, but more and more we do. In the final act they make good. As we procaciously demanded, the government releases the raw data. In forward-thinking precincts, they may even begin publishing bulk downloads on the Internet.

What happens next? You know the script. 

A self-taught newsroom analyst partners with an ambitious reporter to extract a story. A bored developer posts a misleading but beautifully rendered graphic on Tumblr. A data vendor with a cryptic name throws another lump into its billowing furnance.

And then, almost always, all of the focus, research and code that went into taming the source data is lost&mdash;discarded by the harried journalist, forgotten by the intellectually promiscious developer, locked away by the monopoly-seeking vendor.

The result: Each newcomer must repeat the same effort. Every user is required to craft virtually identical methods for downloading, transforming and cleaning the data. And no matter how many analysts use the data, the hurdle remains the same height.

This has to change. It’s a waste of time, energy and money. 

We need a common set of tools that automates away what [Dave Guarino](http://daguar.github.io/2014/03/17/etl-for-america/) and [Bob Lannon](http://sunlightfoundation.com/blog/2014/03/21/data-plumbers/) have called the "plumbling" that prepares any data source for analysis.

Our proposal is that pip, software packaging and web framworks offer one means for achieving that goal ... 

- Explain our solution
- Explain origin of "pluggable apps" in Django and explain the fourfold path
- Connect this idea to our work on CAL-ACCESS
-- Walk through all it takes to make it go 
-- Link to our stuff and gtfo

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