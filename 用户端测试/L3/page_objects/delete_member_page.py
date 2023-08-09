from selenium.webdriver.common.by import By
from 用户端测试.L3.page_objects.base_page import BasePage
from 用户端测试.L3.page_objects.member_list_page import MemberListPage


class DeleteMemberPage(BasePage):
    _BUT_DELETE = '//*[@class="js_operationBar_footer ww_operationBar"]//*[text()="删除"]'

    def single_delete(self):
        """
        点击删除
        """
        self.do_find(By.XPATH, self._BUT_DELETE).click()
        return MemberListPage(self.driver)
