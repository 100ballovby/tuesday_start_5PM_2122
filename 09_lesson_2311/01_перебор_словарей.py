food = {
    'Борис': 'роллы',
    'Евгений': 'пирожок',
    'Яна': 'котлеты',
}

for key in food.keys():
    print(f'Ключ: {key};')

for value in food.values():
    print(f'Значение: {value};')

for key, value in food.items():  # .items() возвращает список кортежей, каждый кортеж я распаковываю на две переменные
    print(f'{key} любит кушать {value}!')


