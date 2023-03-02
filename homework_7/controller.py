from modul import *
from view import *


def menu():
    print("Доступные операции с телефонной книгой:\n\
    1 - импорт;\n\
    2 - поиск контакта.")
    ch = input("Введите цифру: ")
    if ch == '1':
        creating_scv()
        import_scv()
    else:
        data_search = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(data_search, data)
        if item != None:
            print("ID " "Фамилия" "Имя" "Номер телефоня" "Описание")
            print('*'*20)
            print(item[0], item[1], item[2], item[3], item[4])
        else:
            print("Данные не обнаружены")