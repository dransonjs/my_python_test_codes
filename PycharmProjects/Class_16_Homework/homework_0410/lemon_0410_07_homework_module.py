# a.在一个模块中，定义求圆的面积和周长、长方形的面积和周长的函数，然后分别在另一个程序中调用
# b.每个模块中需要添加测试代码

import math


def circle_area(r):
    """
    求圆的面积
    :param r: 半径
    :return: 面积
    """
    return math.pi * r ** 2


def circle_perimeter(r):
    """
    求圆的周长
    :param r: 半径
    :return: 周长
    """
    return math.pi * r * 2


def rectangle_area(l, w):
    """
    求长方形的面积
    :param l: 长
    :param w: 宽
    :return: 面积
    """
    return l * w


def rectangle_perimeter(l, w):
    """
    求长方形的周长
    :param l: 长
    :param w: 宽
    :return: 周长
    """
    return (l + w) * 2


if __name__ == '__main__':
    print('这段代码会被执行')
