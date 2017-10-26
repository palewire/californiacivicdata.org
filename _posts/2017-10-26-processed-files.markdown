---
layout: post
title: "Introducing our new processed data files"
deckhead: "Scraped from CAL-ACCESS and re-formatted into a new community-developed data standard"
byline: "By [James Gordon](https://twitter.com/je_gordon) and the [California Civic Data Coalition](/about/)"
image: ""
published: true
---

The Coalition is excited to announce the release of nearly two decades worth of data on California elections. This information, which Secretary of State Alex Padilla has [blocked](https://www.californiacivicdata.org/2015/03/15/closed-data/) from public release, will now be published and archived daily [here on this site](https://calaccess.californiacivicdata.org/downloads/latest/).

These new data files catalog every candidate, ballot measure and election found in the jumbled, dirty and difficult database tracking money in state politics.

Simple standalone files are now available for quick access and analysis. You can find them on [our redesigned download page](https://calaccess.californiacivicdata.org/downloads/latest/), where the state's disorderly data is reformatted to fit a new open-source standard.

<img src="/img/ballot-measure-downloads.gif" style="padding: 10px">

### How we did it

The raw material of our project is mined from [CAL-ACCESS](http://cal-access.sos.ca.gov), California's state government system that tracks how much money political campaigns raise and spend on elections.

Much to our disappointment, the [bulk exports](http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/) of CAL-ACCESS data released by the California Secretary of State don't include distinct lists of elections, races, public offices, candidates or ballot measures.

<figure style="margin: 8px 0 0 10px; float:right;">
    <img alt="Sahil Chinoy" title="Sahil Chinoy" src="/img/sahil-chinoy.jpg" height="150">
    <figcaption style="text-align:right;">Sahil Chinoy</figcaption>
</figure>

To be clear, this information does reside in CAL-ACCESS. It's displayed on their website and outlined in the database schema. When we asked Secretary of State Alex Padilla's office to include these tables in their bulk data releases, they said "no."

That left us with only one option: Scraping it off their site.

Thankfully, the coalition's student developer, [Sahil Chinoy](http://sahilchinoy.com/), was up to the task. He expanded on [earlier contributions](https://www.californiacivicdata.org/2015/02/17/opennews-scrapers/) to our project to train a computer script to navigate through the CAL-ACCESS website and parse the essential data out.

<img src="/img/web-inspector.gif" style="padding: 10px">

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

In the money race, Lieutenant governor Gavin Newsom leads the pack with more campaign contributions than all his combined competitors. According to reporting by the Times, Newsom is the clear favorite of California's [cannabis industry](http://www.latimes.com/politics/la-pol-ca-newsom-cannabis-20170727-story.html) and [Hollywood](http://www.latimes.com/politics/la-pol-ca-hollywood-money-governors-race-20170804-story.html). Contrary to his environmentalist image, he also has been favored by [waterfront real estate developers in San Francisco](http://www.latimes.com/politics/la-pol-ca-newsom-waterfront-governor-20170519-story.html), where he previously served as mayor.

These stories were made possible through our open-source code and data releases.

### Give us feedback

Whatever addition or change to our new processed data files that would make your life easier – no matter how small – we want to hear it. File a [ticket](https://github.com/california-civic-data-coalition/django-calaccess-processed-data/issues), shoot an [email](mailto:cacivicdata@gmail.com) or find us anytime in
[News Nerdery's](http://newsnerdery.org/) [#california-civic-data](https://newsnerdery.slack.com/messages/california-civic-data/).
