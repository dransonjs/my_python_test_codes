from appium import webdriver
import time
from appium.webdriver import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {
    "automationName": "UiAutomator2",  # 自动化测试框架，定位toast必须用UiAutomator2
    "platformName": "Android",  # 系统
    "platformVersion": "5.1",  # 系统版本
    "deviceName": "Android Emulator",  # 模拟器，真机为序列号
    "appPackage": "com.lemon.lemonban",  # 包名，可通过aapt查到
    # 活动页面，可通过aapt查到，，也可通过adb命令查到：adb shell dumpsys activity | find "mFocusedActivity"
    "appActivity": ".activity.LoginActActivity",
    "noReset": True  # app刚打开时的滑屏或广告等，True为直接跳过进入首页，False则相反
}

# 注意端口号是否正确
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(2)


def wait_presence_element(driver, locator) -> WebElement:
    return WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator))


login_btn_e = wait_presence_element(driver, (MobileBy.ID, "com.lemon.lemonban:id/btn_login"))
login_btn_e.click()

# 定位toast，用xpath文本匹配的方式较为方便
# 前提：1、自动化测试框架必须改为UiAutomator2而不是1
# 2、安卓版本5.0以上
# 3、appium客户端版本1.6.3以上
# 4、jdk版本1.8.64以上
toast_e = wait_presence_element(driver, (MobileBy.XPATH, "//*[contains(@text, '手机号码或密码不能为空')]"))
print(toast_e)

driver.quit()
