---
layout: post
title: New packages deploy CAL-ACCESS apps with Docker, Chef
deckhead: "Take a hack at these new tools for spinning up our stack"
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/)"
published: true
---

This morning we're releasing a set of open-source packages that aim to make it easier
to deploy [our tools](http://www.californiacivicdata.org/2014/09/24/hello-world/) for acquiring and analyzing CAL-ACCESS, the California Secretary of State's campaign finance database.

**[django-calaccess-project-template](https://github.com/california-civic-data-coalition/django-calaccess-project-template)** is a custom template for initializing a preconfigured Django project with our applications already installed and ready to roll.

It works by taking advantage of the underused templating options deep within Django's [``startproject``](https://docs.djangoproject.com/en/1.7/ref/django-admin/#startproject-projectname-destination) command.

{% highlight bash %}
# Create a new empty repo
$ git init repo

# Drop in our project
$ django-admin.py startproject --extension=py,.gitignore --template=https://github.com/california-civic-data-coalition/django-calaccess-project-template/archive/master.zip project repo
{% endhighlight %}


**[django-calaccess-docker](https://github.com/california-civic-data-coalition/django-calaccess-docker)** is a Docker image ready to boot a standalone stack that serves a fully-functioning Django project.

To create a container using this image, start by retriving the image from [Docker Hub](https://registry.hub.docker.com/u/ccdc/django-calaccess/).

{% highlight bash %}
$ sudo docker pull ccdc/django-calaccess:0.6
{% endhighlight %}

Then fire up the container with all the required environmental settings included as options.

{% highlight bash %}
$ sudo docker run \
    -p 127.0.0.1:80:80 \
    --name my-calaccess \
    -e MYSQL_DATABASE=calaccess \
    -e MYSQL_USER=ccdc \
    -e MYSQL_PASSWORD=mycrazypassword \
    -e DJANGO_USER=admin \
    -e DJANGO_EMAIL=foo@bar.com \
    -e DJANGO_PASSWORD=mydjangopassword \
    -d ccdc/django-calaccess:0.6
{% endhighlight %}

Once that finishes, visit [localhost](http://localhost/) in your browser to see the stack in action. The database will be empty but is set to fill once the daily cron rolls around.

**[django-calaccess-cookbook](https://github.com/california-civic-data-coalition/django-calaccess-cookbook)** also serves the full stack by provisioning a server from Amazon Web Services EC2 service with Chef and Fabric.

Once you have the repository installed locally, firing up a working server should be as simple as:

{% highlight bash %}
$ fab ec2bootstrap
{% endhighlight %}

All three projects are experimental and in the early stages of development. The aim is to
make it easier for others to install, explore and improve our code base. But we know
the code isn't perfect and we want for feedback from hackers like you to make it better. So break it. Please.
