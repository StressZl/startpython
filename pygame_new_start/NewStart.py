"""
2048
1.	有2，4，6，8，16，32，64，128，256，512，1024，2048一共12种数字。
2.	初始为5*5的方格。
3.	初始随机生成2格方块数字为2。
4.	W A S D控制上下左右移动。
5.	每次移动条件为有空余或者能够合并。
6.	相同数字可以合并，合并后阶层增加一级，移动位置空出。
7.	空位会移动过去，移动位置空出，
8.	移动后在空位生成一个随机方块2或者方块4。
9.	在移动后判断，如果无空位且无可合并方块，游戏结束，判定为游戏失败。
10.	在移动后判断，如果合并数字为2048，游戏结束，判定为游戏成功。
11.	游戏结束后，设定是否继续。继续则为重来。
12.	支持：c 存档，v 读取存档继续，exit 退出。
TODO 增加内存功能
"""
import random
import copy
import struct
import pygame
import sys
from pygame.locals import *
# 基础设置
number_list = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
Wide = 5
High = 5
# set up the colors.
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
number_dict = dict(zip(number_list, number_color_list))
def create_board():
    # 创造棋盘
    line_list = ['----'.join(['+']*(Wide+1))+'\n'+'    '.join(['|']*(Wide+1)) for i in range(High)]
    line_list.append('----'.join(['+']*(Wide+1)))
    return '\n'.join(line_list)


def crete_data_structure():
    # 创造数据结构
    all_list = [[0]*Wide for i in range(High)]
    return all_list


def get_available_blank(li):
    # 记录空位x,y坐标
    xy_b_list = []
    for y in range(len(li)):
        for x in range(len(li[y])):
            if li[y][x] == 0:
                xy_b_list.append((x, y))
    return xy_b_list


def random_fill_blank(li1, li2, times):
    # 随机填空
    choice_xy_list = random.sample(li2, times)
    for j in range(times):
        num = random.choice([2, 4])
        li1[choice_xy_list[j][1]][choice_xy_list[j][0]] = num
    return li1



def split_list(ls1, fx1):
    x_len = len(ls1[0])
    y_len = len(ls1)
    if fx1 == "W" or fx1 == "S":
        for x in range(x_len):
            # 收集y的变化值
            y_list = []
            for y in range(y_len):
                num1 = ls1[y][x] if fx1 == "W" else ls1[y_len-(y+1)][x]
                if not num1:
                    continue
                if y_list and y_list[-1] == num1:
                    y_list[-1] = 2 * num1
                else:
                    y_list.append(num1)
            for y in range(y_len):
                if fx1 == "W":
                    if len(y_list) > y:
                        ls1[y][x] = y_list[y]
                    else:
                        ls1[y][x] = 0
                if fx1 == "S":
                    if len(y_list) > y:
                        ls1[y_len-(y+1)][x] = y_list[y]
                    else:
                        ls1[y_len-(y+1)][x] = 0
    if fx1 == "A" or fx1 == "D":
        for y in range(y_len):
            # 收集x的变化值
            x_list = []
            for x in range(x_len):
                num1 = ls1[y][x] if fx1 == "A" else ls1[y][x_len - (x + 1)]
                if not num1:
                    continue
                if x_list and x_list[-1] == num1:
                    x_list[-1] = 2 * num1
                else:
                    x_list.append(num1)
            for x in range(x_len):
                if fx1 == "A":
                    if len(x_list) > x:
                        ls1[y][x] = x_list[x]
                    else:
                        ls1[y][x] = 0
                if fx1 == "D":
                    if len(x_list) > x:
                        ls1[y][x_len - (x + 1)] = x_list[x]
                    else:
                        ls1[y][x_len - (x + 1)] = 0
    return ls1


def check_result(data):
    for p in ['W', 'A', 'S', 'D']:
        before_data = copy.deepcopy(data)
        dat = split_list(data, p)
        if dat != before_data:
            return True
    return False


# 生成data
data = crete_data_structure()
print(data)
# 选出空的列表
xy_list = get_available_blank(data)
print(xy_list)
# 随机生成两个随机数
data = random_fill_blank(data, xy_list, 2)
for j in data:
    print(j)
# init game
pygame.init()
# set up the window.
windowSurface = pygame.display.set_mode((500, 500), 0, 32)
windowSurface.fill(WHITE)
pygame.display.set_caption('2048')
for y in range(High):
    for x in range(Wide):
        if data[y][x] != 0:
            pygame.draw.rect(windowSurface, number_dict[data[y][x]], (int(100 * x), int(100 * y), 100, 100), 0)
            # set up the fonts
            basicFont = pygame.font.SysFont(None, 80)# pygame.font.get_fonts()获取所有可使用的字体。
            # set up the text
            text = basicFont.render(str(data[y][x]), True, WHITE, number_dict[data[y][x]])
            textRect = text.get_rect()
            textRect.centerx = int(100 * x + 50)
            textRect.centery = int(100*y+50)
            windowSurface.blit(text, textRect)
StopFlag = False
# Run the game loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and not StopFlag:
            k_dict = {K_LEFT: "A", K_a: "A",
                      K_UP: "W", K_w: "W",
                      K_RIGHT: "D", K_d: "D",
                      K_DOWN: "S", K_s: "S"}
            if event.key in k_dict.keys():
                moveFlag = k_dict[event.key]
                before_data = copy.deepcopy(data)
                data = split_list(data, moveFlag)
                xy_list = get_available_blank(data)
                # 如果棋盘满了，判断是否能够移动
                if len(xy_list) == 0:
                    if not check_result(data):
                        StopFlag = True
                        basicFont = pygame.font.SysFont('华文楷体', 50)
                        text = basicFont.render('你输了！', True, RED, WHITE)
                        textRect = text.get_rect()
                        textRect.centerx = windowSurface.get_rect().centerx
                        textRect.centery = windowSurface.get_rect().centery
                        windowSurface.blit(text, textRect)
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                    continue
                if before_data == data:
                    print('无效移动')
                    continue

                data = random_fill_blank(data, xy_list, 1)
                windowSurface.fill(WHITE)
                for y in range(High):
                    for x in range(Wide):
                        if data[y][x] != 0:
                            pygame.draw.rect(windowSurface, number_dict[data[y][x]], (int(100 * x), int(100 * y), 100, 100), 0)
                            # set up the fonts
                            basicFont = pygame.font.SysFont(None, 50)  # pygame.font.get_fonts()获取所有可使用的字体。
                            # set up the text
                            text = basicFont.render(str(data[y][x]), True, WHITE, number_dict[data[y][x]])
                            textRect = text.get_rect()
                            textRect.centerx = int(100 * x + 50)
                            textRect.centery = int(100 * y + 50)
                            windowSurface.blit(text, textRect)
                # 判断是否出现2048，出现就胜利
                if [d for d in data if 2048 in d]:
                    StopFlag = True
                    basicFont = pygame.font.SysFont('华文楷体', 50)
                    text = basicFont.render('你赢了！', True, BLUE, WHITE)
                    textRect = text.get_rect()
                    textRect.centerx = windowSurface.get_rect().centerx
                    textRect.centery = windowSurface.get_rect().centery
                    windowSurface.blit(text, textRect)
                    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
