shop = {
    'grape': 5.45,
    'ham': 7.98,
    'banana': 2.12,
    'orange': 1.39,
    'cookies': 4.13,
}
# обращение к элементу словаря
print(shop['ham'])

# добавление пары в словарь
shop['lime'] = 3.15
print(shop)

# изменение значения
shop['banana'] = 4.56
print(shop)

# удаление
del shop['orange']
print(shop)

