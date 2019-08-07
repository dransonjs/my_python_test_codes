# import unittest
import pytest
# from ddt import ddt, data
# from selenium.webdriver import Chrome
# from pages.login_page import LoginPage
# from pages.home_page import HomePage
from data.login_data import login_fail_data, login_fail_data2, login_success_data


# @ddt
class TestLogin:
    """
    测试登录类
    """
    # @classmethod
    # def setUpClass(cls):
    #     cls.browser = Chrome()
    #     cls.browser.implicitly_wait(20)
    #     cls.login_page = LoginPage(cls.browser)
    #     cls.home_page = HomePage(cls.browser)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.browser.quit()

    # def tearDown(self):
    #     self.browser.refresh()

    @pytest.mark.unusual
    # @data(*login_fail_data)
    # pytest的参数化，相当于unittest的ddt，用法为@pytest.mark.parametrize('用例中要使用的变量名', 具体变量数据)
    @pytest.mark.parametrize('user_data', login_fail_data)
    def test_1_login_error(self, user_data, init_browser, refresh_browser):
        login_page = init_browser[0]
        login_page.login(user_data["phone"], user_data["pwd"])
        error_tips_e = login_page.get_element_miss_phone
        # self.assertEqual(user_data["tip"], error_tips_e.text, "登录失败提示不一致")
        assert user_data["tip"] == error_tips_e.text, "登录失败提示不一致"

    @pytest.mark.unusual
    # @data(*login_fail_data2)
    @pytest.mark.parametrize('user_data', login_fail_data2)
    def test_2_login_error2(self, user_data, init_browser, refresh_browser):
        login_page = init_browser[0]
        login_page.login(user_data["phone"], user_data["pwd"])
        error_tips_e = login_page.get_element_unauthorized
        # self.assertEqual(user_data["tip"], error_tips_e.text, "登录失败提示不一致")
        assert user_data["tip"] == error_tips_e.text, "登录失败提示不一致"

    @pytest.mark.normal
    def test_3_login_success(self, init_browser):
        login_page, home_page = init_browser[0], init_browser[1]
        login_page.login(login_success_data["phone"], login_success_data["pwd"])
        user_e = home_page.get_element_user
        # self.assertEqual(login_success_data["username"], user_e.text, "登录成功用例不通过")
        assert login_success_data["username"] == user_e.text, "登录成功用例不通过"


if __name__ == '__main__':
    # unittest.main()
    pytest.main(["--resultlog=report1/test.txt",
                 "--junitxml=report1/test.xml",
                 "--html=report1/test.html"])
