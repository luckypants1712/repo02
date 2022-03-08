x_repeat = 1
y_repeat = 12

for i in range(y_repeat):
    for i in range(x_repeat):
        print('/ \_', end='')
    print()
    x_repeat += 1
    for i in range(x_repeat):
        print('\_/ ', end='')
    print()
    x_repeat += 1