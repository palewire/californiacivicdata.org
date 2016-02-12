---
layout: post
title: "Introducing django-postgres-copy v0.0.7"
deckhead: "A new release of our bulk-loading tool includes features contributed by our users"
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/)"
image: "http://www.californiacivicdata.org/img/logo.png"
published: true
---

Today we released a new version of [django-postgres-copy](http://django-postgres-copy.californiacivicdata.org/en/latest/),
our open-source software library that allows users of the Django web framework to more quickly load comma-delimited data into PostgreSQL databases.

It includes a series of bug fixes and features from members of user base, who
are not participating in [our core project](/about/) but share our need for better tools
to bulk load big data files.

For instance, if your database table includes columns that are not in the data file
you're seeking to load, you might want to specify fixed values for the extra fields.

Thanks to contributor [Chaim Kirby](https://github.com/ckirby) you can now
do so with the new ``static_mapping`` option.

An example could be if you want to include the name of the source data file along with each row
you load into a data table.

Your Django database model might look like this:

{% highlight python %}
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=500)
    number = models.IntegerField()
    source_csv = models.CharField(max_length=500)
{% endhighlight %}

And your loader would look like this, adding the new ``static_mapping`` argument
to our existing ``CopyMapping`` tool.


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
            dict(name='NAME', number='NUMBER'),
            # Set the fixed values for the extra column
            static_mapping = {
                'source_csv': 'data.csv'
            }
        )
        # Then save it.
        c.save()
{% endhighlight %}

Check out his changes and learn more about django-postgres-copy in
[the official documentation](http://django-postgres-copy.californiacivicdata.org/en/latest/).

If there are changes you'd like to see, go get involved on [our GitHub repository](https://github.com/california-civic-data-coalition/django-postgres-copy).
