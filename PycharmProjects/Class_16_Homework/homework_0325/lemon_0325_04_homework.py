# 判断是否为闰年
year = input("请输入一个年份：")
# 如果能被4整除，则为闰年
if int(year) % 4 == 0:
    print("{}是闰年".format(int(year)))
else:
    print("{}是平年".format(int(year)))