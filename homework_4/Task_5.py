with open('File_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')

with open('File_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('File_1.txt','r') as file:
    file_1 = file.readline()
    list_of_file_1 = file_1.split()

with open('File_2.txt','r') as file:
    file_2 = file.readline()
    list_of_file_2 = file_2.split()

print(f'{list_of_file_1} + {list_of_file_2}')
sum_file = list_of_file_1 + list_of_file_2

with open('sum_file.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_file_1} + {list_of_file_2}')