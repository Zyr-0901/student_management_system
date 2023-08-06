from selenium.webdriver.common.by import By
from 用户端测试.L3.page_objects.base_page import BasePage


class MemberListPage(BasePage):
    def click_add(self):
        """在通讯录页面，点击添加成员"""
        self.do_find(By.XPATH, '//*[@class="ww_operationBar"]//*[text()="添加成员"]').click()
        from 用户端测试.L3.page_objects.create_member_page import CreateMemberPage
        return CreateMemberPage(self.driver)

    def get_operate_results(self):
        """在通讯录页面获取添加结果"""
        member_list = self.driver.find_elements(By.XPATH, 'member_list')
        results = member_list[-2]
        result = results.find_element(By.CLASS_NAME, 'member_colRight_memberTable_td').text()
        return result
