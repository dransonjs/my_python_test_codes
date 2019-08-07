# 编写一个数学计算类，要求初始化方法带参数（传两个数字），能够实现加减乘除运算（方法）。

class MathCalculate:
    """
    这是一个数学计算类
    """

    def __init__(self, num_1, num_2):
        self.num1 = num_1
        self.num2 = num_2

    def plus(self):
        sum1 = self.num1 + self.num2
        return sum1

    def minus(self):
        difference = self.num1 - self.num2
        return difference

    def multiple(self):
        product = self.num1 * self.num2
        return product

    def divide(self):
        try:
            quotient = self.num1 / self.num2
        except ZeroDivisionError:
            return '∞'
        else:
            return quotient
