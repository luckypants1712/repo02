import math
expectedNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def isPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


numbersOfNumber = ''
digitsList = []
for i in range(100000000, 1000000000):
    if isPrime(i):
        numbersOfNumber = str(i)
        digitsList = list(numbersOfNumber)
        digitsList.sort()
        print(digitsList)