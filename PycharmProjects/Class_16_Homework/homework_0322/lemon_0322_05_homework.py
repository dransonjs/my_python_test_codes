# 删除如下列表中的"矮穷丑"

keyou_info = ["可优", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "Always Be Coding"]

# 指定索引删除
# del keyou_info[3]
# print(keyou_info)

# 指定元素删除
# keyou_info.remove('矮穷丑')
# print(keyou_info)

# 默认删除最后一个，若有指定索引，则删除索引对应的元素
keyou_info.pop(3)
print(keyou_info)

