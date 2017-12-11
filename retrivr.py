from urllib.parse import urlparse
import re
import os
import sys
import json

import praw

import settings
from modules.article import article
from modules.mercury import mercury

# initialize Reddit instance
reddit = praw.Reddit("rsg-retrivr")

# check whether to run in dev mode
if len(sys.argv) == 2 and sys.argv[1] == "dev":
    dev = True
else:
    dev = False

if dev is True:
    print("Initializing retrivr.py in dev mode")
    sub = reddit.subreddit("rsgretrivr")

else:
    print("Initializing retrivr.py")
    sub = reddit.subreddit("singapore")

# open files
with open("sites.txt", "r") as f:
    sites = f.read().split("\n")
    sites = list(filter(None, sites))

with open("replied.txt", "r") as f:
    replied = f.read().split("\n")
    replied = list(filter(None, replied))

for submission in sub.new(limit=10):

    # if submission is a link and I have not replied to it before
    if not submission.is_self and submission.id not in replied:

        parsed_url = urlparse(submission.url)
        site_is_supported = None
        for site in sites:
            if re.search(site, parsed_url.netloc) is not None:
                site_is_supported = True

        #if site_is_supported
        if site_is_supported is True:

            a = mercury(submission.url, settings.mercury_api_key)

            if a.title is not "" and a.body is not "":
                # link to article
                post_footer = "> [Source](" + submission.url + ")\n\n---\n"

                # footer meta information
                with open("footer_meta.md", "r") as f:
                    post_footer += f.read()

                # article author information
                post_author = ""
                if a.author is not None:
                    post_author = "> #####By " + a.author + "\n\n"

                post = "> #" + a.title + "\n\n" + post_author + a.body + post_footer

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
