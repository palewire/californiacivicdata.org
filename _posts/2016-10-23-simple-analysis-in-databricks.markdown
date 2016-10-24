---
layout: post
title: "How to analyze California campaign cash in the cloud with Apache Spark and Databricks"
deckhead: "Run SQL queries across millions of records from the comfort of your browser"
byline: "By [Bill Chambers](http://billchambers.me/about.html)"
image: http://www.californiacivicdata.org/img/ire_sd.jpg
published: true
---

*Editor's note: This post was written (and submitted [via pull request](https://github.com/california-civic-data-coalition/california-civic-data-coalition.github.io/pull/15)) by a contributor to our open-source project who is also a Databricks employee.*

<figure style="margin: 8px 0 0 18px; float:right;" >
   <a href="http://billchambers.me/about.html">
    <img src="/img/bill-chambers.jpg" height="200" alt="Bill Chambers" style="float:right; clear:both;" title="Bill Chambers">
   </a>
   <figcaption style="float:left; clear:both;">Bill Chambers</figcaption>
</figure>

As a [past contributor](http://www.californiacivicdata.org/2014/11/24/postgres-support/) to the California Civic Data Coalition I've been really pleased with how much the project has progressed! It's amazing to see the state's [campaign finance and lobbying activity data](http://calaccess.californiacivicdata.org/downloads/latest/) in a simple, clean format that users can immediately work with.

However, with [some](http://calaccess.californiacivicdata.org/documentation/calaccess-files/smry-cd/) [tables](http://calaccess.californiacivicdata.org/documentation/calaccess-files/expn-cd/) stacking up millions of rows, the data are often too big for standard tools like Microsoft Excel spreadsheets.

The result is that most beginners will need to install a series of complicated computer programming tools before they can begin any analysis.

In my experience teaching at [UC Berkeley](https://www.ischool.berkeley.edu/courses/info/018) and on [Udemy](https://www.udemy.com/data-analysis-in-python-with-pandas/), I've observed students often get caught up installing that kind software on their machines, which hinders their introduction to our field.

### The Databricks fix

Now I'm working as a project manager for new site called [Databricks](https://databricks.com/), which is aiming to solve this problem by making starting and sharing data science easier.

We start by harnessing the power of [Apache Spark](http://spark.apache.org/), a free and open-source tool high-speed data processing that, for the most the part, is only used by super nerds.

Over the last 8 months, the Databricks team has been hard at work integrating Spark into a free [community edition](https://community.cloud.databricks.com/) where even beginners can quickly import, transform and analyze gigantic data files using only their web browser thanks to the power of cloud computing.

### Take a test drive today with California's campaign cash database

As a project manager at Databricks I'm constantly on the look out for innovative ways that our projects can be used.

When the California Civic Data Coalition last month when they started releasing the versioned calaccess datasets. I realized that a [simple Databricks notebook example](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/346304/3910054895802185/484361/latest.html) would make it extremely easy for new users to get started querying the data - without having to install *any* software.

What's amazing about Spark is that it can turn any structured files (in this case CSV files) into an immediately queryable database and the Cal Access Database that is cleaned and maintained by the California Civic Data Coalition is no different! I believe that this really opens up the opportunities for this dataset to be queried. All you have to do is import [this Databricks notebook](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/346304/3910054895802185/484361/latest.html) into your free community edition account and run it. ([Instructions Here](https://docs.databricks.com/user-guide/notebooks/index.html#importing-notebooks)) That will automatically create all the SQL tables that you need and make them available for querying. I've already used it to see top lobbying contributions within the data - what can you find?
