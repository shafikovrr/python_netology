# Алгоритмы (инструкции)

# Логический тип данных. Принимает одно из двух значений: True/False
# Результаты сравнения: ==, <, >, >=, <=, != 
# Основные операции с логическим типом данных: and, or, not

# name = input("Введите имя: ")
# print(name)
# name1 = "Rinat"
# print(name == name1) # При совпадении имен = True, иначе False

# name = input('Введите имя: ')
# login = 'Rinat'

# if name == login:
#     # Выражение true
#     print('Hello,', name)
# elif len(name) <3:
#     print('Такое имя недопустимо')
# elif name == 'Ri':
#     print('Ri, dro')
# else:
#     # Выражение false
#     print('Hello, user')

# print('The end')

##### Первая версия программы #####

# HELP = """
# help - напечатать справку по программе.
# add - добавить задачу в список (название задачи запрашиваем у пользователя).
# show - напечатать все добавленные задачи.""" 

# tasks = [] # Создание списка задач

# command = input('Введите команду ')
# if command == 'help':
#     print(HELP) # Если вводит 'help' вывести на печать HELP
# elif command == 'show':
#     print(tasks) # Если вводит 'show' - вывести на печать все задачи
# elif command == 'add':
#     task = input('Введите название задачи: ') # Если вводит 'add' - вывести запрорс на ввод названия задачи через input
#     tasks.append(task) # Ввод значения переменной task в список задач tasks
#     print('Задача добавлена')
# else:
#     print('Неизвестная задача')