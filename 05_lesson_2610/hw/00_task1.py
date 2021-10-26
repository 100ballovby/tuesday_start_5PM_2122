n = int(input('Введите количество учеников: '))
summ = 0

for student in range(n):  # повторить n раз
    mark = int(input(f'Введите оценку {student + 1} студента: '))  # спросить оценку
    summ += mark  # "посчитать" ее

print(f'Среднее арифметическое: {summ / n}.')
