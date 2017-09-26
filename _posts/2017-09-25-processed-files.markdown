---
layout: post
title: "Introducing our new processed data files"
deckhead: "Scraped from CAL-ACCESS and re-formatted into a new community-developed data standard"
byline: "By [James Gordon](https://twitter.com/je_gordon)"
image: ""
published: false
---

Today the Coalition is excited to announce the release of nearly two decades worth of data on California elections. This information, which the Secretary of State has withheld from exports of its CAL-ACCESS system, will now be published and archived here daily.

These new "processed" data files are the first implementation of a new community-driven standard we drafted and implemented in the hope of facilitating similar civic data projects across U.S. and international jurisdictions.

The elections data can be download in flat or relational formats, in a single ZIP or as individual comma-delimited files.

This new data, and the open-source code we've released which made it possible, bring us closer than ever to our ultimate goal: Frictionless access to comprehensive California state campaign finance and lobbying activity data.


### Introducing django-calaccess-scraped-data

The raw material of our project is mined from [CAL-ACCESS](http://cal-access.sos.ca.gov), California's state government system that tracks how much money political campaigns raise and spend leading up to elections.

Much to our disappointment, however, the [nightly exports](http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/) of CAL-ACCESS data released by the California Secretary of State don't include distinct lists of elections, races, public offices, candidates or ballot measures.

To be clear, this information does reside in CAL-ACCESS. It's displayed on their website and outlined in the database schema. But when we asked the Secretary of State's office to include these tables in their bulk data releases, [they said "no"](https://www.californiacivicdata.org/2015/03/15/closed-data/).

That left us with only one option: Scraping the CAL-ACCESS website. Thankfully, the coalition's student developer, [Sahil Chinoy](http://sahilchinoy.com/), was up to the task.

His work is now available as a stand-alone application written in the Django web framework. Just download our [package from PyPi](https://pypi.python.org/pypi/django-calaccess-scraped-data), plug it into your project, [read our docs](http://django-calaccess.californiacivicdata.org/en/latest/apps/calaccess_scraped.html) and scrape away.


### Open data in an open standard

CAL-ACCESS is notoriously closed-source with a nearly impenetrable database design. By contrast, we've
conformed our scraped elections data to meet a new standard, which we authored with the lovable nerds at Open Civic Data.

OCD is a collaboration by civic data hackers including Forest Gregg of DataMade and James Turk of Open States. Its organizing principle is to share the work of defining data models for domains such as legislative roll call votes.

The OCD folks invited yours truly to draft an [enhancement proposal](https://opencivicdata.readthedocs.io/en/latest/proposals/drafts/elections.html) outlining `Election` and its related data types (`Candidate`, `Contest`, `BallotMeasure` etc.), and then implement those specs in their Django application for use in our project or anyone else's for that matter.

Many months and pull requests later, python-opencivicdata 2.0 was packaged and released on PyPi. Isn't community open-source coding fun?


### Next steps

Along with our specs focused on elections, Abraham Epton of Socrata submitted another OCD enhancement proposal focused on [campaign finance filings](https://opencivicdata.readthedocs.io/en/latest/proposals/drafts/campaign_finance_filings.html).

Once we implement Abe's campaign finance specs, we'll be able to round off the work we've already put into our django-calaccess-processed-data app, currently in beta release.

The processed app is already churning out the scraped elections data in OCD format and archiving those files on our downloads website. Be on the look out for this list of processed files to expand in the coming weeks.


### This data is already fueling great journalism

Reporters at the LA Times have been crushing it lately, revealing how deep-pocketed donors affiliated with California's [cannabis industry](http://www.latimes.com/politics/la-pol-ca-newsom-cannabis-20170727-story.html) and [Hollywood](http://www.latimes.com/politics/la-pol-ca-hollywood-money-governors-race-20170804-story.html) are shoveling money at 2018 gubernatorial candidate Gavin Newsom. These and other stories were made possible through our open-source code and data releases.

http://www.latimes.com/politics/la-pol-ca-newsom-waterfront-governor-20170519-story.html

http://www.latimes.com/projects/la-pol-ca-california-governor-2018-money/


### Give us feedback

Whatever addition or change to our new processed data files that would make your life easier – no matter how small – we want to hear it. File a [ticket](https://github.com/california-civic-data-coalition/django-calaccess-processed-data/issues), shoot an [email](mailto:cacivicdata@gmail.com) or find us anytime in
[News Nerdery's](http://newsnerdery.org/) [#california-civic-data](https://newsnerdery.slack.com/messages/california-civic-data/).
