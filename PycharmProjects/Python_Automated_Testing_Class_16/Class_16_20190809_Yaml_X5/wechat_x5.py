# 测试微信小程序环境配置
# 手机root
# 安装调试模式：在微信聊天窗口输入并打开
# http://debugmm.qq.com/?forcex5=true
# http://debugx5.qq.com
import os
import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {
    # 支持X5内核应用自动化配置
    "recreateChromeDriverSessions": True,

    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "8.1",

    # 测微信小程序需要用真机，不能用模拟器
    "deviceName": "Android Emulator",

    "appPackage": "com.tencent.mm",
    "appActivity": "com.tencent.mm.ui.LauncherUI",

    # 指定X5内核依赖的chromedriver版本目录
    "chromedriverExecutableDir": "D:\\chromdriver",

    "noReset": True,

    # 查找进程的命令：adb shell dumpsys activity top | findstr ACTIVITY
    "chromeOptions": {"androidProcess": "com.tencent.mm:appbrand0"},
    "browserName": ""
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(20)

# 只能从以下步骤进入微信小程序
driver.find_element_by_xpath("//*[@text='发现']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@text='搜一搜']").click()
time.sleep(1)
search_locator = (MobileBy.XPATH, "//*[@text='搜索']")
search_e = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(search_locator))
search_e.click()
time.sleep(1)

search_e.send_keys("柠檬班软件测试")

# 计算键盘上“搜索”的坐标位置比例后，采用adb命令点击

# 计算搜索记录的“软件测试”的坐标，采用adb命令点击
os.system("adb shell input tap 330 194")
time.sleep(1)

# 计算小程序的坐标，采用adb命令点击
os.system("adb shell input tap 350 836")
time.sleep(1)

# 切换到小程序webview
print(driver.contexts)
driver.switch_to.context("WEBVIEW_com.tencent.mm:appbrand0")

# 小程序打开时有可能打开很多窗口，遍历所有的窗口，一旦找到对应元素，则停止循环
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    time.sleep(2)
    if driver.page_source.find("柠檬班") != -1:
        break
