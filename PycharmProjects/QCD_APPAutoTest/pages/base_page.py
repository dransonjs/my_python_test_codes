import os
import time
import logging

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: Remote):
        self.driver = driver

    def wait_click_element(self, locator, timeout=10, poll=0.5) -> WebElement:
        try:
            wait = WebDriverWait(self.driver, timeout, poll)
            return wait.until(EC.element_to_be_clickable(locator))
        except (TimeoutException, NoSuchElementException):
            logging.error("元素没有定位到")
            self.screen_shot()

    def wait_presence_element(self, locator, timeout=10, poll=0.5) -> WebElement:
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(EC.presence_of_element_located(locator))

    def screen_shot(self):
        current_time_str = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        return self.driver.save_screenshot(os.path.join(IMG_PATH, current_time_str))

    def click(self, locator):
        return self.wait_click_element(locator).click()

    def switch_window(self, timeout=20, name=None):
        WebDriverWait(self.driver, timeout).until(EC.new_window_is_opened)
        if not name:
            return self.driver.switch_to.window(self.driver.window_handles[1])
        return self.driver.switch_to.window(name)

    def switch_frame(self, locator=None, timeout=20):
        if not locator:
            return self.driver.switch_to.default_content()
        return WebDriverWait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(locator))

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def swipe_left(self, duration=1000):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        self.driver.swipe(width*0.9, height*0.5, width*0.1, height*0.5, duration)

    def switch_context(self, context_name=None):
        if not context_name:
            return self.driver.switch_to.context("NATIVE_APP")
        contexts = self.driver.contexts
        for ctx in contexts:
            if ctx == context_name:
                return self.driver.switch_to.context(context_name)

    def send_keycode(self, key):
        return self.driver.press_keycode(key)

    def get_toast(self, tip):
        self.wait_presence_element((MobileBy.XPATH, f"//*[contains(@text, {tip})]"))