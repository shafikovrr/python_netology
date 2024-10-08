boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']


if len(boys) != len(girls): # проверка количества элементов (len) и их неравенство в списках 5 = 5
    print('Кто то может остаться без пары, знакомить никого не будем')

else:
    print('Идеальные пары:')
    for boy, girl in zip(sorted(boys), sorted(girls)): 
        print(f'{boy} и {girl}')

# Эталонное решение
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# if len(boys) != len(girls):
#     print('Кому-то не достанется пары!')
# pairs = zip(sorted(boys), sorted(girls))
# print('Идеальные пары: ')
# for boy, girl in pairs:
#     print(f'{boy} и {girl}')