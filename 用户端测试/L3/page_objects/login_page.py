import os
import time
import allure
import yaml
from 用户端测试.L3.page_objects.base_page import BasePage
from 用户端测试.utils.log_util import logger


class LoginPage(BasePage):
    _BASE_URL = "https://work.weixin.qq.com/wework_admin/loginpage_wx"
    _INDEX_URL = "https://work.weixin.qq.com/wework_admin/frame#index"

    def login(self):
        """
        打开首页
        判断cookie是否过期
        强制等待提供人工扫码时间
        获取cookie
        cookie存储
        植入cookie,以便后续请求无需在次登录
        点击首页，验证植入cookie是否成功
        """
        # 判断cookie是否过期,未过期返回cookie,否则返回expire
        with allure.step("登录企业微信"):
            self.driver.get(self._INDEX_URL)
            cookies = self.confirm_cookie_status()
            logger.info(f"cookies的结果 {cookies}")
            if cookies == "expire":
                # 强制等待,人工扫码
                time.sleep(20)
                # 登录成功后获取cookie
                cookies = self.driver.get_cookies()
                # cookie存储
                base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                cookie_path = os.path.join(base_path, 'datas/cookies.yaml')
                with open(cookie_path, 'w') as f:
                    yaml.safe_dump(cookies, f)
                # 保存cookie需要足够的时间，否则会保存不完整，导致无法复用
                time.implicitly_wait(5)
            # 植入cookie
            logger.info("植入cookies")
            for c in cookies:
                self.driver.add_cookie(c)
            # 植入cookie需要足够的时间，否则会出现植入不完整情况

            time.implicitly_wait(5)
            # 打开首页确认cookie是否植入成功
            self.driver.get(self._INDEX_URL)
            # 进入首页
            from 用户端测试.L3.page_objects.home_page import HomePage
            return HomePage(self.driver)
