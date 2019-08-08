from appium import webdriver
import time

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

# 模拟实体按键
# 可用字典封装按键代码
keycodes = {"volumn_up": 24, "volumn_down": 25}


# 也可用类封装，类似selenium里的Keys
class KeyCode:
    VOLUMN_UP = 24
    VOLUMN_DOWN = 25


driver.press_keycode(keycodes["volumn_up"])
driver.press_keycode(KeyCode().VOLUMN_UP)
driver.press_keycode(24)
driver.press_keycode(keycodes["volumn_down"])
driver.press_keycode(KeyCode().VOLUMN_DOWN)
driver.press_keycode(25)


time.sleep(2)
driver.quit()
