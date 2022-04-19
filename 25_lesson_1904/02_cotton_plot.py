import json
import matplotlib.pyplot as plt


days = []  # даты
quantities = []  # количество хлопка
filename = 'series_COTTON.json'
with open(filename) as jf:
    data = json.loads(jf.read())  # читаем содержимое файла и преобразовываем его в словарь
    data = data['data']['rates']
    for line in data:
        try:  # попытаться достать данные и распечатать их
            count = data[line]['COTTON']  # количество хлопка
            day = line  # день
            days.append(day)
            quantities.append(count)
        except:  # если возникает ошибка
            pass  # ничего не делать


plt.title('Количество хлопка за $1')
plt.ylabel('Количество хлопка')
crop_days = list(range(0, 190, 10))  # строю список на 189 элементов, пропускаю по 10 элементов
plt.xticks(crop_days, rotation=45, fontsize=7)  # позволяет управлять декорациями осей
plt.grid()
plt.plot(days, quantities, color='#e834eb',
         linewidth=4)
plt.savefig('gas.jpg')  # сохраняю диаграмму в файл (расширение может быть любым)
plt.savefig('gas.pdf')
plt.show()


