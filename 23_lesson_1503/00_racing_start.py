import pygame as pg
from pygame.draw import rect, circle, polygon

WHITE = (255, 255, 255)
GREEN = (7, 115, 14)
SAND = (255, 237, 181)
GRAY = (64, 64, 64)
RED = (201, 22, 55)

W = 800
H = 900

screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

road = pg.Rect(200, 0, 400, H)
border_left = pg.Rect(road.left - 50, 0, 50, H)
border_right = pg.Rect(road.right, 0, 50, H)

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    screen.fill(GREEN)  # фон игры (трава)
    rect(screen, GRAY, road)  # дорога
    rect(screen, SAND, border_left)  # левая обочина
    rect(screen, SAND, border_right)  # правая обочина
    rect(screen, WHITE, [396, 0, 8, H])

    pg.display.update()