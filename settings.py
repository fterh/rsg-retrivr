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

with open("sites.json", "r") as f:
    sites = json.load(f)

APPROVED_SITES = sites["approved-sites"]
BLOCKED_LINKS = sites["blocked-links"]
