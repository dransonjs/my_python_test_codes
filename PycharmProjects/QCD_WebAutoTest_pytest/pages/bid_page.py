from pages.locators import BidLocator
from pages.base_page import BasePage


class BidPage(BasePage):
    """
    投资页面行为类
    """
    locator = BidLocator

    @property
    def get_element_bid_input(self):
        return self.wait_visitable_element(self.locator.bid_input_locator)

    # def click_bid_input(self):
    #     return self.bid_input.click()

    def get_amount_balance(self):
        amount_balance_str = self.get_element_bid_input.get_attribute("data-amount")
        return int(float(amount_balance_str)*100)

    def bid(self, money):
        return self.get_element_bid_input.send_keys(money)

    @property
    def get_element_bid_button(self):
        return self.wait_visitable_element(self.locator.bid_button2_locator)

    def click_bid_button(self):
        return self.get_element_bid_button.click()

    @property
    def get_element_bid_fail_tip(self):
        return self.wait_visitable_element(self.locator.bid_fail_tip)

    @property
    def get_element_tip_button(self):
        return self.wait_click_element(self.locator.tip_button)

    def confirm_tip_button(self):
        return self.get_element_tip_button.click()

    @property
    def get_element_bid_success_tip(self):
        return self.wait_visitable_element(self.locator.bid_success_tip)

    @property
    def get_element_look_and_active_button(self):
        return self.wait_click_element(self.locator.look_and_active)

    def click_look_and_active_button(self):
        return self.get_element_look_and_active_button.click()
