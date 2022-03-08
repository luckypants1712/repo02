def isPandigital(n):
    num = str(n)
    for digit in num:
        count = 0
        for i in num:
            if int(digit) > len(num) or int(digit) < 1:
                return False
            if digit == i:
                count += 1
            if count > 1:
                return False
    return True

data = []
product = 0
data_str = ''
sum = 0
for i in range(1, 10000):
    for j in range(1, 10000):
        product = i * j
        data_str = str(i) + str(j) + str(product)

        if product in data or len(data_str) != 9:
            continue
        if isPandigital(data_str):
            data.append(product)
            print(i, j, product)
            sum += product
print(sum)



