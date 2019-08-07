from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_presence_element(driver, locator) -> WebElement:
    """
    等待元素加载
    :param driver: 浏览器
    :param locator: 定位方式和表达式
    :return:
    """
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.presence_of_element_located(locator))


def wait_click_element(driver, locator) -> WebElement:
    """
    等待可点击元素加载
    :param driver: 浏览器
    :param locator: 定位方式和表达式
    :return:
    """
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.element_to_be_clickable(locator))


def wait_alert(driver):
    """
    等待弹窗并切换到弹窗
    :param driver: 浏览器
    :return:
    """
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.alert_is_present())


def wait_iframe_switch(driver, locator) -> WebElement:
    """
    等待iframe切换
    :param driver: 浏览器
    :param locator: 定位方式和表达式
    :return:
    """
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.frame_to_be_available_and_switch_to_it(locator))


