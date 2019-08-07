from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
from file_path import IMG_PATH
import os


class BasePage:
    """
    被所有页面操作类继承的基类
    """
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def wait_presence_element(self, locator, timeout=10, poll=0.5) -> WebElement:
        wait = WebDriverWait(self.browser, timeout, poll)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_click_element(self, locator, timeout=10, poll=0.5) -> WebElement:
        wait = WebDriverWait(self.browser, timeout, poll)
        return wait.until(EC.element_to_be_clickable(locator))

    def wait_visitable_element(self, locator, timeout=10, poll=0.5) -> WebElement:
        wait = WebDriverWait(self.browser, timeout, poll)
        return wait.until(EC.visibility_of_element_located(locator))

    def screen_shot(self):
        current_time_str = str(datetime.fromtimestamp(int(time.time())))
        filename = current_time_str+".png"
        return self.browser.save_screenshot(os.path.join(IMG_PATH, filename))

