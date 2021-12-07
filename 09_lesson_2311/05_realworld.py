import requests  # работа с сетью (выход в интернет)
import json  # работа с json-файлами

url = 'https://jsonplaceholder.typicode.com/todos'
response = requests.get(url)  # подключась к сайту в переменной url
todos = json.loads(response.text)

for todo in todos:
    if todo['userId'] == 4 and todo['completed']:
        print(todo)


