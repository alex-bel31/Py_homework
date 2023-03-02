import random
max, min = map(int, input('Введите max и min через пробел: ').split())
list = [random.randrange(1, 10) for i in range(10)]
print(list)
res = []
for i in range(len(list)):
    if max <= list[i] and min >= list[i]:
        res.append(i)
print(res)

