import sys

import praw

import settings
from modules.article import article
from modules.listener import listener
from modules.scanner import scanner

# initialize Reddit instance
reddit = praw.Reddit("bot")

# check whether to run in dev mode
if len(sys.argv) == 2 and sys.argv[1] == "dev":
    dev = True
else:
    dev = False

if dev is True:
    print("Initializing retrivr.py in dev mode")
    subreddit = reddit.subreddit(settings.dev_subreddit)

else:
    print("Initializing retrivr.py in production mode")
    subreddit = reddit.subreddit(settings.prod_subreddit)

# open files
with open("sites.txt", "r") as f:
    sites = f.read().split("\n")
    sites = list(filter(None, sites))

with open("replied.txt", "r") as f:
    replied = f.read().split("\n")
    replied = list(filter(None, replied))

scanner(subreddit, sites, replied, settings)
listener(reddit, subreddit, replied, settings)

print("Ending retrivr.py")
