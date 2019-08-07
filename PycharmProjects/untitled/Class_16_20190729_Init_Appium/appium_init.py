import time
from appium import webdriver

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

