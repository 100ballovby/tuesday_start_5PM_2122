from turtle import *
"""Паук"""
t = Turtle()
t.shape('turtle')
n = int(input('Введи количество лучей: '))

for line in range(n):
    t.fd(100)
    t.stamp()  # оставить отпечаток черепашки на холсте
    t.bk(100)
    t.lt(360 / n)


done()
