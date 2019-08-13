from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import BasePage


class LoginPage(BasePage):

    tel_locator = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiSelector().resourceId(\"com.xxzb.fenwoo:id/et_phone\")')

    next_locator = (MobileBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().textContains(\"下一步\")')

    invalid_tel_locator = (MobileBy.ANDROID_UIAUTOMATOR,
                           'new UiSelector().textContains(\"无效的手机号\")')

    invalid_confirm_locator = (MobileBy.ANDROID_UIAUTOMATOR,
                               'new UiSelector().textContains(\"确定\")')

    pwd_locator = (MobileBy.ID, "com.xxzb.fenwoo:id/et_pwd")

    pwd_confirm_locator = (MobileBy.ID, "com.xxzb.fenwoo:id/btn_next_step")

    back_locator = (MobileBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().resourceId(\"com.xxzb.fenwoo:id/btn_back\")')

    pwd_error_msg_locator = (MobileBy.XPATH, "//*[contains(@text, '手机号或密码错误')]")

    @property
    def input_tel(self):
        return self.wait_visibility_element(self.tel_locator)

    def next_step(self):
        self.wait_click_element(self.next_locator).click()

    @property
    def invalid_tel(self):
        return self.wait_visibility_element(self.invalid_tel_locator)

    def tel_confirm(self):
        self.wait_click_element(self.invalid_confirm_locator).click()

    @property
    def input_pwd(self):
        return self.wait_visibility_element(self.pwd_locator)

    def pwd_confirm(self):
        self.wait_click_element(self.pwd_confirm_locator).click()

    def back(self):
        self.wait_click_element(self.back_locator).click()

    @property
    def pwd_error_msg(self):
        return self.wait_presence_element(self.pwd_error_msg_locator)
