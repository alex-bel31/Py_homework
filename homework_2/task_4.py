import random

num = int(input('Задайте количество элементов: '))

with open('file.txt', 'w')as position:
    position.write(f'{random.randrange(0,num)}\n')
    position.write(f'{random.randrange(0,num)}')

with open('file.txt', 'r')as position:
    # for line in position:
        position.seek(0)
        index_1 =  int(position.readline())
        index_2 =  int(position.readline())

list_number = [i for i in range(-num,num+1)]
result = list_number[index_1] * list_number[index_2]

print(list_number, end="\n")
print (f'Позиции элементов из file.txt: [{index_1}], [{index_2}]\n')
print (f'Произведение элементов на указаных позициях: {result}')




    