import unittest

from homework_0426.lemon_0419_07_homework import MathCalculate


def setUpModule():
    global file_name
    global file
    file_name = 'test_result_3.txt'
    file = open(file_name, mode='a', encoding='utf8')
    file.write('{:=^40s}\n'.format('开始执行用例'))
    

def tearDownModule():
    file.write('{:=^40s}\n'.format('用例执行结束'))
    file.close()


class TestMinus(unittest.TestCase):
    """
    测试减法类
    """
    # @classmethod
    # def setUpClass(cls):
    #     """
    #     重写父类的类方法，全部实例方法（用例）执行完只会被调用1次
    #     :return:
    #     """
    #     cls.file_name = 'test_result.txt'
    #     print('打开【{}】文件'.format(cls.file_name))
    #     print("{:=^40s}".format("开始执行用例"))
    #     cls.file = open(cls.file_name, mode='a', encoding='utf8')
    #     cls.file.write("{:=^40s}\n".format("开始执行用例"))

    # def setUp(self):
    #     """
    #     重写父类方法
    #     在每一个用例执行之前会被调用
    #     :return:
    #     """
    #     file_name = 'test_result.txt'
    #     print('打开【{}】文件'.format(file_name))
    #     print("{:=^40s}".format("开始执行用例"))
    #     file = open(file_name, mode='a', encoding='utf8')
    #     file.write("{:=^40s}\n".format("开始执行用例"))

    @unittest.skip('test_positives')  # 跳过这条用例，不执行
    def test_positives(self):
        """
        测试两个正数相减
        :return:
        """
        actual_result = MathCalculate(1, 2).minus()
        expect_result = -1
        msg = '两个正数相减测试'
        fail_msg = '两个正数相减测试失败'

        try:
            self.assertEqual(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            file.write('{}，执行结果为：{}，具体异常为：{}\n'.format(msg, 'Fail', e))
            raise e
        else:
            file.write('{}，执行结果为：{}\n'.format(msg, 'Pass'))

    def test_negatives(self):
        """
        测试两个负数相减
        :return:
        """
        actual_result = MathCalculate(-1, -2).minus()
        expect_result = 1
        msg = '两个负数相减测试'
        fail_msg = '两个负数相减测试失败'

        try:
            self.assertEqual(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            file.write('{}，执行结果为：{}，具体异常为：{}\n'.format(msg, 'Fail', e))
            raise e
        else:
            file.write('{}，执行结果为：{}\n'.format(msg, 'Pass'))

    def test_pos_neg(self):
        """
        测试前者正数、后者负数相减
        :return:
        """
        actual_result = MathCalculate(1, -2).minus()
        expect_result = 3
        msg = '前者正数、后者负数相减测试'
        fail_msg = '前者正数、后者负数相减测试失败'

        try:
            self.assertEqual(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            file.write('{}，执行结果为：{}，具体异常为：{}\n'.format(msg, 'Fail', e))
            raise e
        else:
            file.write('{}，执行结果为：{}\n'.format(msg, 'Pass'))

    def test_neg_pos(self):
        """
        测试前者负数、后者正数相减
        :return:
        """
        actual_result = MathCalculate(-1, 2).minus()
        expect_result = -3
        msg = '前者负数、后者正数相减测试'
        fail_msg = '前者负数、后者正数相减测试失败'

        try:
            self.assertEqual(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            file.write('{}，执行结果为：{}，具体异常为：{}\n'.format(msg, 'Fail', e))
            raise e
        else:
            file.write('{}，执行结果为：{}\n'.format(msg, 'Pass'))

    def test_neg_zero(self):
        """
        测试前者负数、后者为0相减
        :return:
        """
        actual_result = MathCalculate(-1, 0).minus()
        expect_result = -1
        msg = '前者负数、后者为0相减测试'
        fail_msg = '前者负数、后者为0相减测试失败'

        try:
            self.assertEqual(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            file.write('{}，执行结果为：{}，具体异常为：{}\n'.format(msg, 'Fail', e))
            raise e
        else:
            file.write('{}，执行结果为：{}\n'.format(msg, 'Pass'))

    def test_zero_neg(self):
        """
        测试前者为0、后者负数相减
        :return:
        """
        actual_result = MathCalculate(0, -2).minus()
        expect_result = 2
        msg = '前者为0、后者负数相减测试'
        fail_msg = '前者为0、后者负数相减测试失败'

        try:
            self.assertEqual(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            file.write('{}，执行结果为：{}，具体异常为：{}\n'.format(msg, 'Fail', e))
            raise e
        else:
            file.write('{}，执行结果为：{}\n'.format(msg, 'Pass'))

    def test_zero_pos(self):
        """
        测试前者为0、后者正数相减
        :return:
        """
        actual_result = MathCalculate(0, 2).minus()
        expect_result = -2
        msg = '前者为0、后者正数相减测试'
        fail_msg = '前者为0、后者正数相减测试失败'

        try:
            self.assertEqual(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            file.write('{}，执行结果为：{}，具体异常为：{}\n'.format(msg, 'Fail', e))
            raise e
        else:
            file.write('{}，执行结果为：{}\n'.format(msg, 'Pass'))

    def test_pos_zero(self):
        """
        测试前者为正数、后者为0相减
        :return:
        """
        actual_result = MathCalculate(1, 0).minus()
        expect_result = -1
        msg = '前者为正数、后者为0相减测试'
        fail_msg = '前者为正数、后者为0相减测试失败'

        try:
            self.assertEqual(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            file.write('{}，执行结果为：{}，具体异常为：{}\n'.format(msg, 'Fail', e))
            raise e
        else:
            file.write('{}，执行结果为：{}\n'.format(msg, 'Pass'))

    def test_zero_zero(self):
        """
        测试两个0相减
        :return:
        """
        actual_result = MathCalculate(0, 0).minus()
        expect_result = 0
        msg = '两个0相减测试'
        fail_msg = '两个0相减测试失败'

        try:
            self.assertEqual(actual_result, expect_result, msg=fail_msg)
        except AssertionError as e:
            file.write('{}，执行结果为：{}，具体异常为：{}\n'.format(msg, 'Fail', e))
            raise e
        else:
            file.write('{}，执行结果为：{}\n'.format(msg, 'Pass'))

    # def tearDown(self):
    #     """
    #     重写父类方法
    #     每一个用例执行结束之后会被调用
    #     :return:
    #     """
    #     print("{:=^40s}".format('用例执行结束'))
    #     file.write("{:=^40s}\n".format('用例执行结束'))
    #     print('关闭【{}】文件'.format(file_name))
    #     file.close()

    # @classmethod
    # def tearDownClass(cls):
    #     """
    #     重写父类的类方法，全部实例方法（用例）执行完只会被调用1次
    #     :return:
    #     """
    #     print("{:=^40s}".format('用例执行结束'))
    #     cls.file.write("{:=^40s}\n".format('用例执行结束'))
    #     print('关闭【{}】文件'.format(cls.file_name))
    #     cls.file.close()


class TestDivide(unittest.TestCase):
    """
    测试减法类
    """
    # @classmethod
    # def setUpClass(cls):
    #     cls.file_name = 'test_result_2.txt'
    #     cls.file = open(cls.file_name, mode='a', encoding='utf8')
    #     cls.file.write('{:=^40s}\n'.format('开始执行用例'))

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
            file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

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
            file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

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
            file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

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
            file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

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
            file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

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
            file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

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
            file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

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
            file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

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
            file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            file.write('{}，执行结果：{}\n'.format(msg, 'pass'))

    # @classmethod
    # def tearDownClass(cls):
    #     cls.file.write('{:=^40s}\n'.format('用例执行结束'))
    #     cls.file.close()


if __name__ == '__main__':
    unittest.main()