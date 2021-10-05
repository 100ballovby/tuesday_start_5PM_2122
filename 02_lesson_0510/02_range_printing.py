start = int(input('С чего начать прогрессию? '))
stop = int(input('Чем закончить прогрессию? '))
step = int(input('Шаг прогрессии? '))

my_object = range(start, stop, step)
iterator = 0

while start < (stop - 2):
    print(my_object[iterator])
    iterator += 1
