def power(n, deg=2):
    """Возводит n степень deg"""
    res = 1  # 1 потому что числа нужно перемножать, а на 1 умножать удобно
    for i in range(deg):  # deg раз
        res *= n  # перемножаю числа
    return res

# позиционные аргументы
print(power(2, 9))
# поименные аргументы
print(power(deg=9, n=2))
# аргументы по умолчанию
print(power(3, 3))
print(power(10, 5))
print(power(7))  # степень равна 2
