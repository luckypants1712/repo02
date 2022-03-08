import math
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def rotate(n):
    nStr = str(n)
    num = int(nStr[1 :] + nStr[0])
    return num
primesNeg = [0, 2, 4, 6, 8, 5]

countTwo = 0
for i in range(1, 1000000):
    char = str(i)
    digits = list(char)

    if i > 9:
        isBool = False
        for s in digits:
            if int(s) in primesNeg:
                isBool = True
                break

        if isBool:
            continue

    if isPrime(i):

        rNum = i
        isCircular = True
        count = 1
        for c in range(len(char) - 1) :
            rNum = rotate(rNum)
            if not isPrime(rNum):
                isCircular = False
                break


        if isCircular:
            countTwo += 1
        print('countTwo :', countTwo)
        print(i)






