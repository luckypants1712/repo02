numbers = ''
for i in range(200000):
    numbers += str(i)


solutionOFmyProblems = int(numbers[1]) * int(numbers[10]) * int(numbers[100]) * int(numbers[1000]) * int(numbers[10000]) * int(numbers[100000]) * int(numbers[1000000])
print(solutionOFmyProblems)
