---
layout: post
title: "Introducing django-calaccess-raw-data and django-calaccess-campaign-browser "
deckhead: Two Django applications made to make California campaign finance data easier
byline: "By [Aaron Williams](http://aboutaaron.com), [Agustin Armendariz](http://www.twitter.com/agustin_NYT) and [Ben Welsh](http://palewi.re/who-is-ben-welsh/)"
published: true
---

Hello world. 

We are the California Civic Data Coalition, a loosely coupled team of reporters and developers from the [Los Angeles Times Data Desk](http://www.latimes.com/local/datadesk/), [The Center for Investigative Reporting](http://cironline.org/) and Stanford's new [Computational Journalism Program](http://towcenter.org/blog/data-journalist-profile-cheryl-phillips-stanford-data-journalism/).

Our aim is to make California's public data easier for power users to access and analyze. Even though we represent rival media outlets, we’d rather compete at analyzing the data than downloading and parsing it.

We gathered for the first time last month for a two-day summit sponsored by OpenNews where we sprinted on two new open-source tools we're ready to release today.  

They are:

- [django-calaccess-raw-data](http://django-calaccess-raw-data.californiacivicdata.org/): A Django app to download, extract and load campaign finance and lobbying activity data from the California Secretary of State's CAL-ACCESS database

- [django-calaccess-campaign-browser](http://django-calaccess-campaign-browser.californiacivicdata.org/): A Django app to refine, review and republish campaign finance data drawn from the California Secretary of State’s CAL-ACCESS database

Both are designed and packaged according to our experimental "pluggable data" method, which you can read about at greater length [here](http://www.californiacivicdata.org/2014/09/24/pluggable-data/). But here's how to get hacking as soon as possible.

## Plugging in

Assuming you have a Django project already setup, installation is simple. 

{% highlight bash %}
$ pip install django-calaccess-raw-data
{% endhighlight %}

Update your `settings.py`:

{% highlight python %}
DEBUG = False
INSTALLED_APPS = (
	....
    'calaccess_raw',
)
{% endhighlight %}

Currently we only support MySQL databases that allow bulk loading via ``LOAD DATA INFILE`` (that might sound annoying but it's pretty handy), so make sure you have that configured in ``settings.py`` as well. 

{% highlight python %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_calaccess_db',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
        # Here's the thing we're talking about
        'OPTIONS': {
            'local_infile': 1,
        }
    }
}
{% endhighlight %}

Now, sync your database and download that data:

{% highlight bash %}
$ python manage.py syncdb
$ python manage.py downloadcalaccessraw
$ python manage.py runserver
{% endhighlight %}

You've just installed 76 database tables and nearly 35 million records, including all of the campaign finance and lobbying activity records collected by California government stretching back more than a decade. Visit ``http://localhost:8000`` and you can start exploring them right away.

![admin.png](/img/admin.png)

## Lowering the Barrier to Entry with django-calaccess-campaign-browser

We built `django-calaccess-raw-data` for folks who wanted to build applications on top of CAL-ACCESS. It doesn't provide much abstraction, and still comes with a bring-your-own-analysis prerequisite, but it makes the database easier to consume. That said, we also wanted to build a secondary tool to help folks move more quickly. That's where `django-calaccess-campaign-browser` comes in. The campaign browser goes the next step and associates candidates with their campaign committees, which means you can get a snapshot of a politican's career on a single page. Installation is pretty simple too:

{% highlight bash %}
$ pip install django-calaccess-campaign-browser
{% endhighlight %}

Update your `settings.py`:

{% highlight python %}
DEBUG = False
INSTALLED_APPS = (
    ....
    'calaccess_raw', # calaccess_raw is a dependency!
    'calaccess_campaign_browser',
)
{% endhighlight %}

Now, sync your database and build the new, associated tables:

{% highlight bash %}
$ python manage.py syncdb
$ python manage.py buildcalaccesscampaignbrowser
$ python manage.py runserver
{% endhighlight %}

![homepage.png](/img/homepage.png)

The campaign browser provides a simple interface to look up individual filers and search for individual campaign contributions. You can search for a candidate and see all of their associated committees they created to run for a specific office. On top of that, you can pull of the individual committee see how much many came in and out of that campaign. And if you want the data for that specific committee, all you have to do is click the download tab and select your preferred format.

![How the calaccess campaign browser interface works](/img/ccdc-example.gif)

_The campaign browser makes it very simple to search for a candidate and download their associated data._

While the browser is nice, we imagine there are journalists who just want this data in a CSV they can load into Access, Navicat, Excel or their preferred tool, and do analysis from there. For those folks, we created a Django management command that will export the campaign-browser data into three CSVs with all the associated summaries, expenditures and contributions.

{% highlight bash %}
$ python manage.py exportcalaccesscampaignfinance
{% endhighlight %}

We hope to create a regularly updated page with these flat tables hosted for folks who don't want to install the whole Django project just to get the flat tables. 

## Going Forward

This project represents a huge milestone for California open data advocates and journalists looking to watch how money influences politics in the state. While we're pleased to share what we've done with the world, we still have a lot of work to do. This includes, but is not limited to:

- Bulletproofing the install process
- Adding more documentation
- Regularly generating the flat tables and hosting them online
- Create project for lobbying reports (This is already underway at [django-calaccess-lobbying-browser](https://github.com/california-civic-data-coalition/django-calaccess-lobbying-browser))
- Getting ready for November elections

Whether you're a California journalist or developer passionate about our mission, or a curious person who's looking to contribute, we'd love your help. Keep an eye out on the [California Civic Data Coalition website](http://www.californiacivicdata.org/) for more updates on our progress.