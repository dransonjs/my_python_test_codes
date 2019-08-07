# 先导入模块
import unittest
import inspect

# 导入第三方模块
from Class_16_20190424_Unittest.lemon_0419_07_homework import MathCalculate


class TestMulti(unittest.TestCase):
    """
    测试两数相乘
    """
    def test_negatives_multi(self):
        """
        两个负数相乘
        :return:
        """
        # 能够查看当前运行的实例方法名称
        print('\nRunning Test Method: {}'.format(inspect.stack()[0][3]))
        # 实际结果
        real_result = MathCalculate(-2, -4).multiple()
        # 验证实际结果与预期结果是否一致
        expect_result = 8
        self.assertEqual(expect_result, real_result, msg='两个负数相乘测试失败')

    def test_neg_pos_multi(self):
        """
        一正一负相乘
        :return:
        """
        # 能够查看当前运行的实例方法名称
        print('\nRunning Test Method: {}'.format(inspect.stack()[0][3]))
        real_result = MathCalculate(2, -4).multiple()
        expect_result = 8
        try:
            self.assertEqual(expect_result, real_result, msg='一正一负相乘测试失败')
        except AssertionError as e:
            print('这里需要使用日志器记录日志')
            print('具体异常为：{}'.format(e))
            raise e  # raise关键字是将某个异常主动抛出

    def test_two_zero(self):
        """
        两个零相乘
        :return:
        """
        # 能够查看当前运行的实例方法名称
        print('\nRunning Test Method: {}'.format(inspect.stack()[0][3]))
        real_result = MathCalculate(0, 0).multiple()
        expect_result = 0
        self.assertEqual(expect_result, real_result, msg='两个零相乘测试失败')

    def test_positives_multi(self):
        """
        两个正数相乘
        :return:
        """
        # 能够查看当前运行的实例方法名称
        print('\nRunning Test Method: {}'.format(inspect.stack()[0][3]))
        real_result = MathCalculate(2, 4).multiple()
        expect_result = 9
        try:
            self.assertEqual(expect_result, real_result, msg='两个正数相乘测试失败')
        except AssertionError as e:
            print('这里需要使用日志器记录日志')
            print('具体异常为：{}'.format(e))
            raise e  # raise关键字是将某个异常主动抛出

if __name__ == '__main__':
    unittest.main()