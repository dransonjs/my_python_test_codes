# 使用while循环实现输出2 - 3 + 4 - 5 + 6 ... + 100 的和

i = 3  # 定义一个循环计数器
sum_1 = 2  # 定义一个存储最终计算结果的值

while i < 101:
    while i % 2 != 0:  # 如果为奇数则循环
        sum_1 -= i  # 奇数做减运算
        i += 1  # 奇数变成偶数
    sum_1 += i  # 偶数做加运算
    i += 1  # 修改计数器

print(sum_1)