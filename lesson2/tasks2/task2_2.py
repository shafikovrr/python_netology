month = input('Введите месяц рождения: ')
day = int(input('Введите день рождения: '))

if month == "январь":
    if day < 20:
        print('козерог')
    else:
        print('водолей')
if month == 'февраль':
    if day <= 18:
        print('водолей')
    else:
        print('рыба')
if month == 'март':
    if day <= 20:
        print('рыба')
    else:
        print('овен')
if month == 'апрель':
    if day <= 20:
        print('овен')
    else:
        print('телец')
if month == 'май':
    if day <= 20:
        print('телец')
    else:
        print('близнец')
if month == 'июнь':
    if day <= 21:
        print('близнец')
    else:
        print('рак')
if month == 'июль':
    if day <= 22:
        print('рак')
    else:
        print('лев')
if month == 'август':
    if day <= 22:
        print('лев')
    else:
        print('дева')
if month == 'сентябрь':
    if day <= 23:
        print('дева')
    else:
        print('весы')
if month == 'октябрь':
    if day <= 23:
        print('весы')
    else:
        print('скорпион')
if month == 'ноябрь':
    if day <= 22:
        print('скорпион')
    else:
        print('стрелец')
if month == 'декабрь':
    if day <= 21:
        print('стрелец')
    else:
        print('козерог')