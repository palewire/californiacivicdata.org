---
layout: default
title: Pluggable Data
published: true
---

# Package data like software, and the stories will flow like wine

### A humble suggestion from your friends at the California Civic Data Coalition

By [Agustin Armendariz](mailto:aarmendariz@gmail.com), [Aaron Williams](mailto:awilliams@cironline.org) and [Ben Welsh](mailto:ben.welsh@gmail.com)

The melodrama is so familiar it's mundane. The government is asked to release an important data set. They dither. We moan. We groan. Sometimes we sue, or even (gasp) organize. 

We don't always win, but more and more we do. In the final act, they now often make good. They release the raw data, just as we asked. In forward-thinking precincts they maybe even publish bulk downloads online.

What happens next? You know the script. 

A newsroom analyst partners with an ambitious reporter to extract a story. A bored developer posts a confused but beautifully rendered graphic on Tumblr. A vendor with a cryptic name throws another lump into its billowing data furnance.

And then, almost always, all of the focus, research and code that went into taming the source data is lost&mdash;discarded by the harried journalist, forgotten by the intellectually promiscious developer, locked away by the monopoly-seeking vendor.

The pathetic result: Every newcomer must repeat their efforts by crafting virtually identical methods for downloading, transforming and cleaning the data. And no matter how many analysts do it, the hurdles remains the same height.

This has to change. It’s a waste of time, energy and money so dreary and pointless that even broadsheet newspaper reporters, a faction with revanchist delusions on par with the Putin administration, [see the problem](http://www.nytimes.com/2014/08/18/technology/for-big-data-scientists-hurdle-to-insights-is-janitor-work.html?_r=0).

As [Dave Guarino](http://daguar.github.io/2014/03/17/etl-for-america/) and [Bob Lannon](http://sunlightfoundation.com/blog/2014/03/21/data-plumbers/) have forcefully argued, the open-data community needs to match the effort put into developing the latest, greatest user interface with a better effort to automate away the unglamorous but important work that prepares any data source for meaningful analysis and visualization, what they call the "plumbing."

While there are numerous ways to approach the challenge, we're here to propose one in particular. We call it "pluggable data."

### What we mean

If you have any experience as a developer, you've probably bumped into packaged sofware. Thousands of free and open-source libraries are available for installation over the web from centralized servers, typically unique to each programming language. Command-line tools like [``pip``](http://pip.readthedocs.org/en/latest/index.html) (Python) or [``gem``](https://rubygems.org/) (Ruby), [``CPAN``](http://www.cpan.org/) (Perl) or [``npm``](https://www.npmjs.org/) (NodeJS) can make it easy to do. 

For instance, if I'm a Python developer interested in trying out the [requests](http://docs.python-requests.org/en/latest/) library, installing it on my laptop is as easy as:

~~~ bash
$ pip install requests
~~~

And now using it is only a import away.

~~~ python
>>> import requests
>>> requests.get("http://www.californiacivicdata.org/").status_code
200
~~~

Within the warm confines of a web frameworks&mdash;open-source libraries like [Django](http://www.djangoproject.com/), [Ruby on Rails](http://rubyonrails.org/) so broad that they include all the necessary tools to interact with a database, design an application and publish it to the web&mdash;this concept has been expanded to encourage the packaging not just of freestanding utilities like requests, but of modular applications that "just work" by easily integrating into the framework.

We call "pluggable data" it,  and the id

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