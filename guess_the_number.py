import random

print('Hello! What is your name?')

name = input()

print('Well, ' +name+ ' I am thinking of a number between 1 and 20')
print('So, take a guess')

secret = random.randint(1,20)

for i in range (1,6):
    num = int(input())
    if(num > secret):
        print('Your guess is too high')
    if(num < secret):
        print('Your guess is too low')
    if(num == secret):
        break

if(num == secret):
    print('Good job, ' +name+ ' you guessed the number in ' +str(i)+ ' guesses.')
else:
    print('Nope, I was guissing the number ' +str(secret)+ ' better luck next time.')
