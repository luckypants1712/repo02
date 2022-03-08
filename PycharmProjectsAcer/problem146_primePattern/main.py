import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

numbers = [1, 3, 7, 9, 13, 27]

for n in range(1, 150000000):
     arePrimes = True
     count = 0
     nSqr = n * n
     for i in numbers:
        if not isPrime(nSqr + i):
            arePrimes = False
            break

     areConsecutive = False
     if arePrimes:
        areConsecutive = True
        for i in range(1, 28):
            if i not in numbers:
                if isPrime(nSqr + i):
                    areConsecutive = False
                    break
        if areConsecutive:
            print(n)





