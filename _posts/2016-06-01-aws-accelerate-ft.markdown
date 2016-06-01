---
layout: post
title: 'Amazon S3 uploads slowing you down? Try "Transfer Acceleration"!'
deckhead: "We did. It was easy. And we cut our upload time in half."
byline: "By [James Gordon](https://twitter.com/je_gordon)"
image: "http://www.californiacivicdata.org/img/code-rush-4-share.png"
published: False
---

Now that we've nailed down the [first component](http://www.californiacivicdata.org/2016/05/27/raw-app-v1/) of our California state campaign finance and lobbyist disclosure [data pipeline](http://django-calaccess.californiacivicdata.org/en/latest/index.html), we've started moving our software to the cloud, specifically Amazon Web Services.

The daily process that churns through over 35 million records, spread across 76 data files, will soon be running on an Elastic Compute Cloud (EC2) instance, loading into a Relation Database Service (RDS) hosted database and archiving files to a Simple Storage Service (S3) bucket.

My personal laptop could not be more thankful.

But we hit a snag this week: Our new archiving process, which keeps a raw and cleaned version of each data file in the [daily CAL-ACCESS export](http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/), slowed to crawl when we configured an S3 bucket as our Django project's file storage.

But have you heard of "Transfer Acceleration"? It's a not-so-obvious S3 option that Amazon rolled out [last month](https://aws.amazon.com/blogs/aws/aws-storage-update-amazon-s3-transfer-acceleration-larger-snowballs-in-more-regions/). It's easy to implement, and it cut our archiving time <b>in half</b>, from five to six hours down to just two and half hours.

You can configure accelerated transfer [via the Amazon S3 console](http://docs.aws.amazon.com/AmazonS3/latest/UG/enable-bucket-transfer-acceleration.html), the [S3 REST API](http://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTaccelerate.html) or [other interfaces](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html).

Once that's set, you just need to make a small modification to your endpoint:

```python
    S3_URL = 'https://{bucket_name}.s3.amazonaws.com/'
```

Becomes:

```python
    S3_URL = 'https://{bucket_name}.s3-accelerate.amazonaws.com'
```

That's it!

Faster isn't free, though. Whereas regular tranfers into S3 are free, accelerated transfers costs [$0.04 a GB](http://aws.amazon.com/s3/pricing/).
