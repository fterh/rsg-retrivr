import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

global mercury_api_key
mercury_api_key = os.environ.get("mercury_api_key")
