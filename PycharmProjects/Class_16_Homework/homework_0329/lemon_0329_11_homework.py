# 将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素

list_1 = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
list_2 = []

for i in range(len(list_1) - 1):
    list_2.append(list_1[i])
    if list_2.count(list_1[i]) > 1:
        list_2.remove(list_1[i])
print(list_2)
