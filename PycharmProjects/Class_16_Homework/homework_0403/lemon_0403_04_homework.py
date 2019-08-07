# 从键盘获取一个数字，然后计算它的阶乘，例如输入的是3，那么即计算3!的结果，并输出

num = int(input('输入一个整数：'))
i = 1  # 定义一个循环计数器
factorial = 1  # 定义一个存储整数阶乘的变量

while i <= num:  # 如果计数器不大于输入数字则循环
    factorial *= i
    i += 1

print('{}的阶乘等于：'.format(num), factorial)