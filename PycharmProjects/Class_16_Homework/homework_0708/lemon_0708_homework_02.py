# 2、打印课堂派微信二维码登录中的二维码元素

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from Class_16_Homework.homework_0708.wait_package import \
    wait_click_element, \
    wait_presence_element, \
    wait_iframe_switch

browser = Chrome()
browser.implicitly_wait(10)
browser.get("https://www.ketangpai.com/User/login.html")

wx_login_e = wait_click_element(browser, (By.XPATH, "//a[text()='微信登录']"))
wx_login_e.click()

# iframe_wait = WebDriverWait(browser, 10)
# iframe_wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))
wait_iframe_switch(browser, (By.TAG_NAME, "iframe"))

QR_code_e = wait_presence_element(browser, (By.XPATH, "//img[@class='qrcode lightBorder']"))
print(QR_code_e)

time.sleep(3)
browser.quit()


