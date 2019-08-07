# 灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
# a.根据以上信息，抽象出一个类
# b.定义相关属性，并能在类的外面调用
# c.定义相关方法，在方法中打印相应信息

class Cat:
    """
    定义一个猫类
    """
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
        print('{}的{}猫，今年{}岁'.format(self.color, self.name, self.age))

    def eat(self):
        food = '吃着美味的事物'
        return food

    def drink(self):
        beverage = '喝着可口的饮料'
        return beverage


Tom = Cat('Tom', '灰色', 1)
print(Tom.eat(), Tom.drink())