print("hello world")

import time
import datetime
tester = str(input("what should i call you:"))
print(tester,"this is simple AI designed by Emeka in python")

print("current date and time is:", datetime.datetime.now())

task = str(input("what do  you want me to do for you today, for calculation type \"calculation\" for playing rock paper scissors type \"rps\" "))

if task == "rps":
    import random
    player_name = str(input("hey, whats your name:"))
    if player_name == "emeka":
        print("hello! lets check this programme function")
    else:
        print(player_name, "welcome! lets play this game:)")
    game_time = int(input("how many rounds do you want to play:"))
    you_won = 0
    computer_won = 0
    while game_time!=0:
        computer_choice = random.randint(1,3)
        player_choice = str(input("enter your choice(r/p/s):"))
        if computer_choice == 1:
            computer_choice = "r"
        elif computer_choice == 2:
            computer_choice = "p"
        elif computer_choice == 3:
            computer_choice = "s"
        print("computer choose:", computer_choice)

        if player_choice == "r" and computer_choice == "s":
            print("You win!")
        elif player_choice == "p" and computer_choice == "r":
            print("You win!")
        elif player_choice == "s" and computer_choice == "p":
            print("You win!")
            you_won = int(you_won)
            you_won = you_won + 1
        elif computer_choice == player_choice:
            print("Its a tie ;)")
        else:
            print("you loose!")
            computer_won=int(computer_won)
            computer_won=computer_won+1

        game_time=game_time-1
    #print("You won",you_won "computer won",computer_won)
    if you_won > computer_won:
        print(player_name, "Yaay!! you won")
    else:
        print(player_name, "HAHA :), you lost to a BOT!!")
    getexit = input("press enter to exit")

else:
    def add(a,b): return a+b

    def subtract(a,b): return a-b

    def multiply(a,b): return a*b

    def division(a,b): return a/b

    def power(a,b): return a**b

#if _name_ == "_main_":
    try:
        number1 = float(input("enter the first number: "))
        number2 = float(input("enter the last number: "))
    except:
        print("that is not a number!")

operator = input(("enter an operator (+,-,/,*,**): "))
if operator == "+":
    func = add
elif operator == "-":
    func = subtract
elif operator == "*":
    func = multiply
elif func == "/":
    operator = division
elif operator == "**":
    func = power

else:
    print("invalid operator!")
#print out results

print(func(number1,number2))

getexit = input("press enter to exit ")
