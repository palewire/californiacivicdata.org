---
layout: post
title: "Introducing the new CAL-ACCESS bulk downloads website"
deckhead: "Raw California campaign finance and lobbyist disclosure data never looked so good."
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/), [Cheryl Phillips](http://www.twitter.com/cephillips), [Aaron Williams](http://aboutaaron.com/), [Jennifer LaFleur](https://twitter.com/j_la28), [James Gordon](https://twitter.com/je_gordon) and [Sahil Chinoy](http://sahilchinoy.com/)"
image:
published: false
---

Today we're launching our new bulk downloads website, the only online destination with hassle-free access to bulk California campaign finance and lobbyist disclosure data.

Up until now, reporters and researchers investigating the role of money in California politics have been limited to the official CAL-ACCESS database export published on the California Secretary of State's website.

We've built something better.

Instead of forcing you to download a 750 MB zip just to get the one or two data files you want, you can download each data file from our website or, if you like, all the data files zipped together.

Instead of sprinkling in parsing errors that corrupt analysis or simply block loading into database managers, we publish files cleaned by our raw-data app with the parse errors fixed or segmented into a separate error log (for the super datamungers).

Instead of overwriting the current database snapshot of every day, we automatically archive the original source files, our cleaned files and the error logs.

Instead of digging through PDF upon PDF of outdated, contradictory and cryptic documentation, our extensive explanations of each file, field and lookup code are linked in at every turn.

And we've documented each form submitted by campaigns and lobbyists, broken them down by section and linked them to database tables where their information is stored. Because, as far as we know, no one else has ever bothered. 

## API-like access at calaccess.download

Obviously, we think the design of our new bulk downloads site is prrrreeeetty hot (I mean, have you SEEN our new logo?!). But some nerds just wanna shell. We get it, and that's why we've made all our files available at stable and concise URLs so that you can download and unzip the latest full zip:

```bash
$ curl -O http://calaccess.download/latest/clean.zip
$ unzip clean.zip
```

Or download the cover sheets of all the campaign disclosure filings and pipe them into csvkit:

```bash
```

## What's next

For those who are new to the weird little universe of CAL-ACCESS, we suspect a lot of this is all still pretty intimidating. Not to worry, we're already hard at work chiselling easy-to-understand models out of the original crazy database structure.

Stay tuned for more. Or if you want to help, we would welcome your input. Head over to our processed-data app repo.

## T-shirt contest

Our new logo :fire: right?

But wouldn't it be :fire::fire: if it were on a t-shirt?

BUT wouldn't it be :fire::fire::fire: if it were on YOUR t-shirt?

This could really happen. The first five people who file a confirmed bug win a t-shirt with our new logo.

Ready, set, go!
