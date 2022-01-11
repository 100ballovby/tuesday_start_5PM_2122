import pygame as pg

# настроим окно программы
screen = pg.display.set_mode((640, 480))  # размер окна 640х480 пикселей
clock = pg.time.Clock()  # отвечает за сменяемость кадров
end = False  # пока end=false, игра будет работать

screen.fill((219, 232, 255))  # залить фон цветом в формате RGB
# иногда нужно отобразить на экране игры что-то до начала
pg.display.update()  # обновляю кадры на экране
while not end:  # пока игра не окончена (while True, потому что not False = True)
    clock.tick(30)  # задержка между кадрами
    for event in pg.event.get():  # для каждого события в очереди событий
        if event.type == pg.QUIT:  # когда нажали на крестик в окне
            end = True  # выключить игру

    pg.display.update()  # обновить экран с объектами

