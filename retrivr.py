from urllib.parse import urlparse
import re
import os

import praw
import requests
from bs4 import BeautifulSoup as bs

reddit = praw.Reddit("rsg-retrivr")

if not os.path.isfile("replied.txt"):
    replied = []

else:
    with open("replied.txt", "r") as f:
        replied = f.read()
        replied = replied.split("\n")
        replied = list(filter(None, replied))

    for submission in rsg.new(limit=10):
        # if submission is a link
        if (not submission.is_self):

            # where domain == straitstimes.com
            domain = urlparse(submission.url).netloc
            match = re.search("straitstimes.com$", domain)
            if match:

                # if I have not commented on this post before
                if (submission.id not in replied):

                    # the works
                    r = requests.get(submission.url)
                    if (r.status_code == 200): #if GET is successful
                        retriv = bs(r.text, "html.parser")

                        #extracts article title
                        p_title = retriv.find(class_="headline node-title").string

                        #extracts article body
                        p_body = ""
                        for paragraph in retriv.select("div[itemprop='articleBody'] > p "):
                            p_body += "> " + paragraph.get_text() + "\n\n"

                        p_footer = ("> [Source](" + submission.url + ")\n\n---\n"
                            "v1.0 | [Github](https://github.com/fterh/rsg-retrivr) "
                            "| I'm designed to never spam (i.e. no multiple posts)")
                        post = "># " + p_title + "\n\n" + p_body + p_footer

                        # post my comment subject to character limits
                        if (post.len <= 9500):
                            submission.reply(post)
                        else:
                            post = ("Sorry, the article is too long for me to "
                            "post without spamming. I'm as bummed as you are.")
                            submission.reply(post)

                        replied.append(submission.id)

                        with open("replied.txt", "w") as f:
                            for id in replied:
                                f.write(id + "\n")
