def fibonacci(number):

    if number in [1, 2]: return 1
    else: return fibonacci(number - 1) + fibonacci(number - 2)

def negafibonacci(number):
    if number == 1:                       
        return 1
    elif number == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, number):
            num1, num2 = num2, num1 - num2
        return num2

number = int(input())
list = [0]
for i in range(1,number + 1):
    list.append(fibonacci(i))
    list.insert(0, negafibonacci(i))
print(f' - для k = {number} список будет выглядеть так: {list}')

 