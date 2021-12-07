import json
import requests as r
from requests.exceptions import HTTPError

urls = ['https://google.com/efjgerkj',
        'https://api.github.com/']

for url in urls:  # для каждой ссылки в списке
    try:
        response = r.get(url)
        response.raise_for_status()  # ждать ответа с кодом

        # немного JSONчика
        json_obj = response.content  # метод .content возвращает содержание ответа в виде битов
        # превращаю json объект в обычный словарь Python (парсинг)
        parsed = json.loads(json_obj)  # loads() превращает JSON-объект в словарь Python
        print(parsed['user_url'])

    except HTTPError as h_e:  # сохраняю результат ошибки в переменной
        print(f'HTTP error occurred {h_e}')  # и вывожу ее для ознакомления с текстом ошибки
    except Exception as e:  # Exception - главный класс ВСЕХ исключений. При срабатывании любой ошибки, вызывается сначала он
        print(f'Other error occurred {e}')
    else:  # иначе
        print(f'Successfully! Code: {response.status_code}')  # вывожу сообщение об упехе



