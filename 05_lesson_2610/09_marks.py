n = int(input('Сколько студентов? '))
marks = []  # список оценок

for student in range(n):
    marks.append(int(
            input(f'Введите оценку {student + 1} студента: ')
        ))

print(f'Среднее арифметическое {sum(marks) / n}.')

