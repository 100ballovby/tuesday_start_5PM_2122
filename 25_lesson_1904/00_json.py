import json


filename = 'series_COTTON.json'
with open(filename) as jf:
    data = json.loads(jf.read())  # читаем содержимое файла и преобразовываем его в словарь
    data = data['data']['rates']
    for line in data:
        try:  # попытаться достать данные и распечатать их
            count = data[line]['COTTON']  # количество хлопка
            day = line  # день
            print(day, count * 0.454)
        except:  # если возникает ошибка
            pass  # ничего не делать
