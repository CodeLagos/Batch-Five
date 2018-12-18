#Dice Rolling Simulator


print("Hello and Welcome")

import random

print("Project Title: Dice Rolling")
print("Name: Oladebo Emmanuel Oluwaseun")
print ("Email: oluwaseun847@gmail.com")
print("Centre: Old secretariat Library Ikeja")

#Prompt user to enter a minimum and maximum value
min = 1
max = 6

#Prompt user to generate a random number and save it in a variable
Selected = random.randint(1,6)
print("Selected")

#Prompt user to choose a random number to roll
rolled_number = random.randint(1,6)
print("\n You have rolled: ", rolled_number)

while True:
    rolled_number = random.randint(1,6)
    
#Print out result
    print("\n The dice rolled and you got:", rolled_number)
    input("\n Press any key to roll again:")
    
