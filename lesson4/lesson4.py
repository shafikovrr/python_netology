# dict = {'a': 'alfa', 'o': 'omega', 'g': 'gamma'}
# print(dict)

# # Словарь с помощью функции dict() или фигурных скобок {}
# telephones_dict = dict()
# capitals_dict = {}

# Ключами могут быть любые неизменные типы данных:
# strings (строки), booleans (логические значения), integers (целые числа), float (числа с плавающей точкой), tuple (картежи)

# Если ключ уже существует, то добавление в словарь этого же ключа с новым значением, перезапишет старое значение.

# # Получение значения из словаря  по ключу
# capitals_dict = {'Russia': 'Moscow', 'China': 'Beijing'}
# print(capitals_dict['Russia'])

# # Итерация по словарю
# for country, capital in capitals_dict.items():
#     print(country, '->', capital)

# # Добавление нового элемента в словарь
# capitals_dict['Bashkortostan'] = 'Ufa'
# for country, capital in capitals_dict.items():
#     print(country, '->', capital)

# # Операции с словарями
# del(dict[key]) # удаляет элемент из списка по ключу
# .keys() # позволяет получить все ключи словаря
# .values() # позволяет получить все значения словаря
# .items() # позволяет получить ключи и значения словаря
# .get(key) # "безопасно" возвращает значение по ключу (при отсутствии ключа ошибка не возникает, вернет None)
# .setdefault(key, default) # позволяет получить значение по ключу, автоматически добавляет элемент в словарь, если его нет

# Множества
# Множества (sets) - "контейнер", содержащий неповторяющиеся элементы в случайном порядке
# Множество реализуется с помощью функции set(). Обычно создается из списка 
# К словарям обращаемся только по ключам (не по индексу)

# Операции над множествами

# # Объединение (union) Логическое "ИЛИ" (or)
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}
# set_c = set_a | set_b # {1, 2, 3, 4, 5}

# # Пересечение (intersection) Логическое "И" (and)
# set_c = set_a & set_b # {3}

# # Разность (difference) 
# set_c = set_a - set_b # {1, 2}

# # Симметричная разность (symmetric difference)
# set_c = set_a ^ set_b # {1, 2, 4, 5}

# .add(el) - добавляет элемент в Множество
# .update(set) - соединяет множество с другим множеством/списком
# .discard(el) - удаляет элемент из множества по его значению
# .union(set) - объединяет множества (логическое "ИЛИ")
# .intersection(set) - пересечение множеств (логическое "И")
# .difference(set) - возвращает элементы одного множества, которые не принадлежат другому множеству (разность множеств)
# .symmetric_difference(set) - возвращает элементы, которые встречаются в одном множестве, но не встречаются в обоих

# Статические множества 
# frozenset - неизменяемое множество. Доступны все действия над множествами, за исключением тех, которые их изменяют

courses_list = [
    {'title':'Java-разработчик с нуля',
    'mentors': ['Павел Дерендяев', 'Алексей Яковлев', 'Сергей Сердюк']},
    {'title':'Веб-разработчик с нуля',
    'mentors': ['Николай Лопин', 'Алена Батицкая', 'Алексей Дацков', 'Александр Беспоясов']},
    {'title':'Frontend-разработчик с нуля',
    'mentors': ['Ильназ Гилязов', 'Татьяна Тен', 'Алена Батицкая', 'Алесандр Фитискин', 'Владимир Чебукин', 'Эдгар Нуруллин']}
]