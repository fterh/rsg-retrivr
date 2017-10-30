from urllib.parse import urlparse
import re
import os
import sys
import json

import praw

import settings
from modules.article import article
from modules.mercury import mercury

if len(sys.argv) == 2 and sys.argv[1] == "dev":
    dev = True

if dev is True:
    print("Initializing retrivr.py in dev mode")
else:
    print("Initializing retrivr.py")

reddit = praw.Reddit("rsg-retrivr")

# development or production mode
if dev is True:
    rsg = reddit.subreddit("rsgretrivr")
else:
    rsg = reddit.subreddit("singapore")

with open("sites.json", "r") as f:
    sites = json.load(f)

with open("replied.txt", "r") as f:
    replied = f.read().split("\n")
    replied = list(filter(None, replied))

for submission in rsg.new(limit=10):

    # if submission is a link and I have not replied to it before
    if not submission.is_self and submission.id not in replied:

        a = mercury(submission.url, settings.mercury_api_key)

        if a.title and a.body is not "":
            # article URL
            post_footer = "> [Source](" + submission.url + ")\n\n---\n"

            # footer meta information
            with open("footer_meta.md", "r") as f:
                post_footer += f.read()

            post = "> #" + a.title + "\n\n" + a.body + post_footer

            # post my comment subject to character limits
            if (len(post) <= 9900):
                submission.reply(post)
                print("Replied (success) to " + submission.id)

            else:
                print("Skipped (too long) to " + submission.id)

            replied.append(submission.id)

            with open("replied.txt", "w") as f:
                for id in replied:
                    f.write(id + "\n")

print("Ending retrivr.py")
