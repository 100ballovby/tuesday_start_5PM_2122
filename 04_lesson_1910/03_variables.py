# a = b = c = 0

a, b, c = 5, 3, 11
print(f'''
a = {a}
b = {b}
c = {c}
''')
a = 5
b = 2
a, b = b, a
print(f'a = {a}, b = {b}')