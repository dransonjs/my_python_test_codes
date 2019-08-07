# pytest的测试用例可以脱离类
import sys

import pytest


def add(a, b):
    return a+b


def minus(a, b):
    return a-b


def mutiple(a, b):
    return a*b


def divide(a, b):
    return a/b


# pytest用例执行顺序是从上往下，不是unittest的按照ASCII码顺序
# pytest断言简洁智能，只有assert一个关键字
# 断言格式：assert 表达式, '自定义错误提示'
def test_1_add():
    assert add(3, 4) == 7, '加法测试不通过'


# pytest标签功能：一个测试用例可以带多个标签，可以在pytest.ini配置文件自定义标签，可以放在类或方法上
# 运行标签：pytest -m "标签名（支持逻辑运算or/and/not）"
# 标签第一种运行方法，在命令行(Terminal)运行下面命令
# pytest -m "success and fail" (只能用双引号)

# 类标签第一种设置方法
@pytest.mark.smoke
@pytest.mark.fail
class TestMinus:
    # 类标签第二种设置方法
    # pytestmark = [pytest.mark.smoke, pytest.mark.fail]

    def test_4_minus(self):
        assert minus(1, 2) == 1, '减法测试不通过'

    @pytest.mark.fail
    @pytest.mark.skipif(sys.platform == "linux", reason='系统不支持')
    def test_2_divide(self):
        assert divide(3, 5) == 0.6, '除法测试不通过'


@pytest.mark.fail
@pytest.mark.success
@pytest.mark.skip('不想执行这条用例')
def test_3_multiple():
    assert mutiple(2, 3) == 6, '乘法测试不通过'


# 标签第二种运行方法 pytest.main(['-m "success and fail"'])
if __name__ == '__main__':
    # --resultlog和--junitxml是比较简陋的测试报告
    # --html是相对比较能看的测试报告
    pytest.main(['--resultlog=report/test.txt',
                 '--junitxml=report/test.xml',
                 '--html=report/test.html'])
