from appium.webdriver.common.mobileby import MobileBy
from pages.base_page import BasePage


class HomePage(BasePage):

    swipe_count = 3
    welcome_btn_locator = (MobileBy.ANDROID_UIAUTOMATOR,
                           'new UiSelector().resourceId(\"com.xxzb.fenwoo:id/btn_start\")')

    login_locator = (MobileBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().resourceId(\"com.xxzb.fenwoo:id/btn_login\")')

    set_next_time_locator = (MobileBy.ID, "com.xxzb.fenwoo:id/btn_cancel")

    def welcome(self):
        for _ in range(self.swipe_count):
            self.swipe_left()
        self.wait_click_element(self.welcome_btn_locator).click()

    def home_login(self):
        self.wait_visibility_element(self.login_locator).click()

    def set_next_time(self):
        self.wait_click_element(self.set_next_time_locator).click()
