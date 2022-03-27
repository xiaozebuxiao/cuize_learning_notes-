# 创建枪的类
class Gun:

    def __init__(self, model):
        """
        枪的属性
        :param model: 枪的型号
        """
        self.model = model
        self.gun_count = 0

    def add_bullet(self, count):
        """
        添加子弹
        :param count: 添加子弹的数量
        """
        self.gun_count += count
        print("已经成功添加子弹%d颗..." % count)

    def shoot(self):
        """
        射击
        """
        if self.gun_count > 0:
            self.gun_count -= 1
            print("突突突...剩余%d" % self.gun_count)
        else:
            print("没有子弹！")
            return


# 创建士兵类
class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        """
        士兵开枪
        :return:
        """
        # 判断士兵是否有枪
        if self.gun is None:
            gun = Gun(input("请输入枪的型号："))

        # 高喊口号
        # 士兵给枪装填子弹
        bullet_amount = int(input("请输入子弹数目："))
        if bullet_amount > 0:
            gun.add_bullet()
        else:
            return "子弹数不能为负数"
        # 选择是否开枪
        shuru = input("是否开枪？\n【是】&【否】")
        shuru == "是"

        while shuru == "是":
            # 让枪发射子弹
            gun.shoot()
        else:
            return shuru


# ak47 = Gun("AK47")
# ak47.add_bullet(10)
# ak47.shoot()
# 创建士兵
soldier_xiaoming = Soldier("小明")
soldier_xiaoming.fire()
