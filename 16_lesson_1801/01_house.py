import pygame as pg
from pygame.draw import rect, circle, polygon

WIDTH = 1280
HEIGHT = 720
FPS = 30
LINE = WIDTH / 256

R = HEIGHT * 0.12
SUN_X = 0 - R
SUN_Y = HEIGHT * 0.2

colors = {
    'green': (99, 199, 126),
    'blue': (230, 255, 252),
    'yellow': (255, 253, 150),
    'tree_green': (69, 122, 59),
    'brick': (230, 221, 188),
    'dark_brick': (191, 182, 147),
    'terr': (237, 204, 180),
    'dark_terr': (207, 173, 149),
    'brown': (64, 37, 18),
    'cyan': (57, 84, 158)
}

s = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

pg.display.update()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    rect(s, colors['blue'], [0, 0, WIDTH, HEIGHT * 0.6])
    rect(s, colors['green'], [0, HEIGHT * 0.6, WIDTH, HEIGHT * 0.4])

    # нарисую домик
    house_x = WIDTH * 0.1
    house_y = HEIGHT * 0.35
    house_width = WIDTH * 0.3
    house_height = HEIGHT * 0.4

    rect(s, colors['brick'], [house_x, house_y, house_width, house_height])
    rect(s, colors['dark_brick'], [house_x, house_y, house_width, house_height], 4)

    # солнце
    circle(s, colors['yellow'], [SUN_X, SUN_Y], R)

    # нариcую крышу
    polygon(s, colors['terr'], [
        [house_x - 20, house_y],
        [house_x + house_width + 20, house_y],
        [house_x + (house_width / 2), house_y - 160]
    ])
    polygon(s, colors['dark_terr'], [
        [house_x - 25, house_y],
        [house_x + house_width + 20, house_y],
        [house_x + (house_width / 2), house_y - 160]
    ], 4)

    # нарисуем дверь
    door_x = house_x + (house_x * 0.35)
    door_y = house_y + (house_y * 0.3)
    rect(s, colors['brown'], [door_x, door_y, house_width * 0.3, house_height * 0.72])
    circle(s, colors['yellow'], [door_x + (door_x * 0.53), door_y + (door_y * 0.3)], 10)

    # нарисуем окно
    rect(s, colors['cyan'], [door_x + (door_x * 0.8), door_y,
                             house_width * 0.45, house_height * 0.35], border_radius=15)
    rect(s, colors['dark_brick'], [door_x + (door_x * 0.8), door_y,
                             house_width * 0.45, house_height * 0.35], 5, border_radius=15)

    pg.display.update()

    if SUN_X > WIDTH + R:  # если солнце зашло за пределы правой границы экрана
        SUN_X = 0 - R  # вернуть его налево
    else:  # иначе
        SUN_X += 5  # сдвигать направо