from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from Python_Automated_Testing_Class_16.Class_16_20190705_Select_ActionChains_Keys_Js.wait_package import wait_click_element


browser = Chrome()
browser.implicitly_wait(15)
browser.get("https://www.12306.cn/index")

date_e = wait_click_element(browser, (By.ID, "train_date"))

# python里执行js代码，arguments[0]是占位符，用下面execute方法的data_e传参
# 如果有多个占位符如arguments[1]，则在execute方法的参数js_code后面继续叠加
# js_code里如果有多行代码，则用分号;分隔
js_code = "arguments[0].readOnly = false"
browser.execute_script(js_code, date_e)

# 在js代码和python代码执行之间建议适当加下强制等待
time.sleep(2)
date_e.clear()
date_e.send_keys("2019-07-15")

