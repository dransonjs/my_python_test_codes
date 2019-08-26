# 将test0000~test9999 1万个数据写入txt

with open("acount.txt", "w", encoding="utf8") as f:
    for i in range(10000):
        str1 = "test" + "0" * (4 - len(str(i))) + str(i)
        f.write(str1+"\n")
