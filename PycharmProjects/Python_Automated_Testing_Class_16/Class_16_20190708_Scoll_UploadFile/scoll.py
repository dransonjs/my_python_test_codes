import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from Class_16_20190705_Select_ActionChains_Keys_Js.wait_package import wait_click_element

browser = Chrome()
browser.get("http://readhub.cn")

# e = wait_click_element(browser, (By.XPATH, "//*[text()='联系我们']"))

# 通过窗口滚动条把元素滚动到可视范围
# e.location_once_scrolled_into_view

# e.click()

# 用js代码实现滚动条横向移动和纵向移动的宽度和高度
js_code = "window.scrollTo(0, 10000)"
# 执行js代码
browser.execute_script(js_code)
time.sleep(2)

# scrollHeight属性表示滚动到最下面
js_code2 = "window.scrollTo(0, document.body.scrollHeight)"
browser.execute_script(js_code2)




