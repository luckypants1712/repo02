import math
count = 0
for i in range(1, pow(10, 25) + 1):
    for j in range(1, 10):
        k = len(str(i))
        if i == pow(j, k):
            count += 1
            print(i, '=', j, '*', k)
print(count)