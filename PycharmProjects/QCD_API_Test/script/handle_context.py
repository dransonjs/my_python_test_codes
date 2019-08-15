import re
import os
from script.mysql_class import HandleMysql
from script.config_class import HandleConfig
from script.constant import CONFIG_DIR


class Context:
    """
    实现用例数据参数化
    """
    not_existed_tel_pattern = re.compile(r'\$\{not_existed_tel\}')
    existed_tel_pattern = re.compile(r'\$\{existed_tel\}')
    invest_user_tel_pattern = re.compile(r'\$\{invest_user_tel\}')
    invest_user_pwd_pattern = re.compile(r'\$\{invest_user_pwd\}')
    invest_user_id_pattern = re.compile(r'\$\{invest_user_id\}')
    admin_user_tel_pattern = re.compile(r'\$\{admin_user_tel\}')
    admin_user_pwd_pattern = re.compile(r'\$\{admin_user_pwd\}')
    borrow_user_id_pattern = re.compile(r'\$\{borrow_user_id\}')
    not_existed_id_pattern = re.compile(r'\$\{not_existed_memberId\}')
    loan_id_pattern = re.compile(r'\$\{loan_id\}')

    user_config = HandleConfig(os.path.join(CONFIG_DIR, 'user.conf'))

    @classmethod
    def not_existed_tel_replace(cls, data):
        """
        替换未注册的手机号
        :param data: 要替换的目标完整字符串
        :return:
        """
        if re.search(cls.not_existed_tel_pattern, data):
            do_mysql = HandleMysql()
            # if re.search(self.not_existed_tel_pattern, data):
            #     not_existed_tel = do_mysql.create_mobile()
            #     data = re.sub(self.not_existed_tel_pattern, not_existed_tel, data)
            not_existed_tel = do_mysql.create_mobile()
            data = re.sub(cls.not_existed_tel_pattern, not_existed_tel, data)

            do_mysql.close()
        return data

    @classmethod
    def existed_tel_replace(cls, data):
        """
        替换已注册的手机号
        :param data: 要替换的目标完整字符串
        :return:
        """
        if re.search(cls.existed_tel_pattern, data):
            do_mysql = HandleMysql()
            sql = "SELECT MobilePhone FROM `member` LIMIT 0,1"
            result = do_mysql.sql_execute(sql)
            data = re.sub(cls.existed_tel_pattern, result['MobilePhone'], data)

            do_mysql.close()
        return data

    @classmethod
    def register_parameterization(cls, data):
        """
        实现注册功能的参数化
        :param data:
        :return:
        """
        # 先替换未注册的手机号
        data = cls.not_existed_tel_replace(data)
        # 再替换已经注册的手机号
        data = cls.existed_tel_replace(data)
        return data

    @classmethod
    def invest_user_tel_replace(cls, data):
        """
        替换投资人手机号、密码
        :param data:
        :return:
        """
        if re.search(cls.invest_user_tel_pattern, data):
            data = re.sub(cls.invest_user_tel_pattern, str(cls.user_config('invest_user', 'mobilephone')), data)
            data = re.sub(cls.invest_user_pwd_pattern, str(cls.user_config('invest_user', 'pwd')), data)
        return data

    @classmethod
    def login_parameterization(cls, data):
        """
        实现登录、充值功能参数化
        :param data:
        :return:
        """
        data = cls.invest_user_tel_replace(data)

        data = cls.not_existed_tel_replace(data)

        return data

    @classmethod
    def admin_user_tel_replace(cls, data):
        if re.search(cls.admin_user_tel_pattern, data):
            data = re.sub(cls.admin_user_tel_pattern, str(cls.user_config('admin_user', 'mobilephone')), data)
            data = re.sub(cls.admin_user_pwd_pattern, str(cls.user_config('admin_user', 'pwd')), data)
        return data

    @classmethod
    def borrow_user_id_replace(cls, data):
        if re.search(cls.borrow_user_id_pattern, data):
            data = re.sub(cls.borrow_user_id_pattern, str(cls.user_config('borrow_user', 'id')), data)
        return data

    @classmethod
    def not_existed_id_replace(cls, data):
        if re.search(cls.not_existed_id_pattern, data):
            do_mysql = HandleMysql()
            sql = "SELECT MAX(Id) FROM `member`"
            result = do_mysql.sql_execute(sql)
            data = re.sub(cls.not_existed_id_pattern, str(result['MAX(Id)']+1), data)
            do_mysql.close()
        return data

    @classmethod
    def add_parameterization(cls, data):
        """
        实现加标功能参数化
        :param data:
        :return:
        """
        data = cls.admin_user_tel_replace(data)

        data = cls.borrow_user_id_replace(data)

        data = cls.not_existed_id_replace(data)

        return data

    @classmethod
    def invest_user_id_replace(cls, data):
        if re.search(cls.invest_user_id_pattern, data):
            data = re.sub(cls.invest_user_id_pattern, str(cls.user_config('invest_user', 'id')), data)
            data = re.sub(cls.invest_user_pwd_pattern, str(cls.user_config('invest_user', 'pwd')), data)
        return data

    @classmethod
    def loan_id_replace(cls, data):
        if re.search(cls.loan_id_pattern, data):
            loan_id = getattr(cls, 'loan_id')
            data = re.sub(cls.loan_id_pattern, str(loan_id), data)
        return data

    @classmethod
    def invest_parameterization(cls, data):
        """
        实现投资竞标功能参数化
        :param data:
        :return:
        """
        data = cls.admin_user_tel_replace(data)

        data = cls.borrow_user_id_replace(data)

        data = cls.loan_id_replace(data)

        data = cls.invest_user_id_replace(data)

        return data


if __name__ == '__main__':
    str2 = '{"memberId":${borrow_user_id},"title":"贷款5万","amount":50000,"loanRate":3.73,"loanTerm":12,"loanDateType":0,"repaymentWay":5,"biddingDays":5}'
    print(Context.add_parameterization(str2))
    str3 = '{"memberId":${not_existed_memberId},"title":"贷款5万","amount":50000,"loanRate":3.73,"loanTerm":12,"loanDateType":0,"repaymentWay":5,"biddingDays":5}'
    print(Context.add_parameterization(str3))
