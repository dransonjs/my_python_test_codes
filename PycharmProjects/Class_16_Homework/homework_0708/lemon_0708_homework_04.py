# 3、写一个 HTML 页面，包含文件上传元素和一个有 readOnly 属性的输入框；
# 4、通过 2 种方式上传文件。

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from Class_16_Homework.homework_0708.wait_package import wait_click_element
from Class_16_Homework.homework_0708.windows_upload import windows_upload

browser = Chrome()
browser.implicitly_wait(10)
browser.get("file:///C:/Users/admin/PycharmProjects/untitled/Class_16_Homework/homework_0708/lemon_0708_homework_03.html")

upload_e = wait_click_element(browser, (By.NAME, "upload_file"))

# 第一种上传方法
# upload_e.send_keys(r"C:\Users\admin\Desktop\1.jpg")
# time.sleep(3)
# browser.quit()

# 第二种上传方法
upload_e.click()
time.sleep(2)

windows_upload(r"C:\Users\admin\Desktop\1.jpg")

time.sleep(2)
browser.quit()



