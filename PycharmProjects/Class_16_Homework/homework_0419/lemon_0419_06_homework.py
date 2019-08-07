# 创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。

# a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）
# 和一个名为 open_restaurant()的方法（显示饭店正在营业）。

# b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。

class Restaurant:
    """
    这是一个饭店类
    """
    # def __init__(self, r_name, *args):
    def __init__(self, r_name, c_type):
        self.restaurant_name = r_name
        # self.cooking_type = args
        self.cooking_type = c_type


    def describe_restaurant(self):
        print('这个饭店是{}，里面的美食种类有{}、{}、{}等'.format(self.restaurant_name, *self.cooking_type))


    def open_restaurant(self):
        print('饭店正在营业')


# cooking_type1 = 'seafood'
# cooking_type2 = 'beef'
# restaurant = Restaurant('四海一家', cooking_type1, cooking_type2)
restaurant_msg = ('四海一家', ('seafood', 'beef', 'mutton'))
restaurant = Restaurant(*restaurant_msg)
print(restaurant.restaurant_name, restaurant.cooking_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()