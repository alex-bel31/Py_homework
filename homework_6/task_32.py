a, b = map(int, input('Введите A и B через пробел: ').split())
def pow(a,b):
    if b == 0:
        return 1
    if b < 0:
        return 1/pow(a, -b)
    return a * pow(a, b-1)
print(f'A^(B) -> {pow(a, b)}')

