import pygame
from pygame.draw import *

pygame.init()


FPS = 30
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GRAY = (185, 185, 185)

screen = pygame.display.set_mode((400, 400))
# фон
rect(screen, GRAY, (0, 0, 400, 400))
# морда
circle(screen, YELLOW, (200, 200), 150)
circle(screen, BLACK, (200, 200), 150, 1)
# левый глаз
circle(screen, RED, (150, 180), 30)
circle(screen, BLACK, (150, 180), 25)
# правый глаз
circle(screen, RED, (250, 200), 20)
circle(screen, BLACK, (250, 200), 10)
# рот
rect(screen, BLACK, (150, 280, 100, 20))
# левая бровь
line(screen, BLACK, [50, 50], [180, 150], 7)
# правая бровь
line(screen, BLACK, [220, 170], [350, 50], 7)
# polygon(screen, (255, 255, 0), [(100, 100), (200, 50), (300, 100), (100, 100)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
