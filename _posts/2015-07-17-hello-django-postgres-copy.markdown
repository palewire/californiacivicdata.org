---
layout: post
title: Say hello to our new open-source software for loading bulk data into PostgreSQL
deckhead: "Try our tool to take advantage of the powerful COPY command in Django"
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/)"
published: true
---

This morning we're releasing a new open-source software library that allows users of the Django web framework to more quickly load comma-delimited data into PostgreSQL databases.

**django-postgres-copy**, a new wrapper on the database's powerful [COPY](http://www.postgresql.org/docs/9.4/static/sql-copy.html) command, is now published on [GitHub](https://github.com/california-civic-data-coalition/django-postgres-copy) and packaged for installation in the [Python Package Index](https://pypi.python.org/pypi/django-postgres-copy). Technical documentation has been published via [ReadTheDocs](http://django-postgres-copy.californiacivicdata.org/).

### Why and what for?

Our work as data journalists often calls on us to download, clean and analyze new data sets. That means we write a load of loaders.

And since we code with [Django](https://www.djangoproject.com/), we write a lot of Python scripts that loop through each row in a spreadsheet and drop the data into a database.

Scripts that look something like this:

{% highlight python %}
import csv  # Import our toys
from myapp.models import MyModel

# Open up the CSV file
data = csv.DictReader(open("./data.csv"))
# Loop through it
for row in data:
    # Save each record to the database
    MyModel.objects.create(name=row['NAME'], number=row['NUMBER'])
{% endhighlight %}

But if you have a big CSV, Django will rack up database queries and it can take a long time to finish.

Lucky for us, PostgreSQL has a built-in tool called COPY that can hammer data into the database with one quick query. The only problem: Django doesn't support it.

This package tries to make using COPY as easy any other database routine accessible with Django. It is largely based on the design of the [LayerMapping](https://docs.djangoproject.com/en/1.8/ref/contrib/gis/layermapping/) utility for importing geospatial data.

Once you have our code hooked up, your loader can look more like this.

{% highlight python %}
from myapp.models import MyModel
from postgres_copy import CopyMapping  # Import it here

c = CopyMapping(
    # Provide your database table's model
    MyModel,
    # Your CSV data file
    "./data.csv",
    # And a map between the model fields and CSV column headers
    dict(name='NAME', number='NUMBER')
)
# And fire away!
c.save()
{% endhighlight %}

That may not seem like much difference, but the performance gains can be huge.

### How huge?

As an experiment, we tested two common CSV loading patterns against our new tool using the political campaign expenditure file published as part of the California Secretary of State's CAL-ACCESS database, which is the main focus of [our coalition](http://www.californiacivicdata.org/2014/09/24/hello-world/).

With 4.5 million records spread across dozens of columns, the file fills 1.3 gigabytes of hard drive space. That's not ["big data"](https://en.wikipedia.org/wiki/Big_data) by any formal definition, but it's big enough to bring the laptop of your average hack journalist grinding to a halt.

(This size falls into a zone we think of as "medium data:" Too big and complex to be managable in Excel, but not so big that it requires high-end data management tools like [Hadoop](https://hadoop.apache.org/). In our opinion, this area is in critical need of better tools to help analysts get a foothold.)

In the first test, we timed a simple loop like the one above that stepped through each row in the CSV and loaded that record into the database. By design, Django will ferry each row into the database individually. This adds up quickly.

 On our test machine, a three-year-old Lenovo ThinkPad x220, it took **1 hour and 23 minutes** to complete.

 In the second test, we reorganized our loop to lump the rows into groups of 1000 records. Along the way we used Django's [bulk_create](https://docs.djangoproject.com/en/1.8/ref/models/querysets/#bulk-create) command to drop those groups into the database as large batches.

By reducing the number of database queries, this second test finished in **18 minutes**.

In our final test, we loaded the file using our wrapper on the COPY command. It finished in just **4 minutes and 45 seconds**.

### What now?

If you'd like to try our tool out for yourself, you can install it with Python's ``pip`` like so:

{% highlight bash %}
$ pip install django-postgres-copy
{% endhighlight %}

To learn more about how it works, visit the [technical documentation](http://django-postgres-copy.californiacivicdata.org/). There you'll find more a complete explanation and information about some fancier tricks not covered here, like the capability to transform and clean data on-the-fly as it's loaded into the database.

We've already integrated it into [django-calaccess-raw-data](https://github.com/california-civic-data-coalition/django-calaccess-raw-data), a Django app to download, extract and load campaign finance and lobbying activity data from the CAL-ACCESS database.

This project is experimental and in the early stages of development. The aim is to
make it easier for others to load "medium data." But we know
our code isn't perfect and we want for feedback from hackers like you to make it better. So break it. Please. [Then let us know about it](https://github.com/california-civic-data-coalition/django-postgres-copy).
