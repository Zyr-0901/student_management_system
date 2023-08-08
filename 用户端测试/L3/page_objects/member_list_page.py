from selenium.webdriver.common.by import By
from 用户端测试.L3.page_objects.base_page import BasePage


class MemberListPage(BasePage):
    def click_add(self):
        """在通讯录页面，点击添加成员"""
        ele = self.wait_element_until_visible((By.XPATH, '//*[@class="ww_operationBar"]//*[text()="添加成员"]'))
        ele.click()
        from 用户端测试.L3.page_objects.create_member_page import CreateMemberPage
        return CreateMemberPage(self.driver)

    def get_operate_results(self):
        """在通讯录页面获取添加结果"""
        member_list = self.do_find_elements(By.XPATH, '//*[@id="member_list"]/tr//td[2]')
        # result = member_list.map(item => item.text())
        # return result
