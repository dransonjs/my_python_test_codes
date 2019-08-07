import json

# json格式数据以字符串形式呈现

# 单个json数据
json_data = '{"status": 1, "code": "10001", "data": null, "msg": "注册成功"}'

# 将json格式数据转换为字典
dict_data = json.loads(json_data)

# 数组json数据（多个json数据在数组中）
json_data2 = '[{"status": 1, "code": "10001", "data": null, "msg": "注册成功"}, ' \
             '{"status": 1, "code": "10001", "data": null, "msg": "注册成功"}, ' \
             '{"status": 1, "code": "10001", "data": null, "msg": "注册成功"}]'

nested_dict_list = json.loads(json_data2)

dict1 = {'name': 'dranson', 'age': 20, 'height': 1.7}
json_data3 = json.dumps(dict1)

list1 = [{'name': 'dranson', 'age': 20, 'height': 1.7},
         {'name': 'kk', 'age': 19, 'height': 1.6}]

json_data4 = json.dumps(list1)

# 从文件中读取json格式数据
with open('json_file.txt', encoding='utf8') as file1:
    json_data5 = json.load(file1)

# 将json个数数据写入文件
with open('file2.txt', 'w', encoding='utf8') as file2:
    json.dump(json_data5, file2)
