import os
import requests
from datetime import datetime  # библиотека для работы с датами

url = "https://yahoo-weather5.p.rapidapi.com/weather"

querystring = {"location": "minsk", "format": "json", "u": "c"}

headers = {
    'x-rapidapi-host': "yahoo-weather5.p.rapidapi.com",
    'x-rapidapi-key': os.environ.get('API_KEY')
    }

response = requests.request("GET", url, headers=headers, params=querystring)
json_response = response.json()  # перевожу ответ сервера в JSON-формат

for key in json_response['forecasts']:
    date = datetime.fromtimestamp(key['date']).strftime('%d.%m.%Y')
    print(f'{key["day"]}, {date}, Днем: {key["high"]}, Ночью: {key["low"]}')

# {'day': 'Tue', 'date': 1639450800, 'low': -3, 'high': 0, 'text': 'Cloudy', 'code': 26}
