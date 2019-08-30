import time
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base import BasePage


class LoginPage(BasePage):
    """登陆页面"""
    url = "http://120.78.128.25:8765/Index/login.html"

    user_locator = (By.NAME, "phone")
    pwd_locator = (By.NAME, "password")
    error_locator = (By.CSS_SELECTOR, ".form-error-info")
    auto_locator = (By.CSS_SELECTOR, ".layui-layer-content")

    def login(self, username, pwd):
        self.driver.get(self.url)
        user_ele = self.get_user_info()
        pwd_ele = self.get_pwd_info()

        user_ele.send_keys(username)
        pwd_ele.send_keys(pwd)
        user_ele.submit()
        return self.driver

    def get_error_info(self):
        """获取错误信息"""
        error_ele = self.wait_presence_element(self.error_locator)
        return error_ele

    def get_error_auto(self):
        """获取没有授权信息"""
        error_ele = self.wait_presence_element(self.auto_locator)
        return error_ele

    def clear_user_info(self):
        """清空用户与密码数据"""
        self.clear_username()
        self.clear_pwd()

    def clear_username(self):
        """清空用户"""
        return self.get_user_info().clear()

    def clear_pwd(self):
        """清空密码"""
        return self.get_pwd_info().clear()

    def get_user_info(self):
        """定位用户名输入框"""
        user_ele = self.wait_presence_element(self.user_locator)
        return user_ele

    def get_pwd_info(self):
        """定位密码输入框"""
        pwd_ele = self.wait_presence_element(self.pwd_locator)
        return pwd_ele

