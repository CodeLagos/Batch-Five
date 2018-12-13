
import random
import time

guessTaken = 0
number = random.randint(1, 10)
time1=time.time()
while  guessTaken < 7:
    print('Choose a Number from 1 - 10')
    guess = input()
    guess = int (guess)

    guessTaken = guessTaken + 1
    print( 7 - guessTaken, 'guesses left')
    
    if guess < number: 
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break

myname = input('what is your name?')

if guess == number:
    guessTaken = str(guessTaken)
    print('Congratulations,  ' + myname + '!  you won')
if guess  != number:
    number = str(number)
    print('No! The number i was thinking of was ' + number)
time2=time.time()
totalTime=str(int(time2-time1))
print('it took you ' + totalTime + ' seconds')
