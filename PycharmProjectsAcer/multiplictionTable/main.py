import time
mul = 1

for i in range(11):
    if i == 0:
        print(str(i).ljust(2) + '|', end='')
    else:
        print(str(i).ljust(3), end='')

print()
print('-'*3*11)
for i in range(1, 11):
    print(str(i).ljust(2),  end='')
    print('|', end='')


    for j in range(1, 11):
        mul = i * j
        print(str(mul).ljust(3), end='', flush=False)

    print()
    # #if mul < 10:
    #     print(mul, '  ', end='')
    # else:
    #     print(mul, ' ', end='')