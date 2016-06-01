---
layout: post
title: "How to use Amazon S3's transfer acceleration with django-storages"
deckhead: " It's easy. It cut our upload time in half. You should do it too."
byline: "By [James Gordon](https://twitter.com/je_gordon)"
image: "http://www.californiacivicdata.org/img/acclerated-s3-button.png"
published: true
---

Now that we've nailed down the [first component](http://www.californiacivicdata.org/2016/05/27/raw-app-v1/) of our [data pipeline](http://django-calaccess.californiacivicdata.org/en/latest/index.html) for California's campaign cash, we've started moving our software to the cloud with Amazon Web Services.

But we hit a snag this week: Our new archiving process, which keeps a raw and cleaned version of each file in the [daily 750MB data dump](http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/), slowed to crawl when we configured an [Amazon S3](https://en.wikipedia.org/wiki/Amazon_S3) to store the files.

But then we tried "transfer acceleration." It's a not-so-obvious option that Amazon rolled out [last month](https://aws.amazon.com/blogs/aws/aws-storage-update-amazon-s3-transfer-acceleration-larger-snowballs-in-more-regions/).

We found out that it's easy to implement, and it cut our archiving time **in half**, from more than five hours down less than three.

### How to do it

Before we began, our project was already configured to upload media files to Amazon S3 using
the popular [django-storages](https://django-storages.readthedocs.io/en/latest/) library and Django's ``DEFAULT_FILE_STORAGE`` setting. You can more about how to do that [here](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html).

We then activated accelerated transfer for our file bucket, which can be done [via the Amazon S3 console](http://docs.aws.amazon.com/AmazonS3/latest/UG/enable-bucket-transfer-acceleration.html), the [S3 REST API](http://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTaccelerate.html) or [other interfaces](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html).

We did it simply by clicking this button in the web panel.

<figure style="margin: 8px 0;">
    <img src="/img/acclerated-s3-button.png" width="100%;">
</figure>


Once that was set, we made a small modification to our ``settings.py`` file to point django-storages at the accelerated upload service. This setting:

{% highlight python %}
S3_URL = 'https://{bucket_name}.s3.amazonaws.com/'
{% endhighlight %}

Became this:

{% highlight python %}
S3_URL = 'https://{bucket_name}.s3-accelerate.amazonaws.com'
{% endhighlight %}

That was it! All our uploads started flying up about twice as fast as before.

Faster isn't free, however. A normal upload to S3 is gratis, but accelerated transfers now cost [$0.04 per GB](http://aws.amazon.com/s3/pricing/).

You might not like that Amazon's now offering a walled-off toll road
to its popular static file service, but, to us, it's worth the price.
