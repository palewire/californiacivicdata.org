---
layout: post
title: "Introducing our new source for clean data on California elections"
deckhead: "How we took CAL-ACCESS to the cleaners"
byline: "By [James Gordon](https://twitter.com/je_gordon) and the [California Civic Data Coalition](/about/)"
image: ""
published: true
---

The Coalition is excited to announce the release of nearly two decades worth of data on California elections. This information, previously [blocked](https://www.californiacivicdata.org/2015/03/15/closed-data/) from public release by state officials, is now updated daily [on this site](https://calaccess.californiacivicdata.org/downloads/latest/).

The new data files catalog every candidate, ballot measure and election found in the jumbled, dirty and difficult governoment database tracking money in state politics.

You can find them on [our redesigned download page](https://calaccess.californiacivicdata.org/downloads/latest/), where the state's disorderly data is reformatted to fit our new open-source standard.

<img src="/img/ballot-measure-downloads.gif" style="padding: 10px">

### How we got the data

The raw material of our project is mined from [CAL-ACCESS](http://cal-access.sos.ca.gov), the California state government's system for tracking the money political campaigns raise and spend on elections.

Much to our disappointment, the [bulk exports](http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/) of CAL-ACCESS data released by Secretary of State Alex Padilla don't include coherent and complete lists of elections, races, public offices, candidates or ballot measures.

<figure style="margin: 8px 0 0 10px; float:right;">
    <img alt="Sahil Chinoy" title="Sahil Chinoy" src="/img/sahil-chinoy.jpg" height="150">
    <figcaption style="text-align:right;">Sahil Chinoy</figcaption>
</figure>

To be clear, this information does reside in CAL-ACCESS. It's displayed on their website and outlined in the database schema. When we asked Padilla's office to include these tables in their bulk data releases, they said "no."

That left us with only one option: Scraping it off the state's site.

Thankfully, the Coalition's student developer, [Sahil Chinoy](http://sahilchinoy.com/), was up to the task. He expanded on [earlier contributions](https://www.californiacivicdata.org/2015/02/17/opennews-scrapers/) to our project to train a computer script to navigate through the CAL-ACCESS website and parse the essential data out.

<img src="/img/web-inspector.gif" style="padding: 10px">

His work is now available as a stand-alone application written in the Django web framework. Just download our [package from PyPI](https://pypi.python.org/pypi/django-calaccess-scraped-data), plug it into your project, [read our docs](http://django-calaccess.californiacivicdata.org/en/latest/apps/calaccess_scraped.html) and scrape away.

### How we improved the data


CAL-ACCESS is a mess. And you don't have to take our word for it.

In [a recent public filing](https://twitter.com/palewire/status/922861435461410816), Padilla's office described it as an "old," "fragile" and "not well documented" system that "cannot be patched or modified" and is at risk of collapse.

Rather than force users to wade through its arcane data structures, we've modified our files to meet a new standard we authored with [Open Civic Data](https://opencivicdata.readthedocs.io), a community of leaders in our field aiming to define common schemas for consolidating public data.

<img src="/img/opencivicdata-logo_default_1000.png" style="padding: 10px">

OCD's ranks include Forest Gregg of [DataMade](https://datamade.us), James McKinney of [Popolo Project](http://www.popoloproject.com) and Rachel Shorey of [The New York Times](https://www.nytimes.com).

With their guidance, yours truly drafted a [proposal](https://opencivicdata.readthedocs.io/en/latest/proposals/drafts/elections.html) outlining a new data schema for elections and related data types like candidates, contests and ballot measures. I then implemented those specs in their Django application for use in our project, or anyone else's.

After many months of [back-and-forth](https://github.com/opencivicdata/docs.opencivicdata.org/pull/64) &mdash; and comments from our peers at Google, Socrata and elsewhere &mdash; python-opencivicdata version 2.0 was packaged and [released on PyPI](https://pypi.python.org/pypi/opencivicdata).

Our hope is that this work can help power other open-source projects working with similar data sets in other states and countries.

### What this data is already doing

Early versions of these files have been put to work by reporters at the Los Angeles Times.

[Maloy Moore](http://www.latimes.com/la-bio-maloy-moore-staff.html) and [Ryan Menezes](http://www.latimes.com/la-bio-ryan-menezes-staff.html) have used the experimental release of our software (available to everyone on [GitHub](http://django-calaccess.californiacivicdata.org/en/latest/)) to generate a series of pieces on the millions of dollars flooding the race to be California's next governor.

<img src="/img/governor-2018-graphic.gif" style="padding: 10px">

Lieutenant Governor Gavin Newsom leads the pack with more campaign contributions than all competitors combined, according to the tally in [their graphic, seen above](http://www.latimes.com/projects/la-pol-ca-california-governor-2018-money/).

Their reporting has uncovered Newsom's connection to California's burgeoning [cannabis industry](http://www.latimes.com/politics/la-pol-ca-newsom-cannabis-20170727-story.html), as well as his heavy support from [Hollywood](http://www.latimes.com/politics/la-pol-ca-hollywood-money-governors-race-20170804-story.html).

Contrary to the candidate's environmentalist image, Times reporters have also documented how Newsom has curried favor from [controversial real estate developers in San Francisco](http://www.latimes.com/politics/la-pol-ca-newsom-waterfront-governor-20170519-story.html).

### What we're doing next

As a companion to our work, Abraham Epton of [Socrata](https://socrata.com) has submitted a OCD proposal focused on standardizing [campaign finance filings](https://opencivicdata.readthedocs.io/en/latest/proposals/drafts/campaign_finance_filings.html) across states.

Our next mission is to implement Abe's ideas so we can begin churning out cleaned up files containing the valuable data on campaign committees, contributions and expenditures now locked inside of CAL-ACCESS and its Form 460 filings.

<figure style="margin: 28px 0 8px 0;">
    <a href="https://calaccess.californiacivicdata.org/documentation/calaccess-forms/f460/">
        <img src="/img/form-460-summary.png" style="border: 1px solid black;">
    </a>
</figure>

### What you can do

[Download our files](https://calaccess.californiacivicdata.org/downloads/latest/). Play with them. See something you don't like. Tell us about it. Whatever addition or change to our new processed data files that would make your life easier – no matter how small – we want to hear it. File a [ticket](https://github.com/california-civic-data-coalition/django-calaccess-processed-data/issues), shoot an [email](mailto:cacivicdata@gmail.com) or find us anytime in
[News Nerdery's](http://newsnerdery.org/) [#california-civic-data](https://newsnerdery.slack.com/messages/california-civic-data/).
