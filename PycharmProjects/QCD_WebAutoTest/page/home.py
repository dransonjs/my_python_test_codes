from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    """登录页面行为类"""

    def __init__(self, browser):
        self.browser = browser

    def wait_presence_element(self, locator) -> WebElement:
        """
        等待元素加载
        :param locator: 定位方式和表达式
        :return:
        """
        wait = WebDriverWait(self.browser, 10)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_click_element(self, locator) -> WebElement:
        """
        等待可点击元素加载
        :param locator: 定位方式和表达式
        :return:
        """
        wait = WebDriverWait(self.browser, 10)
        return wait.until(EC.element_to_be_clickable(locator))

    def get_element_user(self):
        return self.wait_presence_element((By.XPATH, "//a[text()='我的帐户[python10]']"))

