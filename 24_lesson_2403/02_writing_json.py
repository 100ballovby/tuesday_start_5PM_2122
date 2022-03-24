import json

with open('numbers.json', 'r') as f:
    data = json.load(f)  # преобразовать json в удобный формат данных
    print(data[3])


