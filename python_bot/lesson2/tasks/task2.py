##### Первая версия программы #####

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.""" 

tasks = [] # Создание списка задач
tasks_today = []
tasks_tomorrow = []
tasks_other = []


run = True
while run:

    command = input('Введите команду ')
    if command == 'help':
        print(HELP) # Если вводит 'help' вывести на печать HELP
    elif command == 'show':
        print(tasks) # Если вводит 'show' - вывести на печать все задачи
    elif command == 'add':
        data = input('Введите дату выполнения задачи')
        task = input('Введите название задачи: ') # Если вводит 'add' - вывести запрорс на ввод названия задачи через input
        if data == 'сегодня':
            tasks_today.append(task) # Ввод значения переменной task в список задач tasks
            print('Задача добавлена на сегодня')
        elif data == 'завтра':
            tasks_tomorrow.append(task) # Ввод значения переменной task в список задач tasks
            print('Задача добавлена на завтра')
        else:
            tasks_other.append(task)
            print('Задача добавлена в список прочее')
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Неизвестная команда')
        # run = False # первый вариант цикла
        print('До свидания!')
        break # второй вариант завершения цикла при вводе неизвесной команды
        