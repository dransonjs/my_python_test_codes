from suds.client import Client
from script.config_class import do_config


class Webservice:
    """
    webservice请求类
    """

    def __init__(self, url, params, method):
        """
        初始化
        :param url: 请求地址
        :param params: 请求参数
        :param method: 请求方法名
        """
        client = Client(url).service

        # 获取client对象里的方法
        method = getattr(client, method)
        # 调用通过反射获取的方法
        try:
            self.result = method(params)
        except Exception as e:
            self.result = e.fault
        # if method == getattr(Webservice, 'send_m_code'):
        #     self.result = Client(self.url1).service.sendMCode(params)
        #
        # if method == getattr(Webservice, 'user_register'):
        #     self.result = Client(self.url2).service.userRegister(params)
        #
        # if method == getattr(Webservice, 'verify_user_auth'):
        #     self.result = Client(self.url2).service.verifyUserAuth(params)
        #
        # if method == getattr(Webservice, 'bind_bank_card'):
        #     self.result = Client(self.url2).service.bindBankCard(params)

    def result_output(self):
        return self.result


if __name__ == '__main__':
    params1 = {"client_ip": "180.14.45.3", "mobile": "13711223344", "tmpl_id": "1"}
    # setattr(Webservice, 'send_m_code', 'send_m_code')
    # setattr(Webservice, 'user_register', 'user_register')
    # setattr(Webservice, 'verify_user_auth', 'verify_user_auth')
    # setattr(Webservice, 'bind_bank_card', 'bind_bank_card')
    do_webservice = Webservice(do_config("api", "send_m_code_url"), params1, 'sendMCode')
    result = do_webservice.result_output()
    print(result)
