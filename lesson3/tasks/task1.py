boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']


if len(boys) != len(girls): # проверка количества элементов (len) и их неравенство в списках 5 = 5
    print('Кто то может остаться без пары, знакомить никого не будем')

else:
    print('Идеальные пары:')
    for boy, girl in zip(sorted(boys), sorted(girls)): 
        print(f'{boy} и {girl}')