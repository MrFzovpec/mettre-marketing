import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidArgumentException
from secret import get_username, get_password
import time


class HashtagUserParser:
    def __init__(self, url):
        self.url = url