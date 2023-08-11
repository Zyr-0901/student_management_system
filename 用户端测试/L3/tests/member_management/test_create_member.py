"""
使用 PO 设计模式编写自动化测试用例，结合 Allure 生成带日志、截图与操作步骤的测试报告。
通过 css/xpath 定位复杂元素。
使用显示等待、隐式等待优化自动化测试用例，提高用例稳定性。
利用Cookie登录解决扫码登录问题。
提交内容:
代码的 git 地址或帖子地址。
Allure 报告截图。
"""
import allure
import pytest
from 用户端测试.L3.page_objects.login_page import LoginPage
from 用户端测试.utils.operate_yaml import OperateYaml


@allure.feature("创建成员")
class TestCreateMember:
    def setup_class(self):
        self.home = LoginPage().login()

    def teardown_class(self):
        self.driver.quit()

    def delete_member(self, username):
        self.home \
            .go_to_member_list() \
            .check_delete_box(username) \
            .single_delete()

    @allure.story("通讯录页面->点击添加成员->点击保存")
    @pytest.mark.parametrize("username, acctid, phone, desc",
                             OperateYaml.read_yaml("dates/mock_data.yaml").get("qywx").get("create"))
    def test_create_member_1(self, username, acctid, phone, desc):
        """
        登录
        点击通讯录
        点击添加成员
        点击保存
        获取结果验证
        """
        desc += desc
        allure.dynamic.title(desc)
        result = self.home \
            .go_to_member_list() \
            .click_add() \
            .create_member_save(username, acctid, phone) \
            .get_operate_results()
        assert result == username
        self.delete_member(username)

    @allure.story("通讯录页面->点击添加成员->点击保存并继续添加")
    @pytest.mark.parametrize("username, acctid, phone, desc",
                             OperateYaml.read_yaml("dates/mock_data.yaml").get("qywx").get("create"))
    def test_create_member_2(self, username, acctid, phone, desc):
        """
        登录
        点击通讯录
        点击添加成员
        点击保存并继续添加
        获取结果验证
        """
        allure.dynamic.title(desc)
        result = self.home \
            .go_to_member_list() \
            .click_add() \
            .create_member_save_and_continue(username, acctid, phone) \
            .get_operate_results()
        assert result == username
        self.delete_member(username)

    @allure.story("首页->点击添加成员->点击保存")
    @pytest.mark.parametrize("username, acctid, phone, desc",
                             OperateYaml.read_yaml("dates/mock_data.yaml").get("qywx").get("create"))
    def test_create_member_3(self, username, acctid, phone, desc):
        """
        登录
        在首页点击添加成员
        填写信息
        点击保存
        """
        allure.dynamic.title(desc)
        result = self.home \
            .click_add() \
            .create_member_save(username, acctid, phone) \
            .get_operate_results()
        assert result == username
        self.delete_member(username)

    @allure.story("首页->点击添加成员->点击保存并继续添加")
    @pytest.mark.parametrize("username, acctid, phone, desc",
                             OperateYaml.read_yaml("dates/mock_data.yaml").get("qywx").get("create"))
    def test_create_member_4(self, username, acctid, phone, desc):
        """
        登录
        在首页点击添加成员
        填写信息
        点击保存并继续添加
        """
        allure.dynamic.title(desc)
        result = self.home \
            .click_add() \
            .create_member_save_and_continue(username, acctid, phone) \
            .get_operate_results()
        assert result == username
        self.delete_member(username)
