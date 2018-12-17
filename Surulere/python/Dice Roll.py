import random

question = input('Would you like to roll the dice [y/n]?\n')

while question != 'n':
    if question == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(die1, die2)
        question = input('Would you like to roll the dice [y/n]?\n')
    else:
      print('Invalid response. Please type "y" or "n".')
      question = input('Would you like to roll the dice [y/n]?\n')
      print('Good-bye!')
