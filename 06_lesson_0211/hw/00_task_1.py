n = int(input('Введите количество учеников: '))
marks = []

for student in range(n):
    mark = int(input('Введите оценку: '))
    marks.append(mark)

summ = 0
for mark in marks:
    summ += mark
print(summ / n)

minimum = 10
maximum = 0
for mark in marks:
    if mark < minimum:
        minimum = mark

for mark in marks:
    if mark > maximum:
        maximum = mark
        
print('Наибольшее: ', maximum)
print('Наименьшее: ', minimum)

