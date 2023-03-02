import random
len_list = int(input("Введите длинну списка "))
list = [random.randrange(1, 10) for i in range(len_list)]
list2 = [ ]

result = 0
for i in range(len(list)):
    while i < len(list)/2 and len_list > len(list)/2:
        len_list = len_list - 1
        a = list[i] * list[len_list]
        list2.append(a)
        i += 1
print(f' - {list} => {list2}')


