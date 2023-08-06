import pytest

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
        pass