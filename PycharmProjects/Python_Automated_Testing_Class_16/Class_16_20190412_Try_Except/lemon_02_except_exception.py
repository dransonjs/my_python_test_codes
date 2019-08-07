try:
    num = int(input('请输入一个整数：'))
    result = 8 / num
    list_1 = [10, 20]
    list_1 * list_1
except ValueError:
    print('请输入一个整数！')
except ZeroDivisionError:
    print('除0错误')
# except TypeError:
#     print('列表与列表不能相乘')
except Exception as e:
    print(e)
    print('列表与列表不能相乘')

print('继续往下执行')