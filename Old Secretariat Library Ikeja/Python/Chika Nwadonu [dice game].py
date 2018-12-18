from random import randint

print("A simple dice game created by Chika Nwadonu")
print("ikeja library")

roll_again=""
while(roll_again.lower() !="e"):
    roll_again=input("Ready to roll? ENTER=Roll. E=Exit. Enter a number to roll ")
    if(roll_again.lower() !="e"):
        num_rolled=randint(1,6)
        print("You rolled a", num_rolled)
    else:
        pass

    print("Thanks for playing")
