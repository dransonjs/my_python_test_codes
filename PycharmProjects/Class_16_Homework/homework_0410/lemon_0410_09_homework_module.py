# 裴伯拉切数列，从第三个元素开始，每个元素为前两个元素之和，用户输入某个大于0的正整数，求出小于等于这个正整数的所有裴伯拉切元素
# a.裴伯拉切数列为：0  1  1  2  3  5  8  13  21  34  55  89  144  ...
# b.例如，用户输入50，那么小于等于50的裴伯拉切元素为：0  1  1  2  3  5  8  13  21  34
# c.要求在一个模块中定义，在另一个程序中调用


def fibonacci_seq(num):
    """
    输入一个数字可以返回该数字对应的裴波拉切数列
    :param num: 一个正整数
    :return: 裴波拉切数列
    """
    a, b = 0, 1
    # sum_1 = [0, 1]

    # while (a + b) <= num:
    while a <= num:
        # sum_1.append(a + b)
        print(a, end=' ')
        a, b = b, a + b

    # return sum_1


if __name__ == '__main__':
    # print('{}的裴波拉切数列为：{}'.format(100, fibonacci_seq(100)))
    fibonacci_seq(100)