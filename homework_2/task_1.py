num = (input("Введите число "))

def sum_digits(num):
    return sum(map(int, num.replace('.','').replace('-','').replace(',','')))
    
print(f' - {num} -> {sum_digits(num)}')