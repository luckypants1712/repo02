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


str_num = ''
result = 0
num = 0
for i in range(1, 10000):
    str_num = ''
    for j in range(1, 10):
        str_num += str(i * j)
        if len(str_num) == 9 and isPandigital(str_num):
            print(str_num)

