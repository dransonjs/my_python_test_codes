# 1、写出腾讯课堂登陆(qq帐号密码方式)操作

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from Class_16_Homework.homework_0708.wait_package import \
    wait_click_element, \
    wait_presence_element, \
    wait_iframe_switch

browser = Chrome()
browser.implicitly_wait(10)
browser.get("https://ke.qq.com/")

# 定位主页右上角登录按钮
login_e = wait_click_element(browser, (By.ID, "js_login"))
login_e.click()

# 定位qq登录按钮
login_e2 = wait_click_element(browser, (By.XPATH, "//a[@data-type='1']"))
login_e2.click()

# 切换到qq登录的iframe界面
# iframe_wait = WebDriverWait(browser, 10)
# iframe_wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@name='login_frame_qq']")))
wait_iframe_switch(browser, (By.XPATH, "//iframe[@name='login_frame_qq']"))

# 定位账号密码登录按钮
iframe_login_e = wait_click_element(browser, (By.XPATH, "//a[@id='switcher_plogin']"))
iframe_login_e.click()

# 输入qq账号密码
account_e = wait_presence_element(browser, (By.XPATH, "//input[@id='u']"))
account_e.send_keys("918319140")
password_e = wait_presence_element(browser, (By.XPATH, "//input[@id='p']"))
password_e.send_keys("321321abc")

# 点击登录
login_e3 = wait_click_element(browser, (By.XPATH, "//input[@class='btn']"))
login_e3.click()

time.sleep(3)
browser.quit()



