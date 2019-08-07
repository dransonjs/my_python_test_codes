# 导入配置文件模块
from configparser import ConfigParser

# 创建配置解析器对象
config = ConfigParser()

# 指定读取的配置文件名
config.read('testcase.ini', encoding='utf8')

# 读取数据
print(config.sections())  # 返回区域名（字符串）组成的一个列表

# 方法一
print(config['file path'])
print(config['file path']['cases_path'])

# 方法二
print(config.get('file path', 'log_path'))  # 第一个参数是区域名，第二个参数是选项名

# 方法三
# config相当于一个嵌套字典的字典
# section是个对象，相当于config的key
# option相当于config的value，是内层字典
for section, option in config.items():
    print(section, dict(option))

for section, option in config.items():
    for option_key, option_value in option.items():
        print(option_key, option_value)