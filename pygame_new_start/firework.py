# 使用 pygame 创建一个经典飞机游戏
# 飞机（fire.png）子弹（月牙） 生命（太阳） 敌人（plan）
# 绘制游戏开始界面
import pygame, sys, random
from pygame.locals import *
import time
pygame.init()
mainClock = pygame.time.Clock()

WW = 400
WD = 400

WdSf = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('XXXX')

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
GRAY = (100, 100, 150)
number_color_list = [CYAN, GREEN, SKYBLUE, GLOD, ORANGE, PINK, VIOLET, PURPLE, SPRINGGREEN, ORANGERED, CHOCOLATE]
start_x = 220
start_y = 440
speed = 5
LZ_list = []
PL_list = []
BM_num = 3
HR_num = 3
plane_num_list = [1, 2, 3]
LZ_x, LZ_y = 2, 6
basicFont = pygame.font.SysFont('华文楷体', 20)
player = pygame.Rect(start_x, start_y, 40, 40)
plane = pygame.Rect(start_x, 0, 40, 40)
playerImage = pygame.image.load('fire.png')
planeImage = pygame.image.load('plan.png')
boomImage = pygame.image.load('boom.png')
heartImage = pygame.image.load('heart.png')
playerStretchedImage = pygame.transform.scale(playerImage, (40, 40))
planeStretchedImage = pygame.transform.scale(planeImage, (40, 40))
boomStretchedImage = pygame.transform.scale(boomImage, (20, 20))
heartStretchedImage = pygame.transform.scale(heartImage, (20, 20))
move_flag_list = [False]*5
stop_flag = False
print(int(time.time()))
last_boom_time = int(time.time())
score = 0
while True:
    WdSf.fill(GRAY)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if not stop_flag:
                if event.key == K_UP or event.key == K_w:
                    move_flag_list[0] = True
                if event.key == K_DOWN or event.key == K_s:
                    move_flag_list[1] = True
                if event.key == K_LEFT or event.key == K_a:
                    move_flag_list[2] = True
                if event.key == K_RIGHT or event.key == K_d:
                    move_flag_list[3] = True
                if event.key == K_q:
                    move_flag_list[4] = True
                # 使用炸弹
                if event.key == K_e and BM_num > 0:
                    BM_num -= 1
                    # 清空plane
                    PL_list = []
            if event.key == K_r:
                # 清空plane
                PL_list = []
                stop_flag = False
                # 还原飞机位置
                start_x = 220
                start_y = 440
                # 还原生命值和炸弹
                HR_num = 3
                BM_num = 3
                score = 0

        if event.type == KEYUP:
            if event.key == K_UP or event.key == K_w:
                move_flag_list[0] = False
            if event.key == K_DOWN or event.key == K_s:
                move_flag_list[1] = False
            if event.key == K_LEFT or event.key == K_a:
                move_flag_list[2] = False
            if event.key == K_RIGHT or event.key == K_d:
                move_flag_list[3] = False
            if event.key == K_q:
                move_flag_list[4] = False
    if move_flag_list[0]:
        start_y = start_y - speed if start_y > 0 else start_y
    if move_flag_list[1]:
        start_y = start_y + speed if start_y < 460 else start_y
    if move_flag_list[2]:
        start_x = start_x - speed if start_x > 0 else start_x
    if move_flag_list[3]:
        start_x = start_x + speed if start_x < 460 else start_x
    if move_flag_list[4]:
        # 射出子弹
        LZ_COLOR = random.sample(number_color_list, 1)[0]
        LZ_list.append({'rect': pygame.Rect(start_x+20, start_y, LZ_x, LZ_y), 'color': LZ_COLOR})
    # 每1秒出现plane
    if time.time() % 2 < 0.05:
        PL_num = random.sample(plane_num_list, 1)[0]
        LZ_X_list = random.sample([i for i in range(50)], PL_num)
        for X in LZ_X_list:
            PL_list.append({'rect': pygame.Rect(X*10, 0, 40, 40), 'count': 3})
    # 绘制plane
    for PL in PL_list[:]:
        p = PL['rect']
        p.top += 1
        # 边界删除
        if p.top < 0 or p.bottom > 500 or p.left < 0 or p.right > 500:
            PL_list.remove(PL)
        # 碰撞检测
        if player.colliderect(PL['rect']) and HR_num > 0:
            HR_num -= 1
            PL_list.remove(PL)
        WdSf.blit(planeStretchedImage, p)

    # 绘制子弹
    for i in LZ_list[:]:
        i['rect'].top -= 20
        # 碰撞检测
        for PL in PL_list[:]:
            if i['rect'].colliderect(PL['rect']) and i in LZ_list:
                LZ_list.remove(i)
                PL['count'] -= 1
                # plane 被击中3次会消失
                if PL['count'] == 0:
                    score += 1
                    PL_list.remove(PL)
        # 边界删除
        if i['rect'].top < 0 or i['rect'].bottom > 500 or i['rect'].left < 0 or i['rect'].right > 500 and i in LZ_list:
            LZ_list.remove(i)
        pygame.draw.rect(WdSf, i['color'], i['rect'])
    # 绘制玩家
    player = pygame.Rect(start_x, start_y, 40, 40)
    WdSf.blit(playerStretchedImage, player)
    # 绘制炸弹
    text = basicFont.render('X%s' % BM_num, True, PURPLE, GRAY)
    textRect = pygame.Rect(40, 460, 40, 40)
    WdSf.blit(text, textRect)
    boom = pygame.Rect(20, 465, 40, 40)
    WdSf.blit(boomStretchedImage, boom)
    # 绘制生命
    text = basicFont.render('X%s' % HR_num, True, BLUE, GRAY)
    textRect = pygame.Rect(460, 460, 40, 40)
    WdSf.blit(text, textRect)
    heart = pygame.Rect(440, 465, 40, 40)
    WdSf.blit(heartStretchedImage, heart)
    # 绘制score
    text = basicFont.render('score: %s' % score, True, BLUE, GRAY)
    textRect = pygame.Rect(20, 20, 40, 40)
    WdSf.blit(text, textRect)
    mainClock.tick(40)
    if HR_num == 0 or stop_flag:
        stop_flag = True
        text = basicFont.render('你输了！', True, RED, GRAY)
        textRect = text.get_rect()
        textRect.centerx = WdSf.get_rect().centerx
        textRect.centery = WdSf.get_rect().centery
        WdSf.blit(text, textRect)
    pygame.display.update()