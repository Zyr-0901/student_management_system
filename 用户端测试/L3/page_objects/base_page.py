from selenium import webdriver


class BasePage:
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

