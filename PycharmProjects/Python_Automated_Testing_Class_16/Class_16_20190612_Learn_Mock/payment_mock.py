import requests


class Payment:
    """
    定义第三方支付类
    """
    def auth(self, card_num, amount):
        """
        请求第三方支付接口，并返回响应码
        :param card_num: 卡号
        :param amount: 金额
        :return: 返回状态码，200代表支付成功，500代表支付失败
        """
        url = "http://third.payment.com"
        data = {"card_num": card_num, "amount": amount}
        self.response = requests.post(url, data=data)
        return self.response.status_code

    def pay(self, user_id, card_num, amount):
        """
        支付
        :param user_id:
        :param card_num:
        :param amount:
        :return:
        """
        try:
            status_code = self.auth(card_num, amount)
        except TimeoutError:
            status_code = self.auth(card_num, amount)

        if status_code == 200:
            print("【{}】支付【{}】成功！进行扣款并记录支付历史".format(user_id, amount))
            return 'success'

        if status_code == 500:
            print("【{}】支付【{}】失败！不进行扣款".format(user_id, amount))
            return 'fail'
