import math


def triangular(n):
    return n * (n + 1) // 2

for tIndex in range(100000000000):
    result = triangular(tIndex)
    pIndex = (1 + math.sqrt(1 + 24 * result)) / 3
    hIndex = (1 + math.sqrt(1 + 8 * result)) / 4
    if pIndex.is_integer() and hIndex.is_integer():
        print(result)


