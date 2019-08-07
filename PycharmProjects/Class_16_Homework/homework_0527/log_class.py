import logging
from logging.handlers import RotatingFileHandler
import time

from Class_16_Homework.homework_0520.config_class import do_config

# 指定日志收集器名字
# 指定日志收集器的日志等级
# 指定日志输出渠道
# 指定日志输出渠道的日志等级
# 指定日志显示格式


class LogHandle:
    """
    日志器类
    """
    def __init__(self):
        self.case_logger = logging.getLogger(do_config('log', 'logger_name'))

        self.case_logger.setLevel(do_config('log', 'logger_level'))

        console_output = logging.StreamHandler()
        file_output = RotatingFileHandler(filename=do_config('log', 'logger_name'),
                                          maxBytes=do_config('log', 'maxBytes'),
                                          backupCount=do_config('log', 'backupCount'),
                                          encoding='utf8')

        console_output.setLevel(do_config('log', 'console_level'))
        file_output.setLevel(do_config('log', 'file_level'))

        simple_formatter = logging.Formatter(do_config('log', 'simple_formatter'))
        verbose_formatter = logging.Formatter(do_config('log', 'verbose_formatter'))

        console_output.setFormatter(simple_formatter)
        file_output.setFormatter(verbose_formatter)

        self.case_logger.addHandler(console_output)
        self.case_logger.addHandler(file_output)

    def get_logger(self):
        """
        获取logger日志器对象
        :return:
        """
        return self.case_logger


do_log = LogHandle().get_logger()

if __name__ == '__main__':
    case_logger = LogHandle().get_logger()
    for _ in range(100):
        time.sleep(0.3)
        case_logger.debug('这是debug日志')
        case_logger.info('这是info日志')
        case_logger.warning('这是warning日志')
        case_logger.error('这是error日志')
        case_logger.critical('这是critical日志')
