---
layout: post
title: "Cut down database imports by a third using this one weird trick"
deckhead: "Our open-source bulk loader for PostgreSQL is faster than ever"
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/)"
image: "http://calaccess.californiacivicdata.org/static/calaccess_website/images/brown-bear-share.png"
published: true
---

Today the California Civic Data Coalition released a powerful improvement to its open-source tool for importing data via the Django web framework.

Version 2.1 of [django-postgres-copy](http://django-postgres-copy.californiacivicdata.org/en/latest/), now available on the Python Package Index, boosts the performance PostgreSQL's powerful [COPY TO](https://www.postgresql.org/docs/9.2/static/sql-copy.html) command by automatically dropping indexes and constraints on the table prior to the load.

The result is a significantly faster ingestion. Our speed tests -- using the tens of millions of state records -- found the change reduced load time of large tables *by nearly one third*.

After data are safely loaded, indexes and constraints are restored to the database. Users of django-postgres-copy can benefit simply by upgrading. No code changes are necessary.

### Why we did it

This improvement was pioneered by [James Gordon](https://twitter.com/je_gordon), the Coalition's lead developer.

He drew instruction from PostgreSQL's official documentation, [which reads](https://www.postgresql.org/docs/10/static/populate.html):

> If you are loading a freshly created table, the fastest method is to create the table, bulk load the table's data using COPY, then create any indexes needed for the table. Creating an index on pre-existing data is quicker than updating it incrementally as each row is loaded.

> If you are adding large amounts of data to an existing table, it might be a win to drop the indexes, load the table, and then recreate the indexes.

[Gordon's code](https://github.com/california-civic-data-coalition/django-postgres-copy/blob/3d7fa390b16c2ded087b206fa7ba9cdd378a415d/postgres_copy/managers.py#L12-L123) handles this task using low-level tools in Django's database manager rarely utilized by the average user.

### What to expect

Our speed tests were conducted in a Jupyter Notebook [now available on GitHub](https://github.com/california-civic-data-coalition/python-calaccess-notebooks/blob/master/calaccess-exploration/django-postgres-copy%20speed%20tests.ipynb). There you can see Python's [timeit](https://docs.python.org/2/library/timeit.html) testing the loading of 41 million records from CAL-ACCESS, the state of California's jumbled, dirty and difficult database tracking money in politics. Each time is loaded three times with the indexes dropped, and then three times without.


- Breakdown how we did the test
- Drop in the charts
- A code example
- How to opt out
- The end

Found only in PostgreSQL, COPY TO can write out tables with millions of rows in a matter of seconds.

Our code, crafted by the Coalition's Lead Developer [James Gordon](https://twitter.com/je_gordon), makes using it this easy:

{% highlight python %}
Person.objects.to_csv("/path/to/your/export.csv")
{% endhighlight %}

The custom to_csv method does it all. To start using it yourself, all you need to do is install our library and add a [custom manager](https://docs.djangoproject.com/en/1.11/topics/db/managers/) to your model.

{% highlight python %}
from django.db import models
from postgres_copy import CopyManager


class Person(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    objects = CopyManager()
{% endhighlight %}

Once that's done you're ready to roll. You can even export database queries that include filters, groups or other Django database tricks. For instance, this will work:

{% highlight python %}
Person.objects.exclude(first_name='BEN').to_csv('/path/to/your/export.csv')
{% endhighlight %}

And so will something like this:

{% highlight python %}
Person.objects.annotate(name_count=Count('first_name')).to_csv('/path/to/your/export.csv')
{% endhighlight %}

In cases where your model is connected to other tables with a foreign key, you can increase the number of fields exported by listing them out and calling in related tables using Django's double underscore notation.

{% highlight python %}
Person.objects.to_csv(
    '/path/to/your/export.csv',
    'first_name',
    'last_name',
    'hometown__name'
)
{% endhighlight %}

### Why do you need this?

The Coalition invented this tool as part of its open-source quest to master [CAL-ACCESS](/about/), the jumbled, dirty and difficult government database tracking money in California politics.

We are nearing the completion of a pipeline of Python code that downloads, extracts, cleans, loads, transforms and republishes the state's raw data as easy-to-understand spreadsheets. This new wrapper for COPY TO allows our pipeline to quickly and clearly export a set of simplified flat files for end users.

### What else can it do?

The library has long supported swiftly importing data files with PostgreSQL's COPY command. Starting today, that old tool is easier to access with a new from_csv method on our custom manager. Code like the following can load millions of records in your database in a matter of seconds.

{% highlight python %}
Person.objects.from_csv(
    # The source file
    "/path/to/your/import.csv",
    # A crosswalk of model fields to CSV headers.
    dict(first_name='FIRST_NAME', last_name='LAST_NAME')
)
{% endhighlight %}

### What now?

If you'd like to try our tool out for yourself, you can install it with Python's ``pip`` like so:

{% highlight bash %}
$ pip install django-postgres-copy
{% endhighlight %}

To learn more about how it works, visit the [technical documentation](http://django-postgres-copy.californiacivicdata.org/). There you'll find more a complete explanation and information about some fancier tricks not covered here, like the capability to transform and clean data on-the-fly as it's loaded into the database.

Since it was [first released](https://www.californiacivicdata.org/2015/07/17/hello-django-postgres-copy/) in 2015, django-posgres-copy has drawn contributions from coders around the world, including some major improvements [from users other fields](https://www.californiacivicdata.org/2016/11/14/django-postgres-copy-0.1/). If there are improvements you'd like to see, go get involved on [our GitHub repository](https://github.com/california-civic-data-coalition/django-postgres-copy).
