# if判断语句格式
sex = input("你的性别是：")
if sex == '男':
    print('你是{}性,你可以进入男厕所'.format(sex))
elif sex == '女':
    print('你是{}性,你可以进入女厕所'.format(sex))
elif sex == '扶她':
    print('男女厕所随便进')
elif sex == '人妖':
    print('请就地解决')
else:
    print('请输入正确性别')