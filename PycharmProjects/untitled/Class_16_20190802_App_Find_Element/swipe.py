import time
from appium import webdriver

desired_caps = {
    "automationName": "UiAutomator1",
    "platformName": "Android",
    "platformVersion": "5.1",
    "deviceName": "Android Emulator",
    "appPackage": "com.xxzb.fenwoo",
    "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",
    "noReset": False
}

# 注意端口号是否正确
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(5)  # app在启动的时候没有像web那么智能，不会等启动完才去定位元素，所以要加强制等待

# 获取手机的长宽
# size = driver.get_window_size()
# width = size['width']
# height = size['height']
# for _ in range(3):
    # 按屏幕大小比例滑屏，从右往左滑
    # driver.swipe(width*0.9, height*0.5, width*0.1, height*0.5)
    # time.sleep(2)


# 滑屏操作封装成函数
def swipe_left():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    driver.swipe(width*0.9, height*0.5, width*0.1, height*0.5)


for _ in range(3):
    swipe_left()
    time.sleep(2)

driver.quit()


