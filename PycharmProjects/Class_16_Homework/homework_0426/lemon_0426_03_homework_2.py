import unittest

from homework_0426.lemon_0419_07_homework import MathCalculate


class TestDivide(unittest.TestCase):
    """
    测试减法类
    """
    @classmethod
    def setUpClass(cls):
        cls.file_name = 'test_result_2.txt'
        cls.file = open(cls.file_name, mode='a', encoding='utf8')
        cls.file.write('{:=^40s}\n'.format('开始执行用例'))

    def test_positives(self):
        """
        测试两个正数相除
        :return:
        """
        actual_result = MathCalculate(1, 2).divide()
        expect_result = 1
        msg = '测试两个正数相除'
        fail_msg = '两个正数相除测试失败'
        try:
            self.assertEqual(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            self.file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            self.file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

    def test_negatives(self):
        """
        测试两个负数相除
        :return:
        """
        actual_result = MathCalculate(-1, -2).divide()
        expect_result = 0.5
        msg = '测试两个负数相除'
        fail_msg = '两个负数相除测试失败'
        try:
            self.assertEqual(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            self.file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            self.file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

    def test_pos_neg(self):
        """
        测试前者正数、后者负数相除
        :return:
        """
        actual_result = MathCalculate(1, -2).divide()
        expect_result = -0.5
        msg = '测试前者正数、后者负数相除'
        fail_msg = '前者正数、后者负数相除测试失败'
        try:
            self.assertEqual(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            self.file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            self.file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

    def test_neg_pos(self):
        """
        测试前者负数、后者正数相除
        :return:
        """
        actual_result = MathCalculate(-1, 2).divide()
        expect_result = -0.5
        msg = '测试前者负数、后者正数相除'
        fail_msg = '前者负数、后者正数相除测试失败'
        try:
            self.assertEqual(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            self.file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            self.file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

    def test_neg_zero(self):
        """
        测试前者负数、后者为0相除
        :return:
        """
        actual_result = MathCalculate(-1, 0).divide()
        expect_result = ZeroDivisionError
        msg = '测试前者负数、后者为0相除'
        fail_msg = '前者负数、后者为0相除测试失败'
        try:
            self.assertIsInstance(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            self.file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            self.file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

    def test_zero_neg(self):
        """
        测试前者为0、后者负数相除
        :return:
        """
        actual_result = MathCalculate(0, -2).divide()
        expect_result = 0
        msg = '测试前者为0、后者负数相除'
        fail_msg = '前者为0、后者负数相除测试失败'
        try:
            self.assertEqual(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            self.file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            self.file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

    def test_zero_pos(self):
        """
        测试前者为0、后者正数相除
        :return:
        """
        actual_result = MathCalculate(0, 2).divide()
        expect_result = 0
        msg = '测试前者为0、后者正数相除'
        fail_msg = '前者为0、后者正数相除测试失败'
        try:
            self.assertEqual(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            self.file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            self.file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

    def test_pos_zero(self):
        """
        测试前者为正数、后者为0相除
        :return:
        """
        actual_result = MathCalculate(1, 0).divide()
        expect_result = ZeroDivisionError
        msg = '测试前者为正数、后者为0相除'
        fail_msg = '前者为正数、后者为0相除测试失败'
        try:
            self.assertIsInstance(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            self.file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            self.file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

    def test_zero_zero(self):
        """
        测试两个0相除
        :return:
        """
        actual_result = MathCalculate(0, 0).divide()
        expect_result = ZeroDivisionError
        msg = '测试两个0相除'
        fail_msg = '两个0相除测试失败'
        try:
            self.assertIsInstance(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            self.file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            self.file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

    @classmethod
    def tearDownClass(cls):
        cls.file.write('{:=^40s}\n'.format('用例执行结束'))
        cls.file.close()


if __name__ == '__main__':
    unittest.main()