    
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

# Вывод списка всех документов в формате passport "2207 876234" "Василий Гупкин"
def list_dict_values(dict_list):
    for dict_item in dict_list:
        print(f"{dict_item['type']} {dict_item['number']} {dict_item['name']}")

# Просит номер документа и выведет имя человека, которому он принадлежит;
def people_dict_values(dict_list):
    number_doc_document = input('введите номер документа: ')
    for dict_item in dict_list:
        if number_doc_document == dict_item['number']:
            print(f"{dict_item['name']}")




def my_def(students):
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            people_dict_values(documents)
        elif user_input == 's':
            shelf_dictionary_values(directories)
        elif user_input == 'l':
            list_dict_values(documents)
        elif user_input == 'q':
            break
        else:
            print('Такой команды не существует')

my_def(documents)

