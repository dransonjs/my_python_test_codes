"""
优化去生鲜超市买橘子程序

a.收银员输入橘子的价格，单位：元／斤

b.收银员输入用户购买橘子的重量，单位：斤

c.计算并且 输出 付款金额

新需求：

d.使用捕获异常的方式，来处理用户输入无效数据的情况
"""

while True:
    try:
        unit_price = abs(float(input('输入橘子单价（元/斤）：')))
        weight = abs(float(input('输入购买橘子重量（斤）：')))
    except ValueError:
        print('请输入数字')
    else:
        print('付款金额为：{}元'.format(unit_price * weight))
        break
    finally:
        pass
