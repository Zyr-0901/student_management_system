"""
要求实现搜索功能的Web自动化测试。
Selenium 常用操作与用例编写。
使用显式等待优化代码。
考虑特殊场景的验证。
输入内容过长。
特殊字符。
其他。
使用参数化优化代码。
步骤截图。
提交内容:
代码的git地址或帖子地址。

场景描述
打开测试人论坛，截图。
跳转到高级搜索页面，添加显式等待判断页面跳转成功并截图。
搜索输入框输入搜索关键字，截图。关键字清单如下：
Selenium
Appium
面试
打印当前结果页面的pagesource并截图。
打印搜索结果的第一个标题。
断言：第一个标题是否包含关键字。
"""
import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from 用户端测试.utils.operate_yaml import OperateYaml


def save_key_screenshots(driver):
    """
    将一些关键步骤进行截图
    设置文件路径
    截图
    存储
    """
    timestamp = int(time.time())
    image_path = f"./images/image_{timestamp}.PNG"
    driver.save_screenshot(image_path)


def save_key_pagesource(driver):
    """
    将一些关键页面截图
    设置存放路径
    保存HTML页面
    """
    timestamp = int(time.time())
    page_path = f"./page_sources/pagesource_{timestamp}.html"
    with open(page_path, "w", encoding="u8") as f:
        f.write(driver.page_source)


class TestAdvancedSearchPlus:
    target_path = "https://ceshiren.com/search"
    search_box_ele = '//*[@aria-label="输入搜索关键字"]'
    search_button_ele = '//*[@aria-label="搜索"][@type="button"]'
    search_result_ele = '//*[@class="fps-result-entries"]/div[1]//*[@class="topic-title"]/span'
    search_result_ele_1 = '//*[@class="fps-result-entries"]'
    search_result_tip_ele = '//*[@class="fps-invalid"]'

    def setup_class(self):
        """
        浏览器初始化
        增加显示等待
        打开目标地址
        """
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get(self.target_path)

    def teardown_class(self):
        """
        执行完当前全部用例后,关闭浏览器
        """
        self.driver.quit()

    @pytest.mark.parametrize('search_text, desc',
                             OperateYaml.read_yaml('datas/search_data.yaml').get("validDates"))
    def test_search_valid(self, search_text, desc):
        """
        设置用例标题
        查找搜索框
        清空搜索框内容
        键入搜索内容
        点击搜索
        确认是结果返回情况: 正常搜索到结果/找不到结果/数据内容太短
        断言
        """
        # 设置标题
        allure.dynamic.title(desc)

        # 1.查找搜索框 2.清空搜索框内容 3.键入搜索内容
        search_box = WebDriverWait(self.driver, 5). \
            until(expected_conditions.element_to_be_clickable((By.XPATH, self.search_box_ele)))
        search_box.clear()
        search_box.send_keys(search_text)

        # 键入输入内容后截图
        save_key_screenshots(self.driver)

        # 点击搜索按钮
        self.driver.find_element(By.XPATH, self.search_button_ele).click()

        # 确认结果返回值
        search_result_object = WebDriverWait(self.driver, 5). \
            until(expected_conditions.visibility_of_element_located((By.XPATH, self.search_result_ele)))
        search_results = search_result_object.text

        # 对查询结果获取页面源码
        save_key_pagesource(self.driver)

        # 断言,确认第一条数据标题是否包含搜索词
        assert search_text.lower() in search_results.lower()

    @pytest.mark.parametrize('search_text, desc',
                             OperateYaml.read_yaml('datas/search_data.yaml').get("invalidDates"))
    def test_search_invalid(self, search_text, desc):
        """
        设置用例标题
        查找搜索框
        清空搜索框内容
        键入搜索内容
        点击搜索
        确认是结果返回情况: 正常搜索到结果/找不到结果/数据内容太短
        断言
        """
        # 设置标题
        allure.dynamic.title(desc)

        # 1.查找搜索框 2.清空搜索框内容 3.键入搜索内容
        search_box = WebDriverWait(self.driver, 5). \
            until(expected_conditions.element_to_be_clickable((By.XPATH, self.search_box_ele)))
        search_box.clear()
        search_box.send_keys(search_text)

        # 键入输入内容后截图
        save_key_screenshots(self.driver)

        # 点击搜索按钮
        self.driver.find_element(By.XPATH, self.search_button_ele).click()

        # 确认结果
        # 断言,确认第一条数据标题是否包含搜索词

        if search_text == "  ":
            # 查找是否有提示,输入为空的情况
            search_result_tip_object = WebDriverWait(self.driver, 5). \
                until(expected_conditions.visibility_of_element_located((By.XPATH, self.search_result_tip_ele)))
            search_result_tip = search_result_tip_object.text

            # 对查询结果获取页面源码
            save_key_pagesource(self.driver)

            assert "您的搜索词过短" in search_result_tip
        else:
            # 查找结果
            search_result_object = WebDriverWait(self.driver, 10). \
                until(expected_conditions.visibility_of_element_located((By.XPATH, self.search_result_ele_1)))
            search_results = search_result_object.text

            # 对查询结果获取页面源码
            save_key_pagesource(self.driver)

            assert search_results == ''

    @pytest.mark.parametrize('search_text, desc',
                             OperateYaml.read_yaml('datas/search_data.yaml').get("specialDates"))
    def test_search_special(self, search_text, desc):
        """
        判断是否可以自动TAB补全
        判断是否可以模糊匹配
        判断多次搜索后的结果
        """

        # 设置标题
        allure.dynamic.title(desc)

        # 1.查找搜索框 2.清空搜索框内容 3.键入搜索内容
        search_box = WebDriverWait(self.driver, 5). \
            until(expected_conditions.element_to_be_clickable((By.XPATH, self.search_box_ele)))
        search_box.clear()
        search_box.send_keys(search_text)

        # 键入输入内容后截图
        save_key_screenshots(self.driver)

        # 搜索时自动补全情况
        if search_text == "seleni":
            except_text = "selenium"
            # 默认手工执行tab操作
            search_box.send_keys(Keys.TAB)
            # 获取当前输入框的值
            actual_text_object = self.driver.find_element(By.XPATH, self.search_box_ele)
            actual_text = actual_text_object.text

            # 断言 当前文本框的实际值是否等于期待值
            assert actual_text != except_text

        # 模糊匹配情况
        if search_text == "selen":
            # 点击搜索按钮
            self.driver.find_element(By.XPATH, self.search_button_ele).click()

            # 确认结果返回值
            search_result_object = WebDriverWait(self.driver, 5). \
                until(expected_conditions.visibility_of_element_located((By.XPATH, self.search_result_ele)))
            search_results = search_result_object.text

            # 对查询结果获取页面源码
            save_key_pagesource(self.driver)

            # 断言,确认第一条数据标题是否包含搜索词
            assert search_text.lower() in search_results.lower()

        # 多次点击情况
        if search_text == "Selenium":
            result = []
            for i in range(3):
                # 点击搜索按钮
                self.driver.find_element(By.XPATH, self.search_button_ele).click()

                # 获取结果列表
                pre_search_result_object = self.driver.find_elements(By.XPATH, self.search_result_ele)
                # 获取结果数量
                search_result_num = len([element.text for element in pre_search_result_object])
                result.append(search_result_num)

            # 对查询结果获取页面源码
            save_key_pagesource(self.driver)

            # 断言,通过判断多次点击后的查询数量是否一致
            assert len(set(result)) == 1
