import requests
import json
from Class_16_Homework.homework_0527.log_class import do_log


class HttpRequest:
    """
    处理请求
    """
    def __init__(self):
        self.a_session = requests.Session()

    def __call__(self, method, url, params=None, is_json=False, **kwargs):
        method = method.lower()
        if isinstance(params, str):
            try:
                params = json.loads(params)
            except Exception as e:
                do_log.error('将json格式数据转换字典时出现异常：{}'.format(e))
                params = eval(params)
        if method == 'get':
            resp = self.a_session.request(method=method, url=url, params=params, **kwargs)
        elif method == 'post':
            if is_json:
                resp = self.a_session.request(method=method, url=url, json=params, **kwargs)
            else:
                resp = self.a_session.request(method=method, url=url, data=params, **kwargs)
        else:
            do_log.error('不支持{}请求方法'.format(method))
            resp = None
        return resp

    def close(self):
        self.a_session.close()


if __name__ == '__main__':
    register_url = 'http://test.lemonban.com:8080/futureloan/mvc/api/member/register'
    login_url = 'http://test.lemonban.com:8080/futureloan/mvc/api/member/login'
    recharge_url = 'http://test.lemonban.com:8080/futureloan/mvc/api/member/recharge'

    register_params = {
        "mobilephone": "18600001111",
        "pwd": "654321",
        "regname": "dranson"
    }

    login_params = {
        "mobilephone": "18600001111",
        "pwd": "654321",
    }

    recharge_params = {
        "mobilephone": "18600001111",
        "amount": 318964,
    }

    send_request = HttpRequest()
    send_request('post', register_url, register_params)
    send_request('GET', login_url, login_params)
    send_request('Post', recharge_url, recharge_params)
    # send_request.close()
    # send_request('Post', recharge_url, recharge_params)
