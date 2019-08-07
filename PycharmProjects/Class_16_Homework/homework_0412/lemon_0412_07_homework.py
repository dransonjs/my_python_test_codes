# 有两行数据，存放在txt文件里面：

# url:http://test.lemonban.com/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
# url:http://test.lemonban.com/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000

# 请利用上课所学知识，把txt里面的两行内容，取出然后返回如下格式的数据：（可定义函数）

# [{'url':'http://test.lemonban.com/futureloan/mvc/api/member/register','mobile':'18866668888','pwd':'123456'},
# {'url':'http://test.lemonban.com/futureloan/mvc/api/member/recharge','mobile':'18866668888','amount':'1000'}]

lemon_msg = open('lemon_msg.txt', mode='w', encoding='utf8')

lemon_msg.write('url:http://test.lemonban.com/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456\n')
lemon_msg.write('url:http://test.lemonban.com/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000')

lemon_msg.close()

lemon_msg = open('lemon_msg.txt', mode='r', encoding='utf8')

lemon_list = lemon_msg.readlines()  # 用一个变量存放文件读取的内容列表

d = []  # 定义空列表，用来返回最终结果

for i in lemon_list:  # 对文件读取的每一行内容循环
    a = i.strip('\n').split('@', 2)  # 对列表lemon_list的元素去除换行符，且用@进行分割，返回3个元素为字符串的列表
    c = []  # 定义空列表，用来存放下方循环append后的列表
    for j in a:  # 对上面处理过的3个元素为字符串的列表a循环
        b = j.split(':', 1)  # 对列表a的元素j用:进行分割，返回2个元素为字符串的列表
        c.append(b)  # 把列表b当成元素放入列表c
    d.append(dict(c))  # 内层循环结束后，把列表c转换为字典，再把字典当成元素存放到列表d

print(d)

lemon_msg.close()