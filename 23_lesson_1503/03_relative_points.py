import pygame as pg
from pygame.draw import rect, circle, polygon


def moving(obj, speed, l_side, r_side):
    """
    Функция отвечает за движение машины по экрану игры
    :param obj: игровой объект-машина
    :param speed: скорость передвижения
    :param l_side: левая обочина
    :param r_side: правая обочина
    :return: None
    """
    obj.x += speed  # передвигаю х машины

    if obj.colliderect(l_side):
        obj.left = l_side.right + 5
    if obj.colliderect(r_side):
        obj.right = r_side.left - 5

WHITE = (255, 255, 255)
GREEN = (7, 115, 14)
SAND = (255, 237, 181)
GRAY = (64, 64, 64)
RED = (201, 22, 55)

W = 800
H = 900

screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

# Game objects
road = pg.Rect(0, 0, W // 2, H)
road.center = W // 2, H // 2
border_left = pg.Rect(road.left - W * 0.1, 0, W * 0.1, H)
border_right = pg.Rect(road.right, 0, W * 0.1, H)

img = pg.image.load('car.png').convert_alpha()  # загружаю картинку машины
img_rect = img.get_rect()  # превращаю картинку в объект
center = W // 2, H * 0.85  # указываю координаты появления машины
img_rect.center = center  # ставлю машину в координаты
car = img  # клон картинки
car_rect = img_rect  # клон объекта

car_speed = 0  # начальная скорость машины
angle = 0  # начальный градус поворота машины

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                car_speed += 10
                angle = -10
            if event.key == pg.K_LEFT:
                car_speed -= 10
                angle = 10
            car = pg.transform.rotate(img, angle)  # поворачиваю картинку на заданный угол
        if event.type == pg.KEYUP:  # если кнопку отпустили
            if event.key == pg.K_RIGHT:
                car_speed -= 10
            if event.key == pg.K_LEFT:
                car_speed += 10
            angle = 0  # угол 0
            car = pg.transform.rotate(img, angle)  # поворачиваю картинку на заданный угол

    # Visuals
    screen.fill(GREEN)  # фон игры (трава)
    rect(screen, GRAY, road)  # дорога
    rect(screen, SAND, border_left)  # левая обочина
    rect(screen, SAND, border_right)  # правая обочина
    rect(screen, WHITE, [396, 0, 8, H])  # линия разметки

    screen.blit(car, car_rect)  # отображаю машину в координатах car_rect
    rect(screen, RED, car_rect, 1)

    pg.display.update()

    # Game logic
    moving(car_rect, car_speed, border_left, border_right)