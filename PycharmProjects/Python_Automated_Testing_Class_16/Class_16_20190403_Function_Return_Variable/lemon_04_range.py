# range函数

print(list(range(1, 10)))  # 取1-9，取不到10

# 以下两种写法意思一样
print(list(range(0, 10)))
print(list(range(10)))

# range函数经常用于for循环

for i in range(2, 10):
    print(i, end='\t')

print()

for i in range(2, 10, 2):  # 第三个数字是步长
    print(i, end='\t')
