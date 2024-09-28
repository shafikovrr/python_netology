# a = 10 +20
# b = a * 30
# c = a / b
# print('Ответ:', c)
#
# x = 10
# print(x)


# закомментировать несколько строк - Ctrl+/

# print(2 > 1)
# print(2 == 3)
# print(15 >= 15)
# print(1 != 1)
# print(2 < 3 > 1)

# my_comparison = 10 < 9
# print(my_comparison)

# print('c' < 'a')
# print('b' > 'B')
# print('aba' > 'abc')
# поочередно сравниваются положения букв в алфавите
# а = а, b = b, c - дальше (больше порядковый номер) a - значит больше

#  len() - определяет длину объекта
# print(len('abc') > len('aba')) # 3 символа = 3 символам
# length1 = len('abc')
# print(length1)

# print(True and True)
# print(True and False)
# print(True or False)
# print(not True)

# print((9 > 7) and (2 < 4)) # сравниваемы лучше в скобки для обозначения приоритета
# print((8 == 8) or (6 != 6))
# print(not (3 <= 1))

# if - если
# elif - иначе если
# else

# x = 8
# if x % 2 == 0: # x % 2 - возвращает остаток от деления 7/2 - остаток 1, 8/2 - 0
#     print(x, '- четное число')
# else:
#     print(x, '- не четное число')

# Определение четного/нечетного числа
# x = int(input('Введи значение х: ', ))
# z = x % 2
# print('Остаток от деления =', z)
# if x % 2 == 0:
#     print(x, '- четное число')
# else:
#     print(x, '- нечетное число')

# height = 170
# age = 17
# if height < 170 and age > 18:
#     print('В танкисты')
# elif height < 185 and age > 18:
#     print('На флот')
# elif height < 200 and age > 18:
#     print('В десантники')
# else:
#     print('В другие войска')


# height = 170
# age = 27
# if 18 <= age <= 27:
#     if height < 170:
#         print('В танкисты')
#     elif height < 185:
#         print('На флот')
#     elif height < 200:
#         print('В десантники')
#     else:
#         print('В другие войска')
# else:
#     print('Непризывной возраст')

# name = input('Введите имя: ')
# if name:
#     print('Привет,', name)
# else:
#     print('Привет, Мир!')

# # Если отлично от нуля то true - "число равно числу", если 0, то false - число равно 0
# number = int(input('Введите число: '))
# if number:
#     print('Число: ', number)
# else:
#     print('Число равно нулю.')


# # эта функция для преобразования типа в логический
# bool()

# a = 15
# b = 20
# c = 4
# if a > b and a > c:
#     print('a =', a, '- максимальное число')
# elif b > a and b > c:
#     print('b =', b, '- максимальное число')
# else:
#     print('c =', c, '- максимальное число')

# # определение счастливого билета
# number = 423342
# number_1 = number // 100000
# # print(number_1)
# number_2 = number % 100000 // 10000
# # print(number_2)
# number_3 = number % 10000 // 1000
# # print(number_3)
# number_4 = number % 1000 // 100
# # print(number_4)
# number_5 = number % 100 // 10
# # print(number_5)
# number_6 = number % 10 // 1
# # print(number_6)
# if number_1 * number_2 * number_3 == number_4 * number_5 * number_6:
#     print('билет счастливый')
# else:
#     print('простой билет')