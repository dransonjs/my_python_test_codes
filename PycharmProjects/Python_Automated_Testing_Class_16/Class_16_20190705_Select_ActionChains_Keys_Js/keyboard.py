from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Python_Automated_Testing_Class_16.Class_16_20190705_Select_ActionChains_Keys_Js.wait_package import wait_click_element


browser = Chrome()
browser.get("https://www.baidu.com")

e = wait_click_element(browser, (By.ID, "kw"))
e.send_keys("柠檬班")
e.send_keys(Keys.CONTROL, "a")
