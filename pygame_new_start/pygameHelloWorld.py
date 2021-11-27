import pygame
import sys
from pygame.locals import *
# init game
pygame.init()

# set up the window.
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('hello world!')

# set up the colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up the fonts
basicFont = pygame.font.SysFont('华文楷体', 100)

# set up the text
text = basicFont.render('你输了！', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# draw the white background onto the surface
windowSurface.fill(WHITE)

# draw a green polygon onto the surface
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 166)))

# draw some blue lines onto the surface
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120), 4)
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# draw a blue circle onto the surface
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# draw a red ellipse onto the surface
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# draw the text's background rectangle onto the surface
pygame.draw.ellipse(windowSurface, RED, (textRect.left - 20, textRect.top - 20,
                                         textRect.width + 40, textRect.height + 40))
# draw a pixel array of the surface
# pixArray = pygame.PixelArray(windowSurface)
# pixArray[480][380] = BLACK
# del pixArray

# draw the text's background rectangle onto the surface
windowSurface.blit(text, textRect)

# draw the windows onto the screen
pygame.display.update()

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
