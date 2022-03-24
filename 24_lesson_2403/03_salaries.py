import json
import csv

with open('salaries.json') as f:
    data = json.loads(f.read())
    headers = ['Год', 'з/п в руб.', 'Курс $', 'з/п в $']
    with open('salaries.csv', 'w', encoding='UTF-8', newline='') as table:
        writer = csv.writer(table)  # буду записывать что-то в открытую таблицу
        writer.writerow(headers)  # записываю заголовки таблицы
        for year in data:  # перебираю данные из объекта JSON
            fee = data[year]["fee"]
            rate = data[year]['dollar_rate']
            line = [year, fee, rate, fee / rate]  # создаю строку
            writer.writerow(line)  # записываю строку в таблицу
