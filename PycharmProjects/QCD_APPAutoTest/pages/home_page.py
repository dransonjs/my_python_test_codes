import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from pages.base_page import BasePage


class HomePage(BasePage):

    swipe_count = 3
    welcome_btn_locator = (MobileBy.ANDROID_UIAUTOMATOR,
                           'new UiSelector().resourceId(\"com.xxzb.fenwoo:id/btn_start\")')

    def welcome(self):
        for _ in range(self.swipe_count):
            self.swipe_left()
        self.wait_click_element(self.welcome_btn_locator).click()


if __name__ == '__main__':
    desired_caps = {
        "automationName": "UiAutomator1",
        "platformName": "Android",
        "platformVersion": "5.1",
        "deviceName": "Android Emulator",
        "appPackage": "com.xxzb.fenwoo",
        "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",
        "noReset": False
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    time.sleep(3)
    home_page = HomePage(driver)
    home_page.welcome()
