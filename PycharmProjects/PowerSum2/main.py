import math
number = pow(2, 1000)
print(number)

numStr = str(number)
print(len(numStr))
sum = 0
for i in numStr:
    sum = sum + int(i)
print(sum)