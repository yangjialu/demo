import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class BasePage(object):
    def __init__(self, driver: Chrome):
        self.driver = driver

    def wait_presence_element(self, locator, timeout=10):
        try:
            user_name = WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(locator))
            return user_name
        except Exception as e:
            print("错误是{}".format(e))
            # 截屏
            self.driver.save_screenshot("test.png")

    def wait_clickable_element(self, locator, timeout=10):
        try:
            user_name = WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable(locator))
            return user_name
        except Exception as e:
            print("错误是{}".format(e))
            # 截屏
            self.driver.save_screenshot("test1.png")