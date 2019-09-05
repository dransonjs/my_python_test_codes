from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = Chrome()
browser.implicitly_wait(10)
browser.get("https://www.chaojiying.com/user/login/")

wait = WebDriverWait(browser, 10)
username_e = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='user']")))
password_e = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='pass']")))

