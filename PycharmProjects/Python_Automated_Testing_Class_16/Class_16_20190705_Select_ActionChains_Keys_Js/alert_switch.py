from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from Python_Automated_Testing_Class_16.Class_16_20190705_Select_ActionChains_Keys_Js.wait_package import wait_click_element, wait_alert

browser = Chrome()
url = "http://localhost:63342/Python_training/Python_Automated_Testing_Class_16/Class_16_20190705_/alert.html?_ijt=4k1lra4t74usf2u56ek4h28ivt"
browser.get(url)

# 显式等待元素加载完后并点击
wait_click_element(browser, (By.ID, "alert")).click()

# 显式等待弹窗后并切换到弹窗
e = wait_alert(browser)
print(e.text)

# 点击弹窗的确定
e.accept()

