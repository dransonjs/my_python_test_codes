# 计算用户输入的整数之和


def sum_count(*args):
    """

    :param args:
    :param kwargs:
    :return:
    """
    num = 0

    for item in args:
        num += item

    print("这些整数的和为：{}".format(num))


num_str = input('请输入多个整数，以逗号分隔')
num_list = num_str.split(',')
new_list = []
for i in num_list:
    new_list.append(int(i))

# tuple_1 = (1, 10, 2, 3, 34, 100, 10000, 23, 99, 132)
sum_count(*new_list)