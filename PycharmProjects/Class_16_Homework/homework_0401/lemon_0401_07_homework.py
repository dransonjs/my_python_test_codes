# 将用户输入的所有数字相乘之后对20取余数
# a.用户输入的数字个数不确定
# b.请使用函数来实现


def modulo_operation(*args):
    """
    这是一个由用户输入的数字相乘对20取模的函数
    :return:
    """
    nums = input('请输入若干数字，以空格隔开：')
    nums_2 = nums.split()  # 返回字符串分隔后的列表
    multi = 1  # 定义一个用来保存乘积的变量

    for i in range(len(nums_2)):
        multi = multi * int(nums_2[i])  # 遍历取出列表数字后循环相乘

    mod = multi % 20
    print(mod)


modulo_operation()