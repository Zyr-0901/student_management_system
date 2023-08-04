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
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def do_find_elements(self, by, locator=None):
        pass