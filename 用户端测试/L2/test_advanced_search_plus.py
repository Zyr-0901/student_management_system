# 要求实现搜索功能的Web自动化测试。
# Selenium 常用操作与用例编写。
# 使用显式等待优化代码。
# 考虑特殊场景的验证。
# 输入内容过长。
# 特殊字符。
# 其他。
# 使用参数化优化代码。
# 步骤截图。
# 提交内容:
# 代码的git地址或帖子地址。
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from 用户端测试.utils.operate_yaml import OperateYaml


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
                             OperateYaml.read_yaml('datas/search_data.yaml').get("validDatas"))
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

        # 点击搜索按钮
        self.driver.find_element(By.XPATH, self.search_button_ele).click()

        # 确认结果返回值
        search_result_object = WebDriverWait(self.driver, 5). \
            until(expected_conditions.visibility_of_element_located((By.XPATH, self.search_result_ele)))
        search_results = search_result_object.text

        # 断言,确认第一条数据标题是否包含搜索词
        assert search_text.lower() in search_results.lower()

    @pytest.mark.parametrize('search_text, desc',
                             OperateYaml.read_yaml('datas/search_data.yaml').get("invalidDatas"))
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

        # 点击搜索按钮
        self.driver.find_element(By.XPATH, self.search_button_ele).click()

        # 确认结果
        # 断言,确认第一条数据标题是否包含搜索词

        if search_text == "  ":
            # 查找是否有提示,输入为空的情况
            search_result_tip_object = WebDriverWait(self.driver, 5). \
                until(expected_conditions.visibility_of_element_located((By.XPATH, self.search_result_tip_ele)))
            search_result_tip = search_result_tip_object.text
            assert "您的搜索词过短" in search_result_tip
        else:
            # 查找结果
            search_result_object = WebDriverWait(self.driver, 10). \
                until(expected_conditions.visibility_of_element_located((By.XPATH, self.search_result_ele_1)))
            search_results = search_result_object.text
            assert search_results == ''
