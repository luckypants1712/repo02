def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def combiForma(n, r):
    formula = factorial(n) / (factorial(r) * factorial(n - r))
    return formula


count = 0

for i in range(1, 101):
     for j in range(i):
         if combiForma(i, j) > 1000000:
             count += 1

print(count)