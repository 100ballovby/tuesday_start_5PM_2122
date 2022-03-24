with open('test.py', 'w') as run_file:
    # с открытием_файла(test.py, запись) <- файл создастся сам
    command = 'print("hello")'
    run_file.write(command)
