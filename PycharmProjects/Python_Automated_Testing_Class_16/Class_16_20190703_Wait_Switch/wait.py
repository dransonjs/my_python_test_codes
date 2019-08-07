from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait  # 导入定时器
from selenium.webdriver.support import expected_conditions as EC  # 导入触发条件
from selenium.webdriver.common.by import By

browser = Chrome()

# 智能等待（隐式、显式）

# 设置隐式等待，每个元素都有10秒可以被发现，若10秒内发现则正常，10秒还未发现则报错
# 优点：只需要设置一次
# 缺点：局限性高，只能用来等元素出现或者某个指令是否完成，并不能等待所有情况，定位错误需要等满时间才报错
browser.implicitly_wait(10)

browser.get('http://www.baidu.com')

browser.find_element_by_xpath("//input[@id='kw']").click()
browser.find_element_by_xpath("//input[@id='kw']").send_keys("柠檬班")

browser.find_element_by_xpath("//input[@id='su']").click()

# 设置显式等待，找不到元素就等待一段时间后继续找，直到找到为止
# 定时器
wait = WebDriverWait(browser, 20)  # 参数：浏览器，过期时间，轮巡时间默认0.5秒
# 条件，visibility_of_element_located的参数是元组(定位方式，定位表达式)
e = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'lemon.ke.qq.com')]")))
print(e)


