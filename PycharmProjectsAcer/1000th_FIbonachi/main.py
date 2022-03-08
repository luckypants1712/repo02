


def recursione(n):
    if n == 1 or n == 2:
        return 1
    return recursione(n - 1) + recursione(n - 2)



for i in range(1, 100000):
    print(recursione(i))
