from turtle import *

t = Turtle()
t.shape('turtle')
step = 10

for figure in range(10):  # рисование фигур
    for square in range(4):
        t.fd(step)
        t.lt(90)

    step += 15

    t.up()
    t.rt(135)
    t.fd(10)
    t.lt(135)
    t.down()

done()
