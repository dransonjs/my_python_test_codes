# 通过年份来判断生肖
zodiac_animal = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

your_birthday_year = 2018  # 生成年份
index_num = your_birthday_year % 12  #索引编号
print('索引值为：', index_num)
print('你的生肖为', zodiac_animal[index_num])