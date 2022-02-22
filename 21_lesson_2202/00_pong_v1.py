import pygame as pg
from pygame.draw import rect, circle, polygon

W = 640
H = 640
screen = pg.display.set_mode((W, H))
pg.display.set_caption('Pong game Python🏓')
clock = pg.time.Clock()


finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    pg.display.update()