"""
fd(x) -> идти вперед на х шагов
bk(x) -> идти назад на х шагов
lt(ang) и rt(ang) -> повернуть влево или вправо на ang градусов
goto(x, y) -> перейти в х, у
up() и down() -> поднять/опустить перо
circle(radius) -> нарисовать круг с радиусом radius
"""
from turtle import *  # импорт черепашки
import shapes as sh  # импортирую файл с функциями для рисования фигур

t = Turtle()  # создаю саму черепашку
t.shape('turtle')  # устанавливаю форму черепашки

sh.draw_square(t, 100, 100, 4, 'purple', 100)
sh.draw_star(t, 150, 10, 6, 'green', 100)
sh.draw_square(t, 300, -300, 7, 'red', 120)
sh.draw_square(t, -250, -100, 10, 'yellow')
sh.x_angle(
    turtle=t, x=-170, y=-210, corners=5,
    p_size=5, color='orange', length=75
)

done()  # препятствую закрытию окна сразу после окончания работы
