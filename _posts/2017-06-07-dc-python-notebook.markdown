---
layout: post
title: "First Python Notebook goes to Washington"
deckhead: "Lessons learned from teaching pandas and Jupyter to Northwestern journalism students"
byline: "By [David Eads](http://www.recoveredfactory.net/)"
image: http://www.californiacivicdata.org/img/eads-dc.jpg
published: true
---

For almost three years I have taught a class called [“Digital Frameworks”](https://digitalframeworks-spring2017.github.io/) at Northwestern University’s Washington D.C. campus.

The ten-week course offers undergraduates an overview of technical topics in journalism, including spreadsheets, web scraping, data visualization and map making.

I was inspired by the California Civic Data Coalition’s “First Python Notebook” class [at the NICAR conference in Jacksonville](/2017/03/12/nicar-python-notebook/). So this year I set out to follow its example and teach my students data analysis with the Python programming language using the [Jupyter Notebook](http://jupyter.org/) and [pandas](http://pandas.pydata.org/) data analysis toolkit.

Happily for me, the Coalition’s [open-source curriculum](http://www.firstpythonnotebook.org/) was expanded and improved for a massive open online course hosted by the Knight Center For Journalism In the Americas. The free class will run from June 12 to July 9. ([And there’s still time to sign up](https://knightcenter.utexas.edu/blog/00-18396-sign-now-our-new-online-course-data-journalism-python-data-journalists-analyzing-money).)

Last month, I worked through its lesson plan with 12 students in my class. We spread the material over three sessions that lasted between two and three hours each. Most students had little prior experience coding. Many of them are aspiring broadcast journalists.

<figure style="margin: 20px 0; width:100% display: block; clear:both;">
    <img src="/img/eads-dc.jpg" style="width:100%" alt="First Python Notebook" title="First Python Notebook">
</figure>

The work was challenging.

“It's rough, I won't lie,” said Jasmine Minor. But, she continued, “this stuff is super useful… knowing how to filter through data would have saved me hours of time last quarter covering all those protests -- we may be broadcast, but our jobs are still to provide information people don't already know. It's helpful when we have the tools to do that.”

Another student had a job interview the day after our final session. She told me her prospective employer was “really excited when I told them I’m taking a data journalism class, and they were even more excited when I told them I used Python for my last assignment.”

I learned a lot myself. In retrospective style, I’ll discuss what went well, what didn’t, and what I’d change for next time. I’ll also discuss some variations I made from the material and how well those changes worked.


### What went well

#### 1. The software isn’t impossible to install

Jupyter and Pandas aren’t easy to install, but generally speaking, there is  a fairly well-understood and doable process, even for people without much coding experience. [The class materials](http://www.firstpythonnotebook.org/notebook/index.html) cover it thoroughly.

I did, however, skip [creating a virtual environment](http://www.firstpythonnotebook.org/virtualenv/index.html) for Windows users. It didn’t seem necessary and activating the environment in Windows seemed like an avoidable pain. I know this isn’t a best practice, but it worked fine in an situation where we needed to get up and running quickly.

#### 2. Jupyter is much friendlier to newbies than alternatives

The ability to put code in a Jupyter Notebook cell and run it right there affords a freedom in teaching coding skills that few other environments can match. Interactive shells are nice, but not as direct or robust, and you can’t save your work easily. Using a text editor and running commands on the command line requires more boilerplate code that’s confusing to newbies (`if __name__ == “__main__”:` what?!) and adds a layer of indirection that isn’t particularly enlightening.

#### 3. Pandas is magic

Some people say you need to know fundamental programming concepts before you learn this stuff. I am not one of those people.

Sure, it’s cool to learn about [for loops](https://wiki.python.org/moin/ForLoop) and everyone should. But pandas’ magical simplicity makes things like computed columns immediately intuitive:

{% highlight python %}
data['% of total'] = data.amount / data.amount.sum()
{% endhighlight %}

That’s nice because it gives the instructor more time to hammer on other fundamental concepts, such as variable assignment, object types and methods, and library imports. And especially on the most important thing: answering journalism questions. That’s a good thing.


### What didn’t go well

#### 1. Pandas is magic

Pandas integrates nicely with Jupyter. It’s fast and it can do some cool stuff. However, it’s also painfully obscure and quirky at times. There’s definitely More Than One Way To Do Things.

This quirkiness makes it harder than one might hope for students to do more with pandas after the lesson is done. [Agate](https://agate.readthedocs.io/) is another option with a cleaner and more consistent interface, but with less of the intuitive magic of pandas at its best and, more critically, without as many affordances for inspecting data using Jupyter.

#### 2. Minor system variations = big headaches

The Python installation bundled with Mac OS X varies in subtle ways across operating system versions, particularly when it comes to SSL support. That meant some students could pull in data via HTTPS without a hitch, while others were confronted with confusing and borderline useless error messages.

The [matplotlib](https://matplotlib.org/) charting library also caused trouble. Some students had trouble installing it &mdash; fixed, weirdly, by simply trying a second time. And for some reason, my own system and a few of the students choked on missing values when plotting. That was both annoying and a little embarrassing for me.

#### 3. Virtualenv doesn’t make sense to newbies

The students already had to get their heads around some tricky and foreign concepts, and virtual environments made no sense. Fortunately on OS X, I was able to simply show them how to reactivate and do some hand-waving that it’s important and don’t worry too much about why. But this could definitely bite them if they ever need to start a new project. Instead, I encouraged them to keep their public notebooks in a single repository while they’re learning and just get the mechanics down.  

#### 4. Pandas doesn’t escape URLs nicely

I had taught a previous lesson about using the [Socrata Open Data API](https://dev.socrata.com/) and the [Socrata Query Language](https://dev.socrata.com/docs/queries/) to aggregate large datasets into more useful forms. But I made a bad assumption. I figured students could simply invoke the Pandas `read_csv(...)` or `read_json(...)` methods without escaping the URLs.

Unfortunately, this doesn’t work:

{% highlight python %}
pd.read_csv('https://data.cityofchicago.org/resource/cwig-ma7x.csv?$group=results&$select=results, count(*) as total&$where=inspection_date > "2017-01-01"')
{% endhighlight %}

What does work is manually escaping the spaces:

{% highlight bash %}
pd.read_csv('https://data.cityofchicago.org/resource/cwig-ma7x.csv?$group=results&$select=results,%20count(*)%20as%20total&$where=inspection_date>"2017-01-01"')
{% endhighlight %}

I should have tested this more thoroughly, as the issue isn’t intractable and could have been avoided. I continue to believe a sequence of lessons starting with my introduction to web APIs and finishing with the First Python Notebook lesson could be a very satisfying sequence.


### What I changed

#### 1. Created a special scratchpad notebook to test basic programming concepts

Instead of reusing the same notebook, I started the class by specifically creating a notebook for demonstrating and playing around with the very basics of Python and then creating another notebook with pandas and data analysis. This gave me the chance to show the concept of multiple notebooks, and to create a notebook specifically designed to act as a scratchpad for experimentation with plain old Python.

#### 2. Markdown made its debut before doing any pandas code

Between the second and third chapters,  I showed the students [Markdown](https://en.wikipedia.org/wiki/Markdown) cells, moving it much closer to the start of the lesson plan This is in part because I’d taught them Markdown in an earlier  class. (They had to use Jekyll to author their homework and Github pull requests to submit their assignments.). I believe it’s important to be able to describe what you want to do, what you intend your code to do, and what you find after you run it.

#### 3. Recapped the overall structure and concepts at the beginning of each class

In the second two lessons, I ran through the notebook we had created up to that point from the top. I pointed out the import block, the assignment of the DataFrame loaded from a remote CSV file to a variable and various pandas commands.


### What I’d do differently next time

#### 1. Better assignment(s)

My homework assignment for students to practice their newfound skills wasn’t as robust as it should have been, in part because I got flummoxed by some unanticipated problems. As mentioned before, I had the bright idea to build on a previous lesson I had taught about web APIs by using the Socrata Open Data API. Unfortunately, the queries the students had created didn’t play well with the `pandas.read_csv(...)` method.

#### 2. More independent learning

A student named Jingnan Huo told me that “the online tutorial is very nice material to go through by oneself, and the classroom time can be better used by troubleshooting and talk about more elaborate tricks.”

I’m not sure -- the hands-on lessons were easy for a handful of students but difficult for most of them. But there are certainly cases where this would make sense, particularly classes where students are expected to spend more time on their homework than this one. I’d be interested to try it some day.
