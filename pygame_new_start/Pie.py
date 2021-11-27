import pygame
import sys
import math
from pygame.locals import *
white = 255, 255, 255
blue = 0, 0, 200
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("The Pie Game - Press 1,2,3,4")
myFont = pygame.font.Font(None, 60)# 设置字体格式
color = 200, 80, 60
wd = 4
x, y = 300, 250
rad = 200
pos = x-rad, y-rad, rad*2, rad*2

piece_list = [False]*4
piece_dict = dict(zip([pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4], [0, 1, 2, 3]))
print(piece_dict)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == KEYDOWN:
            if event.key in piece_dict.keys():
                piece_list[piece_dict[event.key]] = True
    screen.fill(blue)
    for index, item in enumerate([(x+rad/2-20, y-rad/2), (x-rad/2, y-rad/2),
                                 (x-rad/2, y+rad/2-20), (x+rad/2-20, y+rad/2-20)]):
        textImage = myFont.render("%i" % (index+1), True, color)
        screen.blit(textImage, item)
    for index1, item1 in enumerate(piece_list):
        if item1:
            start_angle = math.radians(index1*90)
            end_angle = math.radians(index1*90 + 90)
            pygame.draw.arc(screen, color, pos, start_angle, end_angle, wd)
            line_list = [((x, y-rad), (x+rad, y)),
                         ((x, y-rad), (x-rad, y)),
                         ((x-rad, y), (x, y+rad)),
                         ((x, y+rad), (x+rad, y))]
            pygame.draw.line(screen, color, (x, y), line_list[index1][0], wd)
            pygame.draw.line(screen, color, (x, y), line_list[index1][1], wd)
    if False not in piece_list:
        color = 0, 255, 0
    pygame.display.update()

