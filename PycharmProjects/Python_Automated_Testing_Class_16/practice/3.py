# 1-9999中包含数字2的数字有多少个
count = 0
for i in range(1, 10000):
    i = str(i)
    if '2' in i:
        count += 1

print(count)
