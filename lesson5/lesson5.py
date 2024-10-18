# # Функции
# # def - ключевое слово 
# #   имя функции
# #          параметр функции
# def square(number):
#     result = number ** 2
#     return result
#     # ключевое слово return, возвращающее
#     # значение из функции, автоматически
#     # останавливает работу функции

# print(square(6))

# вызов справки по функциям
# help(print)

# help(len)

# Docstring - встроенное средство документирования модулей, 
# функций, классов и методов (help).

# def square(number):
#     '''
#     возведение числа в квадрат
#     '''
#     result = number ** 2
#     return result

# help(square) # вывод справки на функцию - возведение числа в квадрат

# # Параметры функции
# параметры задаются после запуска функции
# def square_2():
#     user_input = int(input('Введите число: '))
#     result = user_input ** 2
#     return result

# print(square_2())

# def power(num_1, num_2): # функция с двумя параметрами
#     return num_1 ** num_2 # вернуть возведение num_1 в степень num_2

# print(power(2, 5)) # подставляем 2 и 5 в функцию - 2 ** 5 = 32

# def power(num_1, num_2=2): # функция с двумя параметрами, второй параметр равен 2 
#     return num_1 ** num_2 # вернуть возведение num_1 в степень num_2

# print(power(2)) # вызываем функцию с указанием первого параметра (2)ю вывод: 4
# если, при вызове функции, указать оба параметра, то num_2=2 - игнорируется
# и num_2 задается новое значение

# def power(num_1, num_2=2): # функция с двумя параметрами, второй параметр равен 2 
#     return num_1 ** num_2 # вернуть возведение num_1 в степень num_2

# print(power(2, 7)) # вывод: 128

# # Тип данных None
# None - специальный тип данных, который означает отсутствие значения.
# Если в функции нет return, либо он пустой, то она возвращает None.

# def square_2(number):
#     result = number ** 2
#     print(result) # внутри функции - выводит значение 3 ** 2 = 9
#     #return result
# print(square_2(3)) # вычисления выполнены, но функция ничего не возвращает. вывод: None
 
# # Области видимости (scope) - определяет контекст объекта, в рамках которого его можно использовать
# Типы области видимости: 
#   - глобальная видимость (Global scope) - некая переменная является глобальной - определена вне любой из функций и доступна любой функции в программе. 
#   - локальная видимость (Local scope) - локальная переменная определяется внутри функции и доступна только из этой функции, т.е. имеет локальную область видимости 
#   - нелокальная видимость (Nonlocal scope)

# num_1 = 10 # глобальная видимость
# def power(num_1, num_2=2): # num_2 - локальная переменная 
#     return num_1 ** num_2
# print(power(2)) # параметр (2) - нелокальная видимость

# Если Python не может найти нужную переменную в локальной области видимости, 
# то тогда (и только тогда) он будет искать ее в области видимости
# уровнем выше. 

# number = 5  # глобальные переменные
# power = 3   # вне функции 

# def power_2():
#     number = 6  # локальные переменные
#     power = 2   # внутри функции
#     return number ** power

# print(number ** power) # в глобальном контексте. вывод: 5 ** 3 = 125 
# print(power_2()) # в локальном контексте, через функции вывод: 36

# number = 5  # глобальные переменные
# power = 3   # вне функции 

# def power_2():
#     number = 6  # локальные переменные
#     # power = 2   # функция не находит локальную переменную и обращается к глобальной
#     some_number = 1
#     return number ** power

# print(number ** power) # в глобальном контексте. вывод: 125 
# print(power_2()) # в локальном контексте, через функции вывод: 216
# print(some_number) # обращение из глобального контекста к переменной из локального контекста - ошибка
# # Снизу вверх переменные ищет (из локального внешние переменные видит), с верху вниз - нет (из глобального локальные переменные - не видит)

# # Операторы global и nonlocal

# Оператор global позволяет создать глобальную переменную в локальном контексте
# Оператор nonlocal позволяет изменить переменную в области видимости более высокого уровня
# (которая ,в свою очередь, является локальной областью видимости для других переменных)



# name = 'James'

# def say_hi():
#     name = 'Rinat' # используется локальная переменная, если она есть, а она есть
#     print(f'Hello, {name}')

# say_hi() # Hello, Rinat

#print(name) # James


# name = 'James'

# def say_hi():
#     global name # перезаписываем глобальное значение name 'James' на 'Rinat' (локальная переменная стала глобальной)
#     name = 'Rinat' 
#     print(f'Hello, {name}')

# print(name) # James - до вызова функции, поэтому global name - не сработало

# say_hi() # Hello, Rinat

# print(name) # Rinat - после срабатывания функции say_hi (внутри функции есть переопределение переменной на global)

# # Nonlocal

# def say_hi():
#     name = 'Rinat'
#     def get_name():
#         name = input('Введите имя')
#         return name
#     get_name()
#     print(f'Hello, {name}')

# say_hi() # Вывод: Hello, Rinat, так как вызов get_name и print не во вложенной функции - имя берется из name = 'Rinat'
# верхний уровень во вложенный не лезет.  


# def say_hi():
#     name = 'Rinat'
#     def get_name():
#         nonlocal name # задаем значение переменной name как не локальная, т.е. она становиться локальной для функции выше
#         name = input('Введите имя')
#         return name
#     get_name()
#     print(f'Hello, {name}')

# say_hi()
# # nonlocal - поднимает переменную на уровень вверх, но не глобально
# # Глобальных переменных делать не надо

# # Анонимные функции или lambda

#              что возвращает функция без return
# lambda x, pow: x**pow
#      параметр функции

# func = lambda x, y: x + y

# print(func(5, 7))

# # Методы - это функции, которые "принадлежат" к определенному объекту
# У каждого типа объектов есть свои методы.

# Методы списков:   Методы строк:       Методы словарей:
#.index()           .capitalize()       .keys()
#.count()           .upper()            .values()
#.append()          .lower()            .items()
#.remove()          .replace()
#.revers()          .count()

student_list = [
    {'name': 'Василий', 'surname': 'Теркин', 'gender': 'м', 'program_exp': True, 'grade': [8, 8, 9, 10, 9], 'exam': 8},
    {'name': 'Мария', 'surname': 'Павлова', 'gender': 'ж', 'program_exp': True, 'grade': [7, 8, 9, 7, 9], 'exam': 9},
    {'name': 'Ирина', 'surname': 'Андреева', 'gender': 'ж', 'program_exp': False, 'grade': [10, 9, 8, 10, 10], 'exam': 7},
    {'name': 'Татьяна', 'surname': 'Сидорова', 'gender': 'ж', 'program_exp': False, 'grade': [7, 8, 8, 9, 8], 'exam': 10},
    {'name': 'Иван', 'surname': 'Васильевич', 'gender': 'м', 'program_exp': True, 'grade': [9, 8, 9, 6, 9], 'exam': 5},
    {'name': 'Роман', 'surname': 'Золотарев', 'gender': 'м', 'program_exp': False, 'grade': [8, 9, 9, 6, 9], 'exam': 6}
]

# Функция - средняя оценка за экзамен

def get_avg_ex_grade(students): # параметр функции - какой то список студентов
    sum_ex = 0
    for student in students:
        #print(student)
        sum_ex += student['exam']
    return round(sum_ex / len(students), 2)
#print(get_avg_ex_grade(student_list))

# Функция - средняя оценка за домашнее задание у всей группы

def get_avg_hw_grade(students): # параметр функции - какой то список студентов
    sum_hw = 0
    for student in students:
        #print(student)
        sum_hw += sum(student['grade']) / len(student['grade'])
    return round(sum_hw / len(student_list), 2)
#print(get_avg_hw_grade(student_list))

# Функция - средняя оценка за домашнее задание отдельно у 'м' и 'ж'

def get_avg_hw_grade(students, sex='ж'): # параметр функции - какой то список студентов
    sum_hw = 0
    count = 0
    for student in students:
        if student['gender'] == sex: 
            #print(student)
            sum_hw += sum(student['grade']) / len(student['grade'])
            count += 1
    return round(sum_hw / count, 2)
# print('ж', get_avg_hw_grade(student_list))
# print('м', get_avg_hw_grade(student_list, 'м'))

def get_avg_hw_grade(students, sex=None): # параметр функции - какой то список студентов, второй параметр не равен м и ж
    sum_hw = 0
    count = 0
    for student in students:
        if student['gender'] == sex or sex is None: 
            #print(student)
            sum_hw += sum(student['grade']) / len(student['grade'])
            count += 1
    return round(sum_hw / count, 2)
# print('общее', get_avg_hw_grade(student_list))
# print('м', get_avg_hw_grade(student_list, 'м'))
# print('ж', get_avg_hw_grade(student_list, 'ж'))



def get_avg_hw_grade(students, sex=None, exp=None): # параметр функции - какой то список студентов, второй параметр не равен м и ж
    sum_hw = 0
    count = 0
    for student in students:
        if student['gender'] == sex and exp is None or\
        (sex is None and exp is None) or\
        (student['gender'] == sex and student['program_exp'] == exp) or\
        (sex is None and student['program_exp'] == exp):
            #print(student)
            sum_hw += sum(student['grade']) / len(student['grade'])
            count += 1
    return round(sum_hw / count, 2)


# print('ж', get_avg_hw_grade(student_list, 'ж')) # средняя оценка по ж
# print('м', get_avg_hw_grade(student_list, 'м')) # средняя оценка пр м
# print('общее', get_avg_hw_grade(student_list)) # средняя оценка по м + ж 

# print('ж', get_avg_hw_grade(student_list, 'ж', False)) # средняя по ж без опыта
# print('м', get_avg_hw_grade(student_list, 'м', False)) # средняя по м без опыта
# print('общее', get_avg_hw_grade(student_list, 'ж', True)) # средняя по ж с опыта
# print('общее', get_avg_hw_grade(student_list, None, True)) # средняя по всем только с опытом
# print('общее', get_avg_hw_grade(student_list, exp=True)) # средняя по всем только с опытом

# def main():
#     while True:
#         user_input = input('Введите команду')
#         if user_input == '1':
#             print(get_avg_ex_grade(student_list))
#         elif user_input == '2':
#             print(get_avg_hw_grade(student_list))
#         elif user_input == '3':
#             print(get_avg_hw_grade(student_list, 'ж', False))
#         elif user_input == 'q':
#             break

# main()

def main(students):
    while True:
        user_input = input('Введите команду')
        if user_input == '1':
            print(get_avg_ex_grade(students))
        elif user_input == '2':
            print(get_avg_hw_grade(students))
        elif user_input == '3':
            print(get_avg_hw_grade(students, 'ж', False))
        elif user_input == 'q':
            break

main(student_list)