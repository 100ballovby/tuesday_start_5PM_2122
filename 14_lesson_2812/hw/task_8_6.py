"""8-6. Делитель. Напишите функцию, которая принимает 2 значения: число и его делитель.
Функция возвращает результат деления этих двух чисел. Обратите внимание, что функция не должна
ломаться, если в качестве делителя введут 0. (вспомните try...except)"""


def divider(num, div):
    try:
        num = int(num)
        div = int(div)
        res = num / div
        return res
    except (TypeError, ValueError):
        return 'Вы вписали не число!'
    except ArithmeticError:
        return 'Делить на 0 нельзя!'

print(divider(120, 7))
print(divider(19, 'hello'))
print(divider('hello', 'hello'))
print(divider(6, 0))
