import sys

import praw

import settings
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
    subreddit = reddit.subreddit(settings.DEV_SUBREDDIT)
else:
    print("Initializing retrivr.py in live mode")
    subreddit = reddit.subreddit(settings.PROD_SUBREDDIT)

# open files
print("Opening replied.txt")
with open("replied.txt", "r") as f:
    replied = f.read().split("\n")
    replied = list(filter(None, replied))
    print("replied.txt loaded")

print("Loading scanner()")
scanner(subreddit, replied, settings)
print("Loading listener()")
listener(reddit, subreddit, replied, settings)

print("Ending retrivr.py")
