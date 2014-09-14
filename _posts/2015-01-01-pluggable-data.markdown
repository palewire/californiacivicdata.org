---
layout: default
title: Pluggable Data
published: false
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

For instance, if you are a Python developer interested in trying out the [requests](http://docs.python-requests.org/en/latest/) library, installing it on your laptop is as easy as:

~~~ bash
$ pip install requests
~~~

And now using it is only a import away.

~~~ python
>>> import requests
>>> requests.get("http://www.californiacivicdata.org/").status_code
200
~~~

Within the warm confines of a web frameworks&mdash;open-source libraries like [Django](http://www.djangoproject.com/) or [Ruby on Rails](http://rubyonrails.org/) that are so broad they include all the necessary tools to interact with a database, design an application and publish it to the web&mdash;this concept has been expanded to encourage the packaging not just of freestanding utilities like requests, but entire applications that ["just work"](https://www.youtube.com/watch?v=qmPq00jelpc) when integrated with the framework.

This type of application, [championed](http://www.b-list.org/weblog/2007/nov/29/django-blog/) [eloquently](https://www.youtube.com/watch?v=A-S0tqpPga4) by Django leaders like James Bennett, is sometimes called a "pluggable" or "reusable" app, because its modular design makes it portable to a wide range of sites.

A good example is the open-source [Pinax project](http://pinaxproject.com/), which provides Django-ready components that furnish common features like [comments](https://github.com/eldarion/dialogos), [badges](https://github.com/eldarion/brabeion), [phone confirmations](https://github.com/pinax/pinax-phone-confirmation) and [user accounts](https://github.com/pinax/django-user-accounts). Each contains code that configures database tables, administration panels to edit records and application logic that can interact with users.

Our proposal is to bring the exact same approach to packaging data. If a series of simple installation commands can provide a Django application with everything necessary to build a social networking site, why can't it also provide [U.S. Census statistics](http://factfinder2.census.gov/faces/nav/jsf/pages/download_center.xhtml), [the massive federal database that tracks our country's chemical pollutors](http://www2.epa.gov/toxics-release-inventory-tri-program/tri-basic-data-files-calendar-years-1987-2012) or even something as simple as [a list of every U.S. county](http://www.epa.gov/envirofw/html/codes/state.html)? 

### How we do

With that idea in mind, a small group of programmers from the [Los Angeles Times Data Desk](http://www.latimes.com/local/datadesk/), [The Center for Investigative Reporting](http://cironline.org/) and Stanford's new [Computational Journalism Program](http://towcenter.org/blog/data-journalist-profile-cheryl-phillips-stanford-data-journalism/) met for two days last month at Mozilla offices in San Francisco.

Under the newly minted banner of the California Civic Data Coalition, we set out to package and refine [raw data from CAL-ACCESS](http://www.sos.ca.gov/prd/cal-access/), the State of California’s campaign finance and lobbying database.
 
Thanks to a [successful organizing effort](http://maplight.org/content/73249) last year, Secretary of State Debra Bowen [committed](http://www.sos.ca.gov/admin/press-releases/2013/db13-035.htm) to posting a nearly complete dump of the data online, updating it on a regular basis. 

Weighing in at more than 650 megabytes the dump contains 76 database tables and nearly 35 million records. In the past, analysts, including [one of the authors of this post](http://cironline.org/reports/california-speaker-gives-assemblys-juiciest-jobs-biggest-fundraisers-4501), would spend months learning how to negotiate its contours, overcome its quirks and grind out insights from slices released ad hoc on a compact disc only to move on.



 
We’re calling ourselves the California Civic Data Coalition and we’d love to see similar efforts in other states and cities. Think of the insights that could be made if we had access to similar data across the 50 states and even in cities too.
 
Our effort in no way is meant to replace the valuable service that organizations like MapLight, The National Institute for Money in State Politics, The Center for Responsive Politics and the Sunlight Foundation provide. They all glean invaluable insights from the data and inform voters in a way that could never be automated.
 
We hope that they’d want to collaborate with us to ensure everyone has access to the raw data and use the open source tools we make.