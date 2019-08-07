# 使用while打印九九乘法表
j = 1
i = 1

while j < 10:
    print(i ," * ", j ," = ", i*j ,end = '\t')  # end = '\t'表示同一行的分隔符
    if i == j:
        print('\n')
        j += 1  # 只有当i=j换行时j才加1，其他情况下j不变
        i = 1  # 当i=j换行输出时重置i为1
        continue
    i += 1  # 同一行，i不等于j时，i递增1
