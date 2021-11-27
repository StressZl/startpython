import pygame, sys, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WD = 400
WH = 400

windowSurface = pygame.display.set_mode((WD, WH), 0, 32)
pygame.display.set_caption('Collision Detection')

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
Sakura = (241, 204, 226)# 樱花

foodCounter = 0
NewFood = 40
FoodSize = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WD - FoodSize),
                 random.randint(0, WD - FoodSize),
                 FoodSize,
                 FoodSize))

moveLeft = False
moveRight = False
moveUP = False
moveDown = False

MoveSpeed = 6

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUP = True
            if event.key == K_DOWN or event.key == K_s:
                moveUP = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUP = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WH - player.height)
                player.top = random.randint(0, WD - player.width)

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1],
                                     FoodSize, FoodSize))
            foodCounter += 1
        if foodCounter >= NewFood:
            foodCounter = 0
            foods.append(pygame.Rect(random.randint(0, WD - FoodSize),
                                     random.randint(0, WD - FoodSize),
                                     FoodSize,
                                     FoodSize))

        windowSurface.fill(WHITE)

        if moveDown and player.bottom < WH:
            player.top += MoveSpeed
        if moveUP and player.top > 0:
            player.top -= MoveSpeed
        if moveLeft and player.left > 0:
            player.left -= MoveSpeed
        if moveRight and player.right < WD:
            player.right += MoveSpeed

        pygame.draw.rect(windowSurface, BLACK, player)
        for food in foods[:]:
            print(food)
            if player.colliderect(food):
                foods.remove(food)
        for i in range(len(foods)):
            pygame.draw.rect(windowSurface, GREEN, foods[i])

        pygame.display.update()
        mainClock.tick(40)
