import random
import copy

list = [random.randrange(1, 10) for i in range(10)]
print(f'\tПервоначальный список: \t{list}')
temp_list = copy.deepcopy(list)

def mix_list(temp_list):
    list_len = len(list)
    for i in range(list_len):
        index = random.randint(0, list_len-1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return temp_list
mixed_list = mix_list(list)
print(f'\tПеремешанный список: \t{mixed_list}')


