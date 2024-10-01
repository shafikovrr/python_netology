# x = 'Hello'
# y = 'World'
# print(x, y)
# print(x + y)
# greeting = "Hello " + "World"
# print(greeting)
# l = len(greeting) # вывод длины 
# print(l)
# print(len(x))
# strings = ['Hello', 'world'] # список
# numbers = [1, 2, 3, 4, 5]
# data = ['hello', 1]
#
# print(strings)
# print(numbers)
# print(data)
#
# summa = numbers + data # сложение списков (неуникальные данные)
# print(summa)
#
# numbers.append(6) # добавление в список данные
# print(numbers)
#
# first = strings[0]
# print(first) # вывод первого элемента списка
# second = strings[1]
# print(second)
#
# strings_length = len(strings) # длина списка - 2 (Hello и world)
# print(strings_length)
#
# s = sum(numbers) # сумма списка (1+2+3+4+5+6=21)
# print(s)


######## словари

# cat: кошка
# bat: летучая мышь
# ключ: значение

# dictionary = {
#     "cat": "кошка",
#     "bat": "летучая мышь"
# }
# print(dictionary) # вывод словаря на печать
# cat = dictionary["cat"]
# print(cat)

# countries = {
#     "Африка": ["Египет", "Конго", "ЮАР"], # Африка - строка; Египет, Конго, ЮАР - список
#     "Азия": ["Китай", "Тайланд", "Индонезия"]
# }
#
# africa = countries["Африка"] # доступ к элементу по ключу
# print(africa)
#
# africa_key = "Африка" #
# print(countries[africa_key])
#
# countries["Европа"] = ["Австрия", "Испания", "Италия"] # помещение нового ключа в словарь
# print(countries)

# countries[0] = "Hello"
# print(countries)

# africa.append("Эфиопия")
# print(africa)
# print(countries)
# print(len(countries["Африка"])) # 4 страны в "Африка"
#
# name = input("Введите имя: ")
# print("Привет, ", name)

# a = 5
# print(type(a))
# a = 8.9
# print(type(a))
# a = 'world'
# print(type(a))

# Деление
# Обычное деление
# print(17 / 2) # обычное деление - 8.5
# print(17 // 2) # целочисленное деление - 8
# print(17 % 2) # деление с остатком - остаток от деления 1
#
# # Возведение в степень
# print(3 ** 6) # 3 в степени 6 = 729
# print(10 ** (-1)) # 10 в степени -1 = 0.1
# print(25 ** (1/2)) # 25 в степени одна вторая = 5

# Действия со строками

# print(type("Hello, world")) # класс переменно - строка 'str'
# str1 = 'Hello, '
# str2 = 'world'
# print(str1 + str2) # сложение строк = Hello, world
# print(str1 * 3) # умножение строки на 3 = Hello, Hello, Hello,
#
# print(len('строка')) # длина строки - 6 (6 букв в слове "строка")
#
# a = input()
# print(type(a)) # 8 (даже если число - будет строкой) - <class 'str'>
# a = int(input()) # преобразование строки в число
# print(type(a)) # 8 - <class 'int'>
# b = float(input())
# print(b, type(b)) # 3.0 <class 'float'>

# переменная типа bool - два значения: true и false
# print(False)
# print(True)
# print(type(False)) # <class 'bool'>
# print(type(True)) # <class 'bool'>

# a = None
# print(type(a)) # <class 'NoneType'> - None - отсутствие типа

# array = [1, 2, 3, 4, 5] # список из целых чисел int
# print(type(array)) # класс list
# # список состоящий из целого числа 1, из числа с плавающей точкой 2.6, из строки и списка
# ar = [1, 2.6, 'str', [1, 2, 3]]
#
# # обращение к элементу списка
# print(ar[0], ar[3]) # печатаем первый и четвертый элемент списка (счет с 0 - это первый)
# # Добавление в список
# array.append(6)
# print(array)
# # сложение списка
# array2 = [7, 8, 9]
# new_array = array + array2
# print(new_array)
#
# # Длинна списка
# print(len(new_array))
# # добавление в конец списка элемента 1
# new_array.append(1)
# print(new_array)
# # Сортировка списка - добавили 1 - стало 1, 1, 2, 3......
# new_array.sort()
# print(new_array)

# Словари
# dictionary = {
#     'dog': 'собака', # 'dog' - ключ, 'собака' - значение ключа
#     'table': 'стол',
#     'computer': 'компьютер'
# }

# print(dictionary['dog']) # печатаем значение ключа 'dog' из списка dictionary: собака

# dictionary['dog'] = 'пес' # меняем "собака" на "пес"
# print(dictionary['dog'])

# dictionary['laptop'] = 'ноутбук' # добавляем в списко ноутбук
# print(dictionary)