import math
divisors = []
def g(n):
    iSqr = 0
    for i in range(1, int(math.sqrt(n) + 1)):
        ii = i*i
        if n % ii == 0:
            iSqr = ii
    return iSqr

def s(n):
    sum = 0
    for i in range(1, n + 1):
       sum += g(i)
    return sum

print(s(100000000000000))

