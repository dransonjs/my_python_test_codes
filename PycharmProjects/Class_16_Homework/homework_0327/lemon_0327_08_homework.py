# 使用循环实现经典冒泡算法
# 利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法

a = [1,7,4,89,34,2]

for n in range(0,len(a)):  # 遍历前面的大数字沉底
    for a_index in range(0,len(a) - 1):  # 遍历列表a的索引
        if a[a_index] > a[a_index + 1]:  # 若列表前一元素大于后一元素，则调换位置
            b = a[a_index]
            a[a_index] = a[a_index + 1]
            a[a_index + 1] = b

print(a)

# for i in range(len(a) - 1):
#     for j in range(len(a) - i - 1):
#         if a[j] > a[j + 1]:
#             a[j + 1],a[j] = a[j],a[j + 1]

# print(a)