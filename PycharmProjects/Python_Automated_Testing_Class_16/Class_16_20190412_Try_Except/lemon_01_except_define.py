# try:
#     num = int(input('请输入一个整数：'))
#     print(111)
# except:
#     print('请输入一个整数！')
#
# print('继续往下执行')

while True:
    try:
        num = int(input('请输入一个整数：'))
        break
    except:
        print('输入有误，请重新输入')

print('继续往下执行')