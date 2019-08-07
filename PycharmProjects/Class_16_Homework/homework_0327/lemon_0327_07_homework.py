# 使用if语句完成剪刀石头布游戏 石头1 剪刀2 布3
import random  # 导入随机模块

finger_guessing = input('请出拳：')
computer = random.randint(1,3)  # 电脑随机1-3的数

if finger_guessing == '石头' and computer == 1:
    print('电脑出石头\n' , "Deuce(平手)!" , sep='')
elif finger_guessing == '石头' and computer == 2:
    print('电脑出剪刀\n' , "You Win(你赢了)!" , sep='')
elif finger_guessing == '石头' and computer == 3:
    print('电脑出布\n' , "You Win(你输了)!" , sep='')
elif finger_guessing == '剪刀' and computer == 1:
    print('电脑出石头\n' , "You Lost(你输了)!" , sep='')
elif finger_guessing == '剪刀' and computer == 2:
    print('电脑出剪刀\n' , "Deuce(平手)!" , sep='')
elif finger_guessing == '剪刀' and computer == 3:
    print('电脑出布\n' , "You Win(你赢了)!" , sep='')
elif finger_guessing == '布' and computer == 1:
    print('电脑出石头\n' , "You Win(你赢了)!" , sep='')
elif finger_guessing == '布' and computer == 2:
    print('电脑出剪刀\n' , "You Win(你输了)!" , sep='')
elif finger_guessing == '布' and computer == 3:
    print('电脑出布\n' , "Deuce(平手)!" , sep='')
