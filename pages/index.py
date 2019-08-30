from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base import BasePage


class IndexPage(BasePage):
    """初始化首页"""
    bid_locator = (By.XPATH, "//span[text()=' 咖啡馆']")
    user_locator = (By.LINK_TEXT, "我的帐户[python10]")

    def __init__(self, driver):
        self.driver = driver

    def get_user_info(self):
        """获取首页的用户信息"""
        user_name = self.wait_clickable_element(self.user_locator)
        return user_name

    def choose_bid(self):
        """选择标"""
        ele = self.wait_clickable_element(self.bid_locator, 20)
        return ele.click()

