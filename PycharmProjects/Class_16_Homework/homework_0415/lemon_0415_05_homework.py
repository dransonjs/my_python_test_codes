"""
优化剪刀石头布游戏程序

a.提示用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）

b.电脑随机出拳

c.比较胜负，显示用户胜、负还是平局

新需求：

d.使用捕获异常的方式，来处理用户输入无效数据的情况

e.多次进行游戏，可以让用户选择退出游戏，退出后需要显示胜利情况，例如：用户5局胜、3局败、2局平

f.当程序结束之后，要求下一次运行程序能够获取用户历史胜负情况

h.如果使用文件保存用户历史胜负数据，需要使用异常来处理文件不存在的情况和实现程序结束后自动关闭文件的功能（选做）
"""

from random import randint

win_tuple = (1, 2), (2, 3), (3, 1)

while True:
    try:
        file_1 = open('game.txt', mode='a+', encoding='utf8')
        while True:
            computer = randint(1, 3)
            user = int(input('输入要出的拳石头（1）／剪刀（2）／布（3）／结束游戏（0）：'))
            if user != 0:
                if user not in (1, 2, 3):
                    print('输入数字超出范围，请重新输入')
                else:
                    if (user, computer) in win_tuple:
                        print('电脑出的是{}，you win'.format(computer))
                        file_1.write('胜')
                    elif user == computer:
                        print('电脑出的是{}，deuce'.format(computer))
                        file_1.write('平')
                    else:
                        print('电脑出的是{}，you lose'.format(computer))
                        file_1.write('负')
            else:
                print('游戏结束')
                file_1.write('\n')
                file_1.seek(0)
                print(file_1.read())
                break

    except ValueError:
        print('请输入1、2、3其中一个数字')
    except OSError as err:
        print('OS error:{}'.format(err))
    else:
        file_1.close()
        break

