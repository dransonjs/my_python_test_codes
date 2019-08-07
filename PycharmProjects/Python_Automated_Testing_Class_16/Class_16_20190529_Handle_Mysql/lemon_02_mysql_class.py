import pymysql
from Class_16_20190529_Handle_Mysql.config_class import do_config


class HandleMysql:
    """
    mysql类
    """
    def __init__(self):
        self.conn = pymysql.connect(
            host=do_config('mysql', 'host'),
            port=do_config('mysql', 'port'),
            db=do_config('mysql', 'db'),
            user=do_config('mysql', 'user'),
            password=do_config('mysql', 'password'),
            charset=do_config('mysql', 'charset'),
            cursorclass=pymysql.cursors.DictCursor,
        )
        self.cursor = self.conn.cursor()

    # 这里也可以用__call__定义执行sql语句方法
    # def__call__(self, sql, args=None, is_all=False)
    def sql_execute(self, sql, args=None, is_all=False):
        """
        执行sql语句
        :param sql: sql语句，字符类型
        :param args: sql语句的参数，序列类型
        :param is_all:
        :return:
        """
        self.cursor.execute(sql, args)
        self.conn.commit()
        if is_all:
            result = self.cursor.fetchall()
        else:
            result = self.cursor.fetchone()
        return result

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    sql1 = "SELECT * FROM `member` LIMIT 0, 10;"
    sql2 = "SELECT * FROM `member` WHERE LeaveAmount > %s LIMIT 0, %s;"
    do_mysql = HandleMysql()
    print(do_mysql.sql_execute(sql1, is_all=True))
    print(do_mysql.sql_execute(sql2, args=(1000, 5), is_all=True)[3]['LeaveAmount'])
