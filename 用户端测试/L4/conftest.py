from _pytest.config import Config
from _pytest.config.argparsing import Parser

web_env = {}
def pytest_addoption(parser: Parser):
    # 注册一个命令行参数
    # pytest --browser=chrome
    parser.addoption("--browser", default="chrome", dest="browser", help="指定执行的浏览器")

def pytest_configure(config: Config):
    # 获取命令行参数
    browser = config.getoption("--browser")
    web_env['browser'] = browser
