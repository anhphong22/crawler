import os
import re
import csv
import sys

import pandas as pd
import requests
import validators

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException as EC

from register import Register

from utils.utils import get_logger, load_json
logger = get_logger(__name__)


class Ivivu(Register):
    def __init__(self,
                 browser_type=['chrome', 'firefox']
    ):
        super().__init__(browser_type)
        global driver
        driver = self.get_driver()

    def collect_link_data(self, url):
        self.access_website(url)
        destinations = driver.find_elements(by = By.ID, value = 'idpostion_20')
        destinations = destinations[:8]
        destination_link = []
        for des in destinations:
            href = driver.find_element(by = By.XPATH, value = '//a[@title="{des.text}"]'.format(des=des)).get_attribute('href')
            destination_link.append(href)

        driver.close()
        return destination_link

    def retrieve_data(self, url):
        data_link = self.collect_link_data(url)
        for link in data_link:
            self.access_website(link)
            entity_title = driver.find_element(by = By.CLASS_NAME, value = 'entry-title').text




if __name__ == "__main__":
    url = 'https://www.ivivu.com/blog/2013/10/du-lich-ha-noi-cam-nang-tu-a-den-z/'
    ivivu = Ivivu()
    print(ivivu.collect_link_data(url))





