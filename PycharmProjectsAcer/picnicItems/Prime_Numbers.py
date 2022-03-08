def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


while True:
    print('Write in number from which to start from: ')
    message = input('>')

    if message.isdecimal():
        strtNum = int(message)
        break

counter = 0
i = strtNum
while True:
    if isPrime(i):
        if counter % 2 == 0:
            print(' ', i)
        else:
            print(i)
        counter += 1
    i += 1
