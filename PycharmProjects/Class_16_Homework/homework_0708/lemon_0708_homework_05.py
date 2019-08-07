# 5、通过 js 往 readOnly 元素发送数据

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from Class_16_Homework.homework_0708.wait_package import wait_presence_element

browser = Chrome()
browser.implicitly_wait(10)
browser.get("file:///C:/Users/admin/PycharmProjects/untitled/Class_16_Homework/homework_0708/lemon_0708_homework_03.html")

text_e = wait_presence_element(browser, (By.NAME, "text"))

js_code = "arguments[0].readOnly = false"
browser.execute_script(js_code, text_e)

time.sleep(1)
text_e.send_keys("输入信息")

time.sleep(3)
browser.quit()

