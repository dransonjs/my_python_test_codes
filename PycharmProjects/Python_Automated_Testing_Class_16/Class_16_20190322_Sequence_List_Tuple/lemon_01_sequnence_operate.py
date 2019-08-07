# 练习序列类型中支持的操作
# 定义一个包含12生肖的字符串
zodiac_animal = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

# 1、通过索引取值
print(zodiac_animal[3])

# 2、切片操作
print(zodiac_animal[1:9])  # print(zodiac_animal[1:-3])

# 3、成员关系操作（in 或者 not in）
print("猪" in zodiac_animal)
print('猫' not in zodiac_animal)

# 4、连接操作（+）
new_zodiac = zodiac_animal + '猫'
print(new_zodiac)

# 5、重复操作（*）
print(zodiac_animal * 3)

# 6、支持遍历
for item in zodiac_animal:
    print(item)

# 7、求长度
print(len(zodiac_animal))