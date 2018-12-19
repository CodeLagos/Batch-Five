print("IDUH ISAIAH")
print("Ikeja center old secretariate ")
print("isaiahphp@gmail.com")



import random
game_start = input("Would you like to roll the dice?")

def dice_roll():
    while true:
        print("Your number is: " + str(random.randint(1,1)))
        play_again = input("Would you like to play again?")
        while play_again  != 'yes':
           if play_again == 'no':
              return print("game over")
           else:
              print("Input not recognized")
              play_again =("like to place another value")

def main():
    game_start = input("like to place another value")

if game_start == 'yes':
    dice_roll()
else:
    print("too bad")

if _name_=='_main_':
  main()
  
