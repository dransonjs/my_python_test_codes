# 取出列表中最大的值
a_list = [13, 20, 42, 85, 9, 45]
print(max(a_list))  # 用max函数取最大值

# 用for循环冒泡取最大值
for n in range(len(a_list) - 1):
    if a_list[n] > a_list[n + 1]:
        a_list[n], a_list[n + 1] = a_list[n + 1], a_list[n]

print(a_list[n+1])