from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait  # 导入定时器
from selenium.webdriver.support import expected_conditions as EC  # 导入触发条件
from selenium.webdriver.common.by import By

browser = Chrome()

browser.implicitly_wait(5)

browser.get('http://www.baidu.com')

browser.find_element_by_xpath("//input[@id='kw']").send_keys("柠檬班")

# browser.find_element_by_xpath("//input[@id='su']").click()
# 上面注释的语句可以用下面submit代替，只要当前定位的元素的父节点在form里就可以用submit
browser.find_element_by_xpath("//input[@id='kw']").submit()

# 设置显式等待，找不到元素就等待一段时间后继续找，直到找到为止
# 定时器
wait = WebDriverWait(browser, 10)  # 参数：浏览器，过期时间，轮巡时间默认0.5秒
# 条件，visibility_of_element_located的参数是元组(定位方式，定位表达式)
e = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'lemon.ke.qq.com')]")))

# 获取浏览器当前所有窗口的句柄
handles = browser.window_handles

e.click()

# 切换窗口，也需要等待
# wait = WebDriverWait(browser, 10)
wait.until(EC.new_window_is_opened(handles))
# 切换到最新打开的窗口
browser.switch_to.window(browser.window_handles[-1])

# 找到华华老师
huahua = browser.find_element_by_xpath("//h4[text()='华华老师']")


