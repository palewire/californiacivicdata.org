---
layout: post
title: "Introducing a new bulk downloads site tracking money in California politics"
deckhead: "Check out the beta version of our online archive and walk away with a prize."
byline: "By [James Gordon](https://twitter.com/je_gordon), [Aaron Williams](http://aboutaaron.com/), [Sahil Chinoy](http://sahilchinoy.com/), [Ben Welsh](http://palewi.re/who-is-ben-welsh/) and the [California Civic Data Coalition](/about/)"
image: http://www.californiacivicdata.org/img/dl_site_homepage.png
published: true
---

Today we're launching an expansion of this site, remaking it as the only destination offering hassle-free access to the bulk data tracking money in California politics.

Until now, analysts investigating the role of lobbyists and campaign donors at the Sacramento statehouse have been limited to an [unwieldy dump from CAL-ACCESS](http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/), the jumbled, dirty and difficult database maintained by California's Secretary of State.

[We've built something better](http://www.californiacivicdata.org/). And we've got even more in the works.

### First, making access easy

As of this morning, the latest state data are downloaded, parsed, cleaned and republished each day at <span style="word-wrap: break-word;">[calaccess.californiacivicdata.org/downloads/latest/](http://calaccess.californiacivicdata.org/downloads/latest/).</span>

There you can download the entire dump, or just the files you want. The numerous
errors that litter the source files have been eliminated. The data have been converted to simple flat files of comma-separated values,
easily imported to spreadsheets and other database software.

<figure style="margin: 28px 0 8px 0;">
    <a href="http://calaccess.californiacivicdata.org/downloads/latest/">
        <img src="/img/latest_download.png">
    </a>
    <figcaption style="text-align:right;">Download individual raw files or a ZIP of everything.</figcaption>
</figure>

### Second, archiving everything

We also automatically archive each day's source files. That is unlike the state dump, which officials overwrite each day.

If you want to rewind CAL-ACCESS to yesterday, last week or a month ago, [we've got you covered](http://calaccess.californiacivicdata.org/downloads/). We plan to save and serve each day's data into the foreseeable future.

<figure style="margin: 28px 0 8px 0;">
    <a href="http://calaccess.californiacivicdata.org/downloads/">
        <img src="/img/archived_zips.png" width="100%;">
    </a>
    <figcaption style="text-align:right;">We're archiving every database snapshot in case anyone ever needs to rewind the CAL-ACCESS clock.</figcaption>
</figure>

### Third, cracking the codes

The CAL-ACCESS database is one of the most confusing systems we’ve ever encountered. California's Secretary of State Alex Padilla
has called it ["a Frankenstein monster of code."](http://www.sacbee.com/news/politics-government/capitol-alert/article49257065.html)

To spare anyone else from having to sift through the state's outdated, incomplete and inconsistent [documentation](http://calaccess.californiacivicdata.org/documentation/calaccess-official-documentation/) ever again, we’ve compiled simple searchable explanations for each of the system’s [80 data tables](http://calaccess.californiacivicdata.org/documentation/calaccess-files/) and [42 forms](http://calaccess.californiacivicdata.org/documentation/calaccess-forms/).

Thanks to the more than 150 volunteers who have contributed to our project over the past two years, each file, field and lookup code is now linked online.

<figure style="margin: 28px 0 8px 0;">
    <a href="http://calaccess.californiacivicdata.org/documentation/calaccess-files/debt-cd/">
        <img src="/img/file_details.png" width="100%;">
    </a>
    <figcaption style="text-align:right;">Our comprehensive docs will help you traverse the wilderness of CAL-ACCESS.</figcaption>
</figure>

### Fourth, establishing a simple API

Repeat visitors can probably tell we've put a lot of effort into Aaron Williams's redesign for the site. But beneath the surface
is something more: The foundation of a new [web API](https://en.wikipedia.org/wiki/Web_API) that aims to improve access
not just for people, but for the scripts they write as well.

All of our downloads are now available at stable and concise URLs at a new domain, calaccess.download.

That means you can always download and unzip the latest full archive from your terminal like this:

<input type="text" class="download-link input-monospace" style="font-size:14px;" value="curl -O http://calaccess.download/latest/clean.zip && unzip clean.zip" readonly="">

Or, to be a little more creative, fetch the [campaign disclosure cover sheets file](http://calaccess.californiacivicdata.org/documentation/calaccess-files/cvr-campaign-disclosure-cd/) and filter it down to only filings of [Form 460](http://calaccess.californiacivicdata.org/documentation/calaccess-forms/f460/), saving the result to a new file:

<input type="text" class="download-link input-monospace" style="font-size:14px;" value="$ curl http://calaccess.download/latest/cvr_campaign_disclosure_cd.csv | csvgrep -c FORM_TYPE -m F460 > f460_cvrs.csv" readonly="">

### Fifth, charting the course ahead

We're proud of what we've put together. But our work is far from finished.

For newcomers, the odd structure of the CAL-ACCESS database's source files remains a significant obstacle.

But don't worry, our team is on it. We're already hard at work chiseling easy-to-understand files that simplify the system's convoluted structure.

Look for those to arrive in the coming weeks, or jump into the embryonic [django-calaccess-processed-data](https://github.com/california-civic-data-coalition/django-calaccess-processed-data) code repository where that work is happening.

### Finally, how you can play and win

Our new logo is :fire: right?

<figure style="margin: 28px 0;">
    <img src="http://www.californiacivicdata.org/img/geobear.svg" width="100%;">
    <figcaption style="text-align:right;">This is geo-bear. Aaron Williams made him.</figcaption>
</figure>

But wouldn't it be :fire::fire: if it were on a t-shirt?

<figure style="margin: 28px 0;">
    <img src="/img/tshirt.png" width="100%;">
    <figcaption style="text-align:right;">This is geo-bear on a t-shirt. Thomas Suh Lauder made it.</figcaption>
</figure>

BUT wouldn't it be :fire::fire::fire: if it were on YOUR t-shirt?

This can happen. The first five people who visit GitHub and file a confirmed bug report or merged pull request for [our open-source website](https://github.com/california-civic-data-coalition/django-calaccess-downloads-website) win a t-shirt with our new logo.

See you there.
