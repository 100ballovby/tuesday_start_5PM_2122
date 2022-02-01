import pygame as pg
from pygame.draw import rect, circle, polygon
from random import randrange  # для случайных координат появления еды

W = 400
H = 300
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

BLUE = (74, 143, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 74, 74)

x1 = 200  # змея появляется в этих координатах
y1 = 200  # змея появляется в этих координатах
x1_change = 0  # изменение положения змеи в пространстве
y1_change = 0  # изменение положения змеи в пространстве
snake_block = 10  # размер змеи
speed = 5

food_x = round(randrange(0, W - snake_block) / 10) * 10  # случайные координаты появления еды
food_y = round(randrange(0, H - snake_block) / 10) * 10  # случайные координаты появления еды

pg.font.init()  # чтобы работали надписи на экране
font_style = pg.font.SysFont('comicsans', 20)  # (название_шрифта, размер_шрифта)

finished = False
pause = False
while not finished:
    while pause:  # пока игра стоит "на паузе"
        screen.fill(WHITE)
        message = font_style.render('Нажмите C, чтобы продолжить, или ESC, чтобы выйти', True, BLACK)
        screen.blit(message, [100, 100])
        pg.display.update()

        # цикл обработки событий в паузе
        for pause_event in pg.event.get():
            if pause_event.type == pg.KEYDOWN:
                if pause_event.key == pg.K_ESCAPE:  # если нажали ESC, завершить игру
                    pause = False  # выключить паузу
                    finished = True  # выключить игру
                elif pause_event.key == pg.K_c:  # если нажали С, "начать игру заново"
                    x1 = 100
                    y1 = 100
                    pause = False

    clock.tick(speed)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.KEYDOWN:  # если кто-то нажал на кнопку
            if event.key == pg.K_RIGHT:  # pg.K_d  wasd
                x1_change = snake_block
                y1_change = 0
            elif event.key == pg.K_LEFT:  # pg.K_a
                x1_change = -snake_block  # сдвигаю змею по горизонтали на расстояние, равное ее размеру
                y1_change = 0
            elif event.key == pg.K_UP:  # pg.K_w
                x1_change = 0
                y1_change = -snake_block  # сдвигаю змею по вертикали на расстояние, равное ее размеру
            elif event.key == pg.K_DOWN:  # pg.K_s
                x1_change = 0
                y1_change = snake_block

    if (x1 >= W or x1 < 0) or (y1 >= H or y1 < 0):  # если коснулись стены
        pause = True  # остановить игру

    x1 += x1_change
    y1 += y1_change
    screen.fill(WHITE)
    rect(screen, BLUE, [x1, y1, snake_block, snake_block])
    rect(screen, RED, [food_x, food_y, snake_block, snake_block])
    pg.display.update()

    if x1 == food_x and y1 == food_y:
        print('я поела')
        food_x = round(randrange(0, W - snake_block) / 10) * 10  # случайные координаты появления еды
        food_y = round(randrange(0, H - snake_block) / 10) * 10
