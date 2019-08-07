# 在控制台依次提示用户输入：姓名、网名、年龄、性别、爱好、座右铭

name = input('姓名：')
nickname = input('网名：')
age = input('年龄：')
sex = input('性别：')
hobby = input('爱好：')
motto = input('座右铭：')

print('*' * 50)
# print(' 姓名：%s\n' % name,
#       '网名：%s\n' % nickname,
#       '年龄：%s\n' % age,
#       '性别：%s\n' % sex,
#       '爱好：%s\n' % hobby,
#       '座右铭：%s' % motto)
print('个人信息展示\n'
      '姓名（网名）：{} ({})\n'.format(name,nickname),
      '年龄：{}\n'.format(age),
      '性别：{}\n'.format(sex),
      '爱好：{}\n'.format(hobby),
      '座右铭：{}'.format(motto),sep = '')
print('*' * 50)