import pygame as pg
from pygame.draw import rect, circle, polygon
import random as r


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


def paddle_moving(obj, surf, s_height, jump):
    global score, high_score

    if obj.y >= s_height:  # если препятствие ушло за пределы экрана
        x = r.randint(1, 3)
        if x == 1:
            obj.x = surf.x  # ставлю препятствие слева (по левому краю дороги)
        elif x == 2:
            obj.center = surf.center  # ставлю препятствие посередине
        else:
            obj.right = surf.right  # ставлю препятствие справа (по правому краю дороги)
        obj.y = -jump  # отправляю препятствие наверх
        score += 1
    if score > high_score:  # если текущие очки больше рекорда
        high_score = score  # рекорд и есть очки


def show_text(text, size, color, x, y, surf):
    pg.font.init()
    font = pg.font.SysFont('comicsans', size)
    msg = font.render(text, True, color)
    surf.blit(msg, [x, y])


WHITE = (255, 255, 255)
GREEN = (7, 115, 14)
SAND = (255, 237, 181)
GRAY = (64, 64, 64)
RED = (201, 22, 55)
ORANGE = (255, 155, 48)

W = 800
H = 900

screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

# Game objects
road = pg.Rect(0, 0, W // 2, H)
road.center = W // 2, H // 2
border_left = pg.Rect(road.left - W * 0.1, 0, W * 0.1, H)
border_right = pg.Rect(road.right, 0, W * 0.1, H)

road_width = road.width  # измеряет ширину дороги
paddle1 = pg.Rect(road.x, -50, road_width * 0.3, 30)  # препятствие №1
paddle2 = pg.Rect(road.x, -H // 2, road_width * 0.3, 30)  # препятствие №2

score_rect = pg.Rect(20, 20, W * 0.15, H * 0.05)
high_score_rect = pg.Rect(20, score_rect.bottom + 10, W * 0.21, H * 0.05)
start_btn = pg.Rect(0, 0, W * 0.2, H * 0.1)  # кнопка запуска игры
start_btn.center = W // 2, H // 2  # расположить кнопку посередине

# Images
img = pg.image.load('car.png').convert_alpha()  # загружаю картинку машины
img_rect = img.get_rect()  # превращаю картинку в объект
center = W // 2, H * 0.85  # указываю координаты появления машины
img_rect.center = center  # ставлю машину в координаты
car = img  # клон картинки
car_rect = img_rect  # клон объекта

tree1 = pg.image.load('tree-3.png').convert_alpha()
tree1_rect = tree1.get_rect()
tree2 = pg.image.load('tree-3.png').convert_alpha()
tree2_rect = tree2.get_rect()

tree1 = pg.transform.scale(tree1, [W * 0.1, H * 0.2])  # ширина 10% от ширины экрана, высота - 20% от высоты экрана
# scale(что_меняем, [ширина, высота])
tree2 = pg.transform.scale(tree2, [W * 0.1, H * 0.2])
tree1_rect.x = 10
tree1_rect.y = -(H * 0.2)
tree2_rect.x = W - 90
tree2_rect.y = -(H * 0.8)

car_speed = 0  # начальная скорость машины
angle = 0  # начальный градус поворота машины
speed = 10  # общее значение скорости для всех объектов в игре
score = 0
high_score = 0

finished = False
game_over = False
while not finished:

    while game_over:
        screen.fill(WHITE)
        rect(screen, GREEN, start_btn)  # рисую кнопку перезапуска

        rect(screen, ORANGE, score_rect)
        rect(screen, ORANGE, high_score_rect)
        show_text(f'Score {score}', 24, WHITE, score_rect.x, score_rect.y, screen)
        show_text(f'High score {high_score}', 24, WHITE, high_score_rect.x, high_score_rect.y, screen)
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = False
                finished = True
            if event.type == pg.MOUSEBUTTONDOWN:  # если мышь нажата
                if start_btn.collidepoint(event.pos):  # если мышь над кнопкой старта
                    paddle1.y = 0
                    paddle2.y = - 500
                    game_over = False
                    score = 0

    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                car_speed += speed
                angle = -10
            if event.key == pg.K_LEFT:
                car_speed -= speed
                angle = 10
            car = pg.transform.rotate(img, angle)  # поворачиваю картинку на заданный угол
        if event.type == pg.KEYUP:  # если кнопку отпустили
            if event.key == pg.K_RIGHT:
                car_speed -= speed
            if event.key == pg.K_LEFT:
                car_speed += speed
            angle = 0  # угол 0
            car = pg.transform.rotate(img, angle)  # поворачиваю картинку на заданный угол

    # Visuals
    screen.fill(GREEN)  # фон игры (трава)
    rect(screen, GRAY, road)  # дорога
    rect(screen, SAND, border_left)  # левая обочина
    rect(screen, SAND, border_right)  # правая обочина
    rect(screen, WHITE, [(W // 2) - (W * 0.01), 0, W * 0.02, H])  # линия разметки
    rect(screen, RED, paddle1)  # препятствие №1
    rect(screen, RED, paddle2)  # препятствие №2

    screen.blit(car, car_rect)  # отображаю машину в координатах car_rect
    screen.blit(tree1, tree1_rect)
    screen.blit(tree2, tree2_rect)

    rect(screen, ORANGE, score_rect)
    rect(screen, ORANGE, high_score_rect)
    show_text(f'Score {score}', 24, WHITE, score_rect.x, score_rect.y, screen)
    show_text(f'High score {high_score}', 24, WHITE, high_score_rect.x, high_score_rect.y, screen)
    pg.display.update()

    # Game logic
    moving(car_rect, car_speed, border_left, border_right)

    paddle1.y += speed  # препятствие падает вниз
    paddle2.y += speed  # препятствие падает вниз

    paddle_moving(paddle1, road, H, H * 0.2)
    paddle_moving(paddle2, road, H, H * 0.8)

    tree1_rect.y += speed  # дерево летит вниз
    tree2_rect.y += speed  # дерево летит вниз
    if tree1_rect.y >= H:  # если у дерева ушел за пределы экрана
        tree1_rect.y = -(H * 0.2)  # поднять дерево наверх
    if tree2_rect.y >= H:  # если у дерева ушел за пределы экрана
        tree2_rect.y = -(H * 0.8)  # поднять дерево наверх

    # Game over
    if car_rect.colliderect(paddle1) or car_rect.colliderect(paddle2):
        game_over = True
