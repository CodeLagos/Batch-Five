#purpose of the program
print("Puzzle Game to boost up the brain")
print("Name:Salisu Abubakar\nEMail: abusalisu2@gmail.com\nPhoneNo.: 09096912938")
while True:
    print("NOTE: YOU CAN ONLY INPUT 6 LETTER WORD ONLY TO PROCEED")
    print("puzzle1= w, o, g, s, r, n")
    score=0
    level1=["wrongs"]
    ans=input("Enter your word: ")
    if(ans in level1):
        print("correct, proceed to  next level")
        score=score+5
    else:
        print("sorry, no score awarded")
        score=score
        print("your score is", score,  "you lose, try again")
        break



    print("puzzle2=a, e, i, l, s, u, t")
    level2=["saltie", "salute","saulie","stelai","sutile"]
    ans=input("Enter your word: ")
    if(ans in level2):
        print("correct, proceed to next level")
        score=score+5
        print("your score is", score)
    else:
        print("sorry, no score awarded")
        score=score
        print("your score is", score)
        break
   
    print("puzzle3= f, h, t, z, e, r, g, a")
    level3=["father","gather","hafter","trefah"]
    ans3=input("Enter your word: ")
    if(ans3 in  level3):
        print("correct, proceed to next level")
        score=score+5
        print("your score is", score)
    else:
        print("sorry, no score awarded")
        score=score
        print("your score is", score)
        break

    print("puzzle4= i, l, p, o, t, h, g, e")
    level4=["eolith","epilog","hogtie","ophite","piglet","piolet","plight","polite"]
    ans4=input("Enter your word: ")
    if(ans4 in  level4):
        print("correct, proceed to next level")
        score=score+5
        print("your score is", score)
    else:
        print("sorry, no score awarded")
        score=score
        print("your score is", score)
        break

    print("puzzle5= e, u, a, m, t, r, a")
    level5=["aurate","mature","amateur","trauma","retama","ramate"]
    ans5=input("Enter your word: ")
    if(ans5 in level5):
         print("correct, proceed to next level")
         score=score+5
         print("your score is", score)
    else:
        print("sorry, no score awarded")
        score=score
        print("your score is", score)
        break

    print("puzzle6= o, n, n, e, u, d, g,")
    level6=["guenon","gunned","undone","dungeon"]
    ans6=input("Enter your word: ")
    if(ans6 in level6):
         print("correct, proceed to next level")
         score=score+5
         print("your score is", score)
    else:
        print("sorry, no score awarded")
        score=score
        print("your score is", score)
        break

    print("puzzle7= l, u, u, a, e, l, t")
    level7=["luteal","ululate"]
    ans7=input("Enter your word: ")
    if(ans7 in level7):
         print("correct, proceed to next level")
         score=score+5
         print("your score is", score)
    else:
        print("sorry, no score awarded")
        score=score
        print("your score is", score)
        break

    print("puzzle8= l, y, i, a, a, t, c, r")
    level8=["alacrity","clarity","lactary","artily","atrial","citral","clarty","lariat","latria","racial","racily","raiyat","rictal"]
    ans8=input("Enter your word: ")
    if(ans8 in level8):
         print("correct, proceed to next level")
         score=score+5
         print("your score is", score)
    else:
        print("sorry, no score awarded")
        score=score
        print("your score is", score)
        break

    print("NOTE: YOU CAN ONLY INPUT 8 LETTER WORD ONLY TO PROCEED")
    print("puzzle9= m, t, a, l, c, r, e, i, a")
    level9=["material","calamite","metrical","tailrace"]
    ans9=input("Enter your word: ")
    if(ans9 in level9):
        print("correct, proceed to next level")
        score=score+5
        print("your score is", score)
    else:
        print("sorry, no score awarded")
        score=score
        print("your score is", score)
        break

    print("FINAL LEVEL: ONLY 12 LETTER WORD + A WHOOPING BONUS SCORE")
    print("puzzle10= s, a, e, y, g, z, p, p, h, o, y, s")
    level10=["zygapophyses"]
    ans10=input("Enter your word: ")
    if(ans10 in level10):
        print("coorect")
        score=score+25
    else:
        print("sorry, no score awarded")
        score=score
    print("your score is", score)
    print("congratulation, you've come to the end of the puzzle, await more of our coming soon puzzles")
