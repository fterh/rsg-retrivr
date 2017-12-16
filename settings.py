import json
import os
from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

global MERCURY_API_KEY, DEV_SUBREDDIT, PROD_SUBREDDIT
MERCURY_API_KEY = os.environ.get("mercury_api_key")
DEV_SUBREDDIT = os.environ.get("dev_subreddit")
PROD_SUBREDDIT = os.environ.get("prod_subreddit")

APPROVED_SITES = [
    "asiaone.com",
    "channelnewsasia.com",
    "mothership.sg",
    "ricemedia.co",
    "sg.news.yahoo.com",
    "straitstimes.com",
    "theonlinecitizen.com",
    "theindependent.sg",
    "todayonline.com"
]

BLOCKED_LINKS = [
    "facebook.com"
]
