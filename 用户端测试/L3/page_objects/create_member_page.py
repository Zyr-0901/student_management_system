import allure
from selenium.webdriver.common.by import By
from 用户端测试.L3.page_objects.base_page import BasePage


class CreateMemberPage(BasePage):
    def create_member_save(self, username="test4", acctid="test4@qq.com", phone="15650779709"):
        """
        确认待填写字段是否加载出来
        填写相关字段
        点击保存
        """
        with allure.step("创建成员,并点击保存"):
            self.do_send_keys(username, By.ID, 'username')
            self.do_send_keys(acctid, By.ID, 'memberAdd_acctid')
            self.do_send_keys(phone, By.ID, 'memberAdd_phone')
            self.do_find(By.XPATH, '//*[text()="保存"]').click()
            from 用户端测试.L3.page_objects.member_list_page import MemberListPage
            return MemberListPage(self.driver)

    def create_member_save_and_continue(self, username="test5", acctid="test5@qq.com", phone="15650779710"):
        """
        填写相关字段
        点击保存并继续添加
        """
        with allure.step("创建成员,并点击保存并继续添加"):
            self.do_send_keys(username, By.ID, 'username')
            self.do_send_keys(acctid, By.ID, 'memberAdd_acctid')
            self.do_send_keys(phone, By.ID, 'memberAdd_phone')
            self.do_find(By.XPATH, '//*[text()="保存并继续添加"]').click()
            from 用户端测试.L3.page_objects.member_list_page import MemberListPage
            return MemberListPage(self.driver)
