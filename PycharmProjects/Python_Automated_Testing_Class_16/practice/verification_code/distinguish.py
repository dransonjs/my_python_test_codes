from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from chaojiying_Python.chaojiying import ChaojiyingClient


# 创建浏览器，访问登录页
browser = Chrome()
browser.implicitly_wait(10)
browser.get("https://www.chaojiying.com/user/login/")

# 获取输入框，输入账号密码
wait = WebDriverWait(browser, 10)
username = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='user']")))
password = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='pass']")))

username.send_keys("dranson")
password.send_keys("348862312")

# 截取当前网页图像
browser.save_screenshot("page.png")

# 定位验证码图片
verify_code_pic = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@name='fm2']/div/img")))

# 获取验证码图片上下左右的坐标
code_pic_loc = verify_code_pic.location
code_pic_size = verify_code_pic.size
# 注意！！如果电脑桌面右键的显示设置的缩放不是100%（如125%），则下面的坐标都要对应乘以1.25
left = code_pic_loc["x"]
up = code_pic_loc["y"]
right = left + code_pic_size["width"]
down = up + code_pic_size["height"]

# 从网页图像中截取验证码图片
page_pic = Image.open("page.png")
code_pic_coordinate = (left, up, right, down)  # 顺序固定为左上右下，不能变！！
code_pic = page_pic.crop(code_pic_coordinate)
code_pic.save("yzm.png")

# 识别并获取验证码
chaojiying = ChaojiyingClient('dranson', '348862312', '	901409')  # 用户中心>>软件ID 生成一个替换 96001
# im = open('yzm.png', 'rb').read()	 # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
with open("yzm.png", "rb") as f:
    im = f.read()
code_data = chaojiying.post_pic(im, 1902)["pic_str"]  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加())

# 获取验证码输入框，输入验证码
code_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='imgtxt']")))
code_input.send_keys(code_data)

# 点击登录
login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='登录']")))
login_button.click()
