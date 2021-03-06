# this module listens for mentions ("/u/rsg-retrivr")

import re

from modules.core import core

def listener(reddit, subreddit, replied, settings):

    print("Running listener()")

    mentions = reddit.inbox.mentions(limit=5)

    for mention in mentions:

        print("For mention " + mention.id)

        submission = reddit.submission(mention.submission.id)

        if re.search("summon$", mention.body) is not None and \
        not submission.is_self and mention.submission.id not in replied:

            print("Summon's submission (" + submission.id + ") is link and not in replied")

            if(core(submission, replied, settings, mention, True) is False):
                mention.reply("Unfortunately, I can't do that, for various \
                reasons.")
