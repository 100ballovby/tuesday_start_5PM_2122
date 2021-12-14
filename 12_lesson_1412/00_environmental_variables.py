import os

# environ - метод, возвращающий словарь, который
# состоит из переменных окружения и их значений
for var in os.environ:  # для каждой переменной
    print(f'Переменная: {var}')
    print(f'Значения: {os.environ.get(var)} \n')

if os.environ.get('PS1') == 'venv':
    print('Привет!')
else:
    print('Пока!')
