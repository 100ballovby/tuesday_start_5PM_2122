import random as r

question = input('Задай вопрос: ')
answer = ['Да!', 'Нет!', 'Наверное...',
          'Не стоит', 'Попробуй', ]

print(r.choice(answer))
