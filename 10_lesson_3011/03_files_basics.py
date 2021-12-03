''' Режимы работы с файлами
r - read (чтение)
w - write (запись)
r+ / w+ - read + smth_special / write + smth_special (чтение-запись)
a - append (добавления)
'''
with open('test.txt', 'w') as file:  # открываю и сразу присваиваю переменной файл
    file.write('Я создал файл!')

with open('test.txt', 'w') as file:
    text = 'Это новый текст для файла'
    file.write(text)

with open('test.txt', 'a') as file:
    text = '\nМеня добавили в текст!\nПривет!'
    file.write(text)