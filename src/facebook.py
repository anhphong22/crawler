import os
import re
import csv
import sys

import pandas as pd
import requests
import validators

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException as EC

from register import Register

from utils.utils import get_logger, load_json
logger = get_logger(__name__)

class Facebook(Register):
    def __init__(self,
                 browser_type=['chrome', 'firefox']
                 ):
        super().__init__(browser_type)
        global driver
        driver = self.get_driver()

    def auto_comment(self, url, username, password, fanpages, content):
        self.access_website(url)
        self.login_facebook(username, password)
        logger.info(f'Login to {username} account successfully')

        for fanpage in fanpages:
            self.access_website(fanpage)
            comments = driver.find_elements(by = By.XPATH, value = '//*[@aria-label="Viết bình luận"]')
            for comment in comments:
                comment.click()
                comment.send_keys(f' {content}')
                comment.send_keys(Keys.ENTER)
                comment.click()
                logger.info(f'Comment to {fanpage} successfully')


if __name__ == '__main__':
    url = 'https://www.facebook.com'
    username = 'dtung.nss@gmail.com'
    password = 'dangtungnss'
    fanpages = ['https://www.facebook.com/groups/congtyketoanluatdangkhoa', 'https://www.facebook.com/groups/470268646737844',
                'https://www.facebook.com/groups/1480185875533351']
    content = 'Nhà tôi cần bán một nhà ở tại vị trí Phú Thịnh II, thành phố Thuận An, Tỉnh Bình Dương. Diện tích 70m2, nhà 1 trệt, 1 lầu, mới sửa chữa. Pháp lý rõ ràng. Giá bán 3.1 tỷ. Mọi thông tin vui lòng liên hệ qua zalo hoặc gọi trực tiếp Phong 0964.964.038'

    fb = Facebook()
    fb.auto_comment(url, username, password, fanpages, content)



