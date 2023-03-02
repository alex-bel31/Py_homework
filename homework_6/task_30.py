print('Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.') 
a, d, n = map(int, input('Введите a1, d, n через пробел: ').split( ))
res = list(map(int,[a + i * d for i in range(n)]))

print(res)


