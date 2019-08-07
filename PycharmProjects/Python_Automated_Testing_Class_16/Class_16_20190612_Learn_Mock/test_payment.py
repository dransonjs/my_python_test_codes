import unittest
from unittest import mock

from Class_16_20190612_Learn_Mock.payment_mock import Payment


class PaymentTest(unittest.TestCase):
    """
    测试支付接口
    """
    def setUp(self):
        self.payment = Payment()

    def test_success(self):
        """
        测试支付成功
        :return:
        """
        self.payment.auth = mock.Mock(return_value=200)
        res = self.payment.pay(1001, 123456, 777)
        self.assertEqual('success', res)

    def test_fail(self):
        """
        测试支付失败
        :return:
        """
        self.payment.auth = mock.Mock(return_value=500)
        res = self.payment.pay(1002, 123456, 888)
        self.assertEqual('fail', res)

    def test_retry_success(self):
        """
        测试调用第三方接口超时之后，再次支付成功
        :return:
        """
        self.payment.auth = mock.Mock(side_effect=[TimeoutError, 200])
        res = self.payment.pay(1003, 123456, 999)
        self.assertEqual('success', res)

    def test_retry_fail(self):
        """
        测试调用第三方接口超时之后，再次支付失败
        :return:
        """
        # side_effect 可以为序列类型、异常类型、对象
        # 如果为序列类型，每次调用mock对象，会依次side_effect中的元素返回
        self.payment.auth = mock.Mock(side_effect=[TimeoutError, 500])
        res = self.payment.pay(1004, 123456, 1000)
        self.assertEqual('fail', res)


if __name__ == '__main__':
    unittest.main()
