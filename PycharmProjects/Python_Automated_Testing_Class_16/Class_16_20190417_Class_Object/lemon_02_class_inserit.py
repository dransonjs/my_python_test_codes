class Animal:
    """
    创建动物类
    """
    def __init__(self, name, age, color):
        self.name, self.age, self.color = name, age, color

    def eat(self):
        print('{}需要吃东西'.format(self.name))

    def sleep(self):
        print('{}需要睡觉'.format(self.name))


class Dog(Animal):
    """
    定义狗类
    Animal 父类，基类
    Dog 子类
    """
    def bark(self):
        print('{}会汪汪叫'.format(self.name))


class XiaoTianQuan(Dog):
    """
    定义哮天犬类
    """
    def __init__(self, name, age, color, job):
        # 重写，直接丢弃父类的构造方法
        # self.name, self.age, self.color, self.job = name, age, color, job
        # 拓展，不丢弃父类的构造方法，而是在父类的基础上修改，super()相当于父类的一个对象，先调用父类的构造方法设置name、age、color这三个属性，然后再添加一个job属性
        super().__init__(name, age, color)
        self.job = job

    def fly(self):
        print('{}会飞'.format(self.name))

    def sleep(self):
        """
        方法重写
        当定义了一个跟父类一样的方法名时，会覆盖父类的方法，父类的方法将不被执行
        1、首先检查本身有没有该方法，没有则去父类找
        :return:
        """
        print('{}不需要睡觉'.format(self.name))

    def eat(self):
        super().eat()
        print('{}想吃蟠桃'.format(self.name))


# 继承父类，会将父类的所有实例方法和类方法、类属性都继承（私有方法除外）
wangcai = Dog('旺财', 1, '棕色')
wangcai.eat()
wangcai.sleep()
wangcai.bark()

qing_yi_fu_wang = XiaoTianQuan('哮天犬', 10000, '黑色', '追随杨戬，守护天庭')
qing_yi_fu_wang.eat()
qing_yi_fu_wang.bark()
qing_yi_fu_wang.fly()
qing_yi_fu_wang.sleep()

print(qing_yi_fu_wang.job)