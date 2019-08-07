# 模仿王者荣耀定义英雄类
# a、英雄需要有昵称、攻击力、生命值等属性
# b、实例化出两个英雄对象
# c、英雄之间可以相互攻击，被攻击的一方掉血（每次攻击掉的血量等于攻击力数值，如攻击者攻击力为10，每次攻击
# 被攻击者的生命值减10
# d、当血量小于0时，提示某个英雄死亡

class Hero:
    """
    创建一个英雄类
    """
    def __init__(self, name, damage, health):
        self.name, self.damage, self.health = name, damage, health
        print('英雄：{}\n攻击力：{}\n生命值：{}\n'.format(self.name, self.damage, self.health))

    def attack(self, name_2, damage_2):

        while self.health > 0:
            self.health -= damage_2
            if self.health > 0:
                print('英雄（{}）被英雄（{}）攻击，受到{}点伤害，生命值剩余{}'.format(self.name, name_2, damage_2, self.health))
            else:
                print('英雄（{}）生命值为0，阵亡\n'.format(self.name))


xiangyu = Hero('项羽', 170, 5000)
yuji = Hero('虞姬', 300, 3000)
xiangyu.attack(yuji.name, yuji.damage)
yuji.attack(xiangyu.name, xiangyu.damage)
