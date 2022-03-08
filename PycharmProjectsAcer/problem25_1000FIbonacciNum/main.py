def recursion(n):
    if n == 1 or n == 2:
        return 1
    return recursion(n - 1) + recursion(n - 2)

for i in range(1, 100000000):
    num = recursion(i)
    print(num)