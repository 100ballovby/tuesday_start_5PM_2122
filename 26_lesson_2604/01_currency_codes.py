import json

with open('currencies.json') as file:
    cur = json.loads(file.read())
    cur = cur['data']  # захожу в список ключа data
    for currency in cur:
        print(f'Code: {currency["id"]}, Name: {currency["name"]}')


