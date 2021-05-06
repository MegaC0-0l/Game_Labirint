import pygame
from random import choice


# игровой экран параметры


RES = WIDTH, HEIGHT = 1202, 702
TILE = 100
cols, rows = WIDTH // TILE, HEIGHT // TILE

pygame.init()
scr = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

while True:
    scr.fill(pygame.Color('darkslategray'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(30)
# игровой экран пааметры конец