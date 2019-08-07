import unittest
import inspect


class Foo(object):
    pass


class TestCase(unittest.TestCase):
    """
    定义测试类，用于联系各种常用的断言方式
    """
    def test_case01(self):
        print('\nRunning Test Method: {}'.format(inspect.stack()[0][3]))
        self.assertTrue('PYTHON'.isupper(), msg='测试指定字符串为大写失败')

    def test_case02(self):
        print('\nRunning Test Method: {}'.format(inspect.stack()[0][3]))
        obj = Foo()
        new_obj = obj
        self.assertIs(obj, new_obj, msg='测试两个对象是同一个对象失败')

    def test_case03(self):
        print('\nRunning Test Method: {}'.format(inspect.stack()[0][3]))
        obj = Foo()
        self.assertIsInstance(obj, Foo, msg='测试一个对象是某个类的一个实例失败')


if __name__ == '__main__':
    unittest.main()