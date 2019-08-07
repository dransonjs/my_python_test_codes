from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = Chrome()

browser.implicitly_wait(10)

url = "http://localhost:63342/Python_training/Python_Automated_Testing_Class_16/Class_16_20190628_Selenium_WebDriver/iframe.html?_ijt=5mbies1etajdr76lkfuers9jc8"
browser.get(url)

wait = WebDriverWait(browser, 20)
# 第一种切换，通过name切换
# browser.switch_to.frame('iframe2')

# 第二种切换，通过索引切换
# browser.switch_to.frame(1)

# 第三种切换，通过EC里的方法切换
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@name='iframe2']")))

e = browser.find_element_by_id("kw")
print(e.get_attribute("id"))

# 切换到一开始打开浏览器的默认html
browser.switch_to.default_content()
e2 = browser.find_element_by_name("iframe1")
print(e2.get_attribute("name"))
