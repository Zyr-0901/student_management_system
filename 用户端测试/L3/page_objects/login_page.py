import os
import time

import yaml

from 用户端测试.L3.page_objects.base_page import BasePage
from 用户端测试.L3.page_objects.home_page import HomePage


class LoginPage(BasePage):
    _BASE_URL = "https://work.weixin.qq.com/wework_admin/loginpage_wx"
    _INDEX_URL = "https://work.weixin.qq.com/wework_admin/frame"

    def login(self):
        """
        判断cookie是否过期
        打开登录页
        强制等待提供人工扫码时间
        获取cookie
        cookie存储
        植入cookie,以便后续请求无需在次登录
        点击首页，验证植入cookie是否成功
        """
        # 判断cookie是否过期,未过期返回cookie,否则返回expire
        cookies = self.confirm_cookie_status()
        if cookies == "expire":
            # 打开企业微信登录页
            self.driver.get(self._BASE_URL)
            # 强制等待,人工扫码
            time.sleep(15)
            # 登录成功后获取cookie
            cookies = self.driver.get_cookies()
            # cookie存储
            base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            cookie_path = os.path.join(base_path, 'datas/cookies.yaml')
            with open(cookie_path, 'w') as f:
                yaml.safe_dump(cookies, f)
            time.sleep(2)
        # 植入cookie
        for c in cookies:
            self.driver.add_cookie(c)
        time.sleep(2)
        # 打开首页确认cookie是否植入成功
        self.driver.get(self._INDEX_URL)
        # 进入首页
        return HomePage(self.driver)
