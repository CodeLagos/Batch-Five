print("PROJECT BY **OMOROGBE ALEXANDER** BATCH 5 CODE LAGOS")
print("alexrogbe@gmail.com")
print("**********GUESS THE WORDZ*********\n")
name=input("WHAT IS YOUR NAME:").upper()
while True:
    print("\n***STAGE 1***\nFORM A WORD WITH SWA\n")
    ans1=input("WHAT IS THE WORD:").upper()
    word1=["WAS","SAW"]
    score=0
    if(ans1 in word1):
        print("**CORRECT**")
        score= score+10
    else:
        print("**WRONG**")
        score= score+0

    print("\n***STAGE 2***\nFORM A WORD WITH LABDE\n")
    ans2=input("WHAT IS THE WORD:").upper()
    word2=["BLADE"]
    if(ans2 in word2):
        print("**CORRECT**")
        score= score+10
    else:
        print("**WRONG**")
        score= score+0

    print("\n***STAGE 3***\nFORM A WORD WITH CKRO\n")
    ans3=input("WHAT IS THE WORD:").upper()
    word3=["ROCK"]
    if(ans3 in word3):
        print("**CORRECT**")
        score= score+10
    else:
        print("**WRONG**")
        score= score+0


    print("\n***STAGE 4***\nFORM A WORD WITH LOOCHS\n")
    ans4=input("WHAT IS THE WORD:").upper()
    word4=["SCHOOL"]
    if(ans4 in word4):
        print("**CORRECT**")
        score= score+10
    else:
        print("**WRONG**")
        score= score+0


    print("\n***STAGE 5***\nFORM A WORD WITH TERHUN\n")
    ans5=input("WHAT IS THE WORD:").upper()
    word5=["HUNTER"]
    if(ans5 in word5):
        print("**CORRECT**")
        score= score+10
    else:
        print("**WRONG**")
        score= score+0
    
    
    print("\n***STAGE 6***\nFORM A WORD WITH CETISJU\n")
    ans6=input("WHAT IS THE WORD:").upper()
    word6=["JUSTICE"]
    score=0
    if(ans6 in word6):
        print("**CORRECT**")
        score= score+10
    else:
        print("**WRONG**")
        score= score+0

    print("\n***STAGE 7***\nFORM A WORD WITH YADHTRIB\n")
    ans7=input("WHAT IS THE WORD:").upper()
    word7=["BIRTHDAY"]
    if(ans7 in word7):
        print("**CORRECT**")
        score= score+10
    else:
        print("**WRONG**")
        score= score+0

    print("\n***STAGE 8***\nFORM A WORD WITH CTELPATIHE\n")
    ans8=input("WHAT IS THE WORD:").upper()
    word8=["TELEPATHIC"]
    if(ans8 in word8):
        print("**CORRECT**")
        score= score+10
    else:
        print("**WRONG**")
        score= score+0


    print("\n***STAGE 9***\nFORM A WORD WITH ITASOLIRE\n")
    ans9=input("WHAT IS THE WORD:").upper()
    word9=["SOLITAIRE"]
    if(ans9 in word9):
        print("**CORRECT**")
        score= score+10
    else:
        print("**WRONG**")
        score= score+0


    print("\n***STAGE 10***\nFORM A WORD WITH NOLOTECHCIGAL \n")
    ans10=input("WHAT IS THE WORD:").upper()
    word10=["TECHNOLOGICAL"]
    if(ans10 in word10):
        print("**CORRECT**")
        score= score+10
    else:
        print("**WRONG**")
        score= score+0
    print(name, "YOU HAVE COMPLETED THE GAME WITH A SCORE OF:"+   str(score)) 
    if(score>50):
        print("YOUR SCORE IS HIGH ENOUGH ****NICE WORK**** PLAY AGAIN")

    else:
        print("ARE YOU EVEN LOOKING AT THE WORDZ!!! ***DUMB DUMB*** TRY AGAIN")
    

    


    

