import math

poweredNum = []

for a in range(2, 101):
    for b in range(2, 101):
        num = math.pow(a, b)
        if num not in poweredNum:
            poweredNum.append(num)
        else:
            continue
print(len(poweredNum))
