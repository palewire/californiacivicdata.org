---
layout: post
title: "Our downloads are now served with CORS"
deckhead: "Dig into Coalition data from any domain"
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/)"
image: http://www.californiacivicdata.org/img/stanford-hack-day.jpg
published: true
---

All data downloads offered by the California Civic Data Coalition are now served with cross-origin resource sharing allowed, opening our site for creative use in dynamic web applications.

Also known as "CORS," [cross origin resource sharing](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) is an Internet publishing standard that allows code running on other sites to freely request and integrate data.

This change was made to allow an experimental integration with [Observeable](https://beta.observablehq.com), the promising new interactive notebook for developing data-driven applications in the cloud.

Now that we're publishing with CORS, JavaScript code written at Observable, or any other site, can pull data directly from URLs on our [downloads page](https://calaccess.californiacivicdata.org/downloads/latest/).

<figure style="margin: 25px 0 25px 0; clear:both;  display:inline-block;">
    <a href="https://beta.observablehq.com/@palewire/the-decline-of-third-parties-in-california-politics"><img src="/img/observable-pilot.gif" width="100%"></a>
    <figcaption style="clear:both; text-align:right;">Our first Observable notebook</figcaption>
</figure>

You can see an example in action in an analysis third-party candidates we [developed with Observable](https://beta.observablehq.com/@palewire/the-decline-of-third-parties-in-california-politics) at the Coalition's campus invasion of Stanford University earlier this month.

There I worked with Cheryl Phillips' journalism students to document the stark drop off in third-party candidates since California adopted an open primary system.

<figure style="margin: 15px 0 20px 0; clear:both; display:inline-block;">
    <img src="/img/stanford-hack-day.jpg" width="100%">
    <figcaption style="clear:both; text-align:right;">Ubuntu on the big screen, Kendrick on the soundsystem. We hacked all day in McClatchy 215.</figcaption>
</figure>


If you're interested learning more about Observable, I encourage you to check out other examples, such as [Jeremy Ashkenas' earthquakes map](https://beta.observablehq.com/@jashkenas/quakespotter-0-1) and [a fascinating experiment with sound](https://beta.observablehq.com/@freedmand/sounds) by Stanford student Dylan Freedman. Then try to write your own!
