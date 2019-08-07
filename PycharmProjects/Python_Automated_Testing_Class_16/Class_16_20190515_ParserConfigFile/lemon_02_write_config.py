# 导入配置文件模块
from configparser import ConfigParser

# 创建配置解析器对象
config = ConfigParser()

# 将需要写入配置文件中的数据组合为
datas = {
    'file path': {
        'cases_path': 'cases.xlsx',
        'log_path': 'test_result.txt'
    },
    'msg': {
        'success_result': 'Pass',
        'fail_result': 'Fail'
    },
    'excel': {
        'actual_col': '6',
        'result_col': '7'
    }
}

for key in datas:
    config[key] = datas[key]

# 保存到文件
with open('write_config.conf', 'w') as file:
    config.write(file)
