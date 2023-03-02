import math
import random

list = [round(random.uniform(1.0, 10.0), 2) for i in range(5)]

list2 =[]
for i in range(0, len(list)):
    value = list[i] - int(list[i])
    list2.append(round(value,2))

result = max(list2) - min(list2)

print(f' - {list} -> {round(result,2)}')


