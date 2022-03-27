# 定义家具类
class Furniture:
    # 定义家具类属性
    def __init__(self, name, aera):
        self.furniture_name = name
        self.furniture_aera = aera

    # 自定义返回值
    def __str__(self):
        return self.furniture_name


# 定义房子的类
class House:
    # 定义房子的属性
    def __init__(self, type, area):
        self.house_type = type  # 房子户型
        self.house_area = area  # 房子面积
        self.furniture_list = []  # 家具列表
        self.surplus_area = area  # 剩余面积

    def __str__(self):
        return ("这个房子是[%s]有%.2f平米，摆放了%s，现在还剩%.2f平米" %
                (self.house_type, self.house_area, self.furniture_list, self.surplus_area))

    def add_furniture(self, furniture):
        # 判断家具面积
        if furniture.furniture_aera > self.house_area:
            print("对不起,%s太大了,无法添加!" % furniture.furniture_name)
            return
        # 将家居的名称添加到列表中
        self.furniture_list.append(furniture.furniture_name)
        # 计算剩余面积
        self.surplus_area -= furniture.furniture_aera


# 创建家具
ximensi = Furniture("西梦思", 5)
bed = Furniture("床", 10)
closet = Furniture("衣柜", 110)
# 创建房子
home = House("两室一厅", 100)
# 添加家具
home.add_furniture(ximensi)
home.add_furniture(closet)
print(home)
