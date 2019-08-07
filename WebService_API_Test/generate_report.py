# import unittest
import os
from datetime import datetime
# 美化报告
# from HtmlTestRunner import HTMLTestRunner

# 进一步美化报告，解决中文乱码问题
import HTMLTestRunnerNew

from script.constant import REPORT_DIR, CASE_DIR

# 方法一、二：
# from Class_16_Homework.homework_0429.lemon_0426_03_homework_3 import TestMinus, TestDivide

# 方法三、四：
# from case import test_01_register as module1
# from case import test_02_login as module2
# from case import test_03_recharge as module3

# 导入配置文件类
from script.config_class import do_config

# 创建一个测试套件对象
# suite = unittest.TestSuite()

# 加载用例
# 方法一：通过测试对象来加载用例，将实例方法（一条用例）名作为测试类的参数，只能添加测试类的实例（对象）
# suite.addTest(TestMinus('test_negatives'))
# suite.addTest(TestDivide('test_positives'))
# one_tuple = (TestMinus('test_negatives'), TestDivide('test_positives'))
# suite.addTests(one_tuple)  # 将多条用例同时加载进套件中

# 方法二：通过测试类来批量加载测试用例
# 创建一个加载器对象
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestMinus))
# suite.addTest(loader.loadTestsFromTestCase(TestDivide))

# 方法三：通过模块来批量加载测试用例
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(module1))

# 方法四：在创建测试套件同时，加载所有测试模块
# loader = unittest.TestLoader()
# test_modules_tuple = (loader.loadTestsFromModule(module1),
#                       loader.loadTestsFromModule(module2),
#                       loader.loadTestsFromModule(module3))
# 创建测试套件
# suite = unittest.TestSuite(tests=test_modules_tuple)

# 优化上面的加载模块方法，不用每加一个测试用例类后又要写多一次测试模块
suite = unittest.defaultTestLoader.discover(CASE_DIR)

# 执行用例
# 打开文件
# file = open('test_result_3.txt', mode='w', encoding='utf8')
# 创建一个运行器对象，将测试结果存放到文件中
# runner = unittest.TextTestRunner(stream=file, descriptions='测试报告', verbosity=2)
# runner.run(suite)
# 关闭文件
# file.close()

# 上下文管理器，无需关闭文件
# with open('test_result_3.txt', mode='w', encoding='utf8') as file:
#     runner = unittest.TextTestRunner(stream=file, descriptions='测试报告', verbosity=2)
#     runner.run(suite)

# 美化报告
# runner = HTMLTestRunner(output='report', report_name='测试报告', report_title='测试报告标题', combine_reports=True)
# runner.run(suite)

# 进一步美化报告
report_path = os.path.join(REPORT_DIR, do_config('report', 'report_path'))
report_path_full = report_path + '_' + datetime.strftime(datetime.now(), '%Y%m%d%H%M%S') + '.html'
with open(report_path_full, mode='wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title=do_config('report', 'title'),
                                              verbosity=do_config('report', 'verbosity'),
                                              description=do_config('report', 'description'),
                                              tester=do_config('report', 'tester'))
    runner.run(suite)

# 执行结果中，一个"."代表执行成功一条用例，一个"F"代表执行失败一条用例
