import json


def read_json(filename):
    with open(filename) as file:
        data = json.loads(file.read())
    return data

cur_code = read_json('currencies.json')  # коды валют
change = read_json('rates.json')  # курсы валют к доллару

for rate in change['data']['rates']:
    print(rate, change['data']['rates'][rate])
