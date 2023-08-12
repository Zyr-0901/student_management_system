import time

import allure
from selenium.webdriver.common.by import By
from 用户端测试.L3.page_objects.base_page import BasePage
from 用户端测试.utils.log_util import logger


class HomePage(BasePage):
    _ADD_MEMBER = (By.XPATH, '//*[@class="ww_operationBar"]//*[text()="添加成员"]')
    _CLICK_MEMBER_LIST = (By.ID, "menu_contacts")

    def click_add_by_home(self):
        """
        点击添加成员
        """

        with allure.step("在首页,点击添加成员"):
            self.wait_element_until_click(self._ADD_MEMBER).click()
            logger.info("从首页跳转到添加成员页面")
            self.save_key_screenshots()
            from 用户端测试.L3.page_objects.create_member_page import CreateMemberPage
            return CreateMemberPage(self.driver)

    def go_to_member_list(self):
        """
        点击通讯录
        """
        with allure.step("在首页,点击通讯录"):
            try:
                self.wait_element_until_click(self._CLICK_MEMBER_LIST).click()
                # TODO 不加强制等待，进入下一步时当前页面还在首页，所以会报错元素找不到
                # TODO 但是在我在每一步都用了隐式等待，实际并未生效，没看懂为什么？麻烦帮忙解答下
                # TODO 因为隐式等待不生效，所以增加了对应的强制等待
                time.sleep(10)
                from 用户端测试.L3.page_objects.member_list_page import MemberListPage
                return MemberListPage(self.driver)
            except Exception as e:
                logger.error(f"点击通讯录时报错: {e}")
