X = int(input('Введите Х '))
Y = int(input('Введите Y '))
if X > 0 and Y > 0:
    print(f'-  x = {X}; y = {X} -> 1 ')
elif X < 0 and Y > 0:
    print(f'-  x = {X}; y = {X} -> 2 ')
elif X < 0 and Y < 0:
    print(f'-  x = {X}; y = {X} -> 3 ')
elif X > 0 and Y < 0:
    print(f'-  x = {X}; y = {X} -> 4 ')
else: print('ERROR')
    

