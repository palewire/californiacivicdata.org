---
layout: post
title: "Introducing our new processed data files"
deckhead: "Scraped from CAL-ACCESS and re-formatted into a new community-developed data standard"
byline: "By [James Gordon](https://twitter.com/je_gordon)"
image: ""
published: true
---

Today the Coalition is excited to announce the release of nearly two decades worth of data on California elections. This information, which the Secretary of State has withheld from exports of its CAL-ACCESS system, will now be published and archived here daily.

These new "processed" data files are the first implementation of a new community-driven standard we drafted and implemented in the hope of facilitating similar civic data projects across U.S. and international jurisdictions.

Get the [latest](http://calaccess.californiacivicdata.org/documentation/processed-files/downloads/latest/) data in a simplified "flat" format if who would rather the skip the `JOIN` queries. Or if you would rather load everything into database manager, grab the full set files in "relational" format.

You can also download individual CSV files from our [full list](http://calaccess.californiacivicdata.org/documentation/processed-files/documentation/processed-files/).

<img src="/img/ballot-measure-downloads.gif" style="padding: 10px">

This new data — and our open-source code that made it possible — bring us closer than ever to our ultimate goal: Frictionless access to comprehensive California state campaign finance and lobbying activity data.


### Introducing django-calaccess-scraped-data

The raw material of our project is mined from [CAL-ACCESS](http://cal-access.sos.ca.gov), California's state government system that tracks how much money political campaigns raise and spend leading up to elections.

Much to our disappointment, the [nightly exports](http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/) of CAL-ACCESS data released by the California Secretary of State don't include distinct lists of elections, races, public offices, candidates or ballot measures.

To be clear, this information does reside in CAL-ACCESS. It's displayed on their website and outlined in the database schema. But when we asked the Secretary of State's office to include these tables in their bulk data releases, [they said "no"](https://www.californiacivicdata.org/2015/03/15/closed-data/).

That left us with only one option: Scraping. So we wrote code that would routinely navigate through the CAL-ACCESS website and parse the essential data out of their crufty markup.

<img src="/img/web-inspector.gif" style="padding: 10px">

<figure style="margin: 8px 0 0 10px; float:right;">
    <img alt="Sahil Chinoy" title="Sahil Chinoy" src="/img/sahil-chinoy.jpg" height="150">
    <figcaption style="text-align:right;">Sahil Chinoy, web scraping hero.</figcaption>
</figure>

Thankfully, the coalition's student developer, [Sahil Chinoy](http://sahilchinoy.com/), was up to the task.

His work is now available as a stand-alone application written in the Django web framework. Just download our [package from PyPi](https://pypi.python.org/pypi/django-calaccess-scraped-data), plug it into your project, [read our docs](http://django-calaccess.californiacivicdata.org/en/latest/apps/calaccess_scraped.html) and scrape away.

### Open data in an open standard

CAL-ACCESS is notoriously closed-source with an impenetrable database design. By contrast, we've conformed our scraped elections data to meet a new standard, which we authored with the lovable nerds at Open Civic Data.

<img src="/img/opencivicdata-logo_default_1000.png" style="padding: 10px">

OCD is a hub for hackers working in the related fields of civic technology, open government and journalism. Its ranks include the likes of Forest Gregg of [DataMade](https://datamade.us), James McKinney of [Popolo Project](http://www.popoloproject.com)) and Rachel Shorey of [The New York Times](https://www.nytimes.com)).

OCD's organizing principle is to share the work of defining data models and maintaining software packages that power important projects like [Open States](https://openstates.org/), which is steered by Sunlight Foundation alumnus James Turk.

The folks at OCD invited yours truly to draft an [enhancement proposal](https://opencivicdata.readthedocs.io/en/latest/proposals/drafts/elections.html) outlining `Election` and its related data types (`Candidate`, `Contest`, `BallotMeasure` etc.), and then implement those specs in their Django application for use in our project or anyone else's for that matter.

After many months of [back-and-forth](https://github.com/opencivicdata/docs.opencivicdata.org/pull/64), python-opencivicdata 2.0 was packaged and [released on PyPi](https://pypi.python.org/pypi/opencivicdata). Open-source collaboration FTW.

### Next steps

Along with our specs focused on elections, Abraham Epton of [Socrata](https://socrata.com) submitted another OCD enhancement proposal focused on [campaign finance filings](https://opencivicdata.readthedocs.io/en/latest/proposals/drafts/campaign_finance_filings.html).

Once we implement Abe's campaign finance specs, we'll be able to round off the work we've already put into our [django-calaccess-processed-data](https://pypi.python.org/pypi/django-calaccess-processed-data) app, currently in beta release.

The processed app is already churning out the scraped elections data in OCD format and archiving those files on our downloads website. Next up, we'll begin publishing committees, contributions and expenditures extracted from filings of [California Form 460](https://calaccess.californiacivicdata.org/documentation/calaccess-forms/f460/), the disclosure report regularly filed by all recipients of campaign contributions.

<figure style="margin: 28px 0 8px 0;">
    <a href="https://calaccess.californiacivicdata.org/documentation/calaccess-forms/f460/">
        <img src="/img/form-460-summary.png" style="border: 1px solid black;">
    </a>
    <figcaption style="text-align:right;">Our next release on Form 460 data. Get excited.</figcaption>
</figure>

### This data is already fueling great journalism

Reporters at the LA Times have been crushing it lately, shining a light on  the [insane amount of money](http://www.latimes.com/projects/la-pol-ca-california-governor-2018-money/) already raised by California's 2018 gubernatorial candidates.

<img src="/img/governor-2018-graphic.gif" style="padding: 10px">

In the money race, Lieutenant governor Gavin Newsom leads the pack with more campaign contributions than all his combined competitors. According to reporting by the Times, Newsom is the clear favorite of California's [cannabis industry](http://www.latimes.com/politics/la-pol-ca-newsom-cannabis-20170727-story.html) and [Hollywood](http://www.latimes.com/politics/la-pol-ca-hollywood-money-governors-race-20170804-story.html). Contrary to his environmentalist image, he has also found favor among [waterfront real estate developers in San Francisco](http://www.latimes.com/politics/la-pol-ca-newsom-waterfront-governor-20170519-story.html), where he previously served as mayor.

These stories were made possible through our open-source code and data releases.

http://www.latimes.com/politics/la-pol-ca-newsom-waterfront-governor-20170519-story.html

### Give us feedback

Whatever addition or change to our new processed data files that would make your life easier – no matter how small – we want to hear it. File a [ticket](https://github.com/california-civic-data-coalition/django-calaccess-processed-data/issues), shoot an [email](mailto:cacivicdata@gmail.com) or find us anytime in
[News Nerdery's](http://newsnerdery.org/) [#california-civic-data](https://newsnerdery.slack.com/messages/california-civic-data/).
