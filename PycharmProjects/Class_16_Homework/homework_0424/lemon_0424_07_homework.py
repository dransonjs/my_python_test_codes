import unittest

from homework_0424.lemon_0419_07_homework import MathCalculate


class TestDivide(unittest.TestCase):
    """
    测试减法类
    """
    def test_positives(self):
        """
        测试两个正数相除
        :return:
        """
        actual_result = MathCalculate(1, 2).divide()
        expect_result = 1
        try:
            self.assertEqual(actual_result, expect_result, msg='两个正数相除测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            # 把用例执行失败的错误信息写入文件，只在这里实现，后面的用例同理，就不补充写入文件相关代码了
            file_1 = open('test_result.txt', mode='a+', encoding='utf8')
            file_1.write('具体异常为：{}\n'.format(e))
            file_1.close()
            raise e

    def test_negatives(self):
        """
        测试两个负数相除
        :return:
        """
        actual_result = MathCalculate(-1, -2).divide()
        expect_result = 0.5
        try:
            self.assertEqual(actual_result, expect_result, msg='两个负数相除测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            raise e

    def test_pos_neg(self):
        """
        测试前者正数、后者负数相除
        :return:
        """
        actual_result = MathCalculate(1, -2).divide()
        expect_result = -0.5
        try:
            self.assertEqual(actual_result, expect_result, msg='前正后负相除测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            raise e

    def test_neg_pos(self):
        """
        测试前者负数、后者正数相除
        :return:
        """
        actual_result = MathCalculate(-1, 2).divide()
        expect_result = -0.5
        try:
            self.assertEqual(actual_result, expect_result, msg='前负后正相除测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            raise e

    def test_neg_zero(self):
        """
        测试前者负数、后者为0相除
        :return:
        """
        actual_result = MathCalculate(-1, 0).divide()
        expect_result = ZeroDivisionError
        try:
            # 验证actual_result的返回值是否是expect_result除零错误的一个对象
            self.assertIsInstance(actual_result, expect_result, msg='前负后0相除测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            raise e

    def test_zero_neg(self):
        """
        测试前者为0、后者负数相除
        :return:
        """
        actual_result = MathCalculate(0, -2).divide()
        expect_result = 0
        try:
            self.assertEqual(actual_result, expect_result, msg='前0后负相除测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            raise e

    def test_zero_pos(self):
        """
        测试前者为0、后者正数相除
        :return:
        """
        actual_result = MathCalculate(0, 2).divide()
        expect_result = 0
        try:
            self.assertEqual(actual_result, expect_result, msg='前0后正相除测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            raise e

    def test_pos_zero(self):
        """
        测试前者为正数、后者为0相除
        :return:
        """
        actual_result = MathCalculate(1, 0).divide()
        expect_result = ZeroDivisionError
        try:
            self.assertIsInstance(actual_result, expect_result, msg='前正后0相除测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            raise e

    def test_zero_zero(self):
        """
        测试两个0相除
        :return:
        """
        actual_result = MathCalculate(0, 0).divide()
        expect_result = ZeroDivisionError
        try:
            self.assertIsInstance(actual_result, expect_result, msg='两个0相除测试失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            raise e

if __name__ == '__main__':
    unittest.main()