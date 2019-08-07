

def multi_two_num_1(first_num, second_num):
    """
    return案例1 返回一个值
    :param first_num:
    :param second_num:
    :return:
    """

    return first_num * second_num


num_1 = 25
num_2 = 10
result_1 = multi_two_num_1(num_1, num_2)
print(result_1)


def multi_two_num_2(first_num, second_num):
    """
    return案例2 返回多个值
    :param first_num:
    :param second_num:
    :return:
    """

    return first_num, second_num, first_num * second_num
    # print('会执行打印吗？')  # return下的代码不会执行


result_2 = multi_two_num_2(num_1, num_2)
print(result_2)


def multi_two_num_3(first_num, second_num):
    """
    return案例3 没有return返回None
    :param first_num:
    :param second_num:
    :return:
    """

    result = first_num * second_num


result_3 = multi_two_num_3(num_1, num_2)  # 没有返回值
print(result_3)