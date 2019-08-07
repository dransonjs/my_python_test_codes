# 分别使用for、while循环，去除列表[1, 4, 3, 4, 3, 4, 1, 2, 6]中的数字4

list_1 = [1, 4, 3, 4, 3, 4, 1, 2, 6]

# for循环
for i in list_1:
    if i == 4:
        list_1.remove(i)

print(list_1)

# while循环
# i = 0
#
# while i < len(list_1) - 1:
#     if list_1[i] == 4:
#         del list_1[i]
#     i += 1
#
# print(list_1)
