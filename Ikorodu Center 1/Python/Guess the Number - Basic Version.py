import random
highScore = 0

def reverse_number(number):
    reverse = 0
    while number > 0:
        remainder = number%10
        reverse = reverse*10 + remainder
        number = number//10
    return reverse

def levelN(maxi, c, cStr, cl):
    restart = 'y'
    RESTART = 0

    if RESTART == 0:
        highScore = 0
    else:
        hisc = open('highScore.txt', 'r')
        highScore = float(hisc.read())
    theNumber = random.randint(1, maxi)

    print('I\'M THINKING OF A NUMBER BETWEEN 1 AND', maxi)
    print('You\'ve got only', cStr, 'shots at this')
    guessedNumber = int(input('Guess the number: '))

    chances = 0
    score = maxi
    while guessedNumber != theNumber and chances < (c-1):
        print()
        if guessedNumber - theNumber >= cl:
            print('GO LOWER - VERY LOW')
        if guessedNumber - theNumber >= 1 and guessedNumber - theNumber < cl:
            print("GO LOWER - YOU'RE CLOSE")
        if theNumber - guessedNumber >= cl:
            print('GO HIGHER - VERY HIGH')
        if theNumber - guessedNumber >= 1 and theNumber - guessedNumber < cl:
            print("GO HIGHER - YOU'RE CLOSE")        
        if guessedNumber == reverse_number(theNumber):
            print('Right Numbers in the Wrong Places')
        if guessedNumber//10 == theNumber//10:
            print('First Digit is in the Right Place')
        if (guessedNumber%10 == theNumber%10):
            print('Second Digit is in the Right Place')
        print('You have', (c-chances-1), 'chances left.', 'Try again')
        guessedNumber = int(input('Guess the number: '))
        chances+=1
        score = (maxi - (maxi/4)*(chances - (maxi/100)))
    if guessedNumber != theNumber:
        print()
        print('You Lost')
        print('The number IS', theNumber)
        print('Your score IS 0')
    else:
        print()
        if chances == 0:
            print('BRAVO, You tried it 1 time')
        else:
            print('YOU WON!!!' \
                  'You tried it', chances+1, 'times')
        print('Your score is,', score)
        if score > highScore:
            hisc = open('highScore.txt', 'w')
            scoreInStr = str(score)
            hisc.write(scoreInStr)
            print('You\'ve made an high score')
    hisc = open('highScore.txt', 'r')
    highScore = hisc.read()
    print('HIGHSCORE:', highScore)
    hisc.close()
            

    print()
    
    RESTART+=1

print('******************THE GUESSING GAME*************************')            
name = input('Enter your Username: ')
print('Welcome,', name)
levelN(100, 5, 'FIVE', 20)
yes = input('Want to level up?(Y/N):')
if yes.lower() == 'y':
    print()
    levelN(1000, 10, 'TEN', 200)
elif yes.lower() == 'n':
    print()
    yes1 = input('DO YOU WANT TO QUIT?(Y/N): ')
    print()
    if yes1.lower() == 'y' :
        print('Thank You')
    else:
        levelN(100, 5, 'FIVE', 20)
else:
    print('ERROR')

