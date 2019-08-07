import logging  # 是python系统自带的
from logging.handlers import RotatingFileHandler
import time

# 默认有一个root根收集器，使用的日志等级为warning
# logging.debug('这是debug日志')
# logging.info('这是info日志')
# logging.warning('这是warning日志')
# logging.error('这是error日志')
# logging.critical('这是critical日志')

# 定义日志收集器，返回logger对象
case_logger = logging.getLogger('case')  # 如果不传name参数，默认使用root根收集器

# 指定日志收集器的日志等级，往往设置比较低
case_logger.setLevel(logging.DEBUG)

# 定义日志输出渠道，可以指定多个渠道
# 输出到console控制台
console_handle = logging.StreamHandler()

# 输出到文件中
# file_handle = logging.FileHandler('cases.log', encoding='utf8')
file_handle = RotatingFileHandler('cases.log', maxBytes=1024, backupCount=3, encoding='utf8')

# 指定日志输出渠道的日志等级
console_handle.setLevel("ERROR",)  # 如果不能被日志收集器收集的日志，一定不能输出到渠道中
file_handle.setLevel(logging.INFO)

# 定义日志显示的格式
# 简单日志格式
simple_formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - [日志信息]:%(message)s')

# 复杂日志格式
verbose_formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(module)s - '
                                      '%(name)s - %(lineno)d - [日志信息]:%(message)s')

# 设置终端的日志为简单格式
console_handle.setFormatter(simple_formatter)

# 设置文件的日志为复杂格式
file_handle.setFormatter(verbose_formatter)

# 将日志收集器与输出渠道进行对接
case_logger.addHandler(console_handle)
case_logger.addHandler(file_handle)

if __name__ == '__main__':
    for _ in range(100):
        time.sleep(0.3)
        case_logger.debug('这是debug日志')
        case_logger.info('这是info日志')
        case_logger.warning('这是warning日志')
        case_logger.error('这是error日志')
        case_logger.critical('这是critical日志')
