import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def driver(request):
    caps = {
        'browserName': "chrome"
    }
    driver = webdriver.Remote(
        command_executor='http://43.138.100.186:5444',
        desired_capabilities=caps
    )

    def fin():
        driver.quit()
    request.addfinalizer(fin)
    return driver

def test_open_baidu(driver):
    driver.get("https://www.baidu.com")
    search_box = driver.find_element(By.NAME, 'wd')
    search_box.send_keys('Selenium Grid')
    search_box.send_keys(Keys.RETURN)
    # WebDriverWait(driver, 10).until(expected_conditions
    #                                 .presence_of_element_located((By.XPATH, '//h3[contains(text(), "Selenium Grid")]')))

    time.sleep(20)