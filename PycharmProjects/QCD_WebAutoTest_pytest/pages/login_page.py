from pages.locators import LoginLocator
from pages.base_page import BasePage


class LoginPage(BasePage):
    """登录页面行为类"""
    locator = LoginLocator
    url = "http://120.78.128.25:8765/Index/login.html"

    def login(self, username, password):
        self.browser.get(self.url)
        account_e = self.get_element_phone_input
        account_e.send_keys(username)
        pwd_e = self.get_element_pwd_input
        pwd_e.send_keys(password)
        login_e = self.get_element_login_button
        login_e.click()

    @property
    def get_element_unauthorized(self):
        return self.wait_visitable_element(self.locator.login_error1_locator)

    @property
    def get_element_miss_phone(self):
        return self.wait_presence_element(self.locator.login_error2_locator)

    @property
    def get_element_phone_input(self):
        return self.wait_presence_element(self.locator.phone_locator)

    @property
    def get_element_pwd_input(self):
        return self.wait_presence_element(self.locator.pwd_locator)

    @property
    def get_element_login_button(self):
        return self.wait_click_element(self.locator.login_button_locator)
