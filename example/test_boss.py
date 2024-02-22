import csv
import time
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBoss:
    """
    1.整理组合
    城市区域: 深圳 / 杭州 / 广州 / 厦门 / 福州 / 苏州
    职位类型为: 运营客服->电商运营->跨境电商运营/亚马逊运营/亚马逊产品开发
              销售->外贸业务员/外贸经理
              市场/公关广告 -> 海外市场
    公司规模: 100-499/500-5999/1000-9999/10000以上
    2.遍历组合
    """
    def test_boss(self):
        target_path = "https://www.zhipin.com/web/geek/job?city=101280600&scale=303,304,305,306&position=130124"
        country = ["深圳", "杭州", "广州", "厦门", "苏州", "福州"]
        position_types = [" 运营/客服->跨境电商运营", " 运营/客服-->亚马逊运营",
                          " 运营/客服->亚马逊产品开发", " 销售->外贸业务员", " 销售->外贸经理",
                          " 市场/公关广告->海外市场"]

        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(target_path)
        time.sleep(2)

        for c in country:
            try:
                # 选择城市
                if c != "深圳":
                    ele = '//*[contains(@ka,"sel-city-") and text()="'
                    ele += c
                    ele += '"]'
                    driver.find_element(By.XPATH, ele).click()
                time.sleep(random.randint(5,15))
                # 职位类型
                for p in position_types:
                    a, b, = p.split("->")

                    if c == "深圳" and b != "跨境电商运营":
                        # 鼠标移动到职位类型
                        position_type = driver.find_element(By.XPATH, '//*[text()="职位类型"]')
                        ActionChains(driver).move_to_element(position_type).perform()

                        # 选择第一级分类,同时鼠标移动到第一级分类
                        first_name = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, f"//*[text()=\"{a}\"]")))
                        ActionChains(driver).move_to_element(first_name).perform()

                        # 选择第二级分类
                        second_name = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, f"//*[text()=\"{b}\"]")))
                        second_name.click()
                        time.sleep(5)
                    # 获取页数
                    pages = driver.find_element(By.XPATH, '//*[@class="options-pages"]/a[last()-1]').text
                    for page in range(1, int(pages) + 1):
                        if page != 1:
                            driver.find_element(By.XPATH, f"//*[@class='options-pages']/a[text()={page}]").click()
                            time.sleep(10)
                        job_lists = driver.find_elements(By.XPATH, '//li[contains(@ka, "search_list_")]')
                        data = []
                        for job in job_lists:
                            company = job.find_element(By.XPATH, './/h3/a')
                            company_name = company.text
                            href = company.get_attribute("href")
                            data.append([company_name, href])
                        file_path = "result.csv"
                        with open(file_path, 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(data)
                        time.sleep(20)
            except WebDriverException:
                print("报错")
            except Exception:
                print("报错")
        driver.quit()