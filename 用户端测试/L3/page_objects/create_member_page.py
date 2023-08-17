import time
import allure
from selenium.webdriver.common.by import By
from 用户端测试.L3.page_objects.base_page import BasePage
from 用户端测试.utils.log_util import logger


class CreateMemberPage(BasePage):
    _SAVE_BUT = (By.XPATH, '//*[text()="保存"]')
    _SAVE_BUT_AND_ADD = (By.XPATH, '//*[text()="保存并继续添加"]')
    _USERNAME = (By.ID, 'username')
    _ACCTID = (By.ID, 'memberAdd_acctid')
    _PHONE = (By.ID, 'memberAdd_phone')
    _EMAIL = (By.ID, 'memberAdd_mail')
    _INVALID_USERNAME_TIP = (By.CSS_SELECTOR, '#username~.ww_inputWithTips_tips')
    _INVALID_ACCTID_TIP = (By.CSS_SELECTOR, '#memberAdd_acctid~.ww_inputWithTips_tips')
    _INVALID_EMAIL_TIP = (By.CSS_SELECTOR, '#memberAdd_mail~.ww_inputWithTips_tips')
    _INVALID_PHONE_TIP = (By.CSS_SELECTOR, '#memberAdd_phone~.ww_inputWithTips_tips')
    _INDEX_URL = "https://work.weixin.qq.com/wework_admin/frame#index"

    def back_home(self):
        time.implicitly_wait(1)
        self.driver.get(self._INDEX_URL)
        time.implicitly_wait(2)
        self.wait_element_until_click((By.XPATH, '//*[text()="离开此页"]')).click()

    def create_member_save(self, username, acctid, phone, email):
        """
        确认待填写字段是否加载出来
        填写相关字段
        点击保存
        """
        logger.info(f"创建成员 - name:{username};acctid:{acctid};phone:{phone};email:{email}")
        with allure.step("创建成员,并点击保存"):
            self.wait_element_until_visible(self._USERNAME)
            self.do_send_keys(username, self._USERNAME)
            self.do_send_keys(acctid, self._ACCTID)
            self.do_send_keys(phone, self._PHONE)
            self.do_send_keys(email, self._EMAIL)
            self.do_find(self._SAVE_BUT).click()
            time.implicitly_wait(3)
            self.save_key_screenshots(f"创建成员{username}")
            self.save_key_pagesource(f"创建成员{username}")
            from 用户端测试.L3.page_objects.member_list_page import MemberListPage
            return MemberListPage(self.driver)

    def create_member_save_and_continue(self, username, acctid, phone, email):
        """
        填写相关字段
        点击保存并继续添加
        """
        logger.info(f"创建成员 - name:{username};acctid:{acctid};phone:{phone};email:{email}")
        with allure.step("创建成员,并点击保存并继续添加"):
            self.wait_element_until_visible(self._USERNAME)
            self.do_send_keys(username, self._USERNAME)
            self.do_send_keys(acctid, self._ACCTID)
            self.do_send_keys(phone, self._PHONE)
            self.do_send_keys(email, self._EMAIL)
            self.do_find(self._SAVE_BUT_AND_ADD).click()
            time.implicitly_wait(3)
            self.save_key_screenshots(f"创建成员{username}")
            self.save_key_pagesource(f"创建成员{username}")
            from 用户端测试.L3.page_objects.home_page import HomePage
            return HomePage(self.driver)

    def create_member_invalid_username(self, username, acctid, phone, email):
        logger.info(f"创建成员姓名无效 - name:{username};acctid:{acctid};phone:{phone};email:{email}")
        with allure.step(f"无效姓名测试, {username}"):
            self.wait_element_until_visible(self._USERNAME)
            self.do_send_keys(username, self._USERNAME)
            self.do_send_keys(acctid, self._ACCTID)
            tip_text = self.do_find(self._INVALID_USERNAME_TIP).text
            self.save_key_screenshots(f"成员姓名无效{username}")
            self.back_home()
            return tip_text

    def create_member_invalid_acctid(self, username, acctid, phone, email):
        logger.info(f"创建成员账号无效 - name:{username};acctid:{acctid};phone:{phone};email:{email}")
        with allure.step(f"无效账号测试，{acctid}"):
            self.wait_element_until_visible(self._USERNAME)
            self.do_send_keys(username, self._USERNAME)
            self.do_send_keys(acctid, self._ACCTID)
            self.do_send_keys(phone, self._PHONE)
            tip_text = self.do_find(self._INVALID_ACCTID_TIP).text
            self.save_key_screenshots(f"成员账号无效{acctid}")
            self.back_home()
            return tip_text

    def create_member_invalid_email(self, username, acctid, phone, email):
        logger.info(f"创建成员邮箱无效 - name:{username};acctid:{acctid};phone:{phone};email:{email}")
        with allure.step(f"无效邮箱测试, {email}"):
            self.wait_element_until_visible(self._USERNAME)
            self.do_send_keys(username, self._USERNAME)
            self.do_send_keys(acctid, self._ACCTID)
            self.do_send_keys(email, self._EMAIL)
            self.do_find(By.ID, 'memberAdd_title')
            tip_text = self.do_find(self._INVALID_EMAIL_TIP).text
            self.save_key_screenshots(f"成员邮箱无效{email}")
            self.back_home()
            return tip_text

    def create_member_invalid_phone(self, username, acctid, phone, email):
        logger.info(f"创建成员手机号无效 - name:{username};acctid:{acctid};phone:{phone};email:{email}")
        with allure.step(f"无效手机号测试,{phone}"):
            self.wait_element_until_visible(self._USERNAME)
            self.do_send_keys(username, self._USERNAME)
            self.do_send_keys(acctid, self._ACCTID)
            self.do_send_keys(phone, self._PHONE)
            self.do_send_keys(email, self._EMAIL)
            tip_text = self.do_find(self._INVALID_PHONE_TIP).text
            self.save_key_screenshots(f"成员手机号无效{phone}")
            self.back_home()
            return tip_text
