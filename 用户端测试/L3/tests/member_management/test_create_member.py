from selenium import webdriver

from 用户端测试.L3.page_objects.login_page import LoginPage


class TestCreateMember:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def test_create_member_1(self):
        """
        进入通讯录页面
        点击添加成员
        点击保存
        获取结果验证
        :return
        """
        login_page = LoginPage(self.driver)
        result = login_page.\
            login().\
            click_add_member().\
            create_member_to_save().\
            get_results()
        assert result == "test4"


    def test_create_member_2(self):
        """
        进入通讯录页面
        点击添加成员
        点击保存并继续添加
        点击通讯录
        获取结果验证
        :return:
        """
        pass


    def test_create_member_3(self):
        """
        在首页点击添加成员
        填写信息
        点击继续
        :return:
        """


    def test_create_member_4(self):
        """
        在首页点击添加成员
        填写信息
        点击保存并继续添加
        :return:
        """
