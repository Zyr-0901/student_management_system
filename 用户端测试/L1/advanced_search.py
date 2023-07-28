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
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from 用户端测试.utils.operate_yaml import OperateYaml

target_path = "https://ceshiren.com/search"
search_ele = '//*[@type="button" and @aria-label="搜索"]'
result_judgment_ele = '//*[@class="search-results"]//h3'
search_results_ele = '//*[@role="listitem"][1]//*[@class="topic-title"]/span'
result_judgment_tip_ele = '//*[@class="search-notice"]//div'


@pytest.fixture()
# @pytest.fixture(params=["Selenium", "Appium", "面试", "@!#$%", "11111111111111111111111111111111111111"])
def browser(request):
    try:
        # 实例化driver
        driver = webdriver.Chrome()
        yield driver
    except:
        print("执行失败")
    finally:
        driver.quit()


@pytest.mark.parametrize('search_content', OperateYaml.read_yaml('datas/search_data.yaml').get("validDatas"),
                         ids=OperateYaml.read_yaml('datas/search_data.yaml').get("validDataIds"))
def test_advanced_search_valid(browser, search_content):
    """
    连接driver
    打开页面
    找到搜索框
    输入内容
    点击搜索
    判断是否有内容返回
    验证搜索结果
    """
    driver = browser
    # search_content = browser[1]
    # search_content = search_contents[0]

    # 打开目标地址
    driver.get(target_path)
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, search_ele)))

    # 搜索内容
    search(driver, search_ele, search_content)

    # 判断是否有数据返回
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, result_judgment_ele)))
    result_judgment = driver.find_element(By.XPATH, result_judgment_ele)
    result_judgment_value = result_judgment.text

    if "找不到结果" not in result_judgment_value:
        search_results = driver.find_element(By.XPATH, search_results_ele)
        search_results_value = search_results.text
        assert search_content.lower() in search_results_value.lower()
    else:
        print(result_judgment_value)


@pytest.mark.parametrize('search_content', OperateYaml.read_yaml('datas/search_data.yaml').get("invalidDatas"),
                         ids=OperateYaml.read_yaml('datas/search_data.yaml').get("invalidDataIds"))
def test_advanced_search_invalid(browser, search_content):
    """
    连接driver
    打开页面
    找到搜索框
    输入内容
    点击搜索
    判断是否有内容返回
    验证搜索结果
    """
    driver = browser
    # search_content = browser[1]
    # search_content = search_contents[0]

    # 打开目标地址
    driver.get(target_path)
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, search_ele)))

    # 搜索内容
    search(driver, search_ele, search_content)

    # 处理搜索结果
    # 判断是否有结果返回
    # 如果输入框输入为空,是否有提示语
    if search_content == "  ":
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, result_judgment_tip_ele)))
        result_judgment = driver.find_element(By.XPATH, result_judgment_tip_ele)
        result_judgment_value = result_judgment.text
        assert "您的搜索词过短" in result_judgment_value
    else:
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, result_judgment_ele)))
        result_judgment = driver.find_element(By.XPATH, result_judgment_ele)
        result_judgment_value = result_judgment.text
        if "找不到结果" not in result_judgment_value:
            search_results = driver.find_element(By.XPATH, search_results_ele)
            search_results_value = search_results.text
            assert search_content.lower() in search_results_value.lower()
        else:
            print(result_judgment_value)


def search(driver, search_ele, search_content):
    search_box_ele = '//*[@id="ember15" and @aria-label="输入搜索关键字"]'
    # 查找搜索框,写入搜索内容
    search_text = driver.find_element(By.XPATH, search_box_ele)
    search_text.clear()
    search_text.send_keys(search_content)
    # 点击搜索
    driver.find_element(By.XPATH, search_ele).click()
