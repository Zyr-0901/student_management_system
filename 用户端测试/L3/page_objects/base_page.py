import os
from datetime import datetime

import yaml
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _INDEX_URL = "https://work.weixin.qq.com/wework_admin/frame"

    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()
            # 设置隐式等待
            self.driver.implicitly_wait(3)
            # 设置最大窗口
            self.driver.maximize_window()

    def do_find(self, by, locator=None):
        """获取单个元素"""
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def do_find_elements(self, by, locator=None):
        """获取多个元素"""
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    def do_send_keys(self, value, by, locator=None):
        """给单个元素赋值"""
        if locator:
            ele = self.do_find(by, locator)
            ele.clear()
            ele.send_keys(value)
        else:
            ele = self.do_find(*by)
            ele.clear()
            ele.send_keys(value)

    def wait_element_until_visible(self, locator: tuple):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))

    def confirm_cookie_status(self):
        """
        访问企业微信首页
        判断cookies是否过期
        过期返回expiry
        否则返回cookie
        """
        current_time = datetime.now()
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cookie_path = os.path.join(base_path, 'datas/cookies.yaml')
        with open(cookie_path) as f:
            cookies = yaml.safe_load(f)
        if cookies is not None:
            for cookie in cookies:
                expiry = cookie.get("expiry")
                if expiry is not None:
                    expiry_time = datetime.fromtimestamp(expiry)
                    if current_time >= expiry_time:
                        return "expire"
            return cookies
        else:
            return "expire"
