def factoriel(n):
    if n == 0:
        return 1
    return n * factoriel(n-1)


mainNumber = factoriel(100)
digit = 0
sum = 0

while mainNumber != 0:
    digit = mainNumber % 10
    sum += digit
    mainNumber //= 10

print(sum, mainNumber)