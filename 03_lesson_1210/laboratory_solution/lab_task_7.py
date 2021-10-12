from turtle import *
"""Паук"""
t = Turtle()
t.shape('turtle')

steps = 0.01
for i in range(720):
    t.fd(steps)
    t.lt(2)
    steps += 0.01

done()
