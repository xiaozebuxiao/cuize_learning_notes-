# 导入模块
import random
import pygame

# 定义屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 1280, 720)
# 刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量(USEREVENT为用户事件)
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


# 定义GameSprite类，继承自pyganme模块的sprite类
class GameSprite(pygame.sprite.Sprite):

    # 初始化方法
    def __init__(self, image_name, speed=1):
        # 调用父类初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)  # 将指定名称的图像加载到图像属性
        self.rect = self.image.get_rect()
        # 速度
        self.speed = speed

    # 重写update方法
    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed  # 为什么要加速度？


class Background(GameSprite):
    """
    游戏背景精灵类
    """

    def __init__(self, is_alt=False):
        # 调用父类方法实现精灵的创建（image/rect/speed）
        super().__init__("./飞机大战_素材/游戏背景.jpg")
        # 判断是否是交替图像，如果是，需要设置初始位置
        if is_alt is True:
            self.rect.y = - self.rect.height

    # 扩展父类update方法
    def update(self):
        # 1、调用父类的方法
        super().update()
        # 2、新增：判断背景是否溢出窗口，如果溢出窗口，将图像设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """
    敌机精灵
    """

    def __init__(self):
        # 调用父类方法，指定敌机精灵，同时指定敌机图片
        super().__init__("飞机大战_素材/敌机.png")
        # 指定敌机的初始随机速度(1~3)
        self.speed = random.randint(1, 3)
        # 指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类方法，保持垂直方向的飞行
        super().update()
        # 判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # 利用kill方法将精灵从精灵组中移出，实现销毁
            self.kill()

    def __del__(self):
        # print("敌机已在%s销毁" % self.rect)
        pass


class Hero(GameSprite):
    """
    英雄精灵
    """

    def __init__(self):

        # 调用父类方法，设置image和speed
        super().__init__("飞机大战_素材/飞机.png", 0)
        # 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 50
        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 英雄在水平方向上移动
        self.rect.x += self.speed

        # 控制英雄不离开屏幕
        # 左侧控制
        if self.rect.x < 0:
            self.rect.x = 0
        # 右侧控制
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):

        for i in (0, 1, 2):
            # 创建子弹精灵
            bullet = Bullet()

            # 设置子弹精灵的位置
            bullet.rect.bottom = self.rect.y - i * 100
            bullet.rect.centerx = self.rect.centerx

            # 将精灵添加到精灵组
            self.bullets.add(bullet)

    def __del__(self):
        pass


class Bullet(GameSprite):
    """
    子弹精灵
    """

    def __init__(self):
        super().__init__("飞机大战_素材/子弹.png", -10)

    def update(self):
        # 调用父类方法，让子弹垂直飞行
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁！")
