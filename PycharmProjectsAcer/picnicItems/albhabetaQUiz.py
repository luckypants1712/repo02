import random,  time


QUIZ_DURATION = 30

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphaArr = list(ALPHABET)
possible_outcomes = {
    0 : 'Dwight',
    1 : 'Kevin',
    2 : 'Jim',
    3 : 'Michael'
}

start_time = time.time()
wins = 0
while True:
    aSample = random.sample(alphaArr, 5)
    print(aSample)
    aSample.sort()
    newWord = ''.join(aSample)

    print('Sort letter in order: ', end=' ')
    playerChoice = input()

    if playerChoice.upper() == newWord:
        print('you are LEGEND')
        wins += 1

    current_passed = time.time() - start_time
    if current_passed > QUIZ_DURATION:
        break

print('game over')
print('You had ' + str(wins) + ' wins')

if wins > 3:
    print('you are' + possible_outcomes[3])
else:
    print('you are' + possible_outcomes[wins])