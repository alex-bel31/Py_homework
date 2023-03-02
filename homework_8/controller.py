import modul
import view

def randomdict():
    modul.subjgenerator()
    modul.namegenerator()
    modul.markgenerator()

def go():
    
    print('\n')
    pick = view.choise_user()
    if pick == 6:
        return 0
    if pick == 1:
        modul.addstudent()
        print('\n')
        return go()
    if pick == 2:
        modul.addsubject()
        print('\n')
        return go()
    if pick == 3:
        modul.mark()
        print('\n')
        return go()
    if pick == 4:
        modul.showstudents()
        print('\n')
        return go()
        
    if pick == 5:
        modul.showmarks()
        print('\n')
        return go()
    
    else:
        print('Некорректый ввод \n')
        return go()