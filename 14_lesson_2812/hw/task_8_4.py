"""8-4. Большие футболки: измените функцию make_shirt(), чтобы футболки
по умолчанию имели размер L, и на них выводился текст «I love Python.».
Создайте футболку с размером L и текстом по умолчанию, а также футболку
любого размера с другим текстом."""


def make_shirt(size='L', text='I love Python!'):
    msg = f'New shirt. Size {size}, text: "{text}".'
    return msg

print(make_shirt())
print(make_shirt('S', 'I love C++'))