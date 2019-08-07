# 1、定义变量
has_ticket = bool(int(input("您是否有票？(1代表有票，0代表无票)")))

# 2、判断是否有票
if has_ticket:
    # 3、判断道具的长度是否大于20厘米
    knife_length = float(input('您携带的道具长度为：'))
    if knife_length >= 20:
        print('不允许携带{}厘米长度的道具上飞机！'.format(knife_length))
    else:
        print('通过安检，祝您旅途愉快！')
else:
    print('大哥请先去买票！')
