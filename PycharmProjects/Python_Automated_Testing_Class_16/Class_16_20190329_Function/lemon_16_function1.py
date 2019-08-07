username = '柠檬班'


def say_hello():  # 定义函数
    """
    greet, say hello!
    :return:
    """
    print("Hello, 华仔，晚上好！")
    print("来一首忘情水！")


print(username)
say_hello()  # 调用函数
print(say_hello.__doc__)  # 打印函数内部注释