import random
boysnames = ['Владимир','Дмитрий','Александр','Андрей','Сергей','Егор','Евгений']
boyssurenames =['Афанасьев','Ермаков','Петров','Кондратьев','Новицкий','Клепиков','Федоров']
girlsnames = ['Екатерина','Мария','Полина','Светлана','Виктория','Дарья','Анна']
girlssurenames  = ['Афанасьева','Ермакова','Петрова','Кондратьева','Новицкая','Клепикова','Федорова']
subjlist = ['русский язык', 'литература', 'математика', 'иностранный язык', 'история', 'физическая культура', 'музыка', 'технология']
def is_valid(output,error):
    message = input(output)
    if not message.isdigit():
        print(error)
        return is_valid(output,error)
    return int(message)


studentdict = {}  

def idfinder():
    arr = list(studentdict.keys())
    id = len(arr)+1 
    return id

def addstudent():
    name,surname = input('Введите имя и фамилию ученика').split()
    studentdict.update({f'{name} {surname}':[ (elem,[]) for elem in subjlist]})

def addsubject():
    subj = input('Введите название предмета: ')
    for i in studentdict:
        studentdict.get(i).append((subj,[]))


def showstudents():
    studentlist = []
    for i in range(len(studentdict)):
        print(f'{i+1} {list(studentdict.keys())[i]}')
        studentlist.append(list(studentdict.keys())[i])
    return studentlist

def showsubj():
    i = 1
    for subj in subjlist:
        print(f'{i} {subj}')
        i+=1

def subjgenerator():
    
    for i in studentdict:
        print(subjlist)
        studentdict.get(i).append((subjlist[random.randint(0,7)],[]))


def namegenerator():
    for i in range(50):
        studentdict.update({f'{girlsnames[random.randint(0,6)]} {girlssurenames[random.randint(0,6)]}':[ (elem,[]) for elem in subjlist]})
    for i in range(50):
        studentdict.update({f'{boysnames[random.randint(0,6)]} {boyssurenames[random.randint(0,6)]}':[ (elem,[]) for elem in subjlist]})

marklist  = []
def mark():
    a = showstudents()
    pickstudent = is_valid('Выберите ученика по номеру в первом столбике: ', 'Некорректный ввод')
    
    if pickstudent > len(studentdict) or pickstudent <= 0:
        print('Некорректный ввод')
        return mark()
    print('\n')
    showsubj()
    picksubj = is_valid('Выберите предмет по номеру в первом столбике: ', 'Некорректный ввод,')
    while  picksubj > len(subjlist) or picksubj <= 0:
        print('Некорректный ввод, введите номер предмета!')
        showsubj()
        picksubj = is_valid('Выберите предмет по номеру в первом столбике: ', 'Некорректный ввод')
    number = is_valid('Введите оценку : ', 'Некорректный ввод')
    while  number > 5 or number <= 0:
        print('Некорректный ввод')
        number = is_valid('Введите оценку : ', 'Некорректный ввод')
    f = studentdict.get(a[pickstudent-1])
    f[picksubj-1][1].append(number)   

def markgenerator():
    for i in studentdict:
        studentdict.get(i)[random.randint(0,7)][1].append(random.randint(1,5))

def showmarks():
    a = showstudents()
    pickstudent = is_valid('Выберите ученика по номеру в первом столбике: ', 'Некорректный ввод')
    
    if pickstudent > len(studentdict) or pickstudent <= 0:
        print('Некорректный ввод, введите номер ученика!')
        return showmarks()
    print(list(studentdict.keys())[pickstudent-1])
    marks = studentdict.get(a[pickstudent-1])
    for mark in marks:
        print(f'{mark[0]} {mark[1]}')

