import random as r

question = input('Задай вопрос: ')
answer = r.randint(1, 3)

if answer == 1:  # если сгенерировалось число 1
    print('Да!')
elif answer == 2:  # иначе если сгенерировалось число 2
    print('Нет!')
else:
    print('Наверное!')


