import os
from os.path import join, dirname
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

TWITTER_USERNAME = os.environ.get("TWITTER_USERNAME")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
TWITTER_NAME = os.environ.get("TWITTER_NAME")

CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_experimental_option("detach", True)

WAIT_TIME = 5
