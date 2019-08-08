from appium import webdriver
import time

desired_caps = {
    "automationName": "UiAutomator1",  # 自动化测试框架
    "platformName": "Android",  # 系统
    "platformVersion": "5.1",  # 系统版本
    "deviceName": "Android Emulator",  # 模拟器，真机为序列号
    "appPackage": "com.android.browser",  # 包名，可通过aapt查到
    # 活动页面，可通过aapt查到，，也可通过adb命令查到：adb shell dumpsys activity | find "mFocusedActivity"
    "appActivity": ".BrowserActivity",
    "noReset": True  # app刚打开时的滑屏或广告等，True为直接跳过进入首页，False则相反
}

# 注意端口号是否正确
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(2)

url_e = driver.find_element_by_id("com.android.browser:id/url")
url_e.send_keys("https://www.baidu.com")
driver.press_keycode(66)  # 按回车键
time.sleep(2)

print(driver.contexts)  # 所有上下文，相当于web的window_handles

# 这里的context输入时没有提示，切换到WEBVIEW
driver.switch_to.context("WEBVIEW_com.android.browser")  # 混合应用（原生app里有web）的web几乎都是以WEBVIEW开头

# 切换回原生应用
# driver.switch_to.context(None) 或 driver.switch_to.context("NATIVE_APP")

driver.quit()
