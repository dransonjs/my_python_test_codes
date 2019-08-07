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
        quotient = self.num1 / self.num2
        return quotient


cal = MathCalculate(float(input('输入第一个数：')), float(input('输入第二个数：')))
print('{}加{}的和为{}'.format(cal.num1, cal.num2, cal.plus()))
print('{}减{}的差为{}'.format(cal.num1, cal.num2, cal.minus()))
print('{}乘{}的积为{}'.format(cal.num1, cal.num2, cal.multiple()))
print('{}除{}的商为{}'.format(cal.num1, cal.num2, cal.divide()))