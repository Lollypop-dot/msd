import pygame
from pygame.draw import *

FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GRAY = (185, 185, 185)
GINGER = (255, 155, 0)

screen = pygame.display.set_mode((600, 800))
# background
background_start_point_x = 0
background_stary_point_y = 0
background_width = 600
background_height = 400

rect(
    screen,
    YELLOW,
    (
        background_start_point_x,
        background_stary_point_y,
        background_width,
        background_height,
    ),
)
rect(
    screen,
    RED,
    (
        background_start_point_x,
        background_stary_point_y + background_height,
        background_width,
        background_height,
    ),
)
# окно
# rect(screen, WHITE)


# кот
cat_start_point_x = 100
cat_start_point_y = 420


def cat(x, y, color):
    # тело
    ellipse(screen, color, (x, y, 450, 200))
    ellipse(screen, BLACK, (x, y, 450, 200), 1)
    # голова
    circle(screen, color, (x, y + 100), 80)
    circle(screen, BLACK, (x, y + 100), 80, 1)


cat(cat_start_point_x, cat_start_point_y, GINGER)
# # клубок
# circle(screen, GRAY)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
