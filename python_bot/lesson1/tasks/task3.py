dictionary = {} # создаем пустой словарь
data1 = input('Введите дату: ') # вводим значение переменной data1
task1 = input('Введите задачу: ') # вводим значение переменной task1
data2 = input('Введите дату: ')
task2 = input('Введите задачу: ')
data3 = input('Введите дату: ')
task3 = input('Введите задачу: ')
dictionary[data1] = task1 # вводим в словарь ключь и значение (data1 = task1)
dictionary[data2] = task2
dictionary[data3] = task3
print(dictionary) # ввыводим на экран заполненный словарь