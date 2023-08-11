from selenium.webdriver.common.by import By
from 用户端测试.L3.page_objects.base_page import BasePage


class MemberListPage(BasePage):
    def click_add(self):
        """在通讯录页面，点击添加成员"""
        self.do_find((By.XPATH, '//*[@class="ww_operationBar"]//*[text()="添加成员"]')).click()
        from 用户端测试.L3.page_objects.create_member_page import CreateMemberPage
        return CreateMemberPage(self.driver)

    def get_operate_results(self):
        """在通讯录页面获取添加结果"""

        member_list = self.do_find_elements(By.XPATH, '//*[@id="member_list"]/tr//td[2]')
        # result = member_list.map(item => item.text())
        # return result

    def check_delete_box(self, username):
        """
        确认删除数据所在行
        勾选删除数据
        """
        x_path = '//*[text()="'
        x_path += username
        x_path += '"'
        x_path += ']'
        x_path += '//..//../td[1]'
        self.do_find(By.XPATH, x_path).click()
        from 用户端测试.L3.page_objects.delete_member_page import DeleteMemberPage
        return DeleteMemberPage(self.driver)
