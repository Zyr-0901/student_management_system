from selenium.webdriver.common.by import By

from 用户端测试.L3.page_objects.base_page import BasePage
from 用户端测试.L3.page_objects.create_member_page import CreateMemberPage
from 用户端测试.L3.page_objects.member_list_page import MemberListPage


class HomePage(BasePage):

    # 添加成员
    def click_add_member(self):
        """
        点击添加成员
        """
        self.driver.find_element(By.XPATH, '//*[@node-type="addmember"]').click()
        return CreateMemberPage(self.driver)

    # 进入通讯录页面通讯录
    def go_to_member_list(self):
        """
        点击通讯录
        :return:
        """
        return MemberListPage()
