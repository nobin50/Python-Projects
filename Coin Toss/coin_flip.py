import random

print('I will flip a coin 1000 times.'+'\n' +'Lets see how many times head will come..')
print('Enter your guess')
guess = input()
toss = 0
head = 0

while( toss < 1000 ):
    if random.randint(0, 1) == 1:
        head = head + 1
    toss = toss+1
    if( toss == 100):
        print('After 100 iteration heads come upto '+ str(head) +' times.')
    if (toss == 500):
        print('After half iteration heads come upto '+ str(head) +' times.')
    if (toss == 900):
        print('After 900 iteration heads come upto '+ str(head) +' times.')

print()
print('Out of 1000 iteration...')
print('\t','Head comes up: ',head)
tail = 1000 - int(head)
print('\t','Tail comes up: ',tail)
print('Are you close to me?')
print('Happy to see you. Bye')