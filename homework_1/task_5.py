import math

A1 = float(input("Введите А1 "))
A2 = float(input("Введите А2 "))
B1 = float(input("Введите B1 "))
B2 = float(input("Введите B2 "))
result = math.sqrt(((A1 - B1)**2) + ((A2 - B2)**2))
print(f'- A ({A1},{A2}); B ({B1},{B2}) -> {result}')
