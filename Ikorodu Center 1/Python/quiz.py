print("Welcome to who wants to be a scohlar")
print("Please answer all questions correctly")
print("To use a life line press L \nNote: you have just three(3) life lines\n")
score = 5
life=3
Q1=input("The S.I unit of heat is \nA. joule \nB. kelvin \nC. watt \nD. ampere\n")
if (Q1.lower()=="a"):
    print("correct\n")
elif (Q1.lower()=="l"):
    if(life>0):
     l=input("pick a lifeline\n1. phone a friend\n2. 50-50\n3. Ask the audience\n")
     if(l=="2"):
         l1=input("The S.I unit of heat is \nA. joule \nC. watt \n")
         if (l1.lower()=="a"):
            print("correct\n")
            life =life-1
         else:
            print("wrong\n")
            score = score - 1
            life =life-1
     elif (l=="1"):
         l1=input("Calling...........\nHello\n  The answer is a\n------please input your answer\n")
         if (l1.lower()=="a"):
             print("correct\n")
             life =life-1
         else:
             print("wrong\n")
             score = score - 1
             life =life-1
             
     else:
       l1=input("40% of the audience = a\n25% of the audience = b\n15% of the audience = c\n20% of the audience = d\n")
       if (l1.lower()=="a"):
           print("correct\n")
           life =life-1
       else:
          print("wrong\n")
          score = score - 1
          life =life-1
    else:
        print("you are out of Life line")
        Q1=input("Please choose the correct answer to the question above\n")
        if (Q1.lower()=="a"):
            print("correct\n")
        else:
            print("wrong")
            score = score - 1
else:
    print("wrong\n")
    score = score - 1
    
Q2=input("The thermopile is a device for detecting  \nA. radioactive radiations \nB. radiant energy \nC. X-rays \nD. the presence of electrons\n")
if (Q2.lower()=="b"):
    print("correct\n")
elif(Q2.lower()=="l"):
    if(life>0):
     l=input("pick a lifeline\n1. phone a friend\n2. 50-50\n3. Ask the audience\n")
     if(l=="2"):
         l1=input("The thermopile is a device for detecting  \nB. radiant energy \nC. X-rays \n")
         if (l1.lower()=="b"):
            print("correct\n")
            life =life-1
         else:
            print("wrong\n")
            score = score - 1
            life =life-1
     elif (l=="1"):
         l1=input("Calling...........\nHello\nI Think answer is c\n------please input your answer\n")
         if (l1.lower()=="b"):
             print("correct\n")
             life =life-1
         else:
             print("wrong\n")
             score = score - 1
             life =life-1
             
     else:
       l1=input("25% of the audience = a\n40% of the audience = b\n15% of the audience = c\n20% of the audience = d\n")
       if (l1.lower()=="b"):
           print("correct\n")
           life =life-1
       else:
          print("wrong\n")
          score = score - 1
          life =life-1
    else:
        print("you are out of Life line")
        Q1=input("Please choose the correct answer to the question above\n")
        if (Q1.lower()=="b"):
            print("correct\n")
        else:
            print("wrong")
            score = score - 1
else:
    print("wrong\n")
    score = score - 1

    
Q3=input("In the formation of sea breeze, wind blows from \nA. sky to land \nB. sea to sky \nC. land to sea \nD. sea to land\n")
if (Q3.lower()=="d"):
    print("correct\n")
elif(Q3.lower()=="l"):
    if(life>0):
     l=input("pick a lifeline\n1. phone a friend\n2. 50-50\n3. Ask the audience\n")
     if(l=="2"):
         l1=input("In the formation of sea breeze, wind blows from \nC. land to sea \nD. sea to land\n")
         if (l1.lower()=="d"):
            print("correct\n")
            life =life-1
         else:
            print("wrong\n")
            score = score - 1
            life =life-1
     elif (l=="1"):
         l1=input("Calling...........\nHello\nI cant hear you clearly......\nplease repeat that........\n....Hangs up\n------please input your answer\n")
         if (l1.lower()=="d"):
             print("correct\n")
             life =life-1
         else:
             print("wrong\n")
             score = score - 1
             life =life-1
             
     else:
       l1=input("30% of the audience = a\n15% of the audience = b\n15% of the audience = c\n30% of the audience = d\n")
       if (l1.lower()=="d"):
           print("correct\n")
           life =life-1
       else:
          print("wrong\n")
          score = score - 1
          life =life-1
    else:
        print("you are out of Life line")
        Q1=input("Please choose the correct answer to the question above\n")
        if (Q1.lower()=="d"):
            print("correct\n")
        else:
            print("wrong")
            score = score - 1
else:
    print("wrong\n")
    score = score - 1

    
Q4=input("The total area under force-velocity graph represents\nA. energy \nB. momentum \nC. power \nD. pressure\n")
if (Q4.lower()=="a"):
    print("correct\n")
elif (Q4.lower()=="l"):
    if(life>0):
     l=input("pick a lifeline\n1. phone a friend\n2. 50-50\n3. Ask the audience\n")
     if(l=="2"):
         l1=input("The total area under force-velocity graph represents\nA. energy \nD. pressure\n")
         if (l1.lower()=="a"):
            print("correct\n")
            life =life-1
         else:
            print("wrong\n")
            score = score - 1
            life =life-1
     elif (l=="1"):
         l1=input("Calling...........\nHello\nThe answer is drfinately A\n------please input your answer\n")
         if (l1.lower()=="a"):
             print("correct\n")
             life =life-1
         else:
             print("wrong\n")
             score = score - 1
             life =life-1
             
     else:
       l1=input("27% of the audience = a\n25% of the audience = b\n25% of the audience = c\n23% of the audience = d\n")
       if (l1.lower()=="a"):
           print("correct\n")
           life =life-1
       else:
          print("wrong\n")
          score = score - 1
          life =life-1
    else:
        print("you are out of Life line")
        Q1=input("Please choose the correct answer to the question above\n")
        if (Q1.lower()=="a"):
            print("correct\n")
        else:
            print("wrong")
            score = score - 1
else:
    print("wrong\n")
    score = score - 1


    
Q5=input("The rising of a liquid in an open ended glass tube of narrow bore is \nA. Osmosis \nB. Adhension \nC. Capillarity \nD. Surface Tension\n")
if (Q5.lower()=="c"):
    print("correct\n")
elif (Q5.lower()=="l"):
    if(life>0):
     l=input("pick a lifeline\n1. phone a friend\n2. 50-50\n3. Ask the audience\n")
     if(l=="2"):
         l1=input("The rising of a liquid in an open ended glass tube of narrow bore is \nA. Osmosis \nC. Capillarity \n")
         if (l1.lower()=="c"):
            print("correct\n")
            life =life-1
         else:
            print("wrong\n")
            score = score - 1
            life =life-1
     elif (l=="1"):
         l1=input("Calling...........\nHello\nSorry, i dont know the answer\n------please input your answer\n")
         if (l1.lower()=="c"):
             print("correct\n")
             life =life-1
         else:
             print("wrong\n")
             score = score - 1
             life =life-1
             
     else:
       l1=input("25% of the audience = a\n25% of the audience = b\n25% of the audience = c\n25% of the audience = d\n")
       if (l1.lower()=="c"):
           print("correct\n")
           life =life-1
       else:
          print("wrong\n")
          score = score - 1
          life =life-1
    else:
        print("you are out of Life line")
        Q1=input("Please choose the correct answer to the question above\n")
        if (Q1.lower()=="c"):
            print("correct\n")
        else:
            print("wrong")
            score = score - 1
else:
    print("wrong\n")
    score = score-1
    

print("Your total score is ",score,"\nyou have",life,"life line left","\nThank you for your time")

