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
    'mentors': ['Павел Дерендяев', 'Алексей Яковлев', 'Сергей Сердюк'], 'duration':11},
    {'title':'Веб-разработчик с нуля',
    'mentors': ['Николай Лопин', 'Алена Батицкая', 'Алексей Дацков', 'Александр Беспоясов'], 'duration':19},
    {'title':'Frontend-разработчик с нуля',
    'mentors': ['Ильназ Гилязов', 'Татьяна Тен', 'Алена Батицкая', 'Алесандр Фитискин', 'Владимир Чебукин', 'Эдгар Нуруллин'], 'duration':13}
]

# for course in courses_list: # course - это словарь первый, второй, третий по циклу (всего три словаря)
#     print('Название курса: {}'.format(course['title'])) # узнаем название i-го курса в цикле по ключу 'title'
#     print('Преподаватели: {}'.format(', '.join(course['mentors']))) # вывести всех преподавателей строкой (join) через запятую ', ' по ключу 'mentors'
#     print()
# .format() - аналог f-строк. В нужных местах ставим скобки {}, чтобы вставить вместо них нужную информацию
# 

# for course in courses_list:
#     for k, v in course.items(): # .items() возвращает ключ-значение (ключ=title, значение=Java-разработчик с нуля)
#         print(f'ключ={k}, значение={v}')

# ## Вывести название всех курсов, количество преподавателей на каждом курсе. Определить победителя по максимальному количеству преподавателей на курсе
# max_count = 0 # наибольшее количество преподавателей
# lider_id = -1 # порядковый номер курса (инициализируем отрицательным числом, так как ничего о нем не знаем)
# for id, course in enumerate(courses_list): # enumerate() - превращаем список в итерируемый объект, т.е. появляется индекс, обрабатываемого в данный момент элемента (id)
#     print('Название курса: {}'.format(course['title']))
#     count = len(course['mentors']) # количество элементов len() курса по ключу 'mentors' в элементе course - сколько всего преподавателей на каждом курсе
#     print(f'количество преподавателей на курсе: {count}')
#     if count > max_count:
#         max_count = count
#         lider_id = id
# print('Наш лидер - курс {}, преподавателей: {}'.format(courses_list[id]['title'], len(courses_list[id]['mentors'])))
# # courses_list[id] - получили только словарь. ['title'] далее достаем название курса.
# # .format - внутри через запятую указываем те данные, которые нужно вывести в print в фигурных {} скобках

# # Добавление нового курса в существующий словарь
# new_course_dict = {} # создаем пустой словарь
# new_course_dict.setdefault('title', 'C++')
# new_course_dict.setdefault('mentors', [])
# new_course_dict.setdefault('duration', 15)
# print(new_course_dict) # Вывод - {'title': 'C++', 'mentors': [], 'duration': 15}



# new_course_dict = {} # создаем пустой словарь
# new_course_dict.setdefault('title', 'C++')
# new_course_dict.setdefault('mentors', [])
# new_course_dict.setdefault('mentors', ['Елена Никитина']) # добавления нового преподавателя
# new_course_dict.setdefault('duration', 15)
# print(new_course_dict) # Вывод - {'title': 'C++', 'mentors': [], 'duration': 15}. mentors - пусто, после добавления нового преподавателя
# # Команда setdefault() - проверяет, нет ли такого ключа (mentors) в словаре new_course_dict = {}. В первой команде уже присвоено значение [], поэтому добавить через setdefault не получится 

# # Перезаписывается значение mentors - new_course_dict['mentors'] = ['Олег Булыгин']
# new_course_dict = {} # создаем пустой словарь
# new_course_dict.setdefault('title', 'C++')
# new_course_dict.setdefault('mentors', ['Елена Никитина']) # добавления нового преподавателя
# new_course_dict['mentors'] = ['Олег Булыгин'] # если присвоить новое значение, оно перезапишет значение 'Елена Никитина'
# new_course_dict.setdefault('duration', 15)
# print(new_course_dict)


# Добавляет в конец новой значение в mentors - new_course_dict['mentors'].append('Олег Булыгин')
new_course_dict = {} # создаем пустой словарь
new_course_dict.setdefault('title', 'C++')
new_course_dict.setdefault('mentors', ['Елена Никитина']) # добавления нового преподавателя
new_course_dict['mentors'].append('Олег Булыгин') # добавляется новое значение, оно запишется после 'Елена Никитина'
new_course_dict.setdefault('duration', 15)
print(new_course_dict)


# 
# 

# if 'mentors' not in new_course_dict.keys(): # проверка существования 'mentors' - если нет
#     new_course_dict['mentors'] = [] # создаем пустой список 'mentors'

# 
# new_course_dict.setdefault('duration', 15)
# 