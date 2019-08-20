import re

# str1 = "KeYou is handsome!"

# 通过.匹配任意一个字符（除了\n）
# result = re.match("K.You", str1)

# 通过[]匹配[]中列举的单个字符
# result = re.match("K[abcde]You", str1)


# str2 = "K2You is handsome!"

# 通过\d匹配单个数字（0-9）
# result = re.match(r"K\dYou", str2)

# 通过\w匹配单个单词字符（a-z，A-Z，0-9，_)
# result = re.match(r"K\wYou", str2)

# str3 = "KeYou  is handsome!"
# 通过\s匹配单个空白字符，即空格
# result = re.match(r"KeYou\s+is\shandsom", str3)

# if result:
#     print(result.group())
# else:
#     print("匹配不上")

vars_list = ["_lemon", "1lemon", "lemon-1", "lemon_1", "_1lemon", "__lemon"]

for i in vars_list:
    if re.match(r"[a-zA-Z_]+\w*$", i):
        print(f"{i}是合法变量")
    else:
        print(f"{i}不合法")

# 正则自带的字符串分割方法，分割后返回列表
str4 = "KeYou129love7646lemon2134little513girl"
list1 = re.split(r"\d+", str4)
print(' '.join(list1))
