def digitPowerSum(n):
    digit = 0
    number = ''
    numberSum = 0
    while n != 0:
        digit = n % 10
        number = digit * digit * digit * digit * digit
        n //= 10
        numberSum += number
    return numberSum

sum = 0

for i in range(1000000):
    if digitPowerSum(i) == i:
        print(i)
        sum += i
print('warning : ',sum)



