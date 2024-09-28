monthly_salary = int(input('Введите заработную плату в месяц:', ))
mortgage_percent = int(input('Введите, какой процент (%) от зарплаты уходит на ипотеку:', ))
life_percent = int(input('Введите, какой процент (%) уходит на жизнь:', ))

print('Вывод:')
print('На ипотеку было потрачено', 12*(monthly_salary*(mortgage_percent/100)))
print('Было накоплено:', 12*(monthly_salary-((monthly_salary*(mortgage_percent/100))+(monthly_salary*(life_percent/100)))))