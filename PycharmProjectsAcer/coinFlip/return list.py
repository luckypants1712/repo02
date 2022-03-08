import random

spam = ['apples', 'bananas', 'tofu', 'cats']

def listReturn(listz):
    for i in listz:
        print(i+',')
        if i == spam[1]:
            print(' end')

listReturn(spam)