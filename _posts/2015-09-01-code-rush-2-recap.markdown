---
layout: post
title: "Volunteers finish decoding 1,400 cryptic CAL-ACCESS database fields"
deckhead: "California Code Rush 2 met documentation milestone at Media Party 2015"
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/)"
image: http://www.californiacivicdata.org/img/code-rush-2.jpg
published: true
---

Last week I visited Buenos Aires to take part in Media Party 2015, the [annual conference](mediaparty.info) put on by the bustling local chapter of [Hacks/Hackers](http://www.meetup.com/HacksHackersBA/).

<img src="/img/coderush2.png" height="200" style="margin: 8px 0 8px 14px; float:right;">

Along with my luggage, I packed hundreds of tickets for improvements to
our open-source software and a simple pitch: Submit a patch, win a prize.

It's an idea we call the California Code Rush, an informal variation on the classic
code sprint. We had so much fun trying it for [the first time](http://www.californiacivicdata.org/2015/03/11/code-rush-recap/) at this year's NICAR conference, we decided to do it again with [California Code Rush 2](http://www.californiacivicdata.org/2015/08/18/code-rush-2/) in Buenos Aires.

As expected, our industrious community rose to the challenge. By the end of the conference,
27 different people from around the world contributed more than 250 code commits.

It added up to enough to meet the milestone we set: To fully document
the more than 1,400 fields in CAL-ACCESS, the sprawling database that tracks money in
California politics.

<figure>
    <img alt="The California Code Rush table at the Saturday hackathon at Media Party 2015" title="The California Code Rush table at the Saturday hackathon at Media Party 2015" src="/img/code-rush-2.jpg" style="width:100%;">
    <figcaption>A team of volunteers join the California Code Rush at Media Party 2015</figcaption>
</figure>

The work of untangling and explaining the state's system is far from finished
but important information that was buried in PDFs is now merged with our code and [republished in searchable form on the open web](http://django-calaccess-raw-data.californiacivicdata.org/en/latest/models.html).

Many contributors &mdash; like [Flor Coelho](https://twitter.com/palewire/status/637298806741168128) and [Ron Figueroas](https://twitter.com/palewire/status/637635368037294080) &mdash; made their first open-source commit by looking up
and documenting a database field.

Others, like [Luciana Godoy](https://about.me/tocateunvals), [Burt Herman](http://burtherman.com/) and [Douglas Arellanes](https://github.com/SourceDouglas), distinguished themselves by shoveling in dozens of additions.

[Tara Adiseshan](http://www.taraadiseshan.com/), an OpenNews Fellow, decoded the industry and business codes from lobbyist registration forms and integrated them into our application.

[Daniel Cloud](http://danielcloud.org/), a veteran of The Sunlight Foundation, [dug deep](https://github.com/california-civic-data-coalition/django-postgres-copy/pull/14) into our Python wrapper on PostgreSQL's bulk loading command to make a crucial fix.

Tomás Wehner, an 18-year-old hacker interested in news, [redesigned](https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/toolbox/templates/toolbox/models.rst) our database documentation to be more compact and legible.

By the end of the drive, our GitHub contribution charts spiked to a new high and the total number of outside contributors to our open-source effort topped 75 people.

<figure>
    <a href="https://github.com/california-civic-data-coalition/django-calaccess-raw-data/graphs/contributors">
        <img alt="At right, a spike of activity on one of our GitHub repositories triggered by the code rush" title="At right, a spike of activity on one of our GitHub repositories triggered by the code rush" src="/img/code-rush-2-chart.png" style="width:100%; border:0;">
    </a>
    <figcaption>At right, a spike of activity on one of our GitHub repositories triggered by the code rush</figcaption>
</figure>

As our project ramps up after being [named a winner](http://www.californiacivicdata.org/2015/07/22/knight-news-challenge/) of the 2015 Knight News Challenge, we're planning to host a series of similar code sprints in the next year where developers, academics and journalist collaborate with our core team. I hope to see you there!
