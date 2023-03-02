num = int(input())
sum_num = 0

for i in range(1, num+1):
    sum_num += round((1+1/i)**i, 2)
print(f'для n = {num} -> {sum_num}')