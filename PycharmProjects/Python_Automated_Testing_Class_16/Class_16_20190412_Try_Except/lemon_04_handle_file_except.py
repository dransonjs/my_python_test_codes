# 假如文件不存在，无法打开，也就不需要关闭，所以close不能写在finally
# 假如文件存在正常打开，但是后续出异常，该怎么规划代码
try:
    file_1 = open('my_file.txt')
    line_1 = file_1.readline()
    data = int(line_1.strip())
except OSError as err:
    print('Os error: {}'.format(err))
except ValueError:
    print('Value error')
except Exception as e:
    print(e)
else:
    file_1.close()
finally:
    pass

print('继续往下执行')