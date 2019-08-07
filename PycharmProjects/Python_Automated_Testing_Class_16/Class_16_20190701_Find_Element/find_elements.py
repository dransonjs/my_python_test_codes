from selenium.webdriver import Chrome

driver = Chrome()

driver.get("http://baidu.com")

# 定位元素优先使用id，除非是动态id，其他属性（name、class等）都可能动态变化
# 动态属性的判断方式（1、带数字，如kw123；2、不规则字符串）
driver.find_element_by_id("kw")

# 经常使用name定位，返回找到第一个符合要求的元素 WebElement对象
driver.find_element_by_name('wd')

# 返回找到所有符合要求的元素的列表
driver.find_elements_by_name('wd')

# 如果class里含有空格，要把空格去掉，因为python selenium识别不了空格
# driver.find_element_by_class_name("bg s_btn")
botton_e = driver.find_element_by_class_name("s_btn")
# 获取该元素的值
print(botton_e.get_attribute('value'))

code_e = driver.find_element_by_id("setf")
# 动态属性，装饰器@property在text方法上，调用时不需要加括号
print(code_e.text)

# 定位超链接
driver.find_element_by_link_text('新闻')
# 通过部分文字定位超链接
driver.find_element_by_partial_link_text('新')

# Xpath定位元素
# //开头代表相对路径  /开头代表绝对路径

# //form/input  input是儿子
# //form//input  input可以是儿子，还可以是孙子
# //form/.  form的本级目录
# //form/..  form的上级目录

# 谓语条件
# 标签属性需加中括号和@符号
# //span/input[@name='wd']
# //span/input[@class='s_ipt']
# //span/input[@id=‘kw’]

# 可以通过标签里的属性进行组合条件查找元素
# //input[@id=‘kw’ and @name='wd' and @class='s_ipt']

# 通过标签的文本查找，文本查找需带()
# //a[text()='新闻']  需要注意与//a[text()=' 新闻 ']不一样
# //a[contains(text(), '新闻')]  通过文本查找尽量带contains函数，查找到的元素会包含//a[text()=' 新闻 ']

# contains带属性时不需要()
# //a[contains(@class, 'mnav')]

# 轴定位
# //input//parent::form[@id='form']  parent表示轴关系，input标签的父亲是form标签

# *通配符
# //*[@name='kw']  把所有name属性为kw的元素全部查找出来
# //*[@*='kw']  把所有属性为kw的元素全部查找出来
