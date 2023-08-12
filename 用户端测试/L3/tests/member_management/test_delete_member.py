import os
import sys
import allure

sys.path.append(os.getcwd())
from 用户端测试.L3.page_objects.login_page import LoginPage


@allure.epic("通讯录管理")
@allure.feature("删除通讯录成员")
class TestDeleteMember:
    def setup_class(self):
        self.home = LoginPage().login()

    def teardown_class(self):
        self.driver.quit()

    def create_member(self, username, acctid, phone, email):
        self.home \
            .click_add_by_home() \
            .create_member_save(username, acctid, phone, email)

    @allure.title("冒烟测试")
    def test_delete_member(self):
        """
        删除流程
        进入首页
        点击通讯录
        勾选删除数据
        点击删除
        校验结果
        """
        # 创建数据
        username = "删除成员测试"
        acctid = "delete_member@qq.com"
        phone = "15650771234"
        email = "delete_member@qq.com"
        self.create_member(username, acctid, phone, email)

        # 删除数据
        result = self.home \
            .go_to_member_list() \
            .check_delete_box(username) \
            .single_delete() \
            .get_operate_results()

        assert username not in result
