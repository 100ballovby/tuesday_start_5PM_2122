n = int(input('Введите количество учеников: '))
marks = []

for student in range(n):
    mark = int(input('Введите оценку: '))
    marks.append(mark)

print(f'Среднее арифметическое: {sum(marks) / n}.')
print(f'Наибольшее {max(marks)}')
print(f'Наименьшее {min(marks)}')

