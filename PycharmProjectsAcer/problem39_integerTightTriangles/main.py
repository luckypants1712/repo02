import math
a = 0
b = 0
c = 0
P = 1000
maxSol = 0
maxP = 0
for P in range(3, 1001):
    count = 0
    for a in range(1, P):
        for b in range(1, a + 1):
            c = P - a - b
            if c**2 == a**2 + b**2:
                print('a :', a, 'b :', b, 'c :', c)
                count += 1

    if count > maxSol:
        maxSol = count
        maxP = P
    print(P, ':', 'count :', count)
print(maxP, ': ', maxSol)