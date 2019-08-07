"""
输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
b.根据BMI指数，给与相应提醒
低于18.5： 过轻
18.5-25：  正常
25-28：    过重
28-32：    肥胖
高于32：   严重肥胖
"""


def bmi(height, weight):
    """
    计算BMI指数
    :param height:
    :param weight:
    :return:
    """
    bmi_num = float(weight / height ** 2)

    if bmi_num < 18.5:
        print('{:.2f}低于18.5：过轻'.format(bmi_num))
    elif 18.5 <= bmi_num <= 25:
        print('{:.2f}处于18.5-25之间：正常'.format(bmi_num))
    elif 25 <= bmi_num <= 28:
        print('{:.2f}处于25-28之间：过重'.format(bmi_num))
    elif 28 <= bmi_num <= 32:
        print('{:.2f}处于28-32之间：肥胖'.format(bmi_num))
    else:
        print('{:.2f}高于32：严重肥胖'.format(bmi_num))


h = float(input('请输入身高:'))
w = float(input('请输入体重:'))
bmi(h, w)