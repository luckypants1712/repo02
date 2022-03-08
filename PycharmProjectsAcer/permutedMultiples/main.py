def isPrime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def compareDigits(n1, n2):
    n1Str = str(n1)
    n2Str = str(n2)

    n1Arr = list(n1Str)
    n2Arr = list(n2Str)

    n1Arr.sort()
    n2Arr.sort()

    n1Str = ''.join(n1Arr)
    n2Str = ''.join(n2Arr)

    return n1Str == n2Str

numbers = []
for i in range(1000,10000):
    if isPrime(i):
        numbers.append(i)
nTwo = 0
nThree = 0

for n in numbers:
    nTwo = n + 3330
    nThree = nTwo + 3330
    if isPrime(nTwo) and isPrime(nThree):
        if compareDigits(nTwo, nThree) and compareDigits(n, nThree):
            print(n, nTwo, nThree)
