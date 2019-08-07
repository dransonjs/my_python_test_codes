# 假设一年的定期利率为3.52%，需要几年才能让定期存款连本带息的翻一番（例如：需要几年10000才能变成20000）


def principal_double(principal):
    """
    这是一个计算本金经过几年才能翻1倍的函数
    :param principal:
    :return:
    """
    year = 1

    while (1 + 0.0352) ** year * principal < 2 * principal:  # 经过year年后，如果本金加利息小于2倍本金则循环
        year += 1

    print(year)


principal = int(input('请输入本金：'))
principal_double(principal)