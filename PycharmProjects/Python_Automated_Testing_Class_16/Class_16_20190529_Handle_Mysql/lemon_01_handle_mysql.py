import pymysql

# 1、建立连接
conn = pymysql.connect(
    host="test.lemonban.com",
    user='test',
    password='test',
    db='future',
    port=3306,
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

# 2、创建游标
cursor = conn.cursor()

# 3、执行sql语句
# sql = "SELECT * FROM `member` LIMIT 0, 10;"
sql1 = "SELECT * FROM `member` WHERE LeaveAmount > %s LIMIT 0, 10;"
cursor.execute(sql1, args=(400, ))
# 需要手动提交
conn.commit()

# 获取执行sql语句的结果
# result1 = cursor.fetchone()  # 返回所有记录中第一条记录组成的字典
result2 = cursor.fetchall()  # 返回所有记录组成的嵌套字典的列表

# 4、关闭连接
cursor.close()  # 先关游标对象
conn.close()  # 再关连接对象
