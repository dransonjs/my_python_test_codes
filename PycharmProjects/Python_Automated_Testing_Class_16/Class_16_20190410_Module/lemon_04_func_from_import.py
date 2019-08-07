# 只需要导入模块里指定的函数、变量，可分别为指定的函数或变量取别名

from Class_16_20190410_Module.lemon_01_define_more_function import (
    square as sq,
    name as n
)

print(sq(10))
print(n)