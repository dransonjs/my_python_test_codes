import requests
from unittest import mock


def request_lemfix():
    """
    获取柠檬班论坛主页
    :return:
    """
    res = requests.get('http://www.lemfix.com/')
    return res.text.encode('utf8')


if __name__ == '__main__':
    # print(request_lemfix())
    request_lemfix = mock.Mock(return_value='这里会显示柠檬班论坛主页内容')
    print(request_lemfix())
