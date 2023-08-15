import allure
import time
from selenium.webdriver.common.by import By
from 用户端测试.L3.page_objects.base_page import BasePage
from 用户端测试.utils.log_util import logger


class DeleteMemberPage(BasePage):
    _BUT_DELETE = (By.XPATH, '//*[@class="js_operationBar_footer ww_operationBar"]//*[text()="删除"]')
    _CONFIRM_DELETE = (By.XPATH, '//*[@d_ck="submit_hr_helper"]')

    def single_delete(self):
        """
        点击删除
        TODO: 企业微信通讯需要彻底删除，否则使用相同邮箱创建时会提示，该企业邮箱已在邮箱回收站内; 临时处理方法在后台管理、协作 禁用邮箱

        """
        with allure.step("删除勾选的成员"):
            logger.info("通讯录列表删除勾选成员")
            self.wait_element_until_click(self._BUT_DELETE).click()
            time.sleep(1)
            self.wait_element_until_click(self._CONFIRM_DELETE).click()
            time.sleep(2)
            from 用户端测试.L3.page_objects.member_list_page import MemberListPage
            return MemberListPage(self.driver)
