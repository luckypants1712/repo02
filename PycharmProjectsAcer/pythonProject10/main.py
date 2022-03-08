def isPrime(n):
    numToSave = 0
    for i in range (7 ,6857):
        if i % 2 != 0:
            continue
        if n % i == 0:
             numToSave = i;
    return numToSave

numberToCount = 600851475143
print(isPrime(numberToCount))
