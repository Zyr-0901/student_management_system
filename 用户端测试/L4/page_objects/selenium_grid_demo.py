from selene.support.shared import browser, config
from selenium.webdriver import Chrome
import selenium.webdriver

if __name__ == '__main__':
    config.browser_name = 'chrome'
    config.base_url = "http://43.138.100.186/:5444"
    config.timeout = 10
    config.save_screenshot_on_failure = False

    option = selenium.webdriver.ChromeOptions()
    option.add_argument("--disable-infobars")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-extensions")
    option.add_argument("--ignore-ssl-errors")
    option.add_argument("--ignore-certificate-errors")
    option.add_argument('--disable-gpu')
    prefs = {'download.default_directory': '/home/seluser/Downloads/'}
    option.add_experimental_option('prefs', prefs)
    option.add_experimental_option('w3c', False)
    option.add_experimental_option('perfLoggingPrefs', {
        'enableNetwork': True,
        'enablePage': False,
    })
    caps = option.to_capabilities()
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}
    config.driver = selenium.webdriver.Remote(
        command_executor="http://43.138.100.186:5444",
        desired_capabilities=caps,
        keep_alive=True,
        options=option)
    config.driver.set_page_load_timeout(10)

    browser.open('/')
    browser.driver.maximize_window()