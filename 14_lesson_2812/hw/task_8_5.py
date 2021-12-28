"""8-5. Города: напишите функцию describe_city(), которая получает названия
города и страны. Функция должна выводить простое сообщение (например,
«Reykjavik is in Iceland»). Задайте параметру страны значение по умолчанию.
Вызовите свою функцию для трех разных городов, по крайней мере один из которых
не находится в стране по умолчанию."""


def describe_city(city, country='Iceland'):
    msg = f'{city.capitalize()} is in {country.capitalize()}!'
    return msg

for town in ['Selfoss', 'Husavik', 'Washington']:
    print(describe_city(town))