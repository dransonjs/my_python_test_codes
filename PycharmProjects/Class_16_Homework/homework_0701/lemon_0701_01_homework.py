from selenium.webdriver import Chrome
import time

browser = Chrome()
# 打开课堂派首页
browser.get("http://www.ketangpai.com")

# 定位首页登录按钮，并点击
browser.find_element_by_xpath("//a[@class='login']").click()

# 定位登录页账号输入框，并输入账号
browser.find_element_by_xpath("//input[@name='account']").send_keys("13713645854")

# 定位登录页密码输入框，并输入密码
browser.find_element_by_xpath("//input[@name='pass']").send_keys("112233")

# 定位登录页登录按钮，并点击
browser.find_element_by_xpath("//a//parent::div[@class='padding-cont pt-login']/a").click()

time.sleep(2)
# 定位登录后首页的“Python全栈第16期”，并点击
browser.find_element_by_xpath("//a[@class='jumptoclass']").click()

time.sleep(4)
# 定位“Python全栈第16期”页里“元素定位练习”的作业，并点击
browser.find_element_by_xpath("//a//parent::h3[@class='work-title ']/a[contains(text(),'元素定位练习')]").click()

# 定位“元素定位练习”作业里的“作业讨论”，并点击
# browser.find_element_by_xpath("//a[@href='/Discuss/index/homeworkid/MDAwMDAwMDAwMLSGy5mH379s.html']").click()
browser.find_element_by_partial_link_text('作业讨论').click()

time.sleep(2)
# 定位”作业讨论“里的”添加评论“，并点击
browser.find_element_by_xpath("//div[@class='input-click clearfix']").click()

# 定位“添加评论”输入位置，并输入评论文字
browser.find_element_by_xpath("//textarea[@class='comment-txt']").send_keys("WebDriver自动化测试输入：Xpath真好玩")

# 定位评论下方的确定按钮并点击
browser.find_element_by_xpath("//a[text()='确定']").click()

time.sleep(3)
# 关闭浏览器
browser.quit()
