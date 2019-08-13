import time
import unittest
import yaml
from appium import webdriver
from ddt import ddt, data
from data.login_data import tel_error_data, pwd_empty_data, pwd_error_data, login_ok_data
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.user_page import UserPage


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        caps = yaml.load(open("../config/init_app.yml", "r"), Loader=yaml.FullLoader)
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        cls.login_page = LoginPage(cls.driver)
        cls.home_page = HomePage(cls.driver)
        cls.user_page = UserPage(cls.driver)
        time.sleep(3)
        cls.home_page.welcome()
        cls.home_page.home_login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data(*tel_error_data)
    def test_1_tel_error(self, tel):
        self.login_page.input_tel.send_keys(tel)
        self.login_page.next_step()
        expected = "无效的手机号"
        actual = self.login_page.invalid_tel.text
        self.assertEqual(expected, actual, "手机号异常用例-测试失败")
        self.login_page.tel_confirm()
        self.login_page.input_tel.clear()

    def test_2_pwd_empty(self):
        self.login_page.input_tel.send_keys(pwd_empty_data["tel"])
        self.login_page.next_step()
        self.login_page.input_pwd.send_keys(pwd_empty_data["pwd"])
        self.login_page.pwd_confirm()
        expected = pwd_empty_data["pwd"]
        actual = self.login_page.input_pwd.get_attribute('text')
        self.assertEqual(expected, actual, "密码为空用例-测试失败")

    def test_3_pwd_error(self):
        self.login_page.input_pwd.send_keys(pwd_error_data["pwd"])
        self.login_page.pwd_confirm()
        expected = pwd_error_data["msg"]
        actual = self.login_page.pwd_error_msg.text
        self.assertEqual(expected, actual, "密码错误用例-测试失败")

    def test_4_login_success(self):
        self.login_page.input_pwd.send_keys(login_ok_data["pwd"])
        self.login_page.pwd_confirm()
        self.home_page.set_next_time()
        self.home_page.me()
        expected = login_ok_data["username"]
        actual = self.user_page.get_username.text
        self.assertEqual(expected, actual, "登录成功用例-测试失败")


if __name__ == '__main__':
    unittest.main()
