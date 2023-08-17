import time
import allure
from selenium.webdriver.common.by import By
from 用户端测试.L3.page_objects.base_page import BasePage
from 用户端测试.utils.log_util import logger


class MemberListPage(BasePage):
    _ADD_MEMBER = (By.XPATH, '//*[@class="ww_operationBar"]//*[text()="添加成员"]')
    _MEMBER_LIST = (By.XPATH, '//*[@id="member_list"]/tr//td[2]')

    def click_add_by_member(self):
        """在通讯录页面，点击添加成员"""
        with allure.step("在通讯录页面,点击添加成员"):
            self.wait_element_until_click(self._ADD_MEMBER).click()
            from 用户端测试.L3.page_objects.create_member_page import CreateMemberPage
            return CreateMemberPage(self.driver)

    def get_operate_results(self):
        """在通讯录页面获取添加结果"""
        with allure.step("在通讯录页面,获取通讯录列表"):
            logger.info("获取创建成员结果")
            self.wait_element_until_visible(self._MEMBER_LIST)
            self.save_key_screenshots("通讯录列表")
            member_list = self.do_find(By.XPATH, '//*[@id="member_list"]')
            names = []
            emails = []
            phones = []
            rows = member_list.find_elements(By.XPATH, ".//tr")
            for row in rows:
                cells = row.find_elements(By.XPATH, ".//td")
                for index, cell in enumerate(cells):
                    if index == 1 and cell.text:
                        names.append(cell.text)
                    if index == 4 and cell.text:
                        phones.append(cell.text)
                    if index == 5 and cell.text:
                        emails.append(cell.text.split("\n")[1])
            return names, emails, phones

    def check_delete_box(self, username):
        """
        确认删除数据所在行
        勾选删除数据
        """
        with allure.step("在通讯录页面,勾选删除数据"):
            x_path = '//*[text()="'
            x_path += username
            x_path += '"'
            x_path += ']'
            x_path += '//..//../td[1]'
            self.wait_element_until_click((By.XPATH, x_path)).click()
            self.save_key_screenshots(f"删除成员{username}")
            # 给截图一些时间
            time.implicitly_wait(3)
            from 用户端测试.L3.page_objects.delete_member_page import DeleteMemberPage
            return DeleteMemberPage(self.driver)
