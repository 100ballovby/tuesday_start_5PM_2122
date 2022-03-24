with open('pi_digits.txt') as f_obj:
    for line in f_obj:
        print(line)

with open('pi_million_digits.txt') as file:
    lines = file.readlines()  # читает файл построчно, создавая при этом список
    pi_digits = ''
    for line in lines:
        pi_digits += line.strip()  # убирает лишние пробелы

    birthday = input('Введите дату рождения в формате ДДММГГ: ')
    if birthday in pi_digits:
        print('Ваша дата рождения есть в числе π!')
    else:
        print('Вашей даты рождения нет =(')
    #print(pi_digits)
    print(len(pi_digits))
