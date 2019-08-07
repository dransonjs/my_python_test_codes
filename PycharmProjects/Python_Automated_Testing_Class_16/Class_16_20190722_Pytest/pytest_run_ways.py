# 指定测试模块：pytest test_mod.py

# 指定测试目录：pytest testing/

# 通过节点id来运行测试：
# 节点id的组成：pytest 模块名::类名::函数名 或者 pytest 模块名::函数名
# 示例：pytest test_xxx.py::TestXxx::test_xxx

# 通过关键字逻辑运算过滤运行测试：会匹配文件名、类名、方法名逻辑运算的用例
# 示例：pytest -k "类名 and not 方法名"

# 获取用例执行性能数据
# 获取最慢的3个用例的执行耗时
# pytest --durations=3
