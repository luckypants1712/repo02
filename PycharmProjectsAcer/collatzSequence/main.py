def collatz(number):
    if number % 2 == 0:
        return number/2
    elif number %2 == 1:
        return number *3+1
print('unesi broj')
a=input()

try:
    while a!=1:
        a=collatz(int(a))
        print(int(a))
    except:
        print("you must type a integer" )

