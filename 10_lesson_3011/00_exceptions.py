"""
try:
    do_smth()
except:
    do_another()

Type of Exception:
TypeError - неправильно подобранный тип данных
ImportError - ошибка импорта
IndexError - обращение к несуществующему индексу списка
NameError - некорректное имя переменной
ValueError - неправильный тип данных аргумента
ZeroDivisionError - деление на 0
ArithmeticError - ошибка вычислений (их много)
"""
divider = int(input('Введите число: '))

try:  # попробовать выполнить это:
    print(34768 / divider)  # разделить число на значение переменной
except ArithmeticError:  # если возникла ошибка вычислений
    print('На 0 делить нельзя!')

print('hello')
