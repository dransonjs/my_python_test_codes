import time
from appium import webdriver

desired_caps = {
    "automationName": "UiAutomator1",
    "platformName": "Android",
    "platformVersion": "5.1",
    "deviceName": "Android Emulator",
    "appPackage": "com.xxzb.fenwoo",
    "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",
    "noReset": True
}

# 注意端口号是否正确
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(5)
# 通过resource-id定位
borrow_money = driver.find_element_by_id("com.xxzb.fenwoo:id/layout_borrow_money")
print(borrow_money)

time.sleep(5)
# 通过xpath定位
me = driver.find_element_by_xpath("//android.widget.TabWidget[@resource-id=\"android:id/tabs\"]/android.widget.LinearLayout[4]")
me.click()

time.sleep(5)
input_tel = driver.find_element_by_id("com.xxzb.fenwoo:id/et_phone")
input_tel.send_keys("13788889999")

# 通过content-desc定位
# driver.find_element_by_accessibility_id()

# 通过UiSelector定位，由于UiSelector是基于安卓java开发，所以定位语言要写java
# java里的字符串必须用双引号
# UiSelector定位表达式是相当于Web里的ActionChains的链式调用
driver.find_element_by_android_uiautomator('new UiSelector().className(\"android.widget.ScrollView\").resourceId(\"com.xxzb.fenwoo:id/tv_rate\")')
driver.find_element_by_android_uiautomator('new UiSelector().text(\"我\")')



