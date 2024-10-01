##### Первая версия программы #####

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show/print - напечатать все добавленные задачи.""" 

tasks = [] # Создание списка задач

stop = False # Задаем переменной значение False
while not stop:
    command = input('Введите команду ')
    if command == 'help':
        print(HELP) # Если вводит 'help' вывести на печать HELP
    elif command == 'show' or command == 'print':
        print(tasks) # Если вводит 'show' - вывести на печать все задачи
    elif command == 'add':
        task = input('Введите название задачи: ') # Если вводит 'add' - вывести запрорс на ввод названия задачи через input
        tasks.append(task) # Ввод значения переменной task в список задач tasks
        print('Задача добавлена')
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        stop = True
    else:
        print('Неизвестная команда')
        print(HELP)
        # run = False # первый вариант цикла
        stop = True