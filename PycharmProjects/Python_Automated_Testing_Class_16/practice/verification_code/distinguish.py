from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image


browser = Chrome()
browser.implicitly_wait(10)
browser.get("https://www.chaojiying.com/user/login/")

wait = WebDriverWait(browser, 10)
username = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='user']")))
password = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='pass']")))

username.send_keys("dranson")
password.send_keys("348862312")

verify_code_pic = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@name='fm2']/div/img")))
code_pic_loc = verify_code_pic.location
code_pic_size = verify_code_pic.size
left = code_pic_loc["x"]
up = code_pic_loc["y"]
right = left + code_pic_size["width"]
down = up + code_pic_size["height"]
