import requests  # работа с сетью (выход в интернет) [в терминале pip install requests]
import json  # работа с json-файлами

url = 'https://api.github.com/users/GreatRaksin/repos'
response = requests.get(url)  # подключась к сайту в переменной url
repos = json.loads(response.text)

for repo in repos:
    print(repo['svn_url'])

"""Необходимо найти все репозитории, где главным языком программирования
является Python. А затем вывести эти репозитории в формате: 

Name: {name}
URL: {svn_url}
Language: {language}

!!!!🤩🤩🤩🤩!!!!
Сделать список словарей, который будет хранить всю 
информацию из первой части задачи 
"""