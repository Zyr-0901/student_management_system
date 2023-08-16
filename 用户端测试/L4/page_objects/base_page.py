import os
import time
from datetime import datetime
import allure
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from 用户端测试.L4.conftest import web_env


class BasePage:
    _INDEX_URL = "https://work.weixin.qq.com/wework_admin/frame#index"

    def __init__(self, driver=None):
        browser = web_env.get("browser")
        if driver:
            self.driver = driver
        else:
            caps = {
                'browserName': "chrome",
            }
            if browser == "firefox":
                caps['browserName'] = "firefox"
            options = Options()
            # 将浏览器设置为中文
            options.add_argument("--lang=zh-CN")
            # 连接selenium grid
            driver = webdriver.Remote(
                command_executor='http://43.138.100.186:5444',
                desired_capabilities=caps,
                options=options
            )
            # 设置隐式等待
            driver.implicitly_wait(3)
            # 设置最大窗口
            driver.maximize_window()

            self.driver = driver

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

    def wait_element_until_click(self, locator: tuple):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))

    def save_key_screenshots(self, name):
        """
        将一些关键步骤进行截图
        设置文件路径
        截图
        存储
        """
        timestamp = int(time.time())
        base_url = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(base_url, f"images/{timestamp}_{name}.png")
        self.driver.save_screenshot(image_path)
        allure.attach.file(image_path, f"{timestamp}_{name}.PNG", allure.attachment_type.PNG, "png")

    def save_key_pagesource(self, name):
        """
        将一些关键页面截图
        设置存放路径
        保存HTML页面
        """
        timestamp = int(time.time())
        base_url = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        page_path = os.path.join(base_url, f"page_sources/{timestamp}_{name}.html")
        with open(page_path, "w", encoding="u8") as f:
            f.write(self.driver.page_source)
        allure.attach.file(page_path, f"{timestamp}_{name}.html", allure.attachment_type.HTML, "html")

    def confirm_cookie_status(self):
        """
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

    def back_home(self):
        self.driver.get(self._INDEX_URL)

    def quit_driver(self):
        self.driver.quit()

    def switch_language(self):
        self.driver.get('chrome://settings/')
        self.do_find((By.ID, 'languages')).click()
        self.do_find((By.ID, 'addLanguages')).click()
        self.do_find((By.XPATH, '//*[@aria-label="Add Chinese"]')).click()


