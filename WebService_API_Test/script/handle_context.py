import re
from script.webservice_class import Webservice
from script.mysql_class import HandleMysql
from script.config_class import do_config1, do_config2


class Context:
    """
    实现用例手机号参数化
    """
    not_existed_tel_pattern = re.compile(r'\$\{not_existed_tel\}')
    existed_tel_pattern = re.compile(r'\$\{existed_tel\}')
    mobile_pattern = re.compile(r"\$\{mobile\}")
    verify_code_pattern = re.compile(r"\$\{verify_code\}")
    uid_pattern = re.compile(r"\$\{uid\}")
    not_existed_userid_pattern = re.compile(r'\$\{not_existed_userid\}')
    existed_userid_pattern = re.compile(r'\$\{existed_userid\}')
    used_creid_pattern = re.compile(r"\$\{used_creid\}")
    not_used_creid_pattern = re.compile(r"\$\{not_used_creid\}")
    wrong_verify_code_pattern = re.compile(r"\$\{wrong_verify_code\}")

    @classmethod
    def mobile_replace(cls, data):
        if re.search(cls.mobile_pattern, data):
            do_mysql = HandleMysql()
            mobile = do_mysql.create_mobile()
            data = re.sub(cls.mobile_pattern, mobile, data)
            do_mysql.close()
        return data

    @classmethod
    def verify_code_replace(cls, data):
        if re.search(cls.verify_code_pattern, data):
            mobile = eval(data)['mobile']
            params = {"client_ip": "182.46.25.1", "mobile": mobile, "tmpl_id": "1"}
            Webservice('http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl', params, 'sendMCode')
            end_num = mobile[9:]
            do_mysql = HandleMysql(end_num=end_num)
            form_name = "t_mvcode_info_"+mobile[8:9]
            # sql = "SELECT * FROM `%s` WHERE Fmobile_no=%s"
            sql = "SELECT * FROM `{}` WHERE Fmobile_no={}".format(form_name, mobile)
            # result = do_mysql.sql_execute(sql, args=(form_name, mobile))
            result = do_mysql.sql_execute(sql)
            verify_code = result['Fverify_code']
            data = re.sub(cls.verify_code_pattern, verify_code, data)
        return data

    @classmethod
    def wrong_verify_code_replace(cls, data):
        if re.search(cls.wrong_verify_code_pattern, data):
            data = re.sub(cls.wrong_verify_code_pattern, do_config1('user_info', 'verify_code'), data)
        return data

    @classmethod
    def uid_replace(cls, data):
        if re.search(cls.uid_pattern, data):
            do_mysql = HandleMysql()
            sql = "SELECT * FROM `t_user_info` WHERE Fuser_id=%s"
            result = do_mysql.sql_execute(sql, args=(do_config2("user_info", "user_id"), ))
            if result is None:
                uid = str(do_config2("user_auth", "uid"))
            else:
                uid = str(result["Fuid"])
            data = re.sub(cls.uid_pattern, uid, data)
            data = eval(data)
            data.get('uid', int(uid))
            data = str(data)
        return data

    @classmethod
    def not_existed_tel_replace(cls, data):
        """
        替换未注册的手机号
        :param data: 要替换的目标完整字符串
        :return:
        """
        if re.search(cls.not_existed_tel_pattern, data):
            do_mysql = HandleMysql()
            not_existed_tel = do_mysql.create_not_existed_mobile()
            data = re.sub(cls.not_existed_tel_pattern, not_existed_tel, data)
            do_mysql.close()
        return data

    @classmethod
    def not_existed_userid_replace(cls, data):
        if re.search(cls.not_existed_userid_pattern, data):
            do_mysql = HandleMysql()
            not_existed_userid = do_mysql.create_not_existed_userid()
            data = re.sub(cls.not_existed_userid_pattern, not_existed_userid, data)
            do_mysql.close()
        return data

    @classmethod
    def existed_userid_replace(cls, data):
        if re.search(cls.existed_userid_pattern, data):
            data = re.sub(cls.not_existed_userid_pattern, do_config1('user_info', 'user_id'), data)
        return data

    @classmethod
    def existed_tel_replace(cls, data):
        """
        替换已注册的手机号
        :param data: 要替换的目标完整字符串
        :return:
        """
        if re.search(cls.existed_tel_pattern, data):
            data = re.sub(cls.existed_tel_pattern, str(do_config1("user_info", "mobile")), data)
        return data

    @classmethod
    def creid_replace(cls, data):
        """
        替换身份证号
        :param data:
        :return:
        """
        if re.search(cls.not_used_creid_pattern, data):
            data = re.sub(cls.not_used_creid_pattern, str(do_config2("user_auth", "cre_id")), data)
        if re.search(cls.used_creid_pattern, data):
            data = re.sub(cls.used_creid_pattern, str(do_config2("user_auth", "cre_id")), data)
        return data

    @classmethod
    def register_parameterization(cls, data):
        """
        实现注册功能的参数化
        :param data:
        :return:
        """
        data = cls.not_existed_tel_replace(data)
        data = cls.existed_tel_replace(data)
        data = cls.not_existed_userid_replace(data)
        data = cls.verify_code_replace(data)
        return eval(data)

    @classmethod
    def user_verify_parameterization(cls, data):
        """
        实现实名认证功能参数化
        :param data:
        :return:
        """
        data = cls.uid_replace(data)
        data = cls.creid_replace(data)
        return eval(data)


if __name__ == '__main__':
    do_context = Context()
    # str1 = '{"client_ip": "182.46.25.1", "mobile": "${mobile}", "tmpl_id": "1"}'
    # print(do_context.mobile_replace(str1))
    # str2 = '{"channel_id": "1", "ip": "182.46.25.1", "mobile": "13711223344", "pwd": "123123", ' \
    #        '"user_id": "剑圣", "verify_code": "${verify_code}"}'
    # print(do_context.verify_code_replace(str2))
