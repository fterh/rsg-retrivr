from urllib.parse import urlparse
import re
import os
import json

import praw

from modules.article import article

print("Initializing retrivr.py")

reddit = praw.Reddit("rsg-retrivr")
rsg = reddit.subreddit("singapore")

with open("sites.json", "r") as f:
    sites = json.load(f)

with open("replied.txt", "r") as f:
    replied = f.read().split("\n")
    replied = list(filter(None, replied))

for submission in rsg.new(limit=10):

    # if submission is a link and I have not replied to it before
    if not submission.is_self and submission.id not in replied:

        # if domain matches one of the supported sites
        domain = urlparse(submission.url).netloc
        for site in sites["sites"]:
            if (re.search(site["re_url_match"], domain)):

                a = article(submission.url, site)

                if hasattr(a, "title") and hasattr(a, "body"):
                    post_footer = ("> [Source](" + submission.url + ")\n\n---\n"
                        "v1.0 | [Github](https://github.com/fterh/rsg-retrivr) "
                        "| I'm designed to never spam (i.e. no multiple posts)")
                    post = "> #" + a.title + "\n\n" + a.body + post_footer

                    # post my comment subject to character limits
                    if (len(post) <= 9900):
                        submission.reply(post)
                        print("Replied (success) to " + submission.id)

                    else:
                        post = ("Sorry, the article is too long for me to "
                            "post without spamming. I'm as bummed as you are.")
                        submission.reply(post)
                        print("Replied (too long) to " + submission.id)

                    replied.append(submission.id)

                    with open("replied.txt", "w") as f:
                        for id in replied:
                            f.write(id + "\n")

print("Ending retrivr.py")
