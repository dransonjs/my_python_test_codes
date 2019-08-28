import os
import time
import logging

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

from file_path import IMG_PATH


class BasePage:

    me_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(\"我\")')

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

    def wait_visibility_element(self, locator, timeout=10, poll=0.5) -> WebElement:
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(EC.visibility_of_element_located(locator))

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

    def set_gesture_code(self, gesture_e: WebElement, set_points):
        rect = gesture_e.rect
        width = rect.get("width")
        height = rect.get("height")
        start_x = rect.get("x")
        start_y = rect.get("y")

        points = [{"x": start_x + width / 6, "y": start_y + height / 6},
                  {"x": start_x + width / 2, "y": start_y + height / 6},
                  {"x": start_x + width / 6 * 5, "y": start_y + height / 6},
                  {"x": start_x + width / 6, "y": start_y + height / 2},
                  {"x": start_x + width / 2, "y": start_y + height / 2},
                  {"x": start_x + width / 6 * 5, "y": start_y + height / 2},
                  {"x": start_x + width / 6, "y": start_y + height / 6 * 5},
                  {"x": start_x + width / 2, "y": start_y + height / 6 * 5},
                  {"x": start_x + width / 6 * 5, "y": start_y + height / 6 * 5}]

        touch_action = TouchAction(self.driver)
        touch_action.press(**points[set_points[0] - 1]).wait(500)
        for point in set_points[1:]:
            touch_action.move_to(**points[point-1]).wait(500)
        touch_action.release().perform()

    def me(self):
        self.wait_visibility_element(self.me_locator).click()
