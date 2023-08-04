from selenium.webdriver.common.by import By
from 用户端测试.L3.page_objects.base_page import BasePage


class MemberListPage(BasePage):
    def click_add_member(self):
        pass

    def get_results(self):
        member_list = self.driver.find_elements(By.XPATH, 'member_list')
        results = member_list[-2]
        result = results.find_element(By.CLASS_NAME, 'member_colRight_memberTable_td').text()
        return result