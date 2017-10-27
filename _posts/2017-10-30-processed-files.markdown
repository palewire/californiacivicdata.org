---
layout: post
title: "Introducing a new source for California elections data"
deckhead: "How we took CAL-ACCESS to the cleaners"
byline: "By [James Gordon](https://twitter.com/je_gordon) and the [California Civic Data Coalition](/about/)"
image: ""
published: true
---

After years of work, the Coalition is excited to release nearly two decades worth of data on California elections. The information, blocked from public release by state officials, is now published daily here on this site in open formats and according to a new open-source standard.

This marks a major milestone in the Coalition's effort to make it easier for reporters and researchers to explore the role of money in California politics. The new data files catalog every candidate, ballot measure and election found in the jumbled, dirty and difficult government database tracking money in state politics.

You can find the new data on [our revamped download page](https://calaccess.californiacivicdata.org/downloads/latest/), where it will be joined by a second, expanded series of files in the coming months.

<figure style="width: 100%;">
    <a href="https://calaccess.californiacivicdata.org/downloads/latest/">
        <img src="/img/ballot-measure-downloads.gif" style="padding: 10px" title="The new downloads page" alt="The new downloads page">
    </a>
</figure>


### How we got the data

Our original source is [CAL-ACCESS](http://cal-access.sos.ca.gov), the California state government's system for tracking the money political campaigns raise and spend on elections.

While containing some useful information, the [bulk export](http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/) of CAL-ACCESS data released by Secretary of State Alex Padilla does not include coherent and complete lists of elections, races, public offices, candidates or ballot measures.

<figure style="margin: 8px 0 0 10px; float:right;">
    <img alt="Sahil Chinoy" title="Sahil Chinoy" src="/img/sahil-chinoy.jpg" height="150">
    <figcaption style="text-align:right;">Sahil Chinoy</figcaption>
</figure>

To be clear, *this information does reside in CAL-ACCESS*. It is collected by the Secretary of State's office, displayed on its website and outlined its official database schema.

But when we asked Padilla's office to include it in their bulk data release, [they said "no."](https://github.com/california-civic-data-coalition/django-calaccess-raw-data/issues/62#issuecomment-58655390)

That left us with only one option: Scraping it off the state's site.

The Coalition's student developer, [Sahil Chinoy](http://sahilchinoy.com/), was up to the task. He expanded on [earlier contributions from an enterprising group of OpenNews fellows](https://www.californiacivicdata.org/2015/02/17/opennews-scrapers/) to train a computer script to navigate through the CAL-ACCESS website and parse out the essential data.

<img src="/img/web-inspector.gif" style="padding: 10px">

Chinoy's work is now integrated into our open-source data pipeline and also available as a stand-alone application for the Django web framework. Anyone can download it [package from PyPI](https://pypi.python.org/pypi/django-calaccess-scraped-data), plug it into their project, [read our docs](http://django-calaccess.californiacivicdata.org/en/latest/apps/calaccess_scraped.html) and scrape away.


### How we improved the data

Look, CAL-ACCESS is a mess. And you don't have to take our word for it.

In [a recent public filing](https://twitter.com/palewire/status/922861435461410816), Padilla's office described it as an "old," "fragile" and "not well documented" system that "cannot be patched or modified" and is at risk of collapse.

Rather than force users to wade through its arcane data structures, we've modified our files to meet a new standard we authored with [Open Civic Data](https://opencivicdata.readthedocs.io), a community of leaders in our field aiming to define common schemas for consolidating public data.

<img src="/img/opencivicdata-logo_default_1000.png" style="padding: 10px">

OCD's ranks include Forest Gregg of [DataMade](https://datamade.us), James McKinney of [Popolo Project](http://www.popoloproject.com) and Rachel Shorey of [The New York Times](https://www.nytimes.com).

With their guidance, the Coalition's James Gordon &mdash; that's me &mdash; drafted a [proposal](https://opencivicdata.readthedocs.io/en/latest/proposals/drafts/elections.html) outlining a new data schema for elections and related data types like candidates, contests and ballot measures. We then implemented those specs in [Open Civic Data's Django application](https://github.com/opencivicdata/python-opencivicdata) for use in any project, including yours.

After many months of [back-and-forth](https://github.com/opencivicdata/docs.opencivicdata.org/pull/64) &mdash; and comments from our peers at Google, Socrata and elsewhere &mdash; python-opencivicdata version 2.0 was packaged and [released on PyPI](https://pypi.python.org/pypi/opencivicdata).

Our hope is that this work can help power other open-source projects working with similar data sets in other states and countries.


### Who is already using this data?

Early versions of these files have been put to work by reporters at the Los Angeles Times.

[Maloy Moore](http://www.latimes.com/la-bio-maloy-moore-staff.html) and [Ryan Menezes](http://www.latimes.com/la-bio-ryan-menezes-staff.html) have used the experimental release of our software (available to everyone on [GitHub](http://django-calaccess.californiacivicdata.org/en/latest/)) to generate a series of pieces on the millions of dollars flooding the race to be California's next governor.

<img src="/img/governor-2018-graphic.gif" style="padding: 10px">

Lieutenant Governor Gavin Newsom leads the pack with more campaign contributions than all competitors combined, according to the tally in [their graphic, seen above](http://www.latimes.com/projects/la-pol-ca-california-governor-2018-money/).

Their reporting has uncovered Newsom's connection to California's burgeoning [cannabis industry](http://www.latimes.com/politics/la-pol-ca-newsom-cannabis-20170727-story.html), as well as his heavy support from [Hollywood](http://www.latimes.com/politics/la-pol-ca-hollywood-money-governors-race-20170804-story.html).

Contrary to the candidate's environmentalist image, Times reporters have also documented how Newsom has curried favor from [controversial real estate developers in San Francisco](http://www.latimes.com/politics/la-pol-ca-newsom-waterfront-governor-20170519-story.html).

### What we're doing next

As a companion to our work, Abraham Epton of [Socrata](https://socrata.com) has submitted a OCD proposal focused on standardizing [campaign finance filings](https://opencivicdata.readthedocs.io/en/latest/proposals/drafts/campaign_finance_filings.html) across states.

Our next mission is to implement Abe's ideas so we can churn out cleaned up files containing the valuable data on campaign committees, contributions and expenditures now locked inside of CAL-ACCESS and its Form 460 filings.

<figure style="margin: 28px 0 8px 0;">
    <a href="https://calaccess.californiacivicdata.org/documentation/calaccess-forms/f460/">
        <img src="/img/form-460-summary.png" style="border: 1px solid black;">
    </a>
</figure>

### What you can do

[Download our files](https://calaccess.californiacivicdata.org/downloads/latest/). Play with them. See something you don't like. Tell us about it.

Whatever addition or change to our new processed data files that would make your life easier – no matter how small – we want to hear it. File a [ticket](https://github.com/california-civic-data-coalition/django-calaccess-processed-data/issues), shoot an [email](mailto:cacivicdata@gmail.com) or find us anytime in
[News Nerdery's](http://newsnerdery.org/) [#california-civic-data](https://newsnerdery.slack.com/messages/california-civic-data/).
