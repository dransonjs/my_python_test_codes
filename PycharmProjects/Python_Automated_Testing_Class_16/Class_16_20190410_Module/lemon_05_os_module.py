import os

# 操作系统名称
print(os.name)

# 当前路径
print(os.getcwd())

# 系统环境变量
print(os.environ)

# 创建文件夹
# os.mkdir('test1')

# 创建多个嵌套文件夹
# os.makedirs('/Users/admin\PycharmProjects/untitled/test1/test2')

# 删除目录
# os.rmdir('/Users/admin/PycharmProjects/untitled/Class_16_20190410_Module/test1')

# 删除多个目录
# os.removedirs('/Users/admin/PycharmProjects/untitled/test1/test2')

# 列出制定路径下的目录结构
print(os.listdir('/Users/admin/PycharmProjects/untitled'))

# 返回路径的文件名
print(os.path.basename('/Users/admin/PycharmProjects/untitled/Class_16_20190410_Module/lemon_05_os_module.py'))

# 返回文件的路径
print(os.path.dirname('/Users/admin/PycharmProjects/untitled/Class_16_20190410_Module/lemon_05_os_module.py'))

# 文件路径是否存在
print(os.path.exists('/Users/admin/PycharmProjects/untitled/Class_16_20190410_Module/lemon_05_os_module.py'))

# 路径是否是目录
print(os.path.isdir('/Users/admin/PycharmProjects/untitled/Class_16_20190410_Module/lemon_05_os_module.py'))

# 路径是否是文件
print(os.path.isfile('/Users/admin/PycharmProjects/untitled/Class_16_20190410_Module/lemon_05_os_module.py'))

# 拼接路径
print(os.path.join('\\Users\\admin\PycharmProjects\\untitled\Class_16_20190410_Module', 'lemon_05_os_module.py'))

# 分开目录和文件
print(os.path.split('/Users/admin/PycharmProjects/untitled/Class_16_20190410_Module/lemon_05_os_module.py'))