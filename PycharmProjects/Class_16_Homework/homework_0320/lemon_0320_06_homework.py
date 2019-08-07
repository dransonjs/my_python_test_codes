my_hobby = "Never stop learning!"
print(my_hobby[2:6])  # 截取从2~6位置的字符串
print(my_hobby[2:])  # 截取从2~末尾的字符串
print(my_hobby[:6])  # 截取从开始~6位置的字符串
print(my_hobby[:])  # 截取完整的字符串
print(my_hobby[::2])  # 从开始位置，每隔一个字符截取字符串
print(my_hobby[3::3])  # 从索引3开始，每隔2个取一个
print(my_hobby[2:-1])  # 截取从2~末尾-1的字符串
print(my_hobby[-2:])  # 截取字符串末尾两个字符
print(my_hobby[::-1])  # 字符串的逆序（拓展）