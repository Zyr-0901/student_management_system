# 要求实现搜索功能的Web自动化测试。
# Selenium 常用操作与用例编写。
# 使用显式等待优化代码。
# 考虑特殊场景的验证。
# 输入内容过长。
# 特殊字符。
# 其他。
# 使用参数化优化代码。
# 步骤截图。
import time

# 场景描述
# 打开测试人论坛，截图。
# 跳转到高级搜索页面，添加显式等待判断页面跳转成功并截图。
# 搜索输入框输入搜索关键字，截图。关键字清单如下：
# Selenium
# Appium
# 面试
# 打印当前结果页面的pagesource并截图。
# 打印搜索结果的第一个标题。
# 断言：第一个标题是否包含关键字。
# 搜索地址: https://ceshiren.com/search
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_advanced_search():
    """
    连接driver
    打开页面
    找到搜索框
    输入内容
    点击搜索
    根据返回结果判断,是否与搜索内容相符
    """
    # 变量/元素定义
    target_path = "https://ceshiren.com/search"
    search_ele = '//*[@type="button" and @aria-label="搜索"]'
    search_box_ele = '//*[@id="ember15" and @aria-label="输入搜索关键字"]'
    search_results_ele = '//*[@role="listitem"][1]//*[@class="topic-title"]/span'
    search_result_count_ele = '//*[@class="result-count"]/span[1]'
    # 实例化driver
    driver = webdriver.Chrome()
    # 打开目标地址
    driver.get(target_path)
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, search_ele)))

    # 查找搜索框,写入搜索内容
    search_text = driver.find_element(By.XPATH, search_box_ele)
    search_text.clear()
    search_text.send_keys("selenium")
    # 点击搜索
    driver.find_element(By.XPATH, search_ele).click()

    # 判断是否有结果
    # 确认结果
    search_result_count = driver.find_element(By.XPATH, search_result_count_ele)
    search_result_count_value = search_result_count.text

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_selected("listitem"))
    search_results = driver.find_element(By.XPATH, search_results_ele)
    search_results_value = search_results.text
    assert 'selenium' in search_results_value
    driver.quit()
