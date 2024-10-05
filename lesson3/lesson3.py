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
print('y' + 'u')
# Умножение строки *: y * 5 = yyyyy
print('y' * 5)
# Привести строку к верхнему регистру
y = 'rinat'
print(y.upper()) # rinat = RINAT
# Приведение строки к нижнему регистру
x = 'RINAT'
print(x.lower()) # RINAT = rinat
# Приводит первую букву к верхнему регистру
z = 'rinat'
print(z.capitalize()) # rinat = Rinat
# Заменяет один элемент в строке на другой
m = 'my home'
print(m)
print(m.replace('my', 'her'))
# Определяет длину строки
c = 'my home'
print(len(c)) # 2 + 1 + 4 = 7
