# Эталонное решение из ответа на задание

lst = ['2018-01-01', 'yandex', 'cpc', 100]
lst = list(reversed(lst))
new_dict = lst[0]
for e in lst[1:]:
    new_dict = {e: new_dict}

print(new_dict)