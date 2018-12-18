print("NAME: AYENI, ABIMBOLA ADEBOLA")
print("PHONE NUMBER: 09036713237")
print("THIS PROGRAM IS THE GAME HANGMAN; THE PLAYER FORMS ONE WORD WITH THE NUMBER OF DASHES PRESENTED, USING THE HINTS PROVIDED.")

print(" THIS IS A HANGMAN GAME ")
print(" Rules of the game include: \n 1. The number of available dashes tells you the number of letter the word to be formed is. \n 2. You only have 3 trails and a total of 6 questions to answer. \n 3. Once you guess a letter right the system will keep it as a record.")
name=input("Enter your name: ")
score=0
while True:
    print("This is stage one")
    word1=print(" _","_","_","_","_")
    print("Hint: It makes a squeaky sound")
    guess=input("Enter your guess: ").lower()
    ans1=["clean"]
    if(guess in ans1):
        print("This is correct. Congratulations!!!, you advance to stage two.")
        score=score+1
    else:
        print("This is wrong")
        print(name+", you have two more trials")
        score=score+0
        print("Another hint: Its a verb")
        guesa=input(name+", give it another trail: ").lower()
        if(guesa in ans1):
            print("This is correct. Congratulations!!! You advanced to stage two.")
            score=score+1
        else:
            print("Again, this is wrong")
            print(name+", this is your final trial")
            score=score+0
            guesb=input(name+", give it the last trail: ").lower()
            if(guesb in ans1):
                print("This is correct. Congratulations!!! You advanced to stage two.")
                score=score+1
            else:
                print(name+", sorry but, you died in this stage. Better luck next time")
                score=score+0            
    print(" This is stage two")
    word2=print(" _","_","_","_","_","_")
    print("Hint: Laptop name")
    guess2=input("Enter your guess: ").lower()
    ans2=["compaq"]
    if(guess2 in ans2):
        print("This is correct. Congratulations, you advance to stage three.")
        score=score+1
    else:
        print("This is wrong")
        print(name+", you have two more trials")
        score=score+0
        print("Another hint: it has two vowels")
        guesaa=input(name+", enter your second trail: ").lower()
        if(guesaa in ans2):
            print("This is correct. Congratulations!!! You advance to stage three")
            score=score+1
        else:
            print("Again, this is wrong")
            print(name+", this is your final trial")
            score=score+0
            guesbb=input(name+", enter the last trail: ").lower()
            if(guesbb in ans2):
                print("This is correct. Congratulations!!! You advanced to stage three ")
                score=score+1
            else:
                print(name+", sorry but, you died in this stage. Better luck next time")
                score=score+0  
    print(" This is stage three")
    word3=print(" _","_","_","_","_","_","_","_","_","_","_")
    print("Hint: Another word for luck")
    guess3=input("Enter your guess: ").lower()
    ans3=["serendipity"]
    if(guess3 in ans3):
        print("This is correct. Congratulations!!!, you advance to stage four.")
        score=score+1
    else:
        print("This is wrong")
        print(name+", you have two more trials")
        score=score+0
        print("Another hint: It has two vowels reoccuring twice.")
        guesaaa=input(name+", enter your second trail: ").lower()
        if(guesaaa in ans3):
            print("This is correct. Congratulations!!! You advanced to stage four")
            score=score+1
        else:
            print("Again, this is wrong")
            print(name+", this is your final trial")
            score=score+0
            guesbbb=input(name+", enter your last trail: ").lower()
            if(guesbbb in ans3):
                print("This is correct. Congratulations!!! You advanced to stage four")
                score=score+1
            else:
                print(name+", sorry but, you died in this stage. Better luck next time")
                score=score+0  
    print(" This is stage four")
    word4=print(" _","_","_","_","_","_",)
    print("Hint: Another word for shrewd")
    guess4=input("Enter your guess: ").lower()
    ans4=["astute"]
    if(guess4 in ans4):
        print("This is correct. Congratulations!!!. You advance to stage five.")
        score=score+1
    else:
        print("This is wrong")
        print(name+", you have two more trials")
        score=score+0
        print("Another hint: It has a consonant occuring twice")
        guesaaaa=input(name+", enter your second trail: ").lower()
        if(guesaaaa in ans4):
            print("This is correct. Congratulations!!! You advanced to stage five")
            score=score+1
        else:
            print("Again, this is wrong")
            print(name+", this is your final trial")
            score=score+0
            guesbbbb=input(name+", enter the last trail: ").lower()
            if(guesbbbb in ans4):
                print("This is correct. Congratulations!!! You advanced to stage five")
                score=score+1
            else:
                print(name+", sorry but, you died in this stage. Better luck next time")
                score=score+0                
    print(" This is stage five")
    word5=print(" _","_","_","_","_","_","_","_")
    print("Hint: Another word for bitter")
    guess5=input("Enter your guess: ").lower()
    ans5=["acrimony"]
    if(guess5 in ans5):
        print("This is correct. Congratulations!!! You advanced to stage six.")
        score=score+1
    else:
        print("This is wrong")
        print(name+", you have two more trials")
        score=score+0
        print("Another Hint: It has a name similar to a Tyler Perry movie")
        guesaaaaa=input(name+", give it another trail: ").lower()
        if(guesaaaaa in ans5):
            print("This is correct. Congratulations!!! You advanced to stage six.")
            score=score+1
        else:
            print("Again, this is wrong")
            print(name+", this is your final trial")
            score=score+0
            guesbbbbb=input(name+", give it the last trail: ").lower()
            if(guesbbbbb in ans5):
                print("This is correct. Congratulations!!! You advanced to stage six.")
                score=score+1
            else:
                print(name+", sorry but, you died in this stage. Better luck next time")
                score=score+0
    print(" This is stage six. This is also the final stage.")
    word6=print(" _","_","_","_","_","_","_","_","_")
    print("Hint: Another word for comparison")
    guess6=input("Enter your guess: ").lower()
    ans6=["juxtapose"]
    if(guess6 in ans6):
        print("This is correct. Congratulations!!! You have done excellently well in completing this game.")
        score=score+1
    else:
        print("This is wrong")
        print(name+", you have two more trials")
        score=score+0
        print("Another special Hint: it includes the letter X")
        guesaaaaaa=input(name+", give it another trail: ").lower()
        if(guesaaaaaa in ans6):
            print("This is correct. Congratulations!!! You have done excellently well in completing this game.")
            score=score+1
        else:
            print("Again, this is wrong")
            print(name+", this is your final trial")
            score=score+0
            guesbbbbbb=input(name+", give it the last trail: ").lower()
            if(guesbbbbbb in ans6):
                print("This is correct. Congratulations!!! You have done excellently well in completing this game.")
                score=score+1
            else:
                print(name+", sorry but, you died in this stage. Better luck next time")
                score=score+0  
    print("This is the end of the game. \n Thank you for choosing to play this game.")
    score=int(score)
    p=score/6
    p2=p*100
    print(name+", your score at the end of the game is: "+ str(score) + ".")
    print(name+", your score in percentage is "+ str(p2)+ "percent." )    
    again=input(name+", would you like to try the game again? \n A. Yes \n B. No: \n ").upper()
    if(again=="A"):
        print(name+", thank you for choosing to replay. Here you go: ")
    else:
        break
