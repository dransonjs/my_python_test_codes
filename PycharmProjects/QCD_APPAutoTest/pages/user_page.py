from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import BasePage


class UserPage(BasePage):

    username_locator = (MobileBy.ID, "com.xxzb.fenwoo:id/tv_name")

    @property
    def get_username(self):
        return self.wait_visibility_element(self.username_locator)
