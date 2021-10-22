import pygame
from plane_sprites import *

pygame.init()

#  创建游戏窗口
screen = pygame.display.set_mode((480, 852))

# 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load("./images/background.png")
# 2> blit绘制图像到指定位置
screen.blit(bg, (0, 0))
# 3> update更新屏幕显示
pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/hero.jpg")
screen.blit(hero, (160, 692))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(160, 692, 160, 160)

# 创建敌机的精灵
enemy = GameSprite("./images/qiang.jpg")
enemy1 = GameSprite("./images/qiang.jpg", 2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

# 游戏循环->意味着游戏的正式开始!
while True:

    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)

    # 捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)

    # 事件监听
    for event in event_list:
        # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏...")

            pygame.quit()

            # 直接退出系统(break只能退出当前for循环, exit可以直接退出程序)
            exit()

    # 2. 修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机的位置
    if hero_rect.y <= -160:
        hero_rect.y = 852

    # 3. 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    # update--让组中的所有精灵更新位置
    enemy_group.update()
    # draw--在screen上绘制所有的精灵
    enemy_group.draw(screen)

    # 4. 调用update方法更新显示
    pygame.display.update()

pygame.quit()
