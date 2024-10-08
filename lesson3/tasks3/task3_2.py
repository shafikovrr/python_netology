cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',  
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],  
      ]
  ]
]

person = 5

for dish in cook_book: # задаем переменную dish (блюдо) из списка
    print(f'\n{dish[0].title()}:') # dish[0] - в цикле выводит название вложенного списка с заглавной буквой - title()
    for ingredients in dish[1]: # задаем переменную ingredients в списке dish с индексом 1
        print(f'{ingredients[0]}, {ingredients[1] * person}{ingredients[2]}') # [[0] - 'картофель', [1] - 100, [2] - 'гр.']

# эталонное решение
# 
# new_cook_book = []
# for dish, ingredients in cook_book:
#     print(dish)
#     for ingredient in ingredients:
#         ingredient_name = ingredient[0]
#         ingredient_count = ingredient[1] * person
#         ingredient_measure = ingredient[2]
#         print(f'{ingredient_name}, {ingredient_count}{ingredient_measure}')
#     print() 