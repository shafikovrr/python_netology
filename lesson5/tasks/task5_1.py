# Список со вложенными словарями   
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]

# Словарь со вложенными списками
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

# Функция вывода списка всех документов в формате passport "2207 876234" "Василий Гупкин"
def list_dict_values(dict_list):
    for dict_item in dict_list:
        print(f"{dict_item['type']} {dict_item['number']} {dict_item['name']}")

# Функция просит номер документа и выведет имя человека, которому он принадлежит;
def people_dict_values(dict_list):
    number_doc_document = input('введите номер документа: ')
    for dict_item in dict_list:
        if number_doc_document == dict_item['number']:
            print(f"{dict_item['name']}")


# Функция спрашивает номер документа, и затем выводит номер полки, на которой он находится
def shelf_dict_values(directories):
    doc_number = input("Номер документа ")
    for item in directories.items():
        if doc_number in item[1]:
            return print(f"'Номер полки: ' {item[0]}")
        else:
            print('Такого номера документа не существует')

# Функция добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться
def add_dict_values(directories, documents):
    add_value = list(input('Введите <Номер полки>, <Тип документа>, <Номер документа> и <ФИО> через запятую: ').split(', '))
    if add_value[0] not in directories:
        print('Такой полки не существует')
        return
    documents.append({"type": add_value[1], "number": add_value[2], "name": add_value[3]})
    directories[add_value[0]].append(add_value[2])

# Основная функция меню вызова команд
def my_def(students):
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            people_dict_values(documents)
        elif user_input == 's':
            shelf_dict_values(directories)
        elif user_input == 'a':
            add_dict_values(directories, documents)
        elif user_input == 'l':
            list_dict_values(documents)
        elif user_input == 'q':
            break
        else:
            print('Такой команды не существует')

my_def(documents)

