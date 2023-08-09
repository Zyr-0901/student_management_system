import pytest
from selenium.webdriver.common.by import By
from 用户端测试.L3.page_objects.login_page import LoginPage
from 用户端测试.utils.operate_yaml import OperateYaml


class TestDeleteMember:
    def setup_class(self):
        self.home = LoginPage().login()

    @pytest.mark.parametrize("username, acctid, phone, desc",
                             OperateYaml.read_yaml("dates/mock_data.yaml").get("qywx").get("create"))
    def test_delete_member(self, username):
        """
        进入首页
        点击通讯录
        勾选删除数据
        点击删除
        校验结果
        """
        result = self.home\
            .go_to_member_list()\
            .check_delete_box(username)\
            .single_delete()\
            .get_operate_results()

        assert username not in result
