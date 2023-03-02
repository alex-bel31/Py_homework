n = int(input("Введите обозначающую день недели"))
if n == 6 or n == 7:
    print(f'- {n} -> да')
elif n<6 and n>0:
    print(f'- {n} -> нет')
else:
    print('это вообще не день недели')

