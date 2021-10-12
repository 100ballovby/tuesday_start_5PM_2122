from turtle import *
"""Паук"""
t = Turtle()
t.shape('turtle')

k = 1  # будет считать длину дуги
fi_rad = 0.1  # угол поворота в радианах
fi_deg = fi_rad * (180 / 3.14)  # угол поворота в градусах

for i in range(1000000):
    ring = k * fi_rad  # фактическая длина дуги
    t.fd(ring)
    t.lt(fi_deg)
    fi_rad += 0.01
    ring += ring

done()
