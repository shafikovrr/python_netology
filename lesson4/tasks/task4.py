stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

max_value = 0 # задаем (переменную) первый максимальный объем продаж = 0
max_key = '' # задаем (переменную) первый ключ с максимальными продажами = пустая строка
for key, value in stats.items(): # для ключа и значения в stats
    if value > max_value: # если value больше max_value
        max_value = value # приравнять переменной max_value значение value
        max_key = key # и переменной max_key задать значение ключа с максимальным value 
print(max_key) # вывести на печать max_key (ключ с максимальным объемом продаж)