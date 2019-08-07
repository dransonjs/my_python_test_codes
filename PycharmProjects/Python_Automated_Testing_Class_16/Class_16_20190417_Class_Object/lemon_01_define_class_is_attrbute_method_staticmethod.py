class Person:
    """
    定义一个人类
    """
    head = 1

    def __init__(self, name, age, height, hair):
        self.name, self.age, self.height, self.hair = name, age, height, hair
        # self.head = 2
        print('姓名：{}\n年龄：{}\n身高：{}\n发型：{}\n头脑个数：{}'.format(self.name, self.age, self.height, self.hair, self.head))

    def run(self):
        self.weather_forecast()  # 实例方法内部调用静态方法
        print('{}可以去跑步'.format(self.name))

    def eat(self):
        print(self.hair)
        print('{}会吃东西'.format(self.name))

    @classmethod
    def angry(cls):  # 类方法，它的目的是获取或修改类属性
        # Person.head = 2
        # cls.weather_forecast()  # 类方法内部调用静态方法
        cls.head = 2

    @staticmethod
    def weather_forecast():  # 往往会把与类相关的函数，放到类当中，作为静态方法，封装性较好
        # Person.其他静态方法()  # 静态方法内部调用静态方法
        print('天气：晴朗')
        print('温度：23')
        print('适合出游')


keyou = Person('可优', 17, 1.9, '假发')

keyou.run()

# 1、类外部，可以使用对象.静态方法名
# keyou.weather_forecast()

# 2、也可以使用类.静态方法名
# Person.weather_forecast()