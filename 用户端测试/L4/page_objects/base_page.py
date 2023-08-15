import os
import time
from datetime import datetime

import selenium
from selene import browser, config
import allure
import yaml
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _INDEX_URL = "https://work.weixin.qq.com/wework_admin/frame#index"

    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            config.browser_name = 'chrome'
            # 配置使用的基础url
            config.base_url = "https://work.weixin.qq.com"
            # 配置超时时间
            config.timeout = 10
            # 测试失败时不保存截图
            config.save_screenshot_on_failure = False

            # 浏览器选项设置
            option = selenium.webdriver.ChromeOptions()
            # 添加一系列Chrome命令行参数,用于配置浏览器行为
            option.add_argument("--disable-infobars")
            option.add_argument("--disable-dev-shm-usage")
            option.add_argument("--no-sandbox")
            option.add_argument("--disable-extensions")
            option.add_argument("--ignore-ssl-errors")
            option.add_argument("--ignore-certificate-errors")
            option.add_argument('--disable-gpu')

            # 添加实验性选项
            prefs = {'download.default_directory': '/home/seluser/Downloads/'}
            # 设置下载目录
            option.add_experimental_option('prefs', prefs)
            # 禁用W3C标准
            # option.add_experimental_option('w3c', False)

            option.add_experimental_option('perfLoggingPrefs', {
                'enableNetwork': True,
                'enablePage': False,
            })
            # 将chrome选项转换为Selenium的Capabilities对象,用于启动Remote WebDriver
            caps = option.to_capabilities()
            caps['goog:loggingPrefs'] = {'performance': 'ALL'}
            # 创建和配置WebDriver
            # 使用Remote WebDriver 连接到远程的Selenium Grid节点,执行测试
            config.driver = selenium.webdriver.Remote(
                command_executor="http://43.138.100.186:5444",
                desired_capabilities=caps,
                keep_alive=True,
                options=option)
            # 设置页面加载超时时间为10s
            config.driver.set_page_load_timeout(10)
            self.driver = browser.open_url('/wework_admin/frame#index')

            # # self.driver = webdriver.Chrome()
            # # # 设置隐式等待
            # self.driver.implicitly_wait(3)
            # # 设置最大窗口
            # self.driver.maximize_window()

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
