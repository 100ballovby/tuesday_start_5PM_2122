import json
import requests as r
from requests.exceptions import HTTPError

url = 'https://api.github.com/search/repositories'

try:
    p = {'q': 'game', 'l': 'python'}  # q - что ищем (запрос) l - язык программрования
    response = r.get(url, params=p)
    p_d = json.loads(response.content)

    for repo in p_d['items']:
        print(f'Name: {repo["name"]}; URL: {repo["html_url"]}')

except HTTPError as h_e:  # сохраняю результат ошибки в переменной
    print(f'HTTP error occurred {h_e}')


