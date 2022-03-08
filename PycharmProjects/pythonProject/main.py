import math

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

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
num = 0
for i in range(1, 1000000000):
    if isPandigital(i) and isPrime(i):
        num = i
        print(i)
print(i)