from selenium.webdriver import Chrome
import time

browser = Chrome()

# 访问网站
browser.get('http://baidu.com')
# browser.get('http://qq.com')
# 获取当前url
print(browser.current_url)

# 截图保存
# browser.save_screenshot("demo.png")

# 后退
# browser.back()

# 前进
# browser.forward()

# 刷新
# browser.refresh()

# time.sleep(1)
# 设置窗口大小
# browser.set_window_size(800, 500)

# time.sleep(1)
# 最小化
# browser.minimize_window()

# 最大化
# browser.maximize_window()

# time.sleep(1)
# 关闭标签页
# browser.close()

# time.sleep(1)
# 退出浏览器
# browser.quit()

# 获取窗口大小
print(browser.get_window_size())

# 获取窗口大小及起始坐标
print(browser.get_window_rect())

# 获取句柄（窗口id）每次打开浏览器的句柄不一样
print(browser.current_window_handle)

# 获取所有句柄（所有窗口id）
print(browser.window_handles)
