---
layout: post
title: "A new feature imported from Berlin"
deckhead: "Python wrapper on PostgreSQL's power COPY command now supports file objects"
byline: "By [Ben Welsh](http://palewi.re/who-is-ben-welsh/)"
image: "http://calaccess.californiacivicdata.org/static/calaccess_website/images/brown-bear-share.png"
published: true
---

Today the California Civic Data Coalition released a new version of [django-postgres-copy](http://django-postgres-copy.californiacivicdata.org/en/latest/),
an open-source software library that quickly loads large pools of data into PostgreSQL databases.

<figure style="margin: 8px 0 0 18px; float:right;" >
   <a href="https://github.com/jonathan-s">
    <img src="/img/jonathan-sundqvist.jpg" height="150" alt="Jonathan Sundqvist" style="float:right; clear:both;" title="Jonathan Sundqvist">
   </a>
   <figcaption style="float:left; clear:both;">Jonathan Sundqvist</figcaption>
</figure>

It includes a new feature contributed by [Jonathan Sundqvist](https://github.com/jonathan-s) in Berlin, Germany. Thanks to Sundqvist's work, our bulk loader is no longer limited to files stored on your local filesystem. Python file objects, which can be concocted entirely in memory, can now be loaded just as easily.

This easily, in fact:

```python
MyModel.objects.from_csv(file_obj)
```

Unlike our team, Sundqvist doesn't work in journalism. He works for a company called [Zageno](https://zageno.com/) that sells biotechnology products online.

"The dataset consists of products, their variants and prices," Sundqvist [said](https://github.com/california-civic-data-coalition/django-postgres-copy/pull/70#issuecomment-363515674). "There is probably 1 million of those products on the site at the moment. So when updates need to happen or new products are added speed is invaluable. Using this library will help in cleaning up some of that code."

<figure style="width: 100%; margin: 20px 0; padding:0;">
    <a href="https://zageno.com/">
        <img src="/img/zageno.png" style="padding: 10px" title="Zageno" alt="Zageno">
    </a>
</figure>

In our view, this collaboration reaffirms how open-source techniques allow developers in different fields to benefit from each other's efforts. He is the latest in [a line](https://www.californiacivicdata.org/2016/11/14/django-postgres-copy-0.1/) of developers outside journalism who has contributed to django-postgres-copy.

Check out Sundqvists's changes and learn more about django-postgres-copy in
[the official documentation](http://django-postgres-copy.californiacivicdata.org/en/latest/).

If there are changes you'd like to see, go get involved on [our GitHub repository](https://github.com/california-civic-data-coalition/django-postgres-copy).
