# 将列表翻转的所有方法

# 使用reverse函数翻转
a_list = [13,20,42,85,9,45]
# a_list.reverse()
# print(a_list)

# 使用for循环翻转
for n in range(len(a_list) // 2):
    a_list[n], a_list[len(a_list) - 1 - n] = a_list[len(a_list) - 1 - n], a_list[n]

print(a_list)