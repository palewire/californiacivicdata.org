---
layout: post
title: "ONA attendees map dozens of crucial CAL-ACCESS database keys"
deckhead: "California Code Rush 3 sprinted past another milestone thanks to ONA 2015 volunteers"
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/)"
image: http://www.californiacivicdata.org/img/code-rush-3-share.jpg
published: true
---

Last week our team was at the Online News Association conference,
an annual gathering of digital journalists from across America and the world.

<img src="/img/coderush3.png" height="200" style="margin: 8px 0 8px 14px; float:right;">

This year the event was held in [Los Angeles](http://ona15.journalists.org/). So we didn't have to travel far to launch our third California Code Rush.

It's a simple idea. We bring a pile of tickets for improvements to our open-source software
for an informal twist on the classic code sprint.

And it comes a simple pitch: Submit a patch, win a prize.

We had so much fun trying it [at this year's NICAR conference](http://www.californiacivicdata.org/2015/03/11/code-rush-recap/) and again at [Media Party in Buenos Aires](http://www.californiacivicdata.org/2015/09/01/code-rush-2-recap/) that we decided to do it again.

As expected, the nerds came through. By the end of the conference,
20 different people from around the world contributed more than 115 code commits.

It added up to enough to meet our goal for the event: To fully document
the database fields guaranteed to be unique for each of the 76 tables in CAL-ACCESS, the sprawling database that tracks money in California politics.

The technical term for this kind of thing is a ["unique key"](https://en.wikipedia.org/wiki/Unique_key). It sounds arcane, but it's very important to database analysis (ask the nearest nerd).

Having all the keys mapped out opens new possibilities for our project, like more rapid syncing of the daily updates to the data and integration of the next-generation [dat](http://dat-data.com/) version-control system.

The work of untangling and explaining the state's system is far from finished
but important information that was buried in PDFs is now merged with our code and [republished in searchable form on the open web](http://django-calaccess-raw-data.californiacivicdata.org/en/latest/models.html).

<figure style="width:350px; float:left; margin: 8px 14px 8px 0;">
    <img alt="The California Code Rush table on the Midway at ONA 2015" title="The California Code Rush table on the Midway at ONA 2015" src="/img/code-rush-3-action.jpg" style="">
    <figcaption style="text-align:left; margin-top:3px;">Volunteers join the California Code Rush</figcaption>
</figure>

Many contributors &mdash; like Julie Westfall, [Nikki Usher Laysar](https://twitter.com/nikkiusher/status/647519162198175745) and Tami Abdollah &mdash; made their first open-source commit by looking up and documenting a unique key.

Others, like Honest Charley Bodkin and [Douglas Arellanes](https://twitter.com/dougiegyro/status/647452005800108032), moved the needle by shoveling in multiple additions.

By the end of the drive, our GitHub [activity charts](https://github.com/california-civic-data-coalition/django-calaccess-raw-data/graphs/contributors) spiked and the total number of contributors to our effort reached 95 people.

As our project ramps up after being [named a winner](http://www.californiacivicdata.org/2015/07/22/knight-news-challenge/) of the 2015 Knight News Challenge, we're planning to host a series of similar code sprints in the next year where developers, academics and journalist collaborate with our core team. We hope to see you there!
