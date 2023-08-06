import time
from 用户端测试.L3.page_objects.base_page import BasePage
from 用户端测试.L3.page_objects.home_page import HomePage


class LoginPage(BasePage):
    _BASE_URL = "https://work.weixin.qq.com/wework_admin/loginpage_wx"
    _INDEX_URL = "https://work.weixin.qq.com/wework_admin/frame"

    def login(self):
        """
        打开登录页
        强制等待提供人工扫码时间
        获取cookie
        在后续请求植入cookie
        点击首页，验证植入cookie是否成功
        """
        # 打开企业微信登录页
        self.driver.get(self._BASE_URL)
        # 强制等待,人工扫码
        time.sleep(20)
        # 登录成功后获取cookie
        cookies = self.driver.get_cookies()
        # 植入cookie
        for c in cookies:
            self.driver.add_cookie(c)
        time.sleep(2)
        self.driver.get(self._INDEX_URL)
        # 进入首页
        return HomePage(self.driver)
