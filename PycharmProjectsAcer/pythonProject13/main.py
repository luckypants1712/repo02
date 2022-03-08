import math, shutil, sys, time

############################
import random

WIDTH = 70
names = ['Zlatko Hršak', 'Matej Beg', 'Matija Vnnnnn', 'Danijel Smradočajni', 'Darko Belinec' ]
print('Upiši ispisivajuču recenicu: ')

message = input('>')
step = 1.5

while True:
    spaces = ' ' * int((math.sin(step) + 1) / 2 * (WIDTH - len(message)))
    print(spaces + names[random.randint(0, 4)])
    time.sleep(0.07)
    step += 0.3
