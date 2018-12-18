#CODELAGOS PROJECT BY OLOWO OLUKAYODE 
#DICE ROLLING SIMULATOR PROGRAM
print ("CODELAGOS PROJECT BY OLOWO OLUKAYODE")
print ("Welcome to my dice rolling program")
print("Enjoy")

import random
while True:
    print("You rolled",random.randint(1,6))
    repeat = raw_input("Do you want to roll again? \nyes \nno \n ")
    if (repeat.lower() == 'yes'):
        continue
    elif (repeat.lower() == 'no'):
        print("Thank you for playing")
        break
    else:
        print("Invalid Input")
        continue

