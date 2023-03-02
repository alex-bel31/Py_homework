def rle_encoding(data):
    res = " "
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i+1]:
            count += 1
            i += 1
        res += str(count) + data[i]
        i += 1
    return res

def rle_decoding(data):
    res = ''
    count = ''
    for i in data:
        if i.isdigit():
            count += i
        else :
            if not count:
                res += i
            else: 
                res += int(count) * i
                count = ''
    return res
data = input("Введите данные для сжатия: ")
print(f"\nИсходные данные:\t {data}")
print(f"Закодированные данные:\t{rle_encoding(data)}")
print(f"Раскодированные данные:\t {rle_decoding(data)}")