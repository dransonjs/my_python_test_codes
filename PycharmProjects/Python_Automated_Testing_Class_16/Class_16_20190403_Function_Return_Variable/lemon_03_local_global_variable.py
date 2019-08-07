

def manual_fn1():
    """
    全局变量和局部变量案例1
    :return:
    """
    num = 1  # 全局变量和局部变量建议不要同名
    print('函数体内，id(num) = {}'.format(id(num)))
    return num


num = 10
print('函数调用之前，id(num) = {}'.format(id(num)))

# 虽然全局变量和局部变量同名，但调用函数前后全局变量num的值和地址不受影响
manual_fn1()
print('num = {}'.format(num))
print('函数调用之后，id(num) = {}'.format(id(num)))

# return局部变量num后，全局变量num1会接收局部变量num的值和地址
num1 = manual_fn1()
print('num1 = {}'.format(num1))
print('函数调用之后，id(num1) = {}'.format(id(num1)))
print()


def manual_fn2(num_y):
    """
    全局变量和局部变量案例2
    :return:
    """
    print(num_y)
    print('函数体内，id(num_y) = {}'.format(id(num_y)))
    return num_y

num_x = 50
print('函数调用之前，num_x = {}'.format(num_x))
print('函数调用之前，id(num_x) = {}'.format(id(num_x)))
num_x = manual_fn2(100)  # 重新对全局变量num_x赋值，并继承局部变量num_y的值和地址
print('函数调用之后，num_x = {}'.format(num_x))
print('函数调用之后，id(num_x) = {}'.format(id(num_x)))
print()


def manual_fn3():
    """
    全局变量和局部变量案例3
    :return:
    """
    print(num_z)  # 函数被调用时，先在函数体内局部作用域查找是否有定义num_z，找不到则会去函数外部全局作用域查找num_z
    print('函数体内，id(num_z) = {}'.format(id(num_z)))
    # num_z = 30  # num_z不能放在后面，变量必须先定义后使用


num_z = 23
print('函数调用之前，num_z = {}'.format(num_z))
print('函数调用之前，id(num_z) = {}'.format(id(num_z)))
manual_fn3()
print('函数调用之后，num_z = {}'.format(num_z))
print('函数调用之后，id(num_z) = {}'.format(id(num_z)))
print()


def manual_fn4():
    """
    全局变量和局部变量案例4
    :return:
    """
    global num_w  # 能修改函数外部全局变量的关键字
    num_w = 40
    print(num_w)
    print('函数体内，id(num_w) = {}'.format(id(num_w)))


num_w = 50
print('函数调用之前，num_w = {}'.format(num_w))
print('函数调用之前，id(num_w) = {}'.format(id(num_w)))
manual_fn4()
print('函数调用之后，num_w = {}'.format(num_w))
print('函数调用之后，id(num_w) = {}'.format(id(num_w)))