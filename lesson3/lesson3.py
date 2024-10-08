# my_integer = 10
# print(type(my_integer))
#
# my_float = 5.5
# print(type(my_float))
#
# my_string = 'Hello, World'
# print(type(my_string))
#
# my_bool = True
# print(type(my_bool))


# print(type(4 > 5)) # bool

# salary = 1000
# print('Ваша годовая зарплата ' + str(salary) + ' у.е.')

# print(type(20/5.1))
# print(type(1 + True)) # Неявное преобразование типов 1 + 1 = 2. True - преобразовалась в 1 (False - будет преобразовываться в 0)
# print(1 + False) # 1 + 0 = 1

# Объединение строк +: y + u = yu
# print('y' + 'u')
# # Умножение строки *: y * 5 = yyyyy
# print('y' * 5)

# Меняют исходную строку на новую, но исходная остается неизменной
# Привести строку к верхнему регистру
# y = 'rinat'
# print('Измененная строка: ', y.upper()) # rinat = RINAT
# print('Исходная строка: ', y)
# # Приведение строки к нижнему регистру
# x = 'RINAT'
# print(x.lower()) # RINAT = rinat
# # Приводит первую букву к верхнему регистру
# z = 'rinat'
# print(z.capitalize()) # rinat = Rinat
# # Заменяет один элемент в строке на другой
# m = 'my home'
# print(m)
# print(m.replace('my', 'her'))
# # Определяет длину строки
# c = 'my home'
# print(len(c)) # 2 + 1 + 4 = 7

# my_string = 'Hello, World!'
# new_string = my_string.upper()
# print('Было: ', my_string, 'Стало: ', new_string)

# Форматирование строк (f-строки)
# Добавляя префикс f к строке, можно встраивать в нее
# произвольные выражения при помощи фигурных скобок {

# name = 'Коля'
# age = 12
# print(f'Меня зовут {name}. Я родился в {2024 - age} году')
# вычитает из 2024 - 12 = 2012.

# name = 'Ринат'
# lang = 'python'
# my_string = f'Привет, меня зовут {name}, я знаю немного как программировать в {lang}.'
# print(my_string)

# Индексация и срезы строк
# индексация элементов начинается с 0

# 0   1   2   3   4   5 - прямой индекс
# И   Н   Д   Е   К   С
# -6 -5  -4  -3  -2  -1 - обратный индекс (если неизвестно сколько - длина. начинаем с конца)

# # Для получения в выводе буквы И в слове индекс можно:
# my_string = 'индекс'
# print(my_string[0]) # с помощью прямого индекса
# print(my_string[-6]) # с помощью обратного индекса
#
# # Срез (указываем начальный индекс среза и конечный индекс среза)
# print(my_string[1:3]) # нд. т.е. третий индекс не включается.
# # Срез с шагом
# # С нулевого включительно до (4 включительно) 5 (не включается) с шагом 2
# print(my_string[0:5:2]) # с шагом 2 - "идк"

# my_string = 'Hello, World'
# print(my_string[2]) # - l
# print(my_string[4]) # - o
# print(my_string[0:5]) # Hello
# print(my_string[0:8:2]) # Hlo + пробел
# print(my_string[6:]) # пробел + World
# print(my_string[:5]) # Hello
# print(my_string[::-1]) # dlroW ,olleH - задом на перед

# Список (list) - изменяемый тип, в отличие от строк
# Список "Данные пользователя"
#0           1           2           3
#'Петров'    'Николай'  'Иванович'  25

# Многомерные списки
#             0           1   - строки
# tables [[1, 2, 3], [4, 5, 6]]
#          0  1  2    0  1  2 - столбцы

# Можно представить как таблицу
#         0   1   3
#       _____________
#   0   | 1 | 2 | 3 |
#       _____________
#   1   | 3 | 4 | 5 |

# Операции со списками
# del(list[index]) - удаляет элемент из списка по индексу
# .remove(el) - удаляет указанный элемент из списка
# .append(el) - добавляет в конце списка
# .count(el) - считает количество вхождений элемента в список
# .index(el) - позволяет узнать индекс элемента в списке
# .revers() - разворачивает списки
# sorted(list) - сортирует список
# month_list =['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']

# income_list = [13000, 14000, 14300, 15000, 13800, 13000, 14900, 15200, 15300]

