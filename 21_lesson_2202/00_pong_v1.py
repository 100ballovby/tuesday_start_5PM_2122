import pygame as pg
from pygame.draw import rect, circle, polygon, aaline, ellipse


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
    elif obj.left <= 0 or obj.right > width:  # если мяч ударился об правую или левую границу экрана
        ball_speed_x *= -1  # направить его в противоположную сторону

    if obj.colliderect(plr) or obj.colliderect(enm):  # если мяч коснулся игрока или врага
        ball_speed_x *= - 1  # отбить мяч в другую сторону


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

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    # Game logic
    ball_motion(ball, W, H, player, opponent)

    # Visuals
    screen.fill(bg_color)
    rect(screen, blue, player)
    rect(screen, blue, opponent)
    ellipse(screen, blue, ball)
    aaline(screen, blue, [W // 2, 0], [W // 2, H])

    pg.display.update()