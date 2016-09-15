---
layout: post
title: "Introducing our new CAL-ACCESS bulk downloads website"
deckhead: "California campaign finance and lobbyist disclosure data never looked so good."
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/), [Cheryl Phillips](http://www.twitter.com/cephillips), [Aaron Williams](http://aboutaaron.com/), [Jennifer LaFleur](https://twitter.com/j_la28), [James Gordon](https://twitter.com/je_gordon) and [Sahil Chinoy](http://sahilchinoy.com/)"
image:
published: false
---

Today we're launching our new bulk downloads website, the only online destination with hassle-free access to bulk California campaign finance and lobbyist disclosure data.

<figure style="margin: 8px 0;">
    <img src="/img/dl_site_homepage.png" width="100%;">
</figure>

Until now, reporters and researchers investigating the role of money in California politics have been limited to the official CAL-ACCESS database export published on the California Secretary of State's website.

We've built something better.

Instead of forcing you to download a 750 MB zip just to get the one or two data files you want, you can download each data file from our website or, if you like, all the data files zipped together.

<figure style="margin: 8px 0;">
    <img src="/img/archived_files.png" width="100%;">
</figure>

Instead of sprinkling in parsing errors that corrupt analysis or simply block loading into database managers, we publish files cleaned by our raw-data app. All parsing errors are either fixed or segmented into a separate error log, which is also available to download (for the super data-mungers).

<figure style="margin: 8px 0;">
    <img src="/img/errata.png" width="100%;">
</figure>

Instead of overwriting the current database snapshot every single day, we automatically archive the original source files, our cleaned files and the error logs. If you want to rewind CAL-ACCESS to yesterday, last week or a month ago, we've got you covered.

<figure style="margin: 8px 0;">
    <img src="/img/archived_zips.png" width="100%;">
</figure>

Instead of digging through PDF upon PDF of outdated, contradictory and cryptic documentation, our extensive explanations of each file, field and lookup code are linked in at every turn.

<figure style="margin: 8px 0;">
    <img src="/img/file_details.png" width="100%;">
</figure>

And we've documented each form submitted by campaigns and lobbyists, broken them down by section and linked them to database tables where their information is stored. Because, as far as we know, no one else has ever bothered.

<figure style="margin: 8px 0;">
    <img src="/img/form_details.png" width="100%;">
</figure>

## API-like access at calaccess.download

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

## What's next

For newcomers to the weird little universe of CAL-ACCESS, a lot of this still might seem rather intimidating. Not to worry, we are already hard at work chiselling easy-to-understand data models out of CAL-ACCESS' convoluted structure.

Stay tuned for more. Or if your feeling bold, we would love your help. Head over to our processed-data app repo where all the excitement is currently happening.

## T-shirt contest

Our new logo is :fire: right?

<figure style="margin: 8px 0;">
    <img src="/img/geo_bear.png" width="100%;">
</figure>

But wouldn't it be :fire::fire: if it were on a t-shirt?

<figure style="margin: 8px 0;">
    <img src="/img/tshirt.png" width="100%;">
</figure>

BUT wouldn't it be :fire::fire::fire: if it were on YOUR t-shirt?

This could really happen. The first five people who file a confirmed bug on our website win a t-shirt with our new logo.

Ready, set, go!
