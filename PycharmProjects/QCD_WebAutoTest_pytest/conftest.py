import pytest
from selenium.webdriver import Chrome

from pages.bid_page import BidPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.user_page import UserPage
from data.login_data import login_success_data


@pytest.fixture(scope="class")
def init_browser():
    # global browser
    browser = Chrome()
    browser.implicitly_wait(20)
    login_page = LoginPage(browser)
    home_page = HomePage(browser)

    yield login_page, home_page, browser

    browser.quit()


@pytest.fixture()
def refresh_browser(init_browser):
    browser = init_browser[2]
    browser.refresh()


@pytest.fixture(scope="class")
def enter_bid_page(init_browser):
    login_page, home_page, browser = init_browser
    bid_page = BidPage(browser)
    user_page = UserPage(browser)
    login_page.login(login_success_data["phone"], login_success_data["pwd"])
    home_page.click_bid_button()

    yield bid_page, user_page

    browser.quit()


@pytest.fixture()
def clear_bid_input(enter_bid_page):
    bid_page = enter_bid_page[0]
    bid_page.get_element_bid_input.clear()

