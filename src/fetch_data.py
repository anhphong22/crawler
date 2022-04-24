import os

import webbrowser
from webdriver_manager.chrome import *
from webdriver_manager.firefox import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException as EC

from utils.utils import get_logger

logger = get_logger(__name__)

class CrawlerInit():
    def __init__(self):
        self.browser_type = ['chrome', 'firefox']
        global driver
        driver = self.get_driver()

    def get_driver(self):
        try:
            for browser in self.browser_type:
                if browser == 'chrome':
                    driver = webdriver.Chrome(ChromeDriverManager().install())
                    break
                elif browser == 'firefox':
                    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
                    break
                logger('Browser type: {}'.format(browser))
        except:
            raise TypeError('Browser type is not supported')

        return driver

    def access_website(self, url):
        driver.get(url)

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

if __name__ == '__main__':
    url = 'https://vnexpress.net/'
    crawl = CrawlerInit()
    crawl.access_website(url)






