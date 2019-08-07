from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
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

    def login(self, username, password):
        self.browser.get("http://120.78.128.25:8765/Index/login.html")
        account_e = self.wait_presence_element((By.XPATH, "//input[@name='phone']"))
        account_e.send_keys(username)
        pwd_e = self.wait_presence_element((By.XPATH, "//input[@name='password']"))
        pwd_e.send_keys(password)
        login_e = self.wait_click_element((By.XPATH, "//button[text()='登录']"))
        login_e.click()

    def get_element_unauthorized(self):
        return self.wait_presence_element((By.XPATH, "//div[@class='layui-layer-content']"))

    def get_element_miss_phone(self):
        return self.wait_presence_element((By.XPATH, "//div[@class='form-error-info']"))
