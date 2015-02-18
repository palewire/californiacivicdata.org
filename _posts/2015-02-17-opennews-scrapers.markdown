---
layout: post
title: OpenNews fellows liberate crucial California elections data
deckhead: "New web scrapers harvest data withheld by the state"
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/)"
published: true
---

A new release of [our software](http://django-calaccess-campaign-browser.californiacivicdata.org/en/latest/) for analyzing the millions of dollars spent to influence California election now features crucial data withheld by the state.

The upgrade comes thanks to members of [the 2015 class](http://opennews.org/what/fellowships/2015meet/) of Knight-Mozilla OpenNews fellows, who [joined us last month](http://opennews.org/blog/fellowship-onboarding-ccdc/) in Los Angeles to improve our open-source system for downloading and parsing the California Secretary of State's [CAL-ACCESS database](http://cal-access.sos.ca.gov/).

<img src="/img/opennews-fellows.jpg" width="100%" alt="The 2015 OpenNews fellows at the Los Angeles Times" style="border:1px solid black; margin: 5px 0;">

While the [bulk download](http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/) provided by the state provides the foundation for our project, it is incomplete.

Missing is the roster of candidates that participated in primaries and advanced to general elections, as well as the list of ballot measures that special interests have routinely spent millions to support or oppose.

Those missing connections are crucial.  Without them, analysts must fish out the small number of fundraising committees that matter from a crowded pool of thousands of filers.

State officials [declined](https://github.com/california-civic-data-coalition/django-calaccess-raw-data/issues/62#issuecomment-58655390) our request to add the records to their dump. But thanks to [Juan Elosua](http://www.twitter.com/jjelosua), [Francis Tseng](http://www.twitter.com/frnsys) and the OpenNews fellows the story didn't end there. They developed [scripts](https://github.com/california-civic-data-coalition/django-calaccess-campaign-browser/blob/master/calaccess_campaign_browser/management/commands/scrapecalaccesscampaigncandidates.py) [that](https://github.com/california-civic-data-coalition/django-calaccess-campaign-browser/blob/master/calaccess_campaign_browser/management/commands/scrapecalaccesscampaignpropositions.py) scrape the data off the state's website and load it into our database.

<img src="/img/elections.png" width="100%" alt="The elections data in our database" style="margin: 5px 0;">

Their work is now available in version 0.1.1 of [django-calaccess-campaign-browser](http://django-calaccess-campaign-browser.californiacivicdata.org/en/latest/), our Django app to refine and investigate the raw campaign finance data.

It was originally released [last August](http://www.californiacivicdata.org/2014/09/24/hello-world/) by the California Civic Data Coalition, a loosely coupled team from the Los Angeles Times Data Desk, The Center for Investigative Reporting and Stanford's Computational Journalism Lab.

If you'd like to join the effort, [dozens more tickets](https://github.com/california-civic-data-coalition/django-calaccess-campaign-browser/issues) are waiting in our GitHub repository. And stay tuned for more efforts to improve our project as we try to level up the library ahead of the 2016 elections.
