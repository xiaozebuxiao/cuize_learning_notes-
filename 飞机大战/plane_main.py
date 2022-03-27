# 安装pygame模块：pip install pygame
# 验证pygame正确安装：python -m pygame.examples.aliens

import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主程序"""

    # 初始化游戏
    def __init__(self):

        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，创建精灵和精灵组
        self.__create_sprites()

        # ----------------敌机------------------
        # 设置定时器事件，创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # ----------------子弹-------------------
        # 设置定时器事件，创建子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 300)

    # 创建精灵
    def __create_sprites(self):

        # 创建背景精灵
        bj01 = Background()
        bj02 = Background(True)

        # 创建背景精灵组
        self.back_group = pygame.sprite.Group(bj01, bj02)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    # 定义开始游戏的方法
    def start_game(self):
        print("开始游戏！")
        while True:
            # 1、设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2、事件监听
            self.__event_handler()
            # 3、碰撞检测
            self.__check_collide()
            # 4、更新、绘制精灵组
            self.__update_sprites()
            # 5、更新显示
            pygame.display.update()

    # 事件监听
    def __event_handler(self):
        # 捕获事件
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

            # ----------敌机事件--------------

            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出场...")
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)

            # -------------子弹------------------
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # ------------英雄事件----------------

            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右。")
        # 定义变量记录事件返回的列表
        keys_pressed = pygame.key.get_pressed()
        # 返回为右键
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 10
        # 返回为左键
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -10
        # 返回为其他按键
        else:
            self.hero.speed = 0

    # 碰撞检测
    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets,  self.enemy_group, True, True)

        # 敌机撞毁英雄
        enemies_list = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # 实现和敌人飞机相撞，英雄飞机被摧毁
        if len(enemies_list) > 0:
            # 英雄牺牲
            self.hero.kill()
            print("英雄牺牲！")
            # 结束游戏
            PlaneGame.__game_over()

    # 更新精灵
    def __update_sprites(self):

        # 让背景精灵组调用update方法
        self.back_group.update()
        # 让背景精灵组调用draw方法绘制图像
        self.back_group.draw(self.screen)

        # ---------------敌机--------------
        # 让敌机精灵调用upsate方法
        self.enemy_group.update()
        # 让敌机精灵组调用draw方法绘制图像
        self.enemy_group.draw(self.screen)

        # ---------------英雄--------------
        self.hero_group.update()
        self.hero_group.draw(self.screen)

        # ------------子弹------------------
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        # print("游戏结束！")
        pygame.quit()
        exit()


# 使用python内置属性__name__测试代码的执行，方便代码的复用
if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()
