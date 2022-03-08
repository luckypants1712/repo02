import random
numExperiments = 100000
streak = 0
numCoins = 100
streakLength = 20
for experiment in range(numExperiments):
    numbers = []
    for i in range(numCoins):
        result = random.randint(0, 1)
        numbers.append(result)
        #print(str(i) + ': ' + str(numbers[i]))

    streakExists = False
    for i in range(0, numCoins-streakLength+1):
        allSame = True
        for j in range(1, streakLength):
            if numbers[i+j] != numbers[i]:
                allSame = False
                break
        if allSame:
            streakExists = True
            break

    if streakExists:
        #print('postoji streak' + ' ' + str(i))
        streak += 1

print(str(streak/numExperiments*100) + '%')