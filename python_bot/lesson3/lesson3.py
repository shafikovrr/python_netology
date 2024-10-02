# HELP = """
# help - напечатать справку по программе.
# add - добавить задачу в список (название задачи запрашиваем у пользователя).
# show - напечатать все добавленные задачи.""" 

# tasks = {

# } # Создание словаря

# run = True
# while run:

#     command = input('Введите команду ')
#     if command == 'help':
#         print(HELP) # Если вводит 'help' вывести на печать HELP
#     elif command == 'show':
#         print(tasks) # Если вводит 'show' - вывести на печать все задачи
#     elif command == 'add':
#         date = input('Введите дату для добавления задачи: ')
#         task = input('Введите название задачи: ') # Если вводит 'add' - вывести запрорс на ввод названия задачи через input
#         if date in tasks:
#             # Дата есть в словаре
#             # Добавляем в список задачу
#             tasks[date].append(task) # Ввод значения переменной task в словарь задач tasks
#         else:
#             # Если в словаре такой даты нет
#             # Создаем запись в словаре с ключем date
#             tasks[date] = []
#             tasks[date].append(task) # 
#         print('Задача ', task, 'добавлена на дату ', date)
#     else:
#         print('Неизвестная задача')
#         # run = False # первый вариант цикла
#         break # второй вариант завершения цикла при вводе неизвесной команды
# print('До свидания!')


# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: # для переменной i из списка
#     if i % 2 == 0: # если остаток от деления = 0, то число четное 
#         print(i) # вывести его на печать

# HELP = """
# help - напечатать справку по программе.
# add - добавить задачу в список (название задачи запрашиваем у пользователя).
# show - напечатать все добавленные задачи.""" 

# tasks = {

# } # Создание словаря

# run = True
# while run:

#     command = input('Введите команду ')
#     if command == 'help':
#         print(HELP) # Если вводит 'help' вывести на печать HELP
#     elif command == 'show':
#         date = input('Введите дату для отображения списка задач: ')
#         if date in tasks:
#             for task in tasks[date]:
#                 print('- ', task)
#         else:
#             print('Такой даты нет') # Если вводит 'show' - вывести на печать все задачи
#     elif command == 'add':
#         date = input('Введите дату для добавления задачи: ')
#         task = input('Введите название задачи: ') # Если вводит 'add' - вывести запрорс на ввод названия задачи через input
#         if date in tasks:
#             # Дата есть в словаре
#             # Добавляем в список задачу
#             tasks[date].append(task) # Ввод значения переменной task в словарь задач tasks
#         else:
#             # Если в словаре такой даты нет
#             # Создаем запись в словаре с ключем date
#             tasks[date] = []
#             tasks[date].append(task) # 
#         print('Задача ', task, 'добавлена на дату ', date)
#     else:
#         print('Неизвестная задача')
#         # run = False # первый вариант цикла
#         break # второй вариант завершения цикла при вводе неизвесной команды
# print('До свидания!')

# HELP = """
# help - напечатать справку по программе.
# add - добавить задачу в список (название задачи запрашиваем у пользователя).
# show - напечатать все добавленные задачи.
# random - добавление случайной задачи на дату Сегодня""" 

# RANDOM_TASK = 'Записаться на курс в нетологию'

# tasks = {

# } # Создание словаря

# run = True
# while run:

#     command = input('Введите команду ')
#     if command == 'help':
#         print(HELP) # Если вводит 'help' вывести на печать HELP
#     elif command == 'show':
#         date = input('Введите дату для отображения списка задач: ')
#         if date in tasks:
#             for task in tasks[date]:
#                 print('- ', task)
#         else:
#             print('Такой даты нет') # Если вводит 'show' - вывести на печать все задачи
#     elif command == 'add':
#         date = input('Введите дату для добавления задачи: ')
#         task = input('Введите название задачи: ') # Если вводит 'add' - вывести запрорс на ввод названия задачи через input
#         if date in tasks:
#             # Дата есть в словаре
#             # Добавляем в список задачу
#             tasks[date].append(task) # Ввод значения переменной task в словарь задач tasks
#         else:
#             # Если в словаре такой даты нет
#             # Создаем запись в словаре с ключем date
#             tasks[date] = []
#             tasks[date].append(task) # 
#         print('Задача ', task, 'добавлена на дату ', date)
#     elif command == 'random':
#         if 'Сегодня' in tasks:
#             tasks['Сегодня'].append(RANDOM_TASK)
#         else:
#             tasks['Сегодня'] = []
#             tasks['Сегодня'].append(RANDOM_TASK)
#     else:
#         print('Неизвестная задача')
#         # run = False # первый вариант цикла
#         break # второй вариант завершения цикла при вводе неизвесной команды
# print('До свидания!')


# Создание функции

# def my_func(i):     # название функции
#     if i > 2:       # тело функции
#         i = 2
#     return i        # возвращаемое значение
# x = my_func(3)


# def multiply(a, b):     # название функции
#     print('a = ', a)
#     print('b = ', b)
#     result = a * b       # тело функции
#     return result        # возвращаемое значение

# c = multiply(3, 5)
# print(c)
# c = multiply(7, 5)
# print(c)
# c = multiply(3, 518)
# print(c)

# def print_hello():
#     print('Hello')
#     print('World')

# print_hello()
# print_hello()
# print_hello()

# def my_input(promt):
#     print(promt)

#     return inp


# HELP = """
# help - напечатать справку по программе.
# add - добавить задачу в список (название задачи запрашиваем у пользователя).
# show - напечатать все добавленные задачи.
# random - добавление случайной задачи на дату Сегодня""" 

# RANDOM_TASK = 'Записаться на курс в нетологию'

# tasks = {

# } # Создание словаря

# run = True

# def add_todo(date, task):
#     if date in tasks:
#         # Дата есть в словаре
#         # Добавляем в список задачу
#         tasks[date].append(task) # Ввод значения переменной task в словарь задач tasks
#     else:
#         # Если в словаре такой даты нет
#         # Создаем запись в словаре с ключем date
#         tasks[date] = []
#         tasks[date].append(task) # 
#     print('Задача ', task, 'добавлена на дату ', date)

# while run:

#     command = input('Введите команду ')
#     if command == 'help':
#         print(HELP) # Если вводит 'help' вывести на печать HELP
#     elif command == 'show':
#         date = input('Введите дату для отображения списка задач: ')
#         if date in tasks:
#             for task in tasks[date]:
#                 print('- ', task)
#         else:
#             print('Такой даты нет') # Если вводит 'show' - вывести на печать все задачи
#     elif command == 'add':
#         date = input('Введите дату для добавления задачи: ')
#         task = input('Введите название задачи: ') # Если вводит 'add' - вывести запрорс на ввод названия задачи через input
#         add_todo(date, task)
#     elif command == 'random':
#         add_todo('Сегодня', RANDOM_TASK)
#     # elif command == 'random_date':
#     #     add_todo(RANDOM_DATE, RANDOM_TASK)
#     else:
#         print('Неизвестная задача')
#         # run = False # первый вариант цикла
#         break # второй вариант завершения цикла при вводе неизвесной команды
# print('До свидания!')

##### Добавление случайной задачи

# import random
# HELP = """
# help - напечатать справку по программе.
# add - добавить задачу в список (название задачи запрашиваем у пользователя).
# show - напечатать все добавленные задачи.
# random - добавление случайной задачи на дату Сегодня""" 


# RANDOM_TASKS = ['Записаться на курс в Нетологию', 'Написать Гвидо письмо', 'Покормить кошку', 'Помыть машину']

# tasks = {

# } # Создание словаря

# run = True

# def add_todo(date, task):
#     if date in tasks:
#         # Дата есть в словаре
#         # Добавляем в список задачу
#         tasks[date].append(task) # Ввод значения переменной task в словарь задач tasks
#     else:
#         # Если в словаре такой даты нет
#         # Создаем запись в словаре с ключем date
#         tasks[date] = []
#         tasks[date].append(task) # 
#     print('Задача ', task, 'добавлена на дату ', date)

# while run:

#     command = input('Введите команду ')
#     if command == 'help':
#         print(HELP) # Если вводит 'help' вывести на печать HELP
#     elif command == 'show':
#         date = input('Введите дату для отображения списка задач: ')
#         if date in tasks:
#             for task in tasks[date]:
#                 print('- ', task)
#         else:
#             print('Такой даты нет') # Если вводит 'show' - вывести на печать все задачи
#     elif command == 'add':
#         date = input('Введите дату для добавления задачи: ')
#         task = input('Введите название задачи: ') # Если вводит 'add' - вывести запрорс на ввод названия задачи через input
#         add_todo(date, task)
#     elif command == 'random':
#         task = random.choice(RANDOM_TASKS)
#         add_todo('Сегодня', task)
#     # elif command == 'random_date':
#     #     add_todo(RANDOM_DATE, RANDOM_TASK)
#     else:
#         print('Неизвестная задача')
#         # run = False # первый вариант цикла
#         break # второй вариант завершения цикла при вводе неизвесной команды
# print('До свидания!')

# for i in [4, 5, 6]:
#     print(i)

# for i in [4, 5, 6]:
#     if i % 2 == 0:
#         print(i)

# sum = 0
# array = [45, 7, -934, 0, 2839]
# for i in array:
#     sum += i
# print(sum)

# import <lib> # подключить (использовать) библиотеку lib.

# from <lib> import my_func # из библиотеки <lib> использовать объект my_func

import math
i = math.sin(3.14/3)
print(i)