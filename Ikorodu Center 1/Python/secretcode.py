print('Shofile Omowunmi Idowu.')
print('08037107863.')
print('Codelagos Project.')
print('Guess my sewing secretcode.')
print('Welcome To OllyBeauty Home Of Programmig.')
import random
print('Hello. What is your name?')
name = input()
print('Oh, '+ name +', my sewing secretcode is between 1 and 20.')

SecretCode = random.randint (1,20)
for guessesTaken in range(1,5):
    print('Take a guess.')
    guess = int(input)

    if guess < secretCode:
       print('your guess is too low.')
    elif guess > secretCode:
         print('your guess is too high.')
    else:
         break #This condition is for the correct guess!
if guess == secretCode:
   print('Correct,' + name + '! you guessed my secretcode in' + str(guessesTaken) + 'guess!') 
else:
    print('Sorry. My sewing secretcode is' + str(secretcode)