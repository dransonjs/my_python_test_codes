# 求列表所有元素的和
# a.one_list = [13, 21, 3, 76, 54, 12, 44, 80, 92]
# b.使用while循环来实现

one_list = [13, 21, 3, 76, 54, 12, 44, 80, 92]
one_sum = 0  # 定义一个存储和的变量
i = 0  # 定义一个one_list的索引变量

while len(one_list) > 0:  # 当列表长度大于0执行循环
    one_sum += one_list.pop(i)  # 遍历取出列表每个数字后做和运算

print(one_sum)