from Class_16_Homework.lemon_0410_07_homework_module import (
    circle_area,
    circle_perimeter,
    rectangle_area,
    rectangle_perimeter
)

r = float(input('输入圆的半径：'))
print('圆的面积为：{}，圆的周长为：{}'.format(circle_area(r), circle_perimeter(r)))
print()

l = float(input('输入长方形的长：'))
w = float(input('输入长方形的宽：'))
print('长方形的面积为：{}，长方形的周长为：{}'.format(rectangle_area(l, w), rectangle_perimeter(l, w)))
