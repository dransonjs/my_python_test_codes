import unittest

from homework_0424.lemon_0419_07_homework import MathCalculate


class TestMinus(unittest.TestCase):
    """
    测试减法类
    """
    def test_positives(self):
        """
        测试两个正数相减
        :return:
        """
        actual_result = MathCalculate(1, 2).minus()
        expect_result = -1
        try:
            self.assertEqual(actual_result, expect_result, msg='两个正数相减测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            raise e

    def test_negatives(self):
        """
        测试两个负数相减
        :return:
        """
        actual_result = MathCalculate(-1, -2).minus()
        expect_result = 1
        try:
            self.assertEqual(actual_result, expect_result, msg='两个负数相减测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            raise e

    def test_pos_neg(self):
        """
        测试前者正数、后者负数相减
        :return:
        """
        actual_result = MathCalculate(1, -2).minus()
        expect_result = 3
        try:
            self.assertEqual(actual_result, expect_result, msg='前正后负相减测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            raise e

    def test_neg_pos(self):
        """
        测试前者负数、后者正数相减
        :return:
        """
        actual_result = MathCalculate(-1, 2).minus()
        expect_result = -3
        try:
            self.assertEqual(actual_result, expect_result, msg='前负后正相减测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            raise e

    def test_neg_zero(self):
        """
        测试前者负数、后者为0相减
        :return:
        """
        actual_result = MathCalculate(-1, 0).minus()
        expect_result = -1
        try:
            self.assertEqual(actual_result, expect_result, msg='前负后0相减测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            raise e

    def test_zero_neg(self):
        """
        测试前者为0、后者负数相减
        :return:
        """
        actual_result = MathCalculate(0, -2).minus()
        expect_result = 2
        try:
            self.assertEqual(actual_result, expect_result, msg='前0后负相减测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            raise e

    def test_zero_pos(self):
        """
        测试前者为0、后者正数相减
        :return:
        """
        actual_result = MathCalculate(0, 2).minus()
        expect_result = -2
        try:
            self.assertEqual(actual_result, expect_result, msg='前0后正相减测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            raise e

    def test_pos_zero(self):
        """
        测试前者为0、后者正数相减
        :return:
        """
        actual_result = MathCalculate(1, 0).minus()
        expect_result = 1
        try:
            self.assertEqual(actual_result, expect_result, msg='前正后0相减测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            raise e

    def test_zero_zero(self):
        """
        测试两个0相减
        :return:
        """
        actual_result = MathCalculate(0, 0).minus()
        expect_result = 0
        try:
            self.assertEqual(actual_result, expect_result, msg='两个0相减测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            raise e

if __name__ == '__main__':
    unittest.main()