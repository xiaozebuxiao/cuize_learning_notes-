import pygame
from plane_sprites import *

# 初始化pygame模块
pygame.init()

# 初始化游戏窗口并且记录返回结果
screen = pygame.display.set_mode((1280, 720))

# ----------绘制背景图片----------

# 将背景图像加载到内存中
bg = pygame.image.load("飞机大战_素材/游戏背景.jpg")
# 将背景图片绘制在窗口中
screen.blit(bg, (0, 0))
# 刷新窗口显示绘制结果
pygame.display.update()

# ----------绘制飞机-----------

# 将飞机加载到内存中
fj = pygame.image.load("飞机大战_素材/飞机.png")
# 将飞机绘制到游戏窗口中
screen.blit(fj, (720, 600))
# 刷新窗口，显示绘制的飞机
pygame.display.update()

# 创建游戏时钟对象
clock = pygame.time.Clock()

# 定义一个fj_rect记录飞机的初始位置和大小
fj_rect = pygame.Rect(720, 600, 200, 200)


# ---------------------创建敌机的精灵--------------------
enemy_fj01 = GameSprite("飞机大战_素材/敌机.png", 10)
enemy_fj02 = GameSprite("飞机大战_素材/敌机.png", 13)
enemy_fj03 = GameSprite("飞机大战_素材/敌机.png", 15)
enemy_fj04 = GameSprite("飞机大战_素材/敌机.png", 20)

# ---------------------创建敌机的精灵组--------------------
enemy_fj_group = pygame.sprite.Group(
    enemy_fj01,
    enemy_fj02,
    enemy_fj03,
    enemy_fj04,)


# 游戏循环
while True:
    # 设置刷新率，每秒钟刷新60次
    clock.tick(60)

# ---------------------监听事件---------------------

    # 遍历获取到的事件列表
    for user_event in pygame.event.get():

        # 判断事件类型是否是退出事件
        if user_event.type == pygame.QUIT:
            # 卸载pygame所有模块
            pygame.quit()
            # 退出整个系统
            exit()

    # 修改飞机的位置
    fj_rect.y -= 5

    # 判断飞机有没有飞出游戏窗口
    if fj_rect.y == -200:
        # 飞出游戏窗口后，修改y值到最底端
        fj_rect.y = 720

    # 重新绘制背景图像，解决残影的问题
    screen.blit(bg, (0, 0))
    # 调用blit方法绘制图像
    screen.blit(fj, (fj_rect.x, fj_rect.y))

    # 让敌机精灵组调用update方法和draw方法
    enemy_fj_group.update()
    enemy_fj_group.draw(screen)
    
    # 调用updata方法更新显示
    pygame.display.update()

