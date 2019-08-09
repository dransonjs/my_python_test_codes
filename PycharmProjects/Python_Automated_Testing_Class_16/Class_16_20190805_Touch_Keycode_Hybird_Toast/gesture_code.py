from appium.webdriver import WebElement
from appium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
    "automationName": "UiAutomator1",  # 自动化测试框架
    "platformName": "Android",  # 系统
    "platformVersion": "5.1",  # 系统版本
    "deviceName": "Android Emulator",  # 模拟器，真机为序列号
    "appPackage": "com.xxzb.fenwoo",  # 包名，可通过aapt查到
    # 活动页面，可通过aapt查到，，也可通过adb命令查到：adb shell dumpsys activity | find "mFocusedActivity"
    "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",
    "noReset": True  # app刚打开时的滑屏或广告等，True为直接跳过进入首页，False则相反
}

# 注意端口号是否正确
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(2)


def wait_presence_element(driver, locator) -> WebElement:
    return WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator))


# 跳转到九宫格绘制界面，有两种方法
# 1、登录原来的路径
# 2、start_activity()
driver.start_activity("com.xxzb.fenwoo", ".activity.user.CreateGesturePwdActivity")
right_e = wait_presence_element(driver, (MobileBy.ID, "com.xxzb.fenwoo:id/right_btn"))
right_e.click()

# 如果九宫格为九个元素，可以用TouchAction里的move_to绘制
# 如果九宫格为一个元素，只能通过获取坐标绘制
gesture_e = wait_presence_element(driver, (MobileBy.ID, "com.xxzb.fenwoo:id/gesturepwd_create_lockview"))

# 获取元素起始坐标和大小
rect = gesture_e.rect
width = rect.get("width")
height = rect.get("height")
start_x = rect.get("x")
start_y = rect.get("y")

# 需要连接九宫格的点
point1 = {"x": start_x + width/6, "y": start_y + height/6}
point2 = {"x": start_x + width/2, "y": start_y + height/2}
point3 = {"x": start_x + width/6*5, "y": start_y + height/6*5}
point4 = {"x": start_x + width/6*5, "y": start_y + height/2}

# 移动连接点
touch_action = TouchAction(driver)
touch_action.press(**point1).wait(
    500).move_to(**point2).wait(
    500).move_to(**point3).wait(
    500).move_to(**point4).wait(
    500).release().perform()

time.sleep(2)
driver.quit()

