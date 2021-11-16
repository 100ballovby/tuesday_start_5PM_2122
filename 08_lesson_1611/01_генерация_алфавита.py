import random as r

alphabet = ''

for letter in range(65, 91):
    alphabet += chr(letter)
    # chr(n) получает код буквы n и преобразует его в букву

alphabet = alphabet.lower() + alphabet
print(alphabet)
print(f'Случайная буква: {r.choice(alphabet)}')

