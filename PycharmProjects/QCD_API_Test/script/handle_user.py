from script.mysql_class import HandleMysql
from script.http_request_class import HttpRequest
from script.config_class import do_config
from script.constant import USER_FILE_PATH


def create_new_user(regname, pwd="123456"):
    """
    创建一个用户
    :param regname:
    :param pwd:
    :return:
    """
    do_request = HttpRequest()
    do_mysql = HandleMysql()
    url = do_config("api", "prefix_url") + "/member/register"
    sql = "SELECT * FROM future.`member` WHERE `MobilePhone`=%s;"
    while True:
        mobilephone = do_mysql.create_not_existed_mobile()
        data = {"mobilephone": mobilephone, "pwd": pwd, "regname": regname}
        do_request(method="post", url=url, params=data)
        result = do_mysql.sql_execute(sql=sql, args=(mobilephone, ))
        if result:
            user_id = result['Id']
            break

    user_dict = {
        regname: {
            "Id": user_id,
            "regname": regname,
            "mobilephone": mobilephone,
            "pwd": pwd
        }
    }
    do_request.close()
    do_mysql.close()

    return user_dict


def generate_user_config():
    """
    生成三个用户信息
    :return:
    """
    user_datas_dict = {}
    user_datas_dict.update(create_new_user("admin_user"))
    user_datas_dict.update(create_new_user("invest_user"))
    user_datas_dict.update(create_new_user("borrow_user"))
    do_config.write_config(user_datas_dict, USER_FILE_PATH)


if __name__ == '__main__':
    # print(generate_user_config())
    # do_config.write_config(generate_user_config(), 'user.conf')
    generate_user_config()