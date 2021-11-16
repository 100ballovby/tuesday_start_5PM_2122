import string
import random as r

length = int(input('Какой длины пароль? '))
passw = ''  # Здесь храню пароль
nums = input('Цифры? (+/-)')
sym = input('Спецсимволы? (+/-)')
raw = string.ascii_letters

if nums == '+' and sym == '+':
    raw += string.digits + string.punctuation
elif nums == '+':
    raw += string.digits
elif sym == '+':
    raw += string.punctuation

for i in range(length):
    passw += r.choice(raw)

print(passw)