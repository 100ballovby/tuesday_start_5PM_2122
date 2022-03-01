import pygame as pg
from pygame.draw import rect, circle, polygon, aaline, ellipse
import random as r


def ball_motion(obj, width, height, plr, enm):
    """
    Функция движения мяча по игровому полю
    :param obj: игровой объект-мяч
    :param width: ширина экрана
    :param height: высота экрана
    :param plr: игровая ракетка
    :param enm: ракетка-враг
    :return: None
    """
    global ball_speed_x, ball_speed_y

    obj.x += ball_speed_x
    obj.y += ball_speed_y

    if obj.top <= 0 or obj.bottom > height:  # если мяч ударился об нижнюю или верхнюю часть экрана
        ball_speed_y *= -1  # направить его в противоположную сторону

    elif obj.left <= 0:
        restart(width, height, obj)
    elif obj.right > width:  # если мяч ударился об правую или левую границу экрана
        restart(width, height, obj)  # направить его в противоположную сторону

    if obj.colliderect(plr) or obj.colliderect(enm):  # если мяч коснулся игрока или врага
        ball_speed_x *= - 1  # отбить мяч в другую сторону


def opponent_ai(enm, self_speed, height, obj):
    """
    Функция автоматического передвижения платформы-оппонента по игровому полю
    :param enm: платформа-оппонент
    :param self_speed: скорость передвижения
    :param height: высота экрана
    :param obj: игровой объект-мяч
    :return: None
    """
    if enm.top < obj.y:  # если верхняя граница платформы ниже Y мяча
        enm.y += self_speed
    elif enm.bottom > obj.y:  # если нижняя граница платформы выше Y мяча
        enm.y -= self_speed

    if enm.top <= 0:  # если верхняя граница платформы выше верхней границы экрана
        enm.top = 0  # остановить платформу в Y = 0
    elif enm.bottom >= height:  # если нижняя граница платформы ниже нижней границы экрана
        enm.bottom = height  # остановить платформу в Y = H


def player_motion(plr, speed, height):
    plr.y += speed

    if plr.top <= 0:
        plr.top = 0
    elif plr.bottom >= height:
        plr.bottom = height


def restart(width, height, obj):
    global ball_speed_x, ball_speed_y

    obj.center = (width // 2, height // 2)  # ставим мяч в центр экрана
    ball_speed_x *= r.choice([-1, 1])
    ball_speed_y *= r.choice([-1, 1])

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

# Game variables
speed = 8
ball_speed_x = speed
ball_speed_y = speed
opponent_speed = speed
player_speed = 0

# Score text
pg.font.init()
player_score = 0
opponent_score = 0


def show_score(size, color, x, y, text):
    basic_font = pg.font.SysFont('comicsans', size)
    msg = basic_font.render(text, True, color)
    screen.blit(msg, [x, y])

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.KEYDOWN:  # если кнопка нажата
            if event.key == pg.K_UP:  # если нажали на стрелку вверх
                player_speed -= speed
            if event.key == pg.K_DOWN:  # если нажали на стрелку вниз
                player_speed += speed
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                player_speed += speed
            if event.key == pg.K_DOWN:
                player_speed -= speed

    # Game logic
    ball_motion(ball, W, H, player, opponent)
    opponent_ai(opponent, opponent_speed, H, ball)
    player_motion(player, player_speed, H)

    # Visuals
    screen.fill(bg_color)
    rect(screen, blue, player)
    rect(screen, blue, opponent)
    ellipse(screen, blue, ball)
    aaline(screen, blue, [W // 2, 0], [W // 2, H])

    show_score(63, blue, W // 2 + 20, H // 2, f'{player_score}')
    show_score(63, blue, W // 2 - 60, H // 2, f'{opponent_score}')

    pg.display.update()