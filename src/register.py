import os
import validators
from pathlib import Path
from typing import Optional, Union

import webbrowser
from webdriver_manager.chrome import *
from webdriver_manager.firefox import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException as EC
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

from utils.utils import get_logger

logger = get_logger(__name__)

class Register(object):
    def __init__(self,
                 browser_type=['chrome', 'firefox']
    ):
        self.browser_type = browser_type

    def get_driver(self):
        global driver
        try:
            for browser in self.browser_type:
                if browser == 'chrome':
                    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = option)
                    break
                elif browser == 'firefox':
                    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
                    break
        except:
            raise TypeError('Browser type is not supported')

        return driver

    @staticmethod
    def check_browser_exist(browser):
        try:
            if webbrowser.get(browser):
                return True
        except:
            return False

    @staticmethod
    def check_xpath_exist(xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except EC:
            return False
        return True

    @staticmethod
    def login_facebook(username, password):
        driver.find_element(by = By.NAME, value = 'email').send_keys(username)
        driver.find_element(by = By.NAME, value = 'pass').send_keys(password)
        driver.find_element(by = By.NAME, value = 'login').click()

    @staticmethod
    def access_website(url):
        if validators.url(url):
            driver.get(url)
            logger.info('Accessing website: {}'.format(url))
        else:
            logger.error('Invalid url: {}'.format(url))









