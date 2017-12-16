import os
from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

global mercury_api_key, dev_subreddit, prod_subreddit
mercury_api_key = os.environ.get("mercury_api_key")
dev_subreddit = os.environ.get("dev_subreddit")
prod_subreddit = os.environ.get("prod_subreddit")
