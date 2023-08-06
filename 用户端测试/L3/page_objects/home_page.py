from selenium.webdriver.common.by import By
from 用户端测试.L3.page_objects.base_page import BasePage


class HomePage(BasePage):

    def click_add(self):
        """
        点击添加成员
        """
        self.do_find(By.XPATH, '//*[@node-type="addmember"]').click()
        from 用户端测试.L3.page_objects.create_member_page import CreateMemberPage
        return CreateMemberPage(self.driver)

    def go_to_member_list(self):
        """
        点击通讯录
        """
        self.do_find((By.ID, "menu_contacts")).click()
        from 用户端测试.L3.page_objects.member_list_page import MemberListPage
        return MemberListPage(self.driver)
