import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from Class_16_20190705_Select_ActionChains_Keys_Js.wait_package import wait_presence_element
from Class_16_20190708_Scoll_UploadFile.windows_upload import windows_upload

browser = Chrome()
browser.implicitly_wait(10)
browser.get("file:///C:/Users/admin/PycharmProjects/untitled/Class_16_20190708_Scoll_UploadFile/upload_file.html")
e = wait_presence_element(browser, (By.XPATH, "//input[@name='upload_file']"))
# 上传文件
# 第一种方法，send_keys
# e.send_keys(r"C:\Users\admin\Desktop\1.jpg")
# time.sleep(2)
# browser.quit()

# 第二种方法，与windows交互
e.click()
time.sleep(2)
windows_upload(r"C:\Users\admin\Desktop\1.jpg")
time.sleep(2)
browser.quit()

