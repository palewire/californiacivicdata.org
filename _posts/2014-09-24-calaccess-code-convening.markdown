---
layout: post
title: "Introducing django-calaccess-raw-data and django-calaccess-campaign-browser "
deckhead: "Two Django applications made to make California campaign finance easier"
byline: "By [Aaron Williams](http://aboutaaron.com), [Agustin Armendariz](http://www.twitter.com/agustin_NYT) and [Ben Welsh](http://palewi.re/who-is-ben-welsh/)"
published: true
---

![bearwalk_small.gif](/img/bearwalk_small.gif)

After several months of internal work and a two-day code sprint, reporters and developers from The [Los Angeles Times Data Desk](http://www.latimes.com/local/datadesk/), [The Center for Investigative Reporting](http://cironline.org/) and Stanford's new [Computational Journalism Program](http://towcenter.org/blog/data-journalist-profile-cheryl-phillips-stanford-data-journalism/) are premiering two tools:

- [django-calaccess-raw-data](http://django-calaccess-campaign-browser.californiacivicdata.org/en/latest/): A Django app to refine, review and republish campaign finance data drawn from the California Secretary of State’s Cal-Access database.

- [django-calaccess-campaign-browser](https://github.com/california-civic-data-coalition/django-calaccess-lobbying-browser): A simple Django app to build lobbying activity data from the Cal-Access database. It is reliant on django-calaccess-parser.

Both tools aim to make California campaign finance data easier to consume and build upon. If you're curious about our app methodology, we suggest you read our sister post on ["pluggable data"](http://www.californiacivicdata.org/2015/01/01/pluggable-data/).

## Getting Started

Browse the [California Civic Data Coalition](https://github.com/california-civic-data-coalition/) GitHub page for app details and documentation on installation and hacking. Installation is simple. Assuming you have a Django project already setup:

```bash
$ pip install django-calaccess-raw-data
```

Update your `settings.py`:
```python
DEBUG = False
INSTALLED_APPS = (
	....
    'calaccess_raw',
)
```

Now, sync your database and download that data:
```bash
$ python manage.py syncdb
$ python manage.py downloadcalaccessraw
$ python manage.py runserver
```

![admin.png](/img/admin.png)


California recently published its campaign finance database online after a successful campaign by civic hackers. In response, reporters at the Times and CIR built a series ad-hoc tools to deal with this database. But these tools didn't scale and were hard for other developers to read and use. We asked ourselves, "Is there a better way?" 

## Building a Better Way

This project was born late last year when the Times and CIR began sending emails back and forth on ways we could share what we learned building campaign finance applications. As it turned out, Agustin Armendariz, formerly of CIR, had already written a Python script to load parts of the Cal-Access data dump into a Django project. With that script in mind, we created the California Civic Data Coalition Github organization and began hacking on this project in the open. 

And then the project hit a standstill. While we put in the leg-work to parse and harvest some of the initial data, the hurdles were gargantuan. For starters, the load-and-clean script took over 24 hours to complete. For the journalist on a deadline, this was unacceptable. And after that initial download the parse {{_ <-- something is awry in this clause_}} ran, the secondary script for associating candidates and their committees took another 24 hours. The net result was a two-day snorefest and several missed deadlines. Furthermore, the front-end interface was built in roughly a week and, while functional, didn't provide much in the form of help.

{{_I took out the "Before we met in San Francisco" part above because there wasn't any context about why you were in San Francisco, so it made the chronology stumble. Suggest adding a short graf here explaining the nature of the code convening -- it doesn't need to be a big OpenNews advertisement, god forbid, but should provide context and mention "code convening" as a thing, because we'll be tagging this as a convening on Source and it will be confusing otherwise. _ }}

### Optimizing the code

Priority one for the backend was speed. How could we cut down the load time for the parsing and get developers up and running? The answer came in [`cProfile`](https://docs.python.org/2/library/profile.html), a Python standard library module that measures how long parts of a program take to execute.

```bash
$ python -m cProfile example/manage.py downloadcalaccessraw
```

By default, this will print a log of every transaction your script is running. This can get rather long, so it's better to point the output of cProfile to a log file.

```bash
$ python -m cProfile example/manage.py downloadcalaccessraw > speedtest.log
```

`cProfile` showed us that the `downloadcalaccessraw` command had several loops slowing down the script. You can see our work with this in our [Makefile](https://github.com/california-civic-data-coalition/django-calaccess-raw-data/commit/a59e0276100cd5d854225ba9de41715fa1b66b68?diff=unified#diff-b67911656ef5d18c4ae36cb6741b7965R12). With `cProfile`, we saw that some of the loops we were doing in Python took a long time and happened millions of times. 

By refactoring those parts of the code, we were able to get the total script runtime down to roughly __15 minutes__! With the speed increase, we moved on to make sure every table in the Cal-Access data dump had an appropriate Django model.

## Lowering the Barrier to Entry with django-calaccess-campaign-browser

We built `django-calaccess-raw-data` for folks who wanted to build applications on top of Cal-Access. It doesn't provide much abstraction, and still comes with a bring-your-own-analysis prerequisite, but it makes the database easier to consume. That said, we also wanted to build a secondary tool to help folks move more quickly. That's where `django-calaccess-campaign-browser.` The campaign browser goes the next step and associates candidates with their campaign committees, which means you can get a snapshot of a politican's career on a single page. Installation is pretty simple too:

```bash
$ pip install django-calaccess-campaign-browser
```

Update your `settings.py`:
```python
DEBUG = False
INSTALLED_APPS = (
	....
    'calaccess_raw', # calaccess_raw is a dependency!
    'calaccess_campaign_browser',
)
```

Now, sync your database and build the new, associated tables:
```bash
$ python manage.py syncdb
$ python manage.py buildcalaccesscampaignbrowser
$ python manage.py runserver
```

![homepage.png](/img/homepage.png)


The campaign browser provides a simple interface to look up individual filers and search for individual campaign contributions. You can search for a candidate and see all of their associated committees they created to run for a specific office. On top of that, you can pull of the individual committee see how much many came in and out of that campaign. And if you want the data for that specific committee, all you have to do is click the download tab and select your preferred format.


<iframe src="//giphy.com/embed/5xtDarslFDhL7MZTE4g" width="500" height="281" frameBorder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>

_The campaign browser makes it very simple to search for a candidate and download their associated data._


While the browser is nice, we imagine there are journalists who just want this data in a CSV they can load into Access, Navicat, Excel or their preferred tool, and do analysis from there. For those folks, we created a Django management command that will export the campaign-browser data into three CSVs with all the associated summaries, expenditures and contributions.

```bash
$ python manage.py exportcalaccesscampaignfinance
```

We hope to create a regularly updated page with these flat tables hosted for folks who don't want to install the whole Django project just to get the flat tables. 

## Going Forward

This project represents a huge milestone for California open data advocates and journalists looking to watch how money influences politics in the state. While we're pleased to share what we've done with the world, we still have a lot of work to do. This includes, but is not limited to:

- Bulletproofing the install process
- Adding more documentation
- Regularly generating the flat tables and hosting them online
- Create project for lobbying reports (This is already underway at [django-calaccess-lobbying-browser](https://github.com/california-civic-data-coalition/django-calaccess-lobbying-browser))
- Getting ready for November

Whether you're a California journalist or developer passionate about our mission, or a curious person who's looking to contribute, we'd love your help. Keep an eye out on the [California Civic Data Coalition website](http://www.californiacivicdata.org/) for more updates on our progress.
