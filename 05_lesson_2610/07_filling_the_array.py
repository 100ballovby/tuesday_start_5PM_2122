import random as r

r_list = []  # создаю пустой список
for n in range(30):  # повторить 30 раз
    r_list.append(r.randint(1, 300))  # добавить случайное число

print(r_list)


