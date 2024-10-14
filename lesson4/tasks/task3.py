queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

one = 0 # первоначальное количество запросов из одного слова
two = 0 # первоначальное количество запросов из двух слов
three = 0 # первоначальное количество запросов из трех слов
number_of_all_queries = len(queries) # количество всех запросов
print('Количество запросов: ', number_of_all_queries)
print()
for element in queries: # для каждого element (элемент №1 = 'смотреть сериалы онлайн' и т.д.) в списке (queries)
    # print(len(element.split()))
    if len(element.split()) == 1: # если количество слов в запросе равно 1 (разделяем каждый запрос с помощью метода .split() - по умолчанию разделитель - пробел - получаем количество (с помощью len) слов в запросе)  
        one = one + 1 # прибавляем в цикле к one единицу (0+1, 1+1, 2+1 и т.д. если количество элементов в запросе (количество слов) = 1)
        
    elif len(element.split()) == 2:
        two = two + 1
        
    elif len(element.split()) == 3:
        three = three + 1

percent_one = round(one/number_of_all_queries*100, 2) # округляем проценты с помощью round до двух значений поле запятой
percent_two = round(two/number_of_all_queries*100, 2)
percent_three = round(three/number_of_all_queries*100, 2)
print('Количество запросов с одним словом: ', one, 'или в процентах', percent_one)
print('Количество запросов с двумя словами: ', two, 'или в процентах', percent_two)
print('Количество запросов с тремя словами: ', three, 'или в процентах', percent_three)

print(percent_one + percent_two + percent_three)