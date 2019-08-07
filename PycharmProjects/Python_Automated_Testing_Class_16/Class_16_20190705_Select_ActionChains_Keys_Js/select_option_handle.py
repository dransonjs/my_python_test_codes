from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Python_Automated_Testing_Class_16.Class_16_20190705_Select_ActionChains_Keys_Js.wait_package import wait_click_element

browser = Chrome()
browser.get("https://www.baidu.com/")

# 定位“设置”并点击
locator = (By.XPATH, "//a[@href='http://www.baidu.com/gaoji/preferences.html']")
wait_click_element(browser, locator).click()

# 定位“高级搜索”并点击
locator2 = (By.XPATH, "//a[@href='//www.baidu.com/gaoji/advanced.html']")
wait_click_element(browser, locator2).click()

# 定位“所有网页和文件” select下拉框

# 定位select-option

# 第一种，直接通过option定位
# 定位“微软 Word” option选项并点击
# locator4 = (By.XPATH, "//option[@value='doc']")
# wait_click_element(browser, locator4).click()

# 第二种，通过Select类定位
# select_e元素不需要点击事件
locator3 = (By.NAME, "ft")
select_e = wait_click_element(browser, locator3)
select_obj = Select(select_e)
# 有3种方式选择option
# 1 元素的value属性
# select_obj.select_by_value("ppt")
# 2 索引
# select_obj.select_by_index(4)
# 3 option文本
select_obj.select_by_visible_text("微软 Powerpoint (.ppt)")

