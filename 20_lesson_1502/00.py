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

score = 3


def show_text(text, color, x, y):
    pg.font.init()
    font = pg.font.SysFont('comicsans', 32)
    txt = font.render(text, True, color)
    screen.blit(txt, [x, y])


finished = False  # флаг, который отвечает за работу программы
pause = False
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True

    while pause:  # пока игра стоит "на паузе"
        screen.fill((255, 255, 255))
        show_text('Press C to continue of ESC to exit', (0, 0, 0), W // 2, H // 2)
        pg.display.update()

        # цикл обработки событий в паузе
        for pause_event in pg.event.get():
            if pause_event.type == pg.KEYDOWN:
                if pause_event.key == pg.K_ESCAPE:  # если нажали ESC, завершить игру
                    pg.quit()
                elif pause_event.key == pg.K_c:  # если нажали С, "начать игру заново"
                    score = 3
                    pause = False

    screen.fill((255, 255, 255))

    platform = rect(screen, (0, 0, 0), [player_x, player_y, 200, 50])
    enemy = circle(screen, (255, 0, 0), [enemy_x, enemy_y], 40)

    # коллизия платформы
    if platform.colliderect(enemy):
        enemy_y = 0
        enemy_x = randint(0, W)
        score += 1

    if platform.right >= W:
        player_x = W - 200
    elif platform.left <= 0:
        player_x = 0

    show_text(f'Score: {score}', (0, 0, 0), 0, 0)
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
        score -= 1

    # проигрыш
    if score <= 0:
        pause = True

