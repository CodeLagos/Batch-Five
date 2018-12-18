#This python program is an adventure story
#AUTHOR: ADEBANJO DANIEL

trials = 3

print ("Welcome to my adventure game")
name = input("What is your name: ")
print ("Welcome " + name)
age = int(input("\n Press 1 if your age falls between 15 - 20 \n Press 2 if your age falls between 20 - 25 \n Press 3 if your age falls between 25 - 30 \n Press 4 if your age is above 30 \n "))
if age == 1:
    gender = int(input("\n Are a male or female \n Press 1 for male \n Press 2 for female \n "))
    if gender == 1:
            print (" \n You are a hacker \n on your way back from school \n you noticed some people have following you since you left school \n What are you going to do? ")
            option = int(input("\n Press 1 to run away \n Press 2 to ignore them \n Press 3 to approach them \n "))
            if option == 1:
                print ("\n They chased after you. And a black bus pulls up in front of you blocking your path.\n You were bagged, tied up and abducted. You were taken to an old health facility. Then you were taken to a room. \n It looked like a board meeting room and you were the subject.\n You quickly surveyed the round table and none of the five faces were familiar. \n They told you who the name of their organisation and why you were kidnapped")
                request = int(input("\n They call themselves the New World Makers. You were brought in to hack Russia's military satellite. \n And it looks like you were given an option. To help them or not. \n Pick wisely. \n Press 1 to help them. \n Press 2 to reject the offer \n "))
                if request == 1: 
                    print ('\n "Great, welcome to the New World Makers", the one sitting opposite me said. \n They introduced themselves. They all looked like kinda young between 29 - 25. \n "Gabby, take him to changing room. Your first mission starts in few minutes", Solomon Nwabueze told the guard at the door. \n Wait, what? Now! you asked suprised. \n "Yes, is anything the matter", he asked. \n "Of course, there is! I just got here", you said. \n There is no time to waste, I\'m sure you know how strong russia is. \n Any wrong step or move and off our heads go" Solomon said')
                    reply = int(input("\n You are proving stubborn and Solomon thinks you might be a hindrance to their plan. \n are you up to the task? \n Press 1 to reply yes. \n Press 2 to reply no \n "))
                    if reply == 1:
                        print ("Good")
                    else:
                        print("\n I prefer to be one man down, than to have a hindrance on my team. \n Shoot him")
                        print ("*" *50)
                        quit()
            elif option == 2:
                print("")
            else:
                print("")
    elif gender == 2:
            print ("hi") 
    else:
        quit()
else:
    quit()

