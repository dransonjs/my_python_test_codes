from pages.locators import UserLocator
from pages.base_page import BasePage


class UserPage(BasePage):
    """
    用户页面行为类
    """
    locator = UserLocator

    @property
    def get_element_amount_balance(self):
        return self.wait_visitable_element(self.locator.amount_balance)

    def get_amount_balance(self):
        amount_str = self.get_element_amount_balance.text
        return int(float(amount_str[:-1])*100)

    @property
    def get_element_invest_project(self):
        return self.wait_click_element(self.locator.invest_project)

    def click_invest_project(self):
        return self.get_element_invest_project.click()

    def scroll(self):
        js_code = "window.scrollTo(0, document.body.scrollHeight)"
        return self.browser.execute_script(js_code)

    @property
    def get_element_bid(self):
        return self.wait_click_element(self.locator.bid)

    def click_bid(self):
        return self.get_element_bid.click()

