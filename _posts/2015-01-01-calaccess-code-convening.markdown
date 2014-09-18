---
layout: default
title: "CAL-ACCESS code convening"
published: false
---

# Introducing the calaccess-raw-data and calaccess-campaign-browser 
## Two Django applications made to make California campaign finance easier

After several months of internal work and a two-day code sprint, reporters and developers from The [Los Angeles Times Data Desk](http://www.latimes.com/local/datadesk/), [The Center for Investigative Reporting](http://cironline.org/) and Stanford's new [Computational Journalism Program](http://towcenter.org/blog/data-journalist-profile-cheryl-phillips-stanford-data-journalism/) are premiering two tools:

- [django-calaccess-raw-data](): lorem
- [django-calaccess-campaign-browser](): lorem

Both tools aim to make California campaign finance data easier to consume and build upon. If you're curious on our app methodology, we suggest you read our sister post on ["pluggable data"]().

Browse the [California Civic Data Coalition]() Github page for app details and documentation on installation and hacking.

California recently published its campaign finance database online after a successful campaign by civic hackers. Since, reporters at the Times and CIR built ad-hoc(?) tools to deal with this database. But these tools didn't scale and were hard for other developers to read. We asked ourselves, "Is there a better way?" 

## Building a better way

Both applications were born late last year when the Times and CIR began sending emails back and forth on ways we could share what we learned building campaign finance applications. As it turned out, Agustin Armendariz, formerly of CIR, had already written a Python script to load parts of the Cal Access data dump into a Django project. With that script in mind, we created the California Civic Data Coalition Github organization and began hacking on this project in the open. 

Before we met in San Francisco, the Cal Access project had hit a standstill. While we put in the leg work to parse and harvest some of the initial data, the hurdles were gargantuan. For starters, the load and clean script took over 24 hours to complete. For the journalist on a deadline, this was unacceptable. And after that initial download the parse ran, the secondary script for associating candidates and their committees took another 24 hours. The net result was a two-day snorefest and several missed deadlines. Furthermore, the frontend interface was built in roughly a week and, while functional, didn't provide much in the form of help.

## Optimizing the code

Priority one for the backend was speed. How could we cut down the load time for the parsing and get developers up and running? The answer came in `cProfile`, a Python standard library module that measures the speed of a program. cProfile showed us that the `downloadcalaccessraw` command had several loops slowing down the script. 

```bash
$ python -m cProfile example/manage.py downloadcalaccessraw
```

By default, this will print a log of every transaction your script is running. This can get rather long so it's better to point the output of cProfile to a log file.

```bash
$ python -m cProfile example/manage.py downloadcalaccessraw > speedtest.log
```

You can see our work with this in our [Makefile](https://github.com/california-civic-data-coalition/django-calaccess-raw-data/commit/a59e0276100cd5d854225ba9de41715fa1b66b68?diff=unified#diff-b67911656ef5d18c4ae36cb6741b7965R12).
With cProfile, we saw that some of the loops we were doing in Python took a long time and happened millions of times. By refactoring those parts of the code, we were able to get the total script runtime down to roughly __15 minutes__! With the speed increase, we moved on to make sure every table in the Cal Access data dump had an appropriate Django model.

## Lowering the barrier to entry

While these tools are great, but we also wanted to provide a one stop shop for the parsed data as well. That's why we also created URL TK, a weekly updating website with the latest snapshots of the parsed Cal Access data. If you're less interested in the large data dump and would prefer a cleaned set of data to build a graphic, this is what you want. Or throw it into your favorite RDBMS. The world is your oyster.









Other milestones include:

- 1.0 of loading and cleaning data
- 100% coverage: ALL 76 models have data that loads into the db (nearly 35 million records), still super fast
 - Simple, read-only Django admins for all models
- Docstrings for new models
- Refactored models into modules organized in same way that CA does
- Updated the docs to reference new model and admin organization
- Documented new, more flexible management commands

## Frontend

After downloading and parsing the data, we wanted to create a simple way to explore the data without running the Python console. After two days, we rewrote the frontend to work to look great and provide some nifty features:

See a table of data on the page? You can download it as either JSON or CSV
Search for candidate and committee contributions. We hope to have full search coverage soon.
These two features alone make browsing and the consuming the data than ever before. Now, a journalist can find a candidate they're looking for and download their entire reported campaign finance history with the click of a button.

While these tools are great, but we also wanted to provide a one stop shop for the parsed data as well. That's why we also created URL TK, a weekly updating website with the latest snapshots of the parsed Cal Access data. If you're less interested in the large data dump and would prefer a cleaned set of data to build a graphic, this is what you want. Or throw it into your favorite RDBMS. The world is your oyster.

## Going Forward

Get data ready for November Election
More documentation