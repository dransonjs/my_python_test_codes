import unittest
from ddt import ddt, data
from selenium.webdriver import Chrome
from page.login import LoginPage
from page.home import HomePage
from data.login_data import login_fail_data, login_fail_data2, login_success_data


@ddt
class TestLogin(unittest.TestCase):
    """
    测试登录类
    """
    def setUp(self):
        self.browser = Chrome()
        self.browser.implicitly_wait(20)
        self.login_page = LoginPage(self.browser)
        self.home_page = HomePage(self.browser)

    def tearDown(self):
        self.browser.quit()

    def test_login_success(self):
        self.login_page.login(login_success_data["phone"], login_success_data["pwd"])
        user_e = self.home_page.get_element_user()
        self.assertEqual("我的帐户[python10]", user_e.text, "登录成功用例不通过")

    @data(*login_fail_data)
    def test_login_error(self, user_data):
        self.login_page.login(user_data["phone"], user_data["pwd"])
        error_tips_e = self.login_page.get_element_miss_phone()
        self.assertEqual(user_data["tip"], error_tips_e.text, "登录失败提示不一致")

    @data(*login_fail_data2)
    def test_login_error2(self, user_data):
        self.login_page.login(user_data["phone"], user_data["pwd"])
        error_tips_e = self.login_page.get_element_unauthorized()
        self.assertEqual(user_data["tip"], error_tips_e.text, "登录失败提示不一致")


if __name__ == '__main__':
    unittest.main()
