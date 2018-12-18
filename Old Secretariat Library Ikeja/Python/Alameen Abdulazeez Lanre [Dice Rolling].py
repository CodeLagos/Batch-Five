#DICE ROLLING SIMULATION
#Import Random
import random
#Print Welocme
print("Project title : Dice Rolling")
print("Name : Alameen Abdulazeez Lanre")
print("Email : Lanre.zico@gmail.com")
print("Centre : Old Secretariat Library Ikeja")
print("Lets roll some dice")
#Prompt user for to roll or not
Dice = input("Do you want to roll? \n [Y/N]\n")

while Dice != "N":
    if Dice.upper() == "Y":
        Die1= random.randint(1,6)
        Die2= random.randint(1,6)
        #Print verdict
        print("you rolled" , Die1, Die2)
        Dice = input("Do you want to roll again? \n [Yes/No]\n")
    else:
        print("Thank you for your time")
        Dice = input("Do you want to roll? \n [Yes/No]\n")
#Print Goodbye
        print("Thank you for playing", "Goodye!")
