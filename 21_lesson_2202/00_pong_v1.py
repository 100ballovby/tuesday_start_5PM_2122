import pygame as pg
from pygame.draw import rect, circle, polygon, aaline, ellipse

W = 1280
H = 720
screen = pg.display.set_mode((W, H))
pg.display.set_caption('Pong game Python🏓')
clock = pg.time.Clock()

# Colors
bg_color = (224, 224, 224)
blue = (143, 218, 255)

# Game objects
ball = pg.Rect(W // 2 - 15, H // 2 - 15, 30, 30)
player = pg.Rect(W - 20, H // 2, 10, 150)
opponent = pg.Rect(10, H // 2, 10, 150)

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    # Visuals
    screen.fill(bg_color)
    rect(screen, blue, player)
    rect(screen, blue, opponent)
    ellipse(screen, blue, ball)
    aaline(screen, blue, [W // 2, 0], [W // 2, H])

    pg.display.update()