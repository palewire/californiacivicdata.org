---
layout: post
title: "The 2015 CAL-ACCESS challenge"
deckhead: "Four ways to dig deeper into California campaign cash at this week's Stanford symposium, [Corruption: Who plays, who pays?](http://events.stanford.edu/events/501/50185/)"
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/), [Aaron Williams](http://aboutaaron.com) and [Cheryl Phillips](https://comm.stanford.edu/faculty-phillips/)"
image: "http://www.californiacivicdata.org/img/nast-moneybags.jpg"
published: true
---

Who is bankrolling the most powerful politicians in America’s largest state? What are special interests lobbying to stuff in California’s $150 billion budget?

Despite a complex and costly set of regulations, there’s no easy answer. Basic facts and figures are buried deep within an arcane state database, known as CAL-ACCESS, that records the millions of dollars in campaign contributions and lobbying activity that oil the Sacramento statehouse.

In a little-noted landmark, California [yielded](http://maplight.org/data-release/press-release-cal-access-database-available-for-daily-download-by-labor-day-says-califo) to a flurry of pressure in 2014 and for the first time officials posted [a free download](http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/) of the system’s raw data, updated daily.

The newly released information has created an unprecedented opportunity to analyze money in state politics. But it remains unrealized.

Sprawling across 76 database tables and weighing in at more than 650 megabytes, a significant effort is required to understand the dump’s esoteric structure and prepare the records for meaningful analysis.

That project is already underway. Under the new banner of the [California Civic Data Coalition](http://www.californiacivicdata.org/), news developers at the Stanford Computational Journalism Lab, the Bay Area’s Center for Investigative Reporting and the Los Angeles Times Data Desk are collaborating to automate away the database’s difficulties.

We’ve released a first-generation of [open-source tools](https://github.com/california-civic-data-coalition) that begin the work of downloading and decoding the data. In a [series](https://source.opennews.org/en-US/articles/introducing-california-civic-data-coalition/) [of](http://www.californiacivicdata.org/2015/02/17/opennews-scrapers/) [code convenings](http://www.californiacivicdata.org/2015/03/11/code-rush-recap/), more than 50 developers, representing dozens of different news organizations, have contributed code to start building a foundation for future analysts.

Now we need you. We’re looking for developers, data scientists and campaign finance experts to help us advance our cause.

Below are a series of challenges for Friday’s afternoon workshops where we’re hoping your expertise can uncover ways to make advanced analysis easier. Dozens more tasks, of varying size, can be found in our open-source repositories on [GitHub](https://github.com/california-civic-data-coalition).

### Challenge #1: Automate the standardization of campaign donors

There is no master list of the people who fund California’s political campaigns, only the jumbled, misshapen and sometimes deliberately obscured data punched into the [disclosure forms](http://cal-access.ss.ca.gov/PDFGen/pdfgen.prg?filingid=1932072&amendid=0) required by state law.

For instance, Charles Munger Jr., a [top backer](http://www.latimes.com/local/politics/la-me-adv-munger-20150304-story.html#page=1) of California’s Republican Party, has had more than 150 different combinations of his name, occupation, employer and address listed at one time or another.

Most researchers and journalists now resort to time-consuming, error-prone, one-off, brute force methods to merge variations and clean data for analysis.

We need a better way, and it must be automated. We need an algorithm or machine-learning routine that can identify likely variations, allow for the input of human decision making, and automatically reapply judgements across a large data set that updates daily.

Download a list of [1.9 million unique names](https://dl.dropboxusercontent.com/u/3640647/2015-calaccess-challenge/contributors.csv) extracted from the state database. See what you can do.

### Challenge #2: Identify a relevant state law or past corruption scandal, develop an algorithm to detect it

Campaign finance data is used routinely by journalists and regulators to document evidence of corruption in the political process. But the tip typically comes from a human source and is then pinned down piecemeal using public records. The findings are almost always narrow and limited to a single person or group.

We want to know: Could corruption be discovered faster, sooner and more broadly with well-tailored algorithmic analysis?

Past scandals can serve as a useful model. Could the evidence in the following cases been discovered by a well crafted database query, which could then be used to uncover other unknown cases?

* Millions of dollars in “dark money” funneled into ballot measures, like those concealed in 2012 by the notorious [Sean Noble](http://www.propublica.org/article/the-dark-money-man-how-sean-noble-moved-the-kochs-cash-into-politics-and-ma).
* [Illegal laundering](http://www.latimes.com/local/la-me-ethics-berryhill-20140425-story.html) of campaign contributors via party committees in 2008 by state Sen. Tom Berryhill.
* Embarrassing use of campaign funds for luxury travel and spending by [former Speaker Fabian Nunez](http://articles.latimes.com/print/2007/oct/05/local/me-nunez5) and current [state Sen. Isadore Hall III](http://www.latimes.com/local/politics/la-me-pol-isadore-hall-20141130-story.html).

Download this list of [2.5 million campaign expenditures](https://dl.dropboxusercontent.com/u/3640647/2015-calaccess-challenge/expenditures.csv). Can you find the lavish spending of Nunez and Hall? Is there a pattern in their paper trail that can be detected automatically?

### Challenge #3: Reconcile officeholders with a canonical identifier

The state database does not include a unique identifier that allows the campaign activity of officeholders to be connected to other valuable datasets, like voting records, ideological ratings and financial disclosure forms.

It also lacks basic metadata about officials such as age, gender and race. And state officials have [withheld](http://www.californiacivicdata.org/2015/02/17/opennews-scrapers/) crucial data that would make connecting the dots easier.

But thanks to valuable code contributions at [a recent hackathon](http://www.californiacivicdata.org/2015/02/17/opennews-scrapers/), we have extracted a short list of the most important campaign filers.

Your task is to try to reconcile [that list](https://dl.dropboxusercontent.com/u/3640647/2015-calaccess-challenge/candidates.csv) with the [“Open States” identifiers](http://openstates.org/downloads/) developed by the Sunlight Foundation. Then our data can be linked to other sources that use Sunlight's system.

### Challenge #4: Propose a network model or statistic for meaningful analysis of relationships

With thousands of donors and complex coalitions, political movements are difficult to map and understand. We need better tools for probing the immense amount of network connections recorded in campaign finance and lobbying data.

Carefully connecting dots has shown how creative accounting can conceal [organized efforts](http://www.latimes.com/local/politics/la-me-ff-pol-1101-proposition47-20141101-story.html#page=1) behind high-stakes ballot measures and [what really decides](http://cironline.org/reports/california-speaker-gives-assemblys-juiciest-jobs-biggest-fundraisers-4501) who gets important appointments. But few comprehensive indicators exist for routinely mapping the political landscape to visualize its shape.

Draft a schema for modeling the network connections between parties, PACs, candidates, lobbyists, donors and expenditures in the state database, or propose a new statistic, like the [Bedfellows score](https://source.opennews.org/en-US/articles/introducing-bedfellows/) developed by The New York Times, to measure and understand these relationships.
