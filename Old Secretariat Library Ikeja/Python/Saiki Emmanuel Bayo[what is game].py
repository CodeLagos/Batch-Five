#A simple what is game
import random

trial_attempted=0
print("Name:Saiki Emmanuel Bayo\nEmail:saikijoy6@gmail.com\nCenter:Lagos state library,Old Seceteriat,Ikeja,Lagos State")

your_name=input("Welcome Fella.My name is 'Jarvis' and  your name is?:")

number=random.randint(1,20)
print("Okay",your_name,"the rules of the game is simple.I think of a number and you have 5 trials to get it right.NOW iam thinking of a number between the range of 1 to 20,what is the number")

while trial_attempted<5:
    trial=input()
    trial=int(trial)

    trial_attempted=trial_attempted+1

    if trial<number:
        print("your guess is too low")

    if trial>number:
        print("your guess too high")

    if trial==number:
        break

if trial==number:
     trial_attempted = str(trial_attempted)
     print("excellent!!",your_name,"your trials were",trial_attempted)


 

