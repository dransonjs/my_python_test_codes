"""
从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
a.定义一个函数，接收用户输入的用户名和密码作为参数
b.正确的账号，用户名为lemon，密码为best
"""


def login(usr, psw):
    """
    检测用户登录信息
    :param usr:
    :param psw:
    :return:
    """
    if usr == 'lemon' and psw == 'best':
        print('登录系统成功')
    else:
        print('用户名或密码错误')


username = input('用户名：')
password = input('密码：')
login(username, password)