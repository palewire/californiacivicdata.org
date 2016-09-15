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

## First, making access easy

As of this morning, the latest state data is downloaded, parsed, cleaned and republished each day at [calaccess.californiacivicdata.org/downloads/latest/](http://calaccess.californiacivicdata.org/downloads/latest/).

There you can download the entire dump, or just the files you want. The numerous
errors that litter the source files have been eliminated. The data are converted to simple flat files of comma-separated values,
easily imported to spreadsheets and other database software.

<figure style="margin: 28px 0;">
    <a href="http://calaccess.californiacivicdata.org/downloads/latest/">
        <img src="/img/archived_files.png" style="border: 1px solid #ddd;">
    </a>
    <figcaption style="text-align:right;">Download individual raw files or a ZIP of everything.</figcaption>
</figure>

## Second, archiving everything

We also automatically archive each day's source files. That is unlike the state dump, which officials overwrite each day.

If you want to rewind CAL-ACCESS to yesterday, last week or a month ago, [we've got you covered](http://calaccess.californiacivicdata.org/downloads/). We plan to save and serve each day's data into the foreseeable future.

<figure style="margin: 8px 0;">
    <a href="http://calaccess.californiacivicdata.org/downloads/">
        <img src="/img/archived_zips.png" width="100%;">
    </a>
    <figcaption style="text-align:right;">We're archiving ever database snapshot in case anyone ever needs to rewind the CAL-ACCESS clock.</figcaption>
</figure>

## Third, cracking the codes

Instead of digging through PDF upon PDF of outdated, contradictory and cryptic documentation, our extensive explanations of each file, field and lookup code are linked in at every turn.

<figure style="margin: 8px 0;">
    <img src="/img/file_details.png" width="100%;">
    <figcaption style="text-align:right;">Our comprehensive docs will help you traverse the wilderness of CAL-ACCESS.</figcaption>
</figure>

And we've documented each form submitted by campaigns and lobbyists, broken them down by section and linked them to database tables where their information is stored. Because, as far as we know, no one else has ever bothered.

<figure style="margin: 8px 0;">
    <img src="/img/form_details.png" width="100%;">
    <figcaption style="text-align:right;">Connecting the CAL-ACCESS tables to the filing forms has helped up map origin story of the data.</figcaption>
</figure>

## Fourth, establishing a simple API

Obviously, we think the design of our new bulk downloads site is prrrreeeetty hot (I mean, have you SEEN our new logo?!). But some nerds just wanna shell.

We get it, and that's why we've made all our downloads available at stable and concise URLs so that you can download and unzip the latest full zip:

```bash
$ curl -O http://calaccess.download/latest/clean.zip
$ unzip clean.zip
```

Or fetch the campaign disclosure sheets file and filter to only the Form 460 and save them to their own file:

```bash
$ curl http://calaccess.download/latest/cvr_campaign_disclosure_cd.csv | csvgrep -c FORM_TYPE -m F460 > f460_cvrs.csv
```

## Fifth, charting the course ahead

For newcomers to the weird little universe of CAL-ACCESS, a lot of this still might seem rather intimidating. Not to worry, we are already hard at work chiselling easy-to-understand data models out of CAL-ACCESS' convoluted structure.

Stay tuned for more. Or if your feeling bold, we would love your help. Head over to our processed-data app repo where all the excitement is currently happening.

## Finally, how you can play and win

Our new logo is :fire: right?

<figure style="margin: 8px 0;">
    <img src="/img/geo_bear.png" width="100%;">
    <figcaption style="text-align:right;">This is geo-bear.</figcaption>
</figure>

But wouldn't it be :fire::fire: if it were on a t-shirt?

<figure style="margin: 8px 0;">
    <img src="/img/tshirt.png" width="100%;">
    <figcaption style="text-align:right;">This is geo-bear on a t-shirt.</figcaption>
</figure>

BUT wouldn't it be :fire::fire::fire: if it were on YOUR t-shirt?

This could really happen. The first five people who file a confirmed bug on our website win a t-shirt with our new logo.

Ready, set, go!
