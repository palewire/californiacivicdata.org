---
layout: post
title: "California secretary of state refuses to open arcane data systems"
deckhead: "We asked Alex Padilla's office to show us how to use their database tracking money in politics. They said no."
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/)"
published: true
---

The California Secretary of State's office has refused our request for the computer code that accurately extracts data from CAL-ACCESS, the state's campaign finance and lobbying activity database.

[Last year](http://www.californiacivicdata.org/2014/09/24/hello-world/), we began an effort to create open-source software that makes it easier to access and understand a raw copy of the database [published online](http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/).

During careful study of the sprawling dump, which includes more than 36 million records spread across 76 interlocking database tables, we discovered that sophisticated filters, links and transformations are necessary to follow the money that oils the statehouse in Sacramento.

We also found that the [database documentation](http://django-calaccess-raw-data.readthedocs.org/en/latest/officialdocumentation.html) released by the state was insufficient, providing fragmentary and incomplete explanations of how to work with the system.

Because the database techniques used by the state's public-facing CAL-ACCESS website are not documented, significant guesswork is necessary when working with the bulk data.

That creates needless barriers before the public can interpret the data and introduces a huge risk that those working with the files you've released will introduce error.

Outline
------

- The SoS has denied our request
- What we asked for
- Explain why it matters
- What they said
- Link to the full exchange on documentcloud
- This create needless obstacles between the public and the data.
- It now requires weeks or months of work to master the ins and outs
of the database
- The documentation they have is incomplete and doesn't explain usage
or how to properly calculate totals
- "Ask Matt"
- It claims to be a full dump, but isn't
- How the election and ballot measure links are not in the "full" dump
- That had to be

