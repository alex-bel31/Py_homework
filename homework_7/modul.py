from view import user_data as us

def creating_scv():
    file = 'telephone_directory.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'ID Фамилия Имя Номер телефона Описание\n')

info = us()
def import_scv():  
    file = 'telephone_directory.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]}; {info[1]}; {info[2]}; {info[3]}; {info[4]}\n')   

def export_data():
    with open('telephone_directory.csv', 'r') as file:
        data = []
        temp = file.readlines()
        for line in temp:
            data.append(line.strip('\n'))        
    return data
        

def search_data(data_search, data):
    if len(data) > 0:
        for item in data:
            if data_search in item:
                return item
    else:
        return None

     

