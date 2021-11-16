import string
import random as r

length = int(input('Какой длины пароль? '))
passw = ''  # Здесь храню пароль
symbols = string.ascii_letters + string.digits + string.punctuation

for i in range(length):
    passw += r.choice(symbols)

print(passw)

