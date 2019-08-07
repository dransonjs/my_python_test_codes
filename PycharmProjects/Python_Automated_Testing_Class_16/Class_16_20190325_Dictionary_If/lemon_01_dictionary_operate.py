# 定义字典
dict1 = {1:'python',2:'lemon'}
print(type(dict1))

dict2 = dict({1:'python',2:'lemon'})
print(type(dict2))

dict3 = dict([(1,'python'),(2,'lemon')])
print(type(dict3))

# 获取字典内的值
user_info = {'name':'小明','age': 18, 'gender': True,'height': 1.75}
print(user_info['name'])
print(user_info.get('weight',60))  # 如果获取不到，则返回逗号后面的值

# 字典求长度
print(len(dict3))

# 获取所有keys
print(user_info.keys())
print(list(user_info.keys()))

# 获取所有values
print(user_info.values())
print(list(user_info.values()))

# 获取所有的键值对
print(user_info.items())
print(list(user_info.items()))

# 修改值
print(id(user_info))
user_info['name'] = '可优'
print(id(user_info))
print(user_info)

# 合并字典
another_info = {'motto': 'Never Stop Learning!',('hobby',):'Python Automated Testing'}
user_info.update(another_info)
print(user_info)
print(another_info)

# 删除指定的键值对
print(user_info.pop('motto'))
print(user_info)
print(user_info.popitem())  # 删除最后一个键值对
print(user_info)

# 清空字典
user_info.clear()
print(user_info)