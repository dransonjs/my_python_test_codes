# 不传参则将默认区域返回
# 通过区域名以及选项名来获取选项值
# 只传区域名，获取此区域下的所有选项，返回一个字典
# 如果获取到的数据为数字类型的字符串，自动转化为int、float
# 一个对象(is_eval=True) 将获取到的数据使用eval函数转换
# 一个对象(is_bool=True) 将获取到的数据用getboolean转换

# 导入配置文件模块
from configparser import ConfigParser


class HandleConfig(ConfigParser):
    """
    定义处理配置文件的类
    """
    def __init__(self):  # 对父类构造方法进行拓展
        # 调用父类的构造方法
        super().__init__()
        self.filename = 'testcase.ini'
        self.read(self.filename, encoding='utf8')  # 读取配置文件

    def __call__(self, section='DEFAULT', option=None, is_eval=False, is_bool=False):
        """
        ‘对象（）’这种形式，__call__会被调用
        :param section: 区域名
        :param option: 选项名
        :param is_eval: 选项值是否需要进行eval函数转换，默认不转换
        :param is_bool: 选项值是否需要转化为bool类型，默认不转换
        :return:
        """
        # 不传参则将默认区域返回
        # 只传区域名，获取此区域下的所有选项，返回一个字典
        if option is None:
            return dict(self[section])
        # 一个对象(is_bool=True) 将获取到的数据用getboolean转换
        if isinstance(is_bool, bool):
            if is_bool:
                return self.getboolean(section, option)
        else:
            raise ValueError('{}必须是布尔类型'.format(is_bool))
        # 如果获取到的数据为数字类型的字符串，自动转化为int、float
        data = self.get(section, option)
        if data.isdigit():  # 判断是否为数字类型的字符串
            return int(data)
        try:
            return float(data)
        except ValueError:
            pass
        # 一个对象(is_eval=True) 将获取到的数据使用eval函数转换
        if isinstance(is_eval, bool):
            if is_eval:
                return eval(data)
        else:
            raise ValueError('{}必须是布尔类型'.format(is_eval))


if __name__ == '__main__':
    config = HandleConfig()
    print(config())
    print(config('excel'))
    print(config('excel', 'two_res'))
    print(config('excel', 'two_res', is_bool=True))
    print(config('excel', 'five_res', is_eval=True))
