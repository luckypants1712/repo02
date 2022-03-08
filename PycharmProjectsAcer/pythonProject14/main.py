number = 69
def factorial(f):
    if f == 0:
        return 1
    return f * factorial(f - 1)


def factorial_sum(n):
    digit_sum = 0
    n_str = str(n)
    for digit in n_str:
        digit_sum += factorial(int(digit))
    return digit_sum


def row_ceck(number):
    results = []
    results.append(number)
    while True:
        number = factorial_sum(number)
        if number in results:
            break
        else:
            results.append(number)
    return results
count = 0

for i in range(1000000):
    if len(row_ceck(i)) == 60:
        count += 1

print(count)






