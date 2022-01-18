import pygame as pg
from pygame.draw import circle

# настроим окно программы
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
end = False

x = 135  # начальные точки первого кольца
y = 240  # начальные точки первого кольца
for i in range(4):  # повторить 4 раза
    circle(screen, (128, 128, 128), [x, y], 80, 10)  # нарисовать кольцо
    x += 120  # изменить x

pg.display.update()
while not end:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end = True

    pg.display.update()

