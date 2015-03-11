---
layout: post
title: Lessons from the first California Code Rush
deckhead: We brought buggy code, dozens of open tickets and a motherlode of Cali swag to NICAR 2015. You'll never guess what happened next.
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/) and [Aaron Williams](http://aboutaaron.com/)"
image: http://www.californiacivicdata.org/img/code-rush-nicar15.jpg
published: true
---

Last week our team converged on the annual National Institute for Computer-Assisted Reporting Conference (NICAR) in Atlanta. We brought with us our California campaign finance code, dozens of open tickets, a pile of prizes and a weird idea.

<img alt="California Code Rush logo" title="California Code Rush logo" src="/img/coderush.png" height="150" style="margin: 6px 0 6px 10px; float:right;">

The pitch was simple. Submit a patch, win a prize. The bigger the challenge, the bigger the prize. We called it the [California Code Rush](http://localhost:4000/2015/02/26/code-rush/).

We didn't know what to expect. Where would we set up? Would anyone pay attention? Could we convince busy conference goers to sit down and spend even a few minutes with our crappy code?

But, as usual, the NICAR crowd came through. By the end of the weekend, our movable hackathon had set up shop in nooks and crannies all across the conference hotel, pulling 200+ commits from more than 40 different contributors.

<figure>
    <img alt="An popup session on Saturday at NICAR 2015" title="A popup session on Saturday at NICAR 2015" src="/img/code-rush-nicar15.jpg" style="width:100%;">
    <figcaption>Photo by <a href="https://twitter.com/macdiva">Chrys Wu</a></figcaption>
</figure>

Most patches were small, newbies making their first ever open-source commit by improving our documentation of the state's massive database.

Others contributions were large, experienced developers landing significant contributions to the code base.

* [Eric Richardson](http://ewr.is/) of Southern California Public Radio developed a tool to [slice sample data](https://github.com/california-civic-data-coalition/django-calaccess-raw-data/pull/199) for unit tests.
* Vox's [Casey Miller](http://caseymmiller.com/) created [custom icons](https://github.com/california-civic-data-coalition/django-calaccess-campaign-browser/commit/79339e2b31b167211966b0c318198a65f2093106) for each political party.
* [Matt Montgomery](https://github.com/mattmontgomery) of Deseret Digital Media [improved the logging](https://github.com/california-civic-data-coalition/django-calaccess-raw-data/pull/183) of data discarded during the database loading routine.
* [Justin Myers](http://www.justinmyers.net/) of the Associated Press provided [Python 3 support](https://github.com/california-civic-data-coalition/django-calaccess-raw-data/pull/220#issuecomment-78315523).

It was exciting to work with so many smart people. But the real highlight came Saturday night.

That's when we showed our thanks by raffling off a motherlode of swag for the volunteers who contributed code. We gave away California coffee beans, beers, habanero and piles of street style.

<figure>
    <img alt="An popup session on Saturday at NICAR 2015" title="A popup session on Saturday at NICAR 2015" src="/img/code-rush-winners.png" style="width:100%; border:1px solid black;">
</figure>

By the time the conference ended Sunday, we had merged a handful of significant features, helped dozens of people make their first ever open-source commits and introduced our project to hundreds more.

Here's what we learned along the way.

Five lessons
------------

**01. We had two audiences.** One of the things that makes NICAR great is that it brings together a wide variety of people with a range of skills and interests.

We were able to connect to two different groups: Beginners curious to learn how GitHub and open source works; and seasoned hackers who want to flex their muscles.

**02. We could serve both.** In hindsight, the most important thing we did was arrive at the conference with dozens of tickets already defined.

The bigger ones gave the experienced hackers a concrete problem to plug in on.

The little ones &mdash; typically asking for the transfer of a table definition from the state's database documentation into our code &mdash; offered a easy way for newbies to experience the open-source process, an effort made even easier by GitHub's excellent [in-browser editor](https://help.github.com/articles/editing-files-in-your-repository/).

**03. A scheduled time and space helped.** On the conference's second day, we had four hours set aside in the "commons" area outside of the conference rooms where the traditional panels were held.

Promoting that time in the program and via social media drew more than dozen people at the start of the time slot. A TV stationed in the area allowed us to screencast a GitHub walkthrough for beginners.

Most eventually wandered off after landing their first commit and the space transitioned into a more traditional hackathon with a small group of experienced developers working quietly. But the location allowed us to draw in new people each hour as the panel sessions let out.

**04. Hallway conversations often converted into one-on-one instruction.** One of the best features of NICAR is spending time chatting in the hallway. The open-ended design of the contest allowed us to bring up the topic in casual conversation and, if the other person was interested, sit down and knock out a patch right there.

**05. It never hurts to ask. People will surprise you.** You shouldn't underate the intrinisic appeal of public-service software projects. People like doing good things and open source presents a great opportunity to help them do it. If you have a new project, file a dozen tickets and see who shows up.

On that topic, we've still got [plenty of tickets left](https://github.com/california-civic-data-coalition/django-calaccess-raw-data/issues). Close one this week and we will send you one of our remaining [limited-edition stickers](/img/coderush.png).