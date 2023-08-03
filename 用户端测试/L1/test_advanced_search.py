# 要求实现搜索功能的Web自动化测试。
# Selenium 常用操作与用例编写。
# 使用隐式等待优化代码。
# 考虑特殊场景的验证。
# 输入内容过长。
# 特殊字符。
# 其他。
# 使用参数化优化代码。
# 提交内容:
# 代码的git地址或帖子地址。
# 打开测试人论坛。
# 跳转到高级搜索页面
# 搜索输入框输入搜索关键字。关键字清单如下：
# Selenium
# Appium
# 面试
# 打印搜索结果的第一个标题。
# 断言：第一个标题是否包含关键字。
# 搜索地址: https://ceshiren.com/search
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from 用户端测试.utils.operate_yaml import OperateYaml


class TestAdvancedSearch:
    # 所用XPATH路径
    target_path = "https://ceshiren.com/search"
    search_ele = "//*[@class='d-button-label'][text()='搜索']"
    result_judgment_ele = '//*[@class="search-results"]//h3'
    search_results_ele = '//*[@role="listitem"][1]//*[@class="topic-title"]/span'
    result_judgment_tip_ele = '//*[@class="search-notice"]//div'
    search_box_ele = '//*[@aria-label="输入搜索关键字"]'

    def setup_class(self):
        """
        初始化 chrome
        添加显示等待3秒
        打开目标地址
        """
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get(self.target_path)

    def teardown_class(self):
        # 每执行一个测试用例,就要执行退出操作
        self.driver.quit()

    @pytest.mark.parametrize('search_content, desc',
                             OperateYaml.read_yaml('datas/search_data.yaml').get("validDatas"))
    def test_advanced_search_valid(self, search_content, desc):
        """
        找到搜索框
        输入内容
        点击搜索
        判断是否有内容返回
        验证搜索结果
        """
        # 设置用例标题
        allure.dynamic.title(desc)
        # 选择搜索框
        search_input = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.search_box_ele)))
        # 先清空搜索框
        # 输入搜索内容
        search_input.clear()
        search_input.send_keys(search_content)
        # 点击搜索
        self.driver.find_element(By.XPATH, self.search_ele).click()

        # 判断是否有数据返回
        result_judgment = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.result_judgment_ele)))
        result_judgment_value = result_judgment.text

        # 设置断言,判断搜索结果的标题中是否有搜索关键字
        if "找不到结果" not in result_judgment_value:
            search_results = self.driver.find_element(By.XPATH, self.search_results_ele)
            search_results_value = search_results.text
            assert search_content.lower() in search_results_value.lower()
        else:
            print(result_judgment_value)

    @pytest.mark.parametrize('search_content, desc',
                             OperateYaml.read_yaml('datas/search_data.yaml').get("invalidDatas"))
    def test_advanced_search_invalid(self, search_content, desc):
        """
        找到搜索框
        输入内容
        点击搜索
        判断是否有内容返回
        验证搜索结果
        """
        # 设置用例标题
        allure.dynamic.title(desc)
        # 选择搜索框
        search_input = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.search_box_ele)))
        # 先清空搜索框
        # 输入搜索内容
        search_input.clear()
        search_input.send_keys(search_content)
        # 点击搜索
        self.driver.find_element(By.XPATH, self.search_ele).click()

        # 处理搜索结果
        # 判断是否有结果返回
        # 如果输入框输入为空,是否有提示语
        if search_content == "  ":
            WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, self.result_judgment_tip_ele)))
            result_judgment = self.driver.find_element(By.XPATH, self.result_judgment_tip_ele)
            result_judgment_value = result_judgment.text
            assert "您的搜索词过短" in result_judgment_value
        else:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, self.result_judgment_ele)))
            result_judgment = self.driver.find_element(By.XPATH, self.result_judgment_ele)
            result_judgment_value = result_judgment.text
            if "找不到结果" not in result_judgment_value:
                search_results = self.driver.find_element(By.XPATH, self.search_results_ele)
                search_results_value = search_results.text
                assert search_content.lower() in search_results_value.lower()
            else:
                print(result_judgment_value)
