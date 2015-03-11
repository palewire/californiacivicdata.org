import time
from github import Github
from datetime import datetime

START = datetime(2015, 2, 27, 0, 0, 0)
END = datetime(2015, 3, 12, 0, 0, 0)

api = Github("7531e5ea4e41ad458d4a1d89e802567f547c7818")

repo_list = [
    "california-civic-data-coalition/django-calaccess-raw-data",
    "california-civic-data-coalition/django-calaccess-campaign-browser",
]
commit_list = []
committer_dict = {}

for name in repo_list:
    print "Pulling data for repo %s" % name
    repo = api.get_repo(name)
    for c in repo.get_commits(since=START, until=END):
        time.sleep(0.15)
        commit_list.append(c)
        if not c.committer:
            print " No committer"
            continue
        try:
            committer_dict[c.committer.name] += 1
        except KeyError:
            committer_dict[c.committer.name] = 0

print "Total commits: %s" % len(commit_list)
print "Total committers: %s" % len(committer_dict.keys())
print "Top committers"
for name, count in sorted(committer_dict.items(), key=lambda x:x[1], reverse=True):
    print "%s: %s" % (name, count)
