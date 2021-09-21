'''
Метод - это такая штука, которая либо
изменяет объект, либо добавляет дополнительные
свойства
'''

# .lower(), .upper() - приводят символы в строке в нижний/верхний регистр
login = 'zodiac'
login2 = 'Zodiac'
print(login == login2.lower())
print(login.lower())
print(login.upper())

# .isupper(), .islower(), .isdigit()
# проверяют, является ли символ большим, маленьким или числом
print('f'.isupper())  # False
print('f'.islower())  # True
print('4.56'.isdigit())  # False

# replace(x, y) - заменяет символ x символом y
phrase = 'Привет! Я разработчик!'
print(phrase.replace('а', '@'))
print(phrase.replace('разработчик', 'пианист'))
print(phrase.replace('?', 'пианист'))

