import math  # импортировать библиотеку математика
print(math.sqrt(49))  # квадратный корень

import random as r  # импортировать библиотеку рандом, как псевдоним
print(r.randint(1, 4))  # случайное число от 1 до 4

from datetime import date, time, datetime, timedelta
# из библиотеки дата-время импортировать функции
print(time())


from math import *  # из библиотеки математика импортировать все
print(sqrt(121))  # получу 11, потому что эта функция отдает квадратный корень


def sqrt(n):
    return n

print(sqrt(144))  # получу 144, потому что в моей функции переписана логика работы функции sqrt()
