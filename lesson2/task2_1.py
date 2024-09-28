height = int(input('Введите рост: '))
age = int(input('Введите возраст: '))
children = int(input('Количество детей: '))
study = input('Вы учитесь?: ')

if 18 <= age <= 27 and children < 4 and study == "нет":
    if height < 170:
        print('В танкисты')
    elif height < 185:
        print('На флот')
    elif height < 200:
        print('В десантники')
    else:
        print('В другие войска')
elif 18 <= age <= 27 and children < 4 and study == "да":
    print('Отсрочка от армии из-за прохождения обучения')
elif 18 <= age <= 27 and children > 4 and study == "нет":
    print('Отсрочка от армии по количеству детей')
elif 18 <= age <= 27 and children > 4 and study == "да":
    print('Отсрочка от армии по количеству детей (проходит обучение)')
