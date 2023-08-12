"""
使用 PO 设计模式编写自动化测试用例，结合 Allure 生成带日志、截图与操作步骤的测试报告。
通过 css/xpath 定位复杂元素。
使用显示等待、隐式等待优化自动化测试用例，提高用例稳定性。
利用Cookie登录解决扫码登录问题。
提交内容:
代码的 git 地址或帖子地址。
Allure 报告截图。
"""
import os
import sys
import time

import allure
import pytest

sys.path.append(os.getcwd())
from 用户端测试.L3.page_objects.login_page import LoginPage
from 用户端测试.utils.operate_yaml import OperateYaml


@allure.epic("通讯录管理")
@allure.feature("创建通讯录成员")
class TestCreateMember:
    def setup_class(self):
        self.home = LoginPage().login()

    def teardown_class(self):
        self.home.quit_driver()

    def delete_member(self, username):
        """
        TODO:
        创建成功后，会多点一次通讯录，可以怎么优化下

        创建完成后，会回到通讯录页面，获取交过校验结果
        调用删除时，本身当前页面就是通讯录页面，但是为了有通讯录这个对象，所以从self.home 开始
        """
        self.home \
            .go_to_member_list() \
            .check_delete_box(username) \
            .single_delete()

    @allure.story("有效测试")
    @pytest.mark.parametrize("username, acctid, phone, email, desc",
                             OperateYaml.read_yaml("dates/mock_data.yaml").get("qywx").get("validCreate"))
    def test_create_member_1(self, username, acctid, phone, email, desc):
        """
        登录
        点击通讯录
        点击添加成员
        点击保存
        获取结果验证
        """
        allure.dynamic.title(desc)
        names, emails, phones = self.home \
            .go_to_member_list() \
            .click_add_by_member() \
            .create_member_save(username, acctid, phone, email) \
            .get_operate_results()
        assert username in names and email in emails and phone in phones
        self.delete_member(username)

    @allure.story("有效测试")
    @pytest.mark.parametrize("username, acctid, phone, email, desc",
                             OperateYaml.read_yaml("dates/mock_data.yaml").get("qywx").get("validCreate"))
    def test_create_member_2(self, username, acctid, phone, email, desc):
        """
        登录
        点击通讯录
        点击添加成员
        点击保存并继续添加
        获取结果验证
        """
        allure.dynamic.title(desc)
        names, emails, phones = self.home \
            .go_to_member_list() \
            .click_add_by_member() \
            .create_member_save_and_continue(username, acctid, phone, email) \
            .go_to_member_list() \
            .get_operate_results()
        assert username in names and email in emails and phone in phones
        self.delete_member(username)

    @allure.story("有效测试")
    @pytest.mark.parametrize("username, acctid, phone, email, desc",
                             OperateYaml.read_yaml("dates/mock_data.yaml").get("qywx").get("validCreate"))
    def test_create_member_3(self, username, acctid, phone, email, desc):
        """
        登录
        在首页点击添加成员
        填写信息
        点击保存
        """
        allure.dynamic.title(desc)
        names, emails, phones = self.home \
            .click_add_by_home() \
            .create_member_save(username, acctid, phone, email) \
            .get_operate_results()
        assert username in names and email in emails and phone in phones
        self.delete_member(username)

    @allure.story("有效测试")
    @pytest.mark.parametrize("username, acctid, phone, email, desc",
                             OperateYaml.read_yaml("dates/mock_data.yaml").get("qywx").get("validCreate"))
    def test_create_member_4(self, username, acctid, phone, email, desc):
        """
        登录
        在首页点击添加成员
        填写信息
        点击保存并继续添加
        """
        allure.dynamic.title(desc)
        names, emails, phones = self.home \
            .click_add_by_home() \
            .create_member_save_and_continue(username, acctid, phone, email) \
            .go_to_member_list() \
            .get_operate_results()
        assert username in names and email in emails and phone in phones
        self.delete_member(username)

    @allure.story("无效测试")
    @pytest.mark.parametrize("invalid_type, username, acctid, phone, email, excepted, desc",
                             OperateYaml.read_yaml("dates/mock_data.yaml").get("qywx").get("invalidCreate"))
    def test_invalid_create_member(self, invalid_type, username, acctid, phone, email, excepted, desc):
        allure.dynamic.title(desc)
        # if invalid_type == "invalidUsername":
        result = self.home\
            .click_add_by_home()\
            .create_member_invalid_username(username, acctid, phone, email)
        assert result == excepted
        # if invalid_type == "invalidAcctid":
        #     result = self.home\
        #         .click_add_by_home()\
        #         .create_member_invalid_acctid(username, acctid, phone, email)
        #     assert result == excepted
        # if invalid_type == "invalidPhone":
        #     result = self.home \
        #         .click_add_by_home() \
        #         .create_member_invalid_phone(username, acctid, phone, email)
        #     assert result == excepted
        # if invalid_type == "invalidEmail":
        #     result = self.home \
        #         .click_add_by_home() \
        #         .create_member_invalid_email(username, acctid, phone, email)
        #     assert result == excepted
