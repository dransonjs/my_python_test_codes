# import unittest
import pytest
# from ddt import ddt, data
# from selenium.webdriver import Chrome
# from pages.login_page import LoginPage
# from pages.home_page import HomePage
# from pages.bid_page import BidPage
# from pages.user_page import UserPage
# from data.login_data import login_success_data
from data.bid_data import bid_fail_data, bid_fail_data2, bid_success_data


# @ddt
class TestBid:
    """
    测试投资类
    """
    # @classmethod
    # def setUpClass(cls):
    #     cls.browser = Chrome()
    #     cls.browser.implicitly_wait(20)
    #     cls.login_page = LoginPage(cls.browser)
    #     cls.home_page = HomePage(cls.browser)
    #     cls.bid_page = BidPage(cls.browser)
    #     cls.user_page = UserPage(cls.browser)
    #     cls.login_page.login(login_success_data["phone"], login_success_data["pwd"])
    #     cls.home_page.click_bid_button()
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.browser.quit()
    #
    # def tearDown(self):
    #     self.bid_page.get_element_bid_input.clear()

    @pytest.mark.unusual
    # @data(*bid_fail_data)
    @pytest.mark.parametrize('bid_data', bid_fail_data)
    def test_1_bid_fail(self, bid_data, init_browser, enter_bid_page, clear_bid_input):
        bid_page = enter_bid_page[0]
        # self.bid_page.click_bid_input()
        bid_page.bid(bid_data["money"])
        # self.assertEqual(bid_data["tip"], self.bid_page.get_element_bid_button.text, "填写非10的整数倍金额的提示不一致")
        assert bid_data["tip"] == bid_page.get_element_bid_button.text, "填写非10的整数倍金额的提示不一致"

    @pytest.mark.unusual
    def test_2_bid_fail2(self, init_browser, enter_bid_page, clear_bid_input):
        bid_page = enter_bid_page[0]
        bid_page.bid(bid_fail_data2["money"])
        bid_page.click_bid_button()
        # self.assertEqual(bid_fail_data2["tip"], self.bid_page.get_element_bid_fail_tip.text, "不填写数字，直接点击投资按钮弹出的提示不一致")
        assert bid_fail_data2["tip"] == bid_page.get_element_bid_fail_tip.text, "不填写数字，直接点击投资按钮弹出的提示不一致"
        bid_page.confirm_tip_button()

    @pytest.mark.normal
    # @data(*bid_success_data)
    @pytest.mark.parametrize('bid_data', bid_success_data)
    def test_3_bid_success(self, bid_data, init_browser, enter_bid_page, clear_bid_input):
        bid_page, user_page = enter_bid_page
        amount_balance = bid_page.get_amount_balance()
        bid_page.bid(bid_data["money"])
        bid_page.click_bid_button()
        # self.assertEqual(bid_data["tip"], self.bid_page.get_element_bid_success_tip.text, "投标成功的提示不一致")
        assert bid_data["tip"] == bid_page.get_element_bid_success_tip.text, "投标成功的提示不一致"
        bid_page.click_look_and_active_button()
        expected = amount_balance - bid_data["money"]*100
        actual = user_page.get_amount_balance()
        # self.assertEqual(expected, actual, "投标成功后余额扣除错误")
        assert expected == actual, "投标成功后余额扣除错误"
        user_page.click_invest_project()
        user_page.scroll()
        user_page.click_bid()


if __name__ == '__main__':
    pytest.main(["--resultlog=report1/test2.txt",
                 "--junitxml=report1/test2.xml",
                 "--html=report1/test2.html"])

