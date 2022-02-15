import pygame as pg
from pygame.draw import rect, circle
from random import randint

W = 1280
H = 640
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

# расположение платформы
player_x = W // 2
player_y = 580

# расположение шарика
enemy_x = randint(0, W)
enemy_y = 0


finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True

    screen.fill((255, 255, 255))

    platform = rect(screen, (0, 0, 0), [player_x, player_y, 200, 50])
    enemy = circle(screen, (255, 0, 0), [enemy_x, enemy_y], 40)

    pg.display.update()

    # перемещение платформы по кнопкам
    keys = pg.key.get_pressed()  # функция отслеживает нажатия на кнопки
    if keys[pg.K_LEFT]:
        player_x -= 30
    if keys[pg.K_RIGHT]:
        player_x += 30

    # движение шарика
    enemy_y += 15
    if enemy_y > H:
        enemy_y = 0
        enemy_x = randint(0, W)

