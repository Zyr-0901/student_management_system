from selenium.webdriver.common.by import By

from 用户端测试.L3.page_objects.base_page import BasePage
from 用户端测试.L3.page_objects.member_list_page import MemberListPage


class CreateMemberPage(BasePage):
    def create_member_to_save(self):
        """
        填写相关字段
        点击保存
        :return:
        """
        self.driver.find_element(By.ID, 'username').send_keys('test4')
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys('test4@qq.com')
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys('15650779709')
        self.driver.find_element(By.XPATH, '//*[text()="保存"]').click()
        return MemberListPage(self.driver)

    def create_member_to_save_and_continue(self):
        """
        填写相关字段
        点击保存并继续添加
        :return:
        """
        return
