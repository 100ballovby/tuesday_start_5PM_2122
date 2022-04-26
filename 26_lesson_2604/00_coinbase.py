import requests as r

mode = ['currencies', 'exchange-rates']
url = f'https://api.coinbase.com/v2/{mode[1]}'
response = r.get(url)  # подключаюсь к апи и сохраняю ответ
# wb - write bytes - записывается не текст, а биты информации
with open('rates.json', 'wb') as file:
    file.write(response.text.encode('utf8'))  # кодирую информацию от сервера в кодировке UTF-8
    # записываю ответ сервера в файл


