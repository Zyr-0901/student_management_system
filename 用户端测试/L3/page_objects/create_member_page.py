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

    def create_member_save(self, username="test4", acctid="test4@qq.com", phone="15650779709", email="test4@qq.com"):
        """
        确认待填写字段是否加载出来
        填写相关字段
        点击保存
        """
        with allure.step("创建成员,并点击保存"):
            logger.info(f"创建成员 - name:{username};acctid:{acctid};phone:{phone};email:{email}")
            self.wait_element_until_visible(self._USERNAME)
            self.do_send_keys(username, self._USERNAME)
            self.do_send_keys(acctid, self._ACCTID)
            self.do_send_keys(phone, self._PHONE)
            self.do_send_keys(email, self._EMAIL)
            self.do_find(self._SAVE_BUT).click()
            time.sleep(3)
            self.save_key_screenshots(f"创建成员{username}")
            from 用户端测试.L3.page_objects.member_list_page import MemberListPage
            return MemberListPage(self.driver)

    def create_member_save_and_continue(self, username="test5", acctid="test5@qq.com", phone="15650779710", email="test4@qq.com"):
        """
        填写相关字段
        点击保存并继续添加
        """
        with allure.step("创建成员,并点击保存并继续添加"):
            logger.info(f"创建成员 - name:{username};acctid:{acctid};phone:{phone};email:{email}")
            self.wait_element_until_visible(self._USERNAME)
            self.do_send_keys(username, self._USERNAME)
            self.do_send_keys(acctid, self._ACCTID)
            self.do_send_keys(phone, self._PHONE)
            self.do_send_keys(email, self._EMAIL)
            self.do_find(self._SAVE_BUT_AND_ADD).click()
            time.sleep(3)
            self.save_key_screenshots(f"创建成员{username}")
            from 用户端测试.L3.page_objects.member_list_page import MemberListPage
            return MemberListPage(self.driver)
