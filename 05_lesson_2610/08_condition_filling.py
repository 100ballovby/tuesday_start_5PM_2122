import random as r

r_list = []  # создаю пустой список
while len(r_list) <= 10:  # пока нет 10 чисел в списке
    r_int = r.randint(1, 50)  # генерировать число
    if (r_int % 2 == 0) and not (r_int in r_list):  # если оно делится на 2
        r_list.append(r_int)  # добавить случайное число

print(r_list)