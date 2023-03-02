import random

list = [random.randrange(1, 10) for i in range(10)]
print(list)

def calculate(list):
    result = 0
    for i in range(1, len(list)):
        if i % 2 != 0:
            result = list[i] + result
    print(result)

calculate(list)