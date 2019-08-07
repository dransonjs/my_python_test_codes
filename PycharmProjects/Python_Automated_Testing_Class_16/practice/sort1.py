list1 = [20, 3, 111]
# list1.sort()  # 改变原列表
# print(list1)
#
# list2 = sorted(list1)  # 默认升序，会新建另一个列表，不改变原列表
# print(list2)

# 利用key实现倒序
list3 = sorted(list1, key=lambda x: x*-1)
print(list3)

# 利用reverse=True实现倒序
list4 = sorted(list1, reverse=True)
print(list4)

# 匿名函数，x是参数，x*-1是返回值
f = lambda x: x*-1
print(f(2))

