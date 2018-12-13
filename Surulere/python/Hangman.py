import random

def welcomeScreen():
    name = input("Enter Your Name: ")
    print("Welcome", name,"To a Simple Hangman Game in python Using the 36 States of Nigeria")
    print("#################################################")
    print("Try To Guess The State In A Maximum Of 6 Tries")

    hangman()
    print()



def hangman():

    states = random.choice(["abia","Adamawa","Akwa Ibom","Anambra","Bauchi","Bayelsa","Benue","Borno","Delta","Ebonyi","Edo","Ekiti","Enugu","FCT","Gombe","Imo","Jigawa","Kaduna","Kano","Katsina","Kebbi","Kogi","Kwara","Lagos","Nassarawa","Niger","ogun","Ondo","Osun","Oyo","Plateau","Rivers","Sokoto","Taraba","Yobe","Zamfara",]
)

    validLetters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    turns = 10
    guessed = ''

    while len(states) > 0:
        msg = ''
        missed = 0
        for letter in states:
            if letter in guessed:
                msg = msg + letter
            else:
                msg = msg + "_" + " "
                missed += 1

        if msg == states:
            print(msg)
            print("Correct!!! The State was: ", states)
            break

        print ("Guess The State:", msg)
        guess = input()

        if guess in validLetters:
            guessed = guessed + guess
        else:
            print("Enter a Valid Letter: ")
            guess = input()

        if guess not in states:
            turns = turns - 1
            if turns == 9:
                print("  o")
            if turns == 8:
                print("  o")
                print("  |")
            if turns == 7:
                print("  o")
                print("  |")
                print("  \ ")
            if turns == 6:
                print("  o")
                print("  |")
                print(" / ")
            if turns == 5:
                print("  o")
                print("  |")
                print(" / \ ")
            if turns == 4:
                print("   o")
                print("   |")
                print(" _/ \_ ")
            if turns == 3:
                print("   o")
                print("   |-")
                print(" _/ \_ ")
            if turns == 2:
                print("   o")
                print("  -|-")
                print(" _/ \_ ")
            if turns == 1:
                print("You have failed to guess the state:",states)
                break
welcomeScreen()   
