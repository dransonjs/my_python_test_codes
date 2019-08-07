import pymysql
import random
from script.config_class import do_config


class HandleMysql:
    """
    mysql类
    """
    def __init__(self, end_num=None):
        if end_num is not None:
            self.conn = pymysql.connect(
                host=do_config('mysql', 'host'),
                port=do_config('mysql', 'port'),
                db=do_config('mysql', 'sms_db')+end_num,
                user=do_config('mysql', 'user'),
                password=do_config('mysql', 'password'),
                charset=do_config('mysql', 'charset'),
                cursorclass=pymysql.cursors.DictCursor,
            )
        else:
            self.conn = pymysql.connect(
                host=do_config('mysql', 'host'),
                port=do_config('mysql', 'port'),
                db=do_config('mysql', 'user_db'),
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

    @staticmethod
    def create_mobile():
        """
        随机生成11位手机号
        :return:
        """
        start_mobile = ('133', '149', '153', '173', '177', '180', '181', '189', '191', '199', '130', '131', '132',
                        '145', '155', '156', '166', '171', '175', '176', '185', '186', '134', '135', '136', '137',
                        '138', '139', '147', '150', '151', '152', '157', '158', '159', '172', '178', '182', '183',
                        '184', '187', '188', '198')
        start_num = random.choice(start_mobile)  # 参数为序列类型，从序列里随机选择出一个元素
        end_str = '0123456789'
        end_num = ''.join(random.sample(end_str, 8))
        return start_num + end_num

    def is_existed_mobile(self, mobile):
        """
        判断给定的手机号在数据库中是否存在
        :param mobile: 待判断的手机号
        :return: True、False
        """
        db_name = do_config('mysql', 'sms_db')+mobile[9:]
        form_name = "t_mvcode_info_"+mobile[8:9]
        sql = "SELECT * FROM {}.`{}` WHERE `Fmobile_no`={}".format(db_name, form_name, mobile)
        if self.sql_execute(sql):
            return True
        else:
            return False

    def create_not_existed_mobile(self):
        """
        创建一个不存在数据库的手机号码
        :return:
        """
        while True:
            one_mobile = self.create_mobile()
            if not self.is_existed_mobile(one_mobile):
                break
        return one_mobile

    @staticmethod
    def create_userid():
        userid = '剑圣'+str(random.randint(0, 1000))
        return userid

    def is_existed_userid(self, userid):
        sql = "SELECT * FROM `t_user_info` WHERE `Fuser_id`=%s"
        if self.sql_execute(sql, args=(userid, )):
            return True
        else:
            return False

    def create_not_existed_userid(self):
        while True:
            one_userid = self.create_userid()
            if not self.is_existed_userid(one_userid):
                break
        return one_userid

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    # sql1 = "SELECT * FROM `member` LIMIT 0, 10;"
    # sql2 = "SELECT * FROM `member` WHERE LeaveAmount > %s LIMIT 0, %s;"
    do_mysql = HandleMysql()
    # print(do_mysql.sql_execute(sql1, is_all=True))
    # print(do_mysql.sql_execute(sql2, args=(1000, 5), is_all=True)[3]['LeaveAmount'])
    print(do_mysql.create_not_existed_mobile())
