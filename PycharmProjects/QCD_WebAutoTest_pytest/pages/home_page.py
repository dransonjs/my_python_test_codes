from selenium.webdriver.common.by import By
from pages.locators import HomeLocator
from pages.base_page import BasePage


class HomePage(BasePage):
    """首页页面行为类"""
    locator = HomeLocator

    @property
    def get_element_user(self):
        return self.wait_presence_element((By.XPATH, "//a[text()='我的帐户[python10]']"))

    @property
    def get_element_bid_button(self):
        return self.wait_click_element(self.locator.bid_button_locator)

    def click_bid_button(self):
        return self.get_element_bid_button.click()
