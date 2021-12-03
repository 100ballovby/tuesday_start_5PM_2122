import os

cwd = os.getcwd()  # CWD - current working directory
print(cwd)

entries = os.listdir(cwd)  # просматриваю все вложенные элементы рабочей директории
print(entries)

for obj in entries:  # просматриваю каждый объект в рабочей папке
    if os.path.isfile(obj):  # если тип объекта = файл
        with open(obj, 'r') as f:
            print(f.read(), '\n\n\n\n')
