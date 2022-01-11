import pygame as pg
from pygame.draw import rect, circle, polygon

screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
end = False

screen.fill((219, 232, 255))

# нарисуем прямоугольник
rect(screen, (38, 191, 186), [50, 30, 100, 47])
rect(screen, (178, 191, 186), [180, 30, 100, 47], 7)
# где_рисуем, (цвет в RGB), [x, y, ширина, высота], толщина_линии

# нарисуем круг
circle(screen, (230, 70, 32), [50, 170], 40)
circle(screen, (230, 70, 32), [150, 170], 40, 5)
# где_рисуем, (цвет в RGB), [x, y], радиус, толщина_линии

# нарисуем треугольник
polygon(screen, (111, 32, 254), [[310, 254], [560, 254], [470, 164]])
polygon(screen, (111, 32, 254), [[310, 254], [560, 254], [470, 344]], 2)
# где_рисуем, (цвет в RGB), [[x1, y1], [x2, y2], [x3, y3]],толщина_линии

x_cor = 0  # начальные координаты х
y_cor = 240 # начальные координаты у
for i in range(10):  # повторить 10 раз
    rect(screen, (9, 197, 234), [x_cor, y_cor, 40, 40])  # рисую квадрат
    circle(screen, (255, 255, 255), [x_cor + 20, y_cor + 20], 10)  # рисую круг
    x_cor += 43  # изменяю местоположение фигуры по горизонтали
    y_cor += 43  # изменяю местоположение фигуры по вертикали


pg.display.update()
while not end:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end = True

    pg.display.update()

