class Father:
    def __init__(self, name):
        # 定义共有属性name
        self.name = name
        # 定义私有属性age
        self.__age = 18

    # 定义一个私有方法private_way
    def __private_way(self):
        print("这是一个私有方法！")

    # 定义共有方法public_way
    def public_way(self):
        # 在父类共有方法中调用私有属性，方便子类访问
        print("我的名字叫%s，年龄%d（这是一个共有方法！）" % (self.name, self.__age))
        # 在父类共有方法中调用私有方法，方便子类访问
        self.__private_way()


class Son(Father):
    pass


son_xz = Son("小泽")
# print("我的名字叫%s,今年%d" % (son_xz.name, son_xz.age))  因为age是Father类的私有属性，不可访问。此代码执行会报错
print("我的名字叫%s" % son_xz.name)
# 通过访问父类的共有方法间接访问父类的私有属性和方法
son_xz.public_way()
# son_xz.__private_way()  __private_way()方法为Father类私有方法不可访问