# income_by_months = [['Jan', 13000], ['Feb', 14000], ['Mar', 14300], ['Apr', 15000], ['May', 13800], ['Jun', 13000], ['Jul', 14900], ['Aug', 15200], ['Sep', 15300]]
# # print(month_list[0]) # индексация - Jan
# print(month_list[-1]) # индексация - Sep
# print(income_by_months[-4]) # индексация - ['Jun', 13000]
# # Как проиндексировать вложенный список?
# y = income_by_months[-4]
# print(y[-1]) # 13000
# # или
# print(income_by_months[-4][-1]) # индекс вложенного элемента - 13000
# print(income_by_months[-4][0][0]) # ['Jun', 13000] -> Jun -> J
# print(income_by_months[0:2]) # - ['Jan', 13000], ['Feb', 14000]
# print(income_by_months[-8:-6]) # - ['Feb', 14000], ['Mar', 14300]

# # Изменение значения в списке
# print('было: ', income_by_months[0])
# income_by_months[0][1] = 13100
# print('стало: ', income_by_months[0])

# # Сложение списков
# income_by_months_2 = [['Nov', 15400], ['Dec', 17000]]
# income_by_months = income_by_months + income_by_months_2
# print(income_by_months)

# # Удаление элементов списка по индексу
# del(income_by_months[-1]) # удалили ['Sep', 15300]
# print(income_by_months)

# # Удаление элемента списка по названию
# month_list.remove('Jan')
# print(month_list)

# # Удаление из сложного списка (удаление подсписка)
# income_by_months.remove(['Feb', 14000])
# print(income_by_months)

# Если хотим из сложного списка удалить один элемент 'Jan'
# income_by_months[0].remove('Jan')
# print(income_by_months)


# # Добавление в конец списка
# income_by_months.append(['Dec', 17000])
# print(income_by_months)


# # Добавление на позицию (индекс) 9 - ['Nov', 20000] (между 8 и 9 индексом, при этом старый 9 становится 10 индексом)
#
# income_by_months.insert(9, ['Nov', 20000])
# print(income_by_months)
#
#
# # Возвращает значение индекса элемента списка
# income_list = [13000, 14000, 14300, 15000, 13800, 13000, 14900, 15200, 15300]
# print(income_list.index(13000)) # находит первый со значением 13000 (второй не выводит)
#
# # Реверс значений списка
# month_list.reverse()
# print(month_list)
# # аналогично
#print(month_list[::-1])
#

# # Сортировка ()
# print(sorted(income_list)) # по возрастанию
# print(sorted(income_list, reverse=True)) # по убыванию


# print(sorted(income_list)) # sorted(income_list) - создан новый отсортированный список
# print(income_list) # income_list при этом не изменился (неизменяемые исходные данные)

# # метод sort
# income_list.sort() # применение метода sort - меняет исходный список
# print(income_list) # вывод исходного списка - измененный (отсортированный по возрастанию)
# print(income_list.sort()) # ничего нового не возвращает - меняет исходный объект - результат NONE
# Строка - строка неизменяемый тип данных
# Список - изменяемый тип данных
#
#income_by_months = [['Jan', 13000], ['Feb', 14000], ['Mar', 14300], ['Apr', 15000], ['May', 13800], ['Jun', 13000], ['Jul', 14900], ['Aug', 15200], ['Sep', 15300]]
#print(sorted(income_by_months)) # Сортировка вложенных списков - по первому элементу - по алфавиту
#
# # Разделение списка split - сплит делает из строки список
# queries_string = 'смотреть сериалы онлайн,новости спорта,афиша кино,курс доллара,сериалы эти млетом,курс по питону,сериалы про спорт'
# # print(queries_string.split()) # разделение по пробелу (по умолчанию)
# print(queries_string.split(',')) # разделение по параметру ',' - по запятой
# print(type(queries_string.split(','))) # тип 'list'
# # # Преобразование список в строку - join - делает из списка строку
# #print('\t'.join(['Столбец 1', 'Столбец 2', 'Столбец 3'])) # разделение по табу '\t'
# print('\n'.join(['Столбец 1', 'Столбец 2', 'Столбец 3'])) # разделение по табу '\t'
# print(type('\n'.join(['Столбец 1', 'Столбец 2', 'Столбец 3']))) # тип str
# # Экранированные последовательности после '\'
# - \t (табуляция)
# - \n (новая строка, разрыв строки)

# Кортежи (неизменяемые списки) - инициализируются круглыми списками
# salary_tuple = (1000, 1200, 1300, 900, 800)
# print(salary_tuple[0])
# salary_tuple[0] = 500 # ошибка. в кортеже переназначать нельзя

# my_list = list(salary_tuple)
# print(my_list)
# print('Преобразовали в список (list): ', type(my_list))
# my_list = tuple(my_list)
# print('Преобразовали в строку (tuple - картеж): ', type(my_list))
# картежи - более производительные, меньше к памяти, ресурсам

