

def fn_hello_1(greeting, name):
    """
    greeting for somebody in function1
    :param greeting:
    :param name:
    :return:
    """
    print("{},{}!".format(greeting, name))


# fn_hello_1("hello", "可优")


def fn_hello_2(name, greeting):
    """
    greeting for somebody in function2
    :param greeting:
    :param name:
    :return:
    """
    print("{},{}!".format(greeting, name))


fn_hello_2("hello", "可优")


def print_your_birthday(name, year, month, day):
    """
    print your birthday
    :param name:
    :param year:
    :param month:
    :param day:
    :return:
    """
    print("{}的生日是：{}年{}月{}日".format(name, year, month, day))


print_your_birthday(day=4, name='可优', month=3, year=2000)


def fn_hello_3(name, greeting='你好'):
    """
    greeting for somebody in function3
    :param greeting:
    :param name:
    :return:
    """
    print("{},{}!".format(greeting, name))


fn_hello_3("可优")
fn_hello_3("可优", "你吃了吗")


def print_params_1(*args):
    """
    print parameter function
    :param args:
    :return:
    """
    print("params为：{}".format(args))
    print("params的类型为：{}".format(type(args)))


print_params_1()
print_params_1('可优')
print_params_1('可优', '柠檬小姐姐', [520, 1314])


def print_params_2(*args, **kwargs):
    """
    print parameter function
    :param params:
    :return:
    """
    print("params为：{}".format(args))
    print("params的类型为：{}".format(type(args)))

    print("kw_params为：{}".format(kwargs))
    print("kw_params的类型为：{}".format(type(kwargs)))


print_params_2('可优', '柠檬小姐姐', [520, 1314], time=10000, gift='钻戒')