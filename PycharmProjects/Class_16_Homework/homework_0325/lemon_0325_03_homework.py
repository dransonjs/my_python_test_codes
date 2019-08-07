# 求三个整数中的最大值
num1 = int(input('请输入第一个数字：'))
num2 = int(input('请输入第二个数字：'))
num3 = int(input('请输入第三个数字：'))

# # 如果num1是最小值的判断情况
# if num1 < num2 and num1 < num3:
#     if num2 < num3:
#         print("最大的数字为：{}".format(num3))
#     else:
#         print("最大的数字为：{}".format(num2))
# # 如果num1是中间值的判断情况
# elif num2 > num1 > num3:
#     print("最大的数字为：{}".format(num2))
# elif num2 < num1 < num3:
#     print("最大的数字为：{}".format(num3))
# # 除了以上情况，num1为最大值
# else:
#     print("最大的数字为：{}".format(num1))

if num1 < num2:
    max_num = num2
else:
    max_num = num1

if max_num < num3:
    max_num = num3
print("最大的数字为：{}".format(max_num))