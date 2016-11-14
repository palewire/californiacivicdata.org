---
layout: post
title: "Introducing django-postgres-copy v0.1"
deckhead: "A new release of our bulk-loading tool powered by innovation in medical research"
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/)"
image: "http://calaccess.californiacivicdata.org/static/calaccess_website/images/brown-bear-share.png"
published: true
---

Today the California Civic Data Coalition released a new version of [django-postgres-copy](http://django-postgres-copy.californiacivicdata.org/en/latest/),
our open-source software library that empowers users of the Django web framework to more quickly load large pools of data into PostgreSQL databases.

It includes a sweeping rewrite of the code and a series of feature additions largely driven by
a contributor from outside our field of journalism.

<figure style="margin: 8px 0 0 18px; float:right;" >
   <a href="https://github.com/ckirby">
    <img src="/img/chaim-kirby.jpg" height="150" alt="Chaim Kirby" style="float:right; clear:both;" title="Chaim Kirby">
   </a>
   <figcaption style="float:left; clear:both;">Chaim Kirby</figcaption>
</figure>

Thanks to [Chaim Kirby](https://github.com/ckirby), a software developer at [Commonwealth Informatics](http://www.commoninf.com/), the code now allows users
to omit or reuse columns from their source data files during loading.

In the past, the system was more rigid, allowing only exact one-to-one transfers from file to database.

Greater flexibility can be useful if you want to ignore a field, or ingest not just a column's raw values, but also a cleaned-up version.

Here's a simplified example. Django database models can now enlist our existing [transformation tools](http://django-postgres-copy.californiacivicdata.org/en/latest/#model-method-transformations) to
load both a raw string and a companion version converted into all uppercase letters.

{% highlight python %}
from django.db import models

class Person(models.Model):
    raw_name = models.CharField(max_length=500)
    uppercase_name = models.CharField(max_length=500)

    def copy_uppercase_name_template(self):
        return 'upper("%(name)s")'
    copy_uppercase_name_template.copy_type = 'text'
{% endhighlight %}

Our CopyMapping utility functions just as
before, but with the source column mapped to both database fields. Here it is
being run via a Django management command.

{% highlight python %}
from myapp.models import Person
from postgres_copy import CopyMapping
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        c = CopyMapping(
            # Give it the model
            Person,
            # The path to your CSV
            '/path/to/my/data.csv',
            # And a dict mapping the  model fields to CSV headers
            dict(name='NAME', uppercase_name='NAME'),
        )
        # Then save it.
        c.save()
{% endhighlight %}

Kirby is not involved in [our project](http://www.californiacivicdata.org/about/) analyzing money in politics.
He said django-postgres-copy is being used at Commonwealth Informatics to load and study millions of anonymized medical records as part of an effort to automate the detection of disease.

He [writes](https://github.com/california-civic-data-coalition/django-postgres-copy/pull/34#issuecomment-260317627) that django-postgres-copy "gives us a nice, clean and quick way to load the data into our data store while respecting the Django-ness of everything."

"[It] also sped up the processing from a naive [csvreader](https://docs.python.org/2/library/csv.html) implementation that took hours to running in about 10 minutes," he said.

In our view, this collaboration reaffirms how open-source techniques
allow developers in different fields to benefit from each other's efforts.

Check out Kirby's changes and learn more about django-postgres-copy in
[the official documentation](http://django-postgres-copy.californiacivicdata.org/en/latest/).

If there are changes you'd like to see, go get involved on [our GitHub repository](https://github.com/california-civic-data-coalition/django-postgres-copy).
