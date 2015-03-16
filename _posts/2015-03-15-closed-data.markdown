---
layout: post
title: "California secretary of state refuses to open arcane data systems"
deckhead: "We asked Alex Padilla's office to show us how to use their database tracking money in politics. They said no."
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/)"
image: "http://www.californiacivicdata.org/img/ask-matt-share.png"
published: true
---

<figure style="margin: 8px 0 0 10px; float:right;">
    <img alt="Alex Padilla" title="Alex Padilla" src="/img/alex-padilla.jpg" height="150">
    <figcaption style="text-align:center;">Alex Padilla</figcaption>
</figure>

The office of California Secretary of State Alex Padilla has refused our request for the computer code that accurately extracts data from the state's campaign finance and lobbying activity database.

[Last year](http://www.californiacivicdata.org/2014/09/24/hello-world/), we began an effort to create open-source software that makes it easier to access and understand a raw copy of the database, known as CAL-ACCESS, [published online](http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/) by Padilla's predecessor.

During careful study of the sprawling dump, which includes more than 36 million records spread across 76 interlocking database tables, we discovered that sophisticated filters, links and transformations are necessary to follow the millions of dollars that oil the statehouse in Sacramento.

We also found the [database documentation](http://django-calaccess-raw-data.readthedocs.org/en/latest/officialdocumentation.html) released by the state insufficient, offering fragmentary and incomplete explanations of how to work with the data.

Many database tables have been defined only by [cryptic references](https://www.documentcloud.org/documents/1308002-cal-access-about.html#document/p107) to characters named "Matt," "D H," J M" and "Cox."

<figure>
    <img alt="An example of what to expect" src="/img/ask-matt.jpg" style="width:100%;">
    <figcaption>An example of what to expect</figcaption>
</figure>

Further, some important elements of the database have been excluded entirely, like [the crucial connections](http://www.californiacivicdata.org/2015/02/17/opennews-scrapers/) that link campaign fundraising committees to elected officeholders and high-stakes ballot initiatives.

The result: A high barrier before anyone seeking to interpret the data, requiring weeks of study and significant guesswork to overcome, while raising the menacing risk that uninitiated analysts will make a grievous error.

In an effort to solve the problem, last month we utilized the California Public Records Act [to request](https://www.foiamachine.org/requests/3307/) that state officials release the computer code that supplies data to the state's searchable user-interface at [cal-access.ss.ca.gov](http://cal-access.ss.ca.gov/default.aspx).

While the tools provided by the state site are limited, the codebase that powers it should include a negotiation of the underlying CAL-ACCESS database that returns accurate data.

On March 2, that request was denied by an anonymous email account, [constituent.affairs@sos.ca.gov](mailto:Constituent.Affairs@sos.ca.gov).

"This source code is computer software that is not a public record pursuant to Government Code Section 6254.9 and, therefore, is not subject to disclosure requirements of the California Public Records Act," the response said.

That same day we responded with disappointment and requested that Padilla's office reconsider its decision. We have yet to receive a reply.