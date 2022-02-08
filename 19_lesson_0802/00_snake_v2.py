import pygame as pg
from pygame.draw import rect, circle, polygon
from random import randrange  # для случайных координат появления еды


def draw_snake(block, s_list):
    for x in s_list:  # для каждой пары координат
        snake = rect(screen, BLUE, [x[0], x[1], block, block])  # рисую сегмент змейки
    return snake  # возвращаю сегмент змеи

W = 1600
H = 900
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

BLUE = (74, 143, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 74, 74)


def game_loop():
    x1 = 200  # змея появляется в этих координатах
    y1 = 200  # змея появляется в этих координатах
    x1_change = 0  # изменение положения змеи в пространстве
    y1_change = 0  # изменение положения змеи в пространстве
    snake_block = 30  # размер змеи
    speed = 15
    snake_list = []
    snake_length = 1

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
                        game_loop()  # вызываю функцию, я обнуляю всю игру (начинаю ее заново)

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

        x1 += x1_change  # изменение координат змеи
        y1 += y1_change  # изменение координат змеи
        screen.fill(WHITE)

        snake_segment = []  # храню координаты каждого сегмента змеи
        snake_segment.append(x1)  # записываю обновленную координату х
        snake_segment.append(y1)  # записываю обновленную координату у
        snake_list.append(snake_segment)  # добавляю координаты сегмента в список со змеей
        if len(snake_list) > snake_length:
            snake_list.pop(0)

        for x in snake_list[:-1]:  # просмотреть все сегменты, кроме головы
            if x == snake_segment:  # если сегмент столкнулся с головой
                pause = True  # остановить игру

        snake = draw_snake(snake_block, snake_list)  # рисую змею
        food = rect(screen, RED, [food_x, food_y, snake_block, snake_block])

        show_score = font_style.render(f'Score {snake_length - 1}',
                                       True, BLACK)
        screen.blit(show_score, [0, 0])

        pg.display.update()

        if snake.colliderect(food):
            snake_length += 1  # длина змеи увеличивается на 1, когда змея ест еду
            food_x = round(randrange(0, W - snake_block) / 10) * 10  # случайные координаты появления еды
            food_y = round(randrange(0, H - snake_block) / 10) * 10

game_loop()
