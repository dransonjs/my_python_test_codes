import unittest
import inspect
from Class_16_Homework.homework_0520.ddt import ddt, data  # 导入ddt，ddt和data必须同时导入
# 导入数学计算的测试类
from Class_16_Homework.homework_0520.math_cal import MathCalculate
# 导入Excel类
from Class_16_Homework.homework_0520.excel_class import HandleExcel
# 导入配置文件类
from Class_16_Homework.homework_0520.config_class import do_config
# 导入日志类
from Class_16_Homework.homework_0520.log_class import do_log

do_excel = HandleExcel(do_config('file path', 'cases_path'), 'divide')


@ddt  # 在类的上一行加
class TestDivide(unittest.TestCase):
    """
    测试除法类
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
        do_log.info("{:=^40s}".format("开始执行用例"))
        # print("{:=^40s}".format("开始执行用例"))
        # cls.file = open(cls.file_name, mode='a', encoding='utf8')
        # cls.file.write("{:=^40s}\n".format("开始执行用例"))

    @classmethod
    def tearDownClass(cls):
        do_log.info("{:=^40s}".format("用例执行结束"))
        # cls.file.write('{:=^40s}\n'.format('用例执行结束'))
        # cls.file.close()

    @data(*cases_list)  # 遍历用例
    def test_case(self, case_value):
        # print('\nRunning Test Method: {}'.format(inspect.stack()[0][3]))
        do_log.info('\nRunning Test Method: {}'.format(inspect.stack()[0][3]))
        # data_namedtuple = cases_list.pop(0)
        case_id = case_value.case_id
        msg = case_value.title
        l_data = case_value.l_data
        r_data = case_value.r_data
        expect_result = case_value.expect_result
        actual_result = MathCalculate(l_data, r_data).divide()
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
