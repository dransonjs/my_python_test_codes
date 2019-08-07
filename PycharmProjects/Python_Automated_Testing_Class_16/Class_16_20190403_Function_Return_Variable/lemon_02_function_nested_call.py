

def outer():
    """
    函数嵌套调用案例
    :return:
    """
    print("+" * 50)
    print('outer function is called')


def inner():
    """
    函数嵌套调用案例
    :return:
    """
    print("*" * 50)
    print('inner function is called')

    outer()  # 函数在定义时调用另一个函数
    print("*" * 50)


inner()