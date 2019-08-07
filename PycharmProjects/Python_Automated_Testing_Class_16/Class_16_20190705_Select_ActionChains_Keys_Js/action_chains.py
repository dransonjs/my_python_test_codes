from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Python_Automated_Testing_Class_16.Class_16_20190705_Select_ActionChains_Keys_Js.wait_package import wait_click_element


browser = Chrome()
browser.get("https://www.baidu.com")

action_chains = ActionChains(browser)

# 定位设置
setting_e = wait_click_element(browser, (By.XPATH, "//a[@href='http://www.baidu.com/gaoji/preferences.html']"))

# 每个鼠标事件方法返回的是对象本身
# 所以action_chains对象后面可以不断叠加方法，如action_chains.move_to_element(setting_e).click().double_click().perform()
# 执行鼠标事件之后必须调用perform方法
# perform方法是收集鼠标事件后，通过for循环遍历释放，调用对应的鼠标事件方法
action_chains.move_to_element(setting_e).perform()

# 定位高级搜索
senior_search_e = wait_click_element(browser, (By.XPATH, "//a[@href='//www.baidu.com/gaoji/advanced.html']"))

action_chains.click(senior_search_e).perform()
