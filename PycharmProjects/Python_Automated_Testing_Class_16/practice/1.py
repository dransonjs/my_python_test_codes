def list_reversed(a_list):
    """
    列表翻转，且不改变原列表函数
    :param a_list:
    :return:
    """
    b_list = []
    b_list.extend(a_list)
    for i in range(len(b_list)//2):
        b_list[i], b_list[len(b_list)-1-i] = b_list[len(b_list)-1-i], b_list[i]

    return b_list


list_1 = [1, 3, 5, 7, 9]
list_2 = list_reversed(list_1)
print(list_2, list_1)

