import pygame as pg
from pygame.draw import circle

s = pg.display.set_mode((640, 480))
clock = pg.time.Clock()

GREEN = (237, 255, 217)
VIOLET = (139, 55, 204)
ORANGE = (255, 189, 56)

circle_x = 320  # начальные координаты круга
circle_y = 240  # начальные координаты круга
r = 70  # радиус круга
change_x = 0  # изменение начальных координат
change_y = 0  # изменение начальных координат

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.KEYDOWN:  # если нажали кнопку на клавиатуре
            print(f'Key pressed: {pg.key.name(event.key)}')
            if event.key == pg.K_ESCAPE:  # если нажали на esc
                change_x = 0
                change_y = 0
            elif event.key == pg.K_LEFT:  # если нажали на кнопку стрелка_
                change_x = -0.5  # уменьшаю х (двигаюсь влево)
                change_y = 0  # запрещаю двигаться вертикально, когда двигаюсь горизонтально
            elif event.key == pg.K_RIGHT:  # если нажали на кнопку стрелка_
                change_x = 0.5  # увеличиваю х (двигаюсь вправо)
                change_y = 0  # запрещаю двигаться вертикально, когда двигаюсь горизонтально
            elif event.key == pg.K_UP:  # если нажали на кнопку стрелка_
                change_y = -0.5  # уменьшаю у (двигаюсь вверх)
                change_x = 0  # запрещаю двигаться горизонтально, когда двигаюсь вертикально
            elif event.key == pg.K_DOWN:  # если нажали на кнопку стрелка_
                change_y = 0.5  # увеличиваю у (двигаюсь вниз)
                change_x = 0  # запрещаю двигаться горизонтально, когда двигаюсь вертикально

    s.fill(GREEN)  # заливаю экран, чтобы можно было убрать старые объекты
    player = circle(s, ORANGE, [circle_x, circle_y], r)
    mob = circle(s, VIOLET, [200, 200], 30)
    pg.display.update()

    if circle_x == 100 and circle_y == 100:  # если координаты двух объектов совпадают
       VIOLET = (0, 0, 0)  # моб становится черным


    circle_x += change_x  # заставляю объект двигаться по иксу
    circle_y += change_y  # заставляю объект двигаться по игреку

    if (circle_x > 640) or (circle_x < 0) or (circle_y > 480) or (circle_y < 0):
        change_y, change_x = 0, 0  # останавливаю объект
        circle_x = 640 / 2  # помещаю его в центр экрана
        circle_y = 480 / 2  # помещаю его в центр экрана