# Функция zip - берет несколько списков/кортежей и создает из них специальный zip-объект ([1, 2, 3] + [a, b, c] = [1, a], [2, b], [3, c])
#
# salaries = [1000, 1200, 1300, 900, 800, 1000]
# names = ['Robert', 'Jane', 'Liza', 'Richard', 'John']
# salaries_by_names = zip(names, salaries)
# print(salaries_by_names) # <zip object at 0x0000015D98ABBC40>
# print(list(salaries_by_names)) # список

# company_tuple = ('Orange', 100000000, 20000)
# company_name, capitalization, personal = company_tuple
# print(company_name)
# print(capitalization)
# print(personal)

# # Операторы проверки вхождения (есть ли в списке элемент)
# # IN - True если элемент входит в объект
# # NOT IN - True - если элемент не входит в объект
#
# print('Hello' in 'Hello, World') # - да входит, результат True
# month_list =['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
# print(len(month_list)) # выдает длину списка = 9
# print('Jun' in month_list) # - да входит, в результате True

# # Посчитать количество одинаковых элементов в списке (метод count)
# income_list = [13000, 14000, 14300, 15000, 13800, 13000, 14900, 15200, 15300]
# print(income_list.count(13000))

# Циклы (повторение операций n количество раз) - while и for
# While - позволяет выполнять одну и туже последовательность действий, пока проверяемое условие истинно
# Если True - идем по кругу, как только False - заканчиваем выполнение кода
# x = 0
# while x < 5: # пока х меньше 5
#     print(x) # код, который будет повторяться
#     x = x + 1 # пока условие True
#
# x = 5
# while x != 0:
#     x -= 1
#     print(x)
# 4, 3, 2, 1, 0

# x = 7
# while x != 0:
#     if x % 2 == 0:
#         print(x, ' - четное число')
#         x = x - 1
#     else:
#         print(x, ' - нечетное число')
#         x = x - 1

# x = 7
# while x != 0:
#     if x % 2 == 0:
#         print(x, ' - четное число')
#     else:
#         print(x, ' - нечетное число')
#     x -= 1
#     # x /= 2 -> x = x / 2
#     # x += 1 -> x = x + 1
#     # x *= 2 -> x = x * 8



# y = 0
# x = ''
# while x != 0:
#     x = int(input('Введите число ', ))
#     y += x
# print(y)

# while True:
#     x = input('Введите  команду: ')
#     if x == '1':
#         pass
#     elif x == '2':
#         pass
#     elif x == 'quite':
#         break

# Цикл for - проходит по элементам любого итерируемого объекта (строки, списка и т.д.) и во время кажодго прохода выполняет заданную последовательность действий.abs

# for element in list:
#     element = element**2    # код который будет
#     print(element)          # выполняется при каждой итерации

# company_name = 'Orange'
# for letter in company_name:
#     print(letter)
#     letter = letter.capitalize()
#     print(letter) # у print - аргумент по умолчанию - end (разрыв строки)
#     #print(letter, end='')


# companies_capitalization =[
#     ['Orange', 1.3],
#     ['Maxisoft', 1.5],
#     ['Headbook', 0.8],
#     ['Nicola', 2.2]
# ]

# for company in companies_capitalization:
#     print(f'Капитализация компании {company[0]} составляет {company[1]} миллионов рублей')
# # Или
# for company, capitalizatuion in companies_capitalization:
#     print(f'Капитализация компании {company} составляет {capitalizatuion} миллионов рублей')

# phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

# for letter in phrase:
#     if letter == ' ':
#         break
#     print(letter, end='') # 640Кб


# for letter in phrase:
#     if letter == ' ':
#         continue
#     print(letter, end='') # 640Кбдолжнохватитьдлялюбыхзадач.БиллГейтс(полегенде)



# for letter in phrase:
#     if letter == ' ':
#         pass
#     print(letter, end='') # 640Кб должно хватить для любых задач. Билл Гейтс (по легенде)

# professions = ['IT', 'Физика', 'Математика']
# persons = [['Гейтс', 'Джобс', 'Возняк'], ['Энштейн', 'Фейнман'], ['Эвклин', 'Ньютон']]

# for el in zip(professions, persons):
#     print(el[0], ':')
#     for letter in el[1]:
#         if letter == ' ':
#             pass 
#         print(letter)

# for pro, names in zip(professions, persons):
#     print(f'{pro}:')
#     for name in names:
#         print(name)
#     print()