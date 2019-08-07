# 使用序号输出

# print('{1} {2} {3} {0}!'.format('forever','I','like','Python'))
# print('{1} {2} {3} {0}!'.format(1,2,3,4))

# 指定类型输出

# print('{:s} {:06d} {:.3f}'.format('python',10,5))

# 既使用序号，又指定输出类型
print('{2} {1:06d} {0:.3f}'.format(5.5,10,5))