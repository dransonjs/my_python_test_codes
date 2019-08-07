# 求圆的面积
# a.传入一个圆的半径，将其面积返回
# b.函数中的Π，可以导入import math，通过math.pi来获取（也可以直接使用3.14）

import math


def circle_area(radius):
    """
    这是一个计算圆的面积的函数
    :return:
    """
    circle_a = math.pi * radius ** 2
    print(circle_a)


r = float(input('输入圆的半径：'))
circle_area(r)