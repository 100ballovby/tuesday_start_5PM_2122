import json

person = {'name': 'John', 'lastName': 'Silver', 'city': 'Minsk'}
# dumps() переводит Python словарь в JSON объект
j = json.dumps(person, indent=4)  # indent - выстраивает отступы в готовом JSONе
print(j)


