print('Authored by Balogun Abdulwasiu Adewale \t 07085738024 \n abdulwasiubalogun@gmail.com \t python batch 5 \n GAME - battleground')
#the user is looking to shoot down a target thats hiding behind the shields 
print()
print()

from random import randint 

board = []

for a in range(7):
  board.append(['O'] * 7)

def battle_ground(board):
  for build in board:
    print(' '.join(build))

print(battle_ground(board))

battle_row = randint(1, len(board) - 1)
battle_col = randint(1, len(board) - 1)

#print(battle_row)
#print(battle_col)

guesses = 0

while guesses < 4:

  print('You can only guess among shield number 0 - 6')
  guess_row = int(input('Guess row: ')) 
  guess_col = int(input('Guess column: ')) 

  #checks if guesses is outside the 7x7 grid
  if guess_row not in range(7) or guess_col not in range(7):
    print('Ooops, you are shooting way off target')

  #checks if guesses r correct
  elif guess_row == battle_row and guess_col == battle_col:
    print('Congratulations, you have conquered this battle')
    break

  #checks if you already guessed on that location
  elif board[guess_row][guess_col] == 'X':
    print('You guessed that one already')

  else:
    #tells u if u missed, n mark the spot as X
    print('Aww, u missed your target, try again')
    board[guess_row][guess_col] = 'X'
    print(battle_ground(board))
    guesses = guesses + 1

    if guesses == 4:  
      print('Game Over, you have run out of guesses, SORRY')
      print('The right row: ' + str(battle_row) + ' and column: ' + str(battle_col))

      break
