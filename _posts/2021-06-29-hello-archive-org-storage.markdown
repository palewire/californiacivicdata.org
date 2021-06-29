---
layout: post
title: "We’re storing open data at archive.org, and you can too"
deckhead: "Use our Django plugin to upload to The Internet Archive"
byline: "By [Ben Welsh](https://palewi.re/who-is-ben-welsh/)"
published: true
---

All data downloads offered by the California Civic Data Coalition are now hosted by [The Internet Archive](https://archive.org/), the non-profit library of free books, movies, software, music, websites, and, in our case, open data. The change will ensure that the coalition’s collection of data tracking money in California politics will endure long into the future.

The innovation points to a more sustainable model for archiving data. To encourage others to experiment with this approach, the coalition is releasing [the open-source software](https://github.com/california-civic-data-coalition/django-internetarchive-storage) that made the migration possible so that other archival projects can more easily automate uploads to archive.org.

<figure style="margin: 25px 0 25px 0; clear:both;  display:inline-block;">
    <a href="https://archive.org/details/california-civic-data-coalition"><img src="/img/internetarchive.png" width="100%"></a>
    <figcaption style="clear:both; text-align:right;">Our special collection at archive.org</figcaption>
</figure>

Download URLs previously listed on this site will no longer update. Our team will gradually end our reliance on a costly commercial hosting provider. All download URLs now point to our Internet Archive collection at [archive.org/details/california-civic-data-coalition](https://archive.org/details/california-civic-data-coalition). For the latest links, revisit [our download pages](https://calaccess.californiacivicdata.org/downloads/latest/) and make the change to what you see there now.

The change was achieved by developing a new upload tool for the [Django web framework](https://www.djangoproject.com/). We call it [django-internetarchive-storage](https://github.com/california-civic-data-coalition/django-internetarchive-storage). It makes sending files to Internet Archive as easy as writing a couple lines of [Python code](https://en.wikipedia.org/wiki/Python_(programming_language)).

All it takes is adding our custom file field to your database table. Like this:

```python
from django.db import models
from ia_storage.fields import InternetArchiveFileField


class Memento(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    data = InternetArchiveFileField()  # <--- Right here!
```

You can learn more about the system, including how to save a file to the field, by reading our documentation at [github.com/california-civic-data-coalition/django-internetarchive-storage](https://github.com/california-civic-data-coalition/django-internetarchive-storage).

Before you can being storing your work, you'll need to establish a special collection. The Internet Archive provides a guide on how to get one going [in its help section](https://help.archive.org/hc/en-us/articles/360017502272-How-to-request-a-collection-).

We couldn't have figured it out without help from archive.org staffers [Mark Graham](https://www.linkedin.com/in/markjohngraham/) and Duncan Hall, who provided vital guidance and encouragement. You can support their efforts by <a href="https://archive.org/donate/?origin=iawww-TopNavDonateButton">donating to the non-profit's coffers</a>.

Today’s release corresponds with the Los Angeles Times data journalism team publishing [a new page](https://www.latimes.com/projects/california-recall-election-money-newsom-vs-jenner-cox/) tracking the tens of millions of dollars flooding the campaign to recall California Governor Gavin Newsom. The reporters who developed that page — [Maloy Moore](https://www.latimes.com/people/maloy-moore) and [Ryan Menezes](https://www.latimes.com/people/ryan-menezes) — are among the leading consumers of the coalition's data services.

Their work is a reminder of why our team remains focused on refining CAL-ACCESS, the jumbled, dirty and difficult government database that tracks campaign finance and lobbying activity in California politics.

The coalition was formed in 2014 by myself and Agustin Armendariz to lead the development of open-source software that makes California's public data easier to access and analyze. The effort has drawn hundreds of contributions from developers and journalists at dozens of news organizations.
