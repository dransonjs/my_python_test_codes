# 导入配置文件模块
from configparser import ConfigParser

# 创建配置解析器对象
config = ConfigParser()

# 指定读取的配置文件名
config.read('testcase.ini', encoding='utf8')

# 读取数据
# print(config.sections())  # 返回区域名（字符串）组成的一个列表

# 方法一
# print(config['file path'])
# print(config['file path']['cases_path'])

# 方法二
# print(config.get('file path', 'log_path'))  # 第一个参数是区域名，第二个参数是选项名

# 方法三
# config相当于一个嵌套字典的字典
# section是个对象，相当于config的key
# option相当于config的value，是内层字典
# for section, option in config.items():
#     print(section, dict(option))
#
# for section, option in config.items():
#     for option_key, option_value in option.items():
#         print(option_key, option_value)

# 从配置文件获取到的所有值都是字符串
# msg = config['excel']
# for value in msg.values():
#     print('值为：{}\n类型为：{}'.format(value, type(value)))
# 数字型字符串可以用int/float转换
# 也可以用配置文件中自带的getint, getfloat, getboolean方法
print(config.getint('excel', 'actual_col'))
print(config.getfloat('excel', 'four_res'))
# 读取1、yes、on、true，使用getboolean方法都会被识别为True
print(config.getboolean('excel', 'two_res'))
# 读取0、no、off、false，使用getboolean方法都会被识别为False
print(config.getboolean('excel', 'one_res'))
# 其他类型只能用eval函数
print(eval(config.get('excel', 'five_res')))

# 配置文件中有一个默认区域DEFAULT,保存的是所有区域的公共数据
# 如果不定义DEFAULT,就是个空字典
