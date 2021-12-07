"""Необходимо найти все репозитории, где главным язком программирования
является Python. А затем вывести эти репозитории в формате:

Name: {name}
URL: {svn_url}
Language: {language}

!!!!🤩🤩🤩🤩!!!!
Сделать список словарей, который будет хранить всю
информацию из первой части задачи
"""
import json
import requests as r
from requests.exceptions import HTTPError

rep_log = []  # список всех репозиториев

try:
    url = 'https://api.github.com/users/GreatRaksin/repos'
    response = r.get(url)  # обращаюсь к серверу
    reps = json.loads(response.content)
    for rep in reps:  # перебираю каждый репозиторий из найденных
        if rep['language'] == 'Python':  # основной ЯП репозитория - Python
            rep_log.append({
                'name': rep['name'],
                'url': rep['html_url'],
                'language': rep['language']
            })  # формирую список словарей

    json_obj = json.dumps(rep_log, indent=4)  # превращаю список словарей в JSON
    with open('GR_github.json', 'w') as f:
        f.write(json_obj)  # записываю объект в файл .json

except HTTPError as h_e:
    print(f'Error: {h_e}')