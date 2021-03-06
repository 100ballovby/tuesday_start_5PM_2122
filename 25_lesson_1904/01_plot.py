import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7]  # числа
y = [0, 1, 4, 9, 16, 25, 36, 49]  # квадраты чисел
y1 = [0, 1, 8, 27, 64, 125, 216, 343]  # кубы чисел

plt.title('Квадраты чисел')  # название графика
plt.xlabel('Числа')  # подписи к осям графика
plt.ylabel('Степени')  # подписи к осям графика
plt.grid()  # сетка
plt.plot(x, y, y1,
         linewidth=6,
         linestyle='dashed')  # строю график по данным из списков x и у
plt.show()  # показать график


