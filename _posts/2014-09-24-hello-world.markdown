---
layout: post
title: Introducing the California Civic Data Coalition
deckhead: "We're here with wwo Django applications ready made to make California campaign finance data easier to access"
byline: "By [Aaron Williams](http://aboutaaron.com), [Agustin Armendariz](http://www.twitter.com/agustin_NYT) and [Ben Welsh](http://palewi.re/who-is-ben-welsh/)"
published: true
---

Hello world. 

We are the California Civic Data Coalition, a loosely coupled team of reporters and developers from the [Los Angeles Times Data Desk](http://www.latimes.com/local/datadesk/), [The Center for Investigative Reporting](http://cironline.org/) and Stanford's new [Computational Journalism Program](http://towcenter.org/blog/data-journalist-profile-cheryl-phillips-stanford-data-journalism/).

Our aim: To make California's public data easier for power users to access and analyze. Even though we represent rival media outlets, we’d rather compete at analyzing the data than downloading and parsing it.

Our inspiration: Raw data from CAL-ACCESS, the state of California’s campaign finance and lobbying activity database, is being published online for the first time.

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

## Taking it to the next level

We built `django-calaccess-raw-data` for folks who wanted to build applications on top of CAL-ACCESS. It doesn't provide much abstraction, and still comes with a bring-your-own-analysis prerequisite, but it makes the database easier to consume. 

We also wanted to build a secondary tool to help folks move more quickly. That's where `django-calaccess-campaign-browser` comes in. It goes the next step and begins to clean, regroup, filter and transform the massive, hairy state database into something more legible. Installation is just as simple.

{% highlight bash %}
$ pip install django-calaccess-campaign-browser
{% endhighlight %}

Update your `settings.py`:

{% highlight python %}
DEBUG = False
INSTALLED_APPS = (
    ....
    'calaccess_raw', # Note that calaccess_raw is a dependency!
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

The campaign browser now provides a simple interface to look up individual filers and search for individual campaign contributions. You can search for a candidate and see all of their associated committees they created to run for a specific office. And if you want the data for that specific committee, all you have to do is click the download tab and select your preferred format.

![How the calaccess campaign browser interface works](/img/ccdc-example.gif)

This code base is still a work in progress, however, and its analysis should be considered as provisional until it is further tested and debugged. We're working better map out the state's complex system and bulletproof our figures, but we're not there yet. 

## Where you come in

This release represents a milestone for our team, but we still have a lot of work to do. This includes, but is not limited to:

- Bulletproofing the analysis process of the campaign browser
- Expanding our documentation to more fully explain the contents of the raw CAL-ACCESS database
- Bringing the campaign browser's approach to the lobbying activity data also provided by CAL-ACCESS (Already underway but far from complete at [django-calaccess-lobbying-browser](https://github.com/california-civic-data-coalition/django-calaccess-lobbying-browser))
- And, most importantly, generating journalism that demonstrates the power of automating away access to this valuable data set.

Whether you're a California journalist or developer passionate about our mission, or a curious person who's looking to contribute, we'd got pplenty](https://github.com/california-civic-data-coalition/django-calaccess-campaign-browser/issues) [of tickets](https://github.com/california-civic-data-coalition/django-calaccess-campaign-browser/issues) for you. 

Keep an eye out on the [California Civic Data Coalition website](http://www.californiacivicdata.org/) for more updates on our progress.