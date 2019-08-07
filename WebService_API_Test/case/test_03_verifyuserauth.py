import unittest
import inspect
import os
from lib.ddt import ddt, data  # 导入ddt，ddt和data必须同时导入
# 导入http请求类
# 尽量选择导入类，而不是直接导入对象，因为导入同一个对象（同一个绘画）来测试不同的接口这种做法不太标准
from script.webservice_class import Webservice
# 导入Excel类
from script.excel_class import HandleExcel
# 导入配置文件类
from script.config_class import do_config, do_config2
# 导入日志类
from script.log_class import do_log

from script.constant import DATA_FILE_PATH

from script.handle_context import Context

from script.mysql_class import HandleMysql

from script.constant import CONFIG_USER_FILE_PATH2

do_excel = HandleExcel(DATA_FILE_PATH, 'verifyuserauth')


@ddt  # 在类的上一行加
class TestVerifyUserAuth(unittest.TestCase):
    """
    测试实名认证功能
    """
    cases_list = do_excel.get_cases()

    @classmethod
    def setUpClass(cls):
        """
        重写父类的类方法，全部实例方法（用例）执行完只会被调用1次
        :return:
        """
        # cls.file_name = 'test_result.txt'
        # cls.file_name = do_config('file path', 'log_path')
        # print('打开【{}】文件'.format(cls.file_name))
        cls.do_mysql = HandleMysql()
        end_num = str(do_config2('user_info', 'mobile'))[9:]
        cls.do_mysql1 = HandleMysql(end_num=end_num)
        do_log.info("{:=^40s}".format("开始执行用例"))
        # print("{:=^40s}".format("开始执行用例"))
        # cls.file = open(cls.file_name, mode='a', encoding='utf8')
        # cls.file.write("{:=^40s}\n".format("开始执行用例"))

    @classmethod
    def tearDownClass(cls):

        form_name = 't_mvcode_info_'+str(do_config2('user_info', 'mobile'))[8:9]
        sql = "DELETE FROM {} WHERE Fmobile_no={}".format(form_name, do_config2('user_info', 'mobile'))
        cls.do_mysql1.sql_execute(sql)
        cls.do_mysql1.close()

        sql = "DELETE FROM `t_user_info` WHERE Fuser_id=%s"
        cls.do_mysql.sql_execute(sql, args=(do_config2("user_info", "user_id")))
        cls.do_mysql.close()
        do_log.info("{:=^40s}".format("用例执行结束"))
        # cls.file.write('{:=^40s}\n'.format('用例执行结束'))
        # cls.file.close()

    @data(*cases_list)  # 遍历用例
    def test_case(self, case_value):
        # print('\nRunning Test Method: {}'.format(inspect.stack()[0][3]))
        do_log.info('\nRunning Test Method: {}'.format(inspect.stack()[0][3]))
        # data_namedtuple = cases_list.pop(0)
        case_id = case_value.case_id
        setattr(Context, 'case_id', 1)
        msg = case_value.title
        url = case_value.url
        data3 = Context.user_verify_parameterization(case_value.data)
        method = case_value.method
        expect_result = case_value.expected
        actual_result = str(Webservice(url, data3, method).result_output())
        if case_id == 1:
            user_data = {'user_auth': data3}
            do_config.write_config(user_data, "user_data2.ini")
        if case_id == 2:
            sql = "DELETE f1,f2 FROM `t_user_info` AS f1 LEFT JOIN `t_user_auth_info` AS f2 ON f1.Fuid=f2.Fuid WHERE f2.Fuid=%s"
            self.do_mysql.sql_execute(sql, args=(do_config2("user_auth", "uid")))

        if case_id == do_excel.ws.max_row-1:
            os.remove(CONFIG_USER_FILE_PATH2)
        # try:
        #     self.assertEqual(200,
        #                      actual_result.status_code,
        #                      msg='测试{}时，请求失败！状态码为{}'.format(case_value.title, actual_result.status_code))
        # except AssertionError as e:
        #     do_log.error('具体异常为：{}'.format(e))
        #     raise e
        # 将实际结果写入excel
        # ws.cell(row=case_id + 1, column=6, value=actual_result)
        try:
            self.assertEqual(actual_result, expect_result, msg='测试{}失败'.format(msg))
        except AssertionError as e:
            # print('具体异常为：{}'.format(e))
            do_log.error('具体异常为：{}'.format(e))
            # self.file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, 'Fail', e))
            # self.file.write('{}，执行结果：{}，具体异常为：{}\n'.format(msg, do_config('msg', 'fail_result'), e))
            # ws.cell(row=case_id + 1, column=7, value='Fail')
            # self.handle_excel.write_result(case_id + 1, actual_result, 'Fail')
            do_excel.write_result(case_id + 1, actual_result, do_config('msg', 'fail_result'))
            raise e
        else:
            # self.file.write('{}，执行结果：{}\n'.format(msg, 'Pass'))
            # self.file.write('{}，执行结果：{}\n'.format(msg, do_config('msg', 'success_result')))
            # ws.cell(row=case_id + 1, column=7, value='Pass')
            # self.handle_excel.write_result(case_id + 1, actual_result, 'Pass')
            do_excel.write_result(case_id + 1, actual_result, do_config('msg', 'success_result'))


if __name__ == '__main__':
    unittest.main()
