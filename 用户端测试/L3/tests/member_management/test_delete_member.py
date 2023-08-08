import pytest
from selenium.webdriver.common.by import By

from 用户端测试.L3.page_objects.login_page import LoginPage
from 用户端测试.utils.operate_yaml import OperateYaml


class TestDeleteMember:
    def setup_class(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.home = LoginPage().login()

    @pytest.mark.parametrize("username, acctid, phone, desc",
                             OperateYaml.read_yaml("dates/mock_data.yaml").get("qywx").get("create"))
    def test_delete_member(self, username):
        """
        查找创建的数据
        若找到
            勾选创建的数据
            点击删除
        若未找到
            创建数据
            删除数据
        """

        x_path = '//*[text()="'
        x_path += username
        x_path += '"'
        x_path += ']'

        ele = self.do_find_elements(By.XPATH, x_path)
        ele.click()
        # // *[ @
        #
        # class ="ww_operationBar"] // *[text()="删除"]
        # self.driver
