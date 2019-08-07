# 列表中append和extend方法的区别

a_list = ['abc',5,4.0,True]

# a_list.append('大帅B')
# print(a_list)
#
# a_list.extend('大帅B')
# print(a_list)

a_list.append([3,2,1])
print(a_list)

a_list.extend([3,2,1])
print(a_list)