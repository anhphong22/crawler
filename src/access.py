import os
import re
import csv
import sys

import pandas as pd
import requests

from utils.utils import get_logger, load_json

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger(__name__)

"""
    This class is to access the website and pass login information
"""

class Authentication(object):
    def __init__(self, config):
        self.config = config
        cr = CrawlerInit()
        global driver
        driver = cr.get_driver()
        driver.get(self.url)

    def login(self):
        pass

