# 列表相关操作

# 定义列表
a_var = "Python自动化测试16班人才辈出"
print(list(a_var))
a_list = ["可优",18,a_var,True,None,['Python','java','PHP']]
print('源列表：\n',a_list)

# 修改列表
a_list[1] = 17
print('修改列表元素后的列表：\n',a_list)
print('*' * 50)

# 通过切片赋值
a_list[3:5] = [1,0]
print('通过切片赋值之后的列表：\n',a_list)

# 整体插入元素
a_list.append(['apple','orange','banana'])
print('插入元素之后的列表：\n',a_list)

# 将序列类型的数据扩充到列表中
a_list.extend(['apple','orange','banana'])
print(a_list)
# a_list.extend('lemon')

# 指定位置插入数据
a_list.insert(3,'lemon')
print(a_list)

# 删除元素(指定索引)
del a_list[1]
print(a_list)

# 若有多个同样元素，默认删除第一个（指定元素）
a_list.remove(1)
print(a_list)

# pop（指定索引）
a_list.pop(1)
print(a_list)

# 删除整个列表
a_list.clear()
print(a_list)

# count（求数量）
list2 = list('lemon is the best')
print(list2.count('e'))

# 升序
list3 = [8,2,89,23,62,40]
list3.sort()
print(list3)

# 降序
list4 = [8,2,89,23,62,40]
list4.sort(reverse=True)
print(list4)

# 倒序
list5 = [8,2,89,23,62,40]
list5.reverse()
print(list5)

# all()
list6 = [1,2,3,4,0]
print(all(list6))

# any()
print(any(list6))