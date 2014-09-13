---
layout: default
title: "CAL-ACCESS code convening"
published: true
---

# What We're Building

Yet far too much handcrafted work — what data scientists call “data wrangling,” “data munging” and “data janitor work” — is still required. Data scientists, according to interviews and expert estimates, spend from 50 percent to 80 percent of their time mired in this more mundane labor of collecting and preparing unruly digital data, before it can be explored for useful nuggets.

Steve Lohr, The New York Times: "For Big-Data Scientists, ‘Janitor Work’ Is Key Hurdle to Insights"
We are not making Yet Another Campaign Finance Website for the average schmuck reporter
We are making power tools for power users that allow them quickly begin working with the “Big Data” dump rather than sucking through a straw on a search form (Need a metaphor that holds up here)
The second goal is to make it easier for us to collaborate with investigative reporters in our newsroom.
Compare the “raw-data” app to the “ETL” (Extract-Transform-Load) routines that are a fixture in major software and data companies.
And our proposal for how to do that is to leverage the packaging and distribution system that has been so successfully with other software for data. If I can pip install django, why can’t I pip install census? Pluggable Data.
Pluggable Data -- there’s the hook. And mention how easy it is to swap out front ends if you don’t like the one in the repo. And if you don’t even want a front end that’s fine. Just open Navicat / SQL Yog / MySQL Workbench and go to town
Uncharted Waters: The background

Before we met in San Francisco, the Cal Access project had hit a standstill. While we put in the leg work to parse and harvest some of the initial data, the hurdles were gargatuan. For starters, the load and clean script took over 24 hours to complete. For the journalist on a deadline, this was unacceptable. And after that initial download the parse ran, the secondary script for associating candidates and their committees took another 24 hours. The net result was a two-day snorefest and several missed deadlines. Furthermore, the frontend interface was built in roughly a week and, while functional, didn't provide much in the form of help.

Back End

Priority one for the backend was speed. How could we cut down the load time for the parsing and get developers up and running? The answer came in cProfile, a Python standard library module that measures the speed of a program. cProfile should us that the downloadcalaccess command had several loops that slowed the script. By refactoring those parts of the code, we were able to get the total script runtime down to roughly 15 minutes. With the speed increase, were able to provide 1-to-1 coverage of every table provided by the Cal Access data dump. On top of speed, we added docs and comments throughout the codebase.

After the parser gets the raw data into shape and we rip out the campaign finance data we export to a sensible set of flat tables that set the Lance’s of the world off and running on stories they would otherwise never do. Plus they use the data on a daily basis to verify what tipsters are saying to them on the phone. Not only does it facilitate more and better stories it frees up the time of the power users to craft more tools and focus on solving hard reporting problems. Money saver. Efficient use of resources.

Other milestones include:

1.0 of loading and cleaning data
100% coverage: ALL 76 models have data that loads into the db (nearly 35 million records), still super fast
Simple, read-only Django admins for all models
Docstrings for new models
Refactored models into modules organized in same way that CA does
Updated the docs to reference new model and admin organization
Documented new, more flexible management commands
Frontend

After downloading and parsing the data, we wanted to create a simple way to explore the data without running the Python console. After two days, we rewrote the frontend to work to look great and provide some nifty features:

See a table of data on the page? You can download it as either JSON or CSV
Search for candidate and committee contributions. We hope to have full search coverage soon.
These two features alone make browsing and the consuming the data than ever before. Now, a journalist can find a candidate they're looking for and download their entire reported campaign finance history with the click of a button.

While these tools are great, but we also wanted to provide a one stop shop for the parsed data as well. That's why we also created URL TK, a weekly updating website with the latest snapshots of the parsed Cal Access data. If you're less interested in the large data dump and would prefer a cleaned set of data to build a graphic, this is what you want. Or throw it into your favorite RDBMS. The world is your oyster.

Going Forward

Get data ready for November Election
More documentation