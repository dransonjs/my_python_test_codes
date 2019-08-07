# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2019/5/15 22:37 
  @Auth : 可优
  @File : lemon_05_parser_config_5.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""
from configparser import ConfigParser


class HandleConfig:

    def __init__(self):
        self.filename = "testcase.conf"
        self.config = ConfigParser()
        self.config.read(self.filename, encoding='utf-8')

    def get_value(self, section, option):
        """
        获取选项值
        :param section: 区域名
        :param option: 选项名
        :return:
        """
        return self.config.get(section, option)

    def get_int(self, section, option):
        """
        将获取的选项值转化为int类型
        :param section: 区域名
        :param option: 选项名
        :return:
        """
        return self.config.getint(section, option)

    def get_float(self, section, option):
        """
        将获取的选项值转化为float类型
        :param section: 区域名
        :param option: 选项名
        :return:
        """
        return self.config.getfloat(section, option)

    def get_boolean(self, section, option):
        """
        将获取的选项值转化为bool类型
        :param section: 区域名
        :param option: 选项名
        :return:
        """
        return self.config.getboolean(section, option)


if __name__ == '__main__':
    res = HandleConfig().get_boolean("excel", "two_res")
    print(res)
