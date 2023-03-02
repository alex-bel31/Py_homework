number = int(input("Введите число "))
decimal_num = ''
while number > 0:
    decimal_num = str(number % 2) + decimal_num
    number = number // 2

print(f' - {number} -> {decimal_num}')

