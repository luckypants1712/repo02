
def digitSort(n):
    sortedNum = []
    numberStr = str(n)
    digits = list(numberStr)
    digits.sort()
    return ''.join(digits)

for i in range(1, 1000000):

    if digitSort(i) == digitSort(i*2) and digitSort(i) == digitSort(i*3) and digitSort(i) == digitSort(i*4) and digitSort(i) == digitSort(i*5) and digitSort(i) == digitSort(i*6):
        print(i)

