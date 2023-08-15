from selene import browser, config
from selenium.webdriver import Chrome
import selenium.webdriver


def demo():
    # 配置使用的浏览器
    config.browser_name = 'chrome'
    # 配置使用的基础url
    config.base_url = "http://43.138.100.186:5444"
    # 配置超时时间
    config.timeout = 10
    # 测试失败时不保存截图
    config.save_screenshot_on_failure = False

    # 浏览器选项设置
    option = selenium.webdriver.ChromeOptions()
    # 添加一系列Chrome命令行参数,用于配置浏览器行为
    option.add_argument("--disable-infobars")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-extensions")
    option.add_argument("--ignore-ssl-errors")
    option.add_argument("--ignore-certificate-errors")
    option.add_argument('--disable-gpu')

    # 添加实验性选项
    prefs = {'download.default_directory': '/home/seluser/Downloads/'}
    # 设置下载目录
    option.add_experimental_option('prefs', prefs)
    # 禁用W3C标准
    # option.add_experimental_option('w3c', False)

    option.add_experimental_option('perfLoggingPrefs', {
        'enableNetwork': True,
        'enablePage': False,
    })
    # 将chrome选项转换为Selenium的Capabilities对象,用于启动Remote WebDriver
    caps = option.to_capabilities()
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}
    # 创建和配置WebDriver
    # 使用Remote WebDriver 连接到远程的Selenium Grid节点,执行测试
    config.driver = selenium.webdriver.Remote(
        command_executor="http://43.138.100.186:5444",
        desired_capabilities=caps,
        keep_alive=True,
        options=option)
    # 设置页面加载超时时间为10s
    config.driver.set_page_load_timeout(10)

    # 执行测试操作
    # 使用brower对象打开基础URL
    browser.open_url('/')
    # 最大化浏览器窗口


if __name__ == '__main__':
    # demo()
    demo()
