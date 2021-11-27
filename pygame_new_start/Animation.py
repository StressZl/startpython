import pygame
import sys
import time
import random
from pygame.locals import *

pygame.init()
# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)# 粉红
VIOLET = (238, 130, 238)# 紫罗兰
PURPLE = (128, 0, 128)# 紫
SKYBLUE = (135, 206, 235)# 天蓝
CYAN = (0, 255, 255)# 青
GLOD = (255, 215, 0)# 金
ORANGE = (255, 165, 0)# (*≧︶≦))(￣▽￣* )ゞ
CHOCOLATE = (210, 105, 30)# 巧克力
ORANGERED = (255, 69, 0)# 橙红
SPRINGGREEN = (0, 255, 127)# 春🦌
number_color_list = [CYAN, GREEN, SKYBLUE, GLOD, ORANGE, PINK, VIOLET, PURPLE, SPRINGGREEN, ORANGERED, CHOCOLATE]
# 宽
WW = 1000
# 长
WH = 500
# set window
windowSurface = pygame.display.set_mode((WW, WH), 0, 32)
# tip
pygame.display.set_caption('粒子')
# 移动速度
LZ_speed = 4
# 粒子数量
LZ_num = 500
# 粒子大小
LZ_D = 4
LZ_H = 4
# 设定粒子参数
LZ_list = []
LZ_X_list = random.sample([i for i in range(WW)], LZ_num)
LZ_Y_list = random.sample([i for i in range(WH)], LZ_num)
for i in range(LZ_num):
    LZ_COLOR = number_color_list[int(i % len(number_color_list))]
    LZ_dir = random.choice(['+', '-'])+random.choice(['+', '-'])
    b = {'rect': pygame.Rect(LZ_X_list[i], LZ_Y_list[i], LZ_D, LZ_H),
         'color': LZ_COLOR,
         'dir': LZ_dir}
    LZ_list.append(b)

# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # windowSurface.fill(BLACK)
    for b in LZ_list:
        dir1 = b['dir'][0]
        dir2 = b['dir'][1]
        if dir1 == '+':
            b['rect'].left += LZ_speed+random.choice([0, LZ_speed])
        if dir1 == '-':
            b['rect'].left -= LZ_speed+random.choice([0, LZ_speed])
        if dir2 == '+':
            b['rect'].top += LZ_speed+random.choice([0, LZ_speed])
        if dir2 == '-':
            b['rect'].top -= LZ_speed+random.choice([0, LZ_speed])
        if b['rect'].top < 0:
            dir2 = '+'
        if b['rect'].bottom > WH:
            dir2 = '-'
        if b['rect'].left < 0:
            dir1 = '+'
        if b['rect'].right > WW:
            dir1 = '-'
        b['dir'] = dir1+dir2
        pygame.draw.rect(windowSurface, b['color'], b['rect'])
    pygame.display.update()
    time.sleep(0.02)
