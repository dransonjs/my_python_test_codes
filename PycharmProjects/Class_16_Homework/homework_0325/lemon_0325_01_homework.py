# 定义两个字典
# 第一个字典存放你的这些信息：姓名、性别、年龄、身高
# 第二个字典存放你的其他信息：性格、爱好、座右铭
dict1 = {'name':'dranson' , 'sex': '男' , 'age': 30 , 'height': 1.66}
dict2 = {'character':'开朗' , 'hobby':'打游戏' , 'motto':'Never Stop Learning!'}

# 将两个字典合并为第三个字典之后，打印出来
dict1.update(dict2)
print(dict1)

# 修改年龄并打印
dict1['age'] = 18
print(dict1)

# 获取座右铭
print(dict1.get('motto'))
print(dict1['motto'])

# 字典支持序列类型的哪些操作
# 求长度
print(len(dict1))

# 成员关系
print('age' in dict1)
print(30 not in dict1)

# 内置函数all、any、list
dict3 = {0:1,None:2}
dict1.update(dict3)
print(dict1)
print(all(dict1))
print(any(dict1))
print(list(dict1))