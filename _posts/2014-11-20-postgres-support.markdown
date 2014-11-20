---
layout: post
title: "CAL-ACCESS app now supports PostgreSQL"
deckhead: "Version 0.1.0 of django-calaccess-raw-data can connect to the popular database backend"
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/)"
published: false
---

A new version of [our software](http://django-calaccess-raw-data.californiacivicdata.org/en/latest/) for downloading campaign finance and lobbying data now supports the popular [PostgreSQL](http://en.wikipedia.org/wiki/PostgreSQL) database backend, thanks to significant contributions from a new volunteer.

Version 0.1.0 of [django-calaccess-raw-data](http://django-calaccess-raw-data.californiacivicdata.org/en/latest/) is now freely available on the [Python Package Index](https://pypi.python.org/pypi/django-calaccess-raw-data) and [GitHub](https://github.com/california-civic-data-coalition/django-calaccess-raw-data). Upgrades include [Django 1.7](https://docs.djangoproject.com/en/1.7/releases/1.7/) support and fancier logging outputs, as well as numerous bug fixes and small improvements to documentation.

If you already have it installed, an upgrade is as easy as:

{% highlight bash %}
$ pip install django-calaccess-raw-data --upgrade
{% endhighlight %}

The chief improvement is the ability to load data into the PostgreSQL database. Previous versions only worked with [MySQL](http://en.wikipedia.org/wiki/MySQL).

The new feature was provided by [Bill Chambers](http://billchambers.me/), a graduate student at the [UC Berkeley School of Information](http://www.ischool.berkeley.edu/).

"I hope that users of the system, including myself, will be able to unveil key insights about the lobbying and fundraising activities done by our state representatives and associated political groups," Chambers said. "Fundamentally, this kind of information deeply deserves to be open and accessible."

[django-calaccess-raw-data](http://django-calaccess-raw-data.californiacivicdata.org/en/latest/) is a free and open-source Django app to download, extract and load campaign finance and lobbying activity data from the California Secretary of State's [CAL-ACCESS database](http://www.sos.ca.gov/prd/cal-access/).

It was originally released [in August](http://www.californiacivicdata.org/2014/09/24/hello-world/) by the California Civic Data Coalition, a loosely coupled team from the Los Angeles Times Data Desk, The Center for Investigative Reporting and Stanford's Computational Journalism Lab.

[Upstream](https://github.com/california-civic-data-coalition/django-calaccess-campaign-browser) [applications](https://github.com/california-civic-data-coalition/django-calaccess-lobbying-browser) refine and review the source data. They still lack PostgreSQL support. If you're interested contributing, we'd be thrilled if someone wants to follow Bill's lead and [pitch in](https://github.com/california-civic-data-coalition/django-calaccess-campaign-browser/issues/120).
