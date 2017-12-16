# this module scans the latest "new" submissions
# this is, essentially, the original functionality of the Bot

from urllib.parse import urlparse
import re

from modules.core import core

def scanner(subreddit, replied, settings):
    
    for submission in subreddit.new(limit=10):

        # if submission is a link and I have not replied to it before
        if not submission.is_self and submission.id not in replied:

            parsed_url = urlparse(submission.url)
            site_is_supported = None
            for site in settings.APPROVED_SITES:
                if re.search(site, parsed_url.netloc) is not None:
                    site_is_supported = True
                    break

            # if site is supported
            if site_is_supported is True:
                core(submission, replied, settings)
