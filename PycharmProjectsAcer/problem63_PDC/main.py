import math
count = 0
for i in range(1, 10):
    for j in range(1, 23):
        result = pow(i, j)
        if len(str(result)) == j:
            print(i, '^', j, '=', result)
            count += 1
print(count)