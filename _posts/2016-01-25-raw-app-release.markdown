---
layout: post
title: "New calaccess_raw app release boasts more command options, more flexibility for users"
deckhead: "Our contributors made these improvements possible"
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/), [Cheryl Phillips](http://www.twitter.com/cephillips), [Aaron Williams](http://aboutaaron.com/), [Jennifer LaFleur](https://twitter.com/j_la28) and [James Gordon](https://twitter.com/je_gordon)"
published: True
---

<img style="-webkit-user-select: none; cursor: zoom-in;" src="/img/cli_2.gif" width="543" height="97">

Today we're releasing version 0.2.0 of our [software](http://django-calaccess-raw-data.californiacivicdata.org/en/latest/) for downloading, cleaning and loading raw campaign finance and lobbying data.

The goal of our app is simple: Make access to the raw data in [CAL-ACCESS](http://cal-access.ss.ca.gov/) -- Califonia's overwhelming and jumbled campaign finance database -- as simple as a few keystrokes. And with the improvements included in this release, our users now have greater control over the flow of the data pipeline.

We owe a big shout-out and thank you to contributors who've volunteered their time and energy to our project. In particular [Ben Cipilloni](https://github.com/bcipolli/) and [Aaron Borden](https://github.com/adborden) authored or instigated many of these improvements. Ben and Aaron are both doing great work with groups like CA Civic Lab and OpenOakland, who focus on the influence of money in local elections. 

We appreciate your help and feedback and look forward to more of the same.

Here's an overview of the changes in this release:

*	The `downloadcalaccessrawdata` command has a narrower purpose: Downloading and unzipping the CAL-ACCESS database;
*	If your download is interrupted, you can restart were you left off by invoking the `--resume-download` option;
*	We're introducing an `updatecalaccessrawdata` command that performs all the actions of downloading, cleaning and loading the raw data into your own database;
*	You can now load into any database configured in your Django project by invoking the `--database` command line option;
*	The `loadcalaccessrawfile` command takes a `--csv` option that in case you need to load from another source file into our data models;
*	Since we're downloading and processing up to 12 GB of data and diskspace is an issue for some of our users, each of the app's commands will clear out the original and intermediate processing files. If you'ld prefer to keep these files, you can invoke the `--keep-files` option when running these commands.

These features were added as we've future-proofed our code by bringing it inline with Python's [Pep 8](https://www.python.org/dev/peps/pep-0008/) style guide and the latest versions of our adopted framework, [Django](https://www.djangoproject.com/).

As we continue to make progess, our full team has been hammering out a roadmap for the work ahead. This includes milestones we expect to hit as the 2016 primary and general elections approach. We'll keep you posted on the details.
