phone = {
    'mother': {
        'phone': '+375291234567',
        'email': {'work': 'example@example.com',
                  'private': 'oughf3924hr@gmail.com'},
        'birthdate': '23.11.1950'
    },
    'father': {
        'phone': ['+375255643748', '+3754434123433'],
        'email': 'rtjghektrg@example.com',
        'birthdate': '03.07.1967'
    },
    'sister': {
        'phone': '+3753357438934',
        'email': 'tbd@example.com',
        'birthdate': '11.01.2000'
    },
}

print(phone['mother']['email']['private'])
print(phone['father']['phone'][1])



