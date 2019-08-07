import unittest
import os
from datetime import datetime
import HTMLTestRunnerNew
from file_path import ROOT_PATH, REPORT_PATH


suite = unittest.defaultTestLoader.discover(ROOT_PATH)

report_path = os.path.join(REPORT_PATH, 'test_report')
report_path_full = report_path+'_'+datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")+".html"

with open(report_path_full, mode="wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title="前程贷登录+投标测试报告",
                                              verbosity=2,
                                              description="前程贷测试用例执行结果",
                                              tester="dranson")
    runner.run(suite)
