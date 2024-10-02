# def my_func(my_list):
#     count = 0
#     letter = 'c'
#     my_list = ['python', 'c++', 'c', 'scala', 'java']
#     for word in my_list:
#         if letter in word == 'c':
#             count += 1
#     return count    
#     print(count)

my_list = input('Введите слова через пробел: ')
letter = input('Введите букву для поиска: ')

def count_letters(my_list, letter):
    count = 0
    for item in my_list:
        if letter in item:
            count += item.count(letter)
    return count

result = count_letters(my_list, letter)
print(f'{letter} встречается {result} раз(а) в списке.')
