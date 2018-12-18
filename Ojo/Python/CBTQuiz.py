#Display the purpose of the program
print("WELCOME TO MEXMEDIA COMPUTER BASED TEST")

#Display the purpose of the program
print("\n IF YOU PASS THIS TEST, YOU WILL BE CONTACTED FOR WHEN TO COME BACK FOR YOUR INTERVIEW")

#Display the instructions
print("\n INSTRUCTIONS: ATTEMPT ALL QUESTIONS. SUBMIT WHEN DONE")

#Initialize the score variable
score = 0
done = False


while done is not True:

    #Ask user subject to begin with
    beginwith = input("SELECT COURSE: \n (a)English Language \n (b)Mathematics \n (c)Logic \n (d)General Knowlwdge \n (e)Quit \n")

    #Wait for selection

    #If selection is English Language, display "Questions for Engish Language test"
    if (beginwith.lower()== "a"):
        print ("\n QUESTIONS FOR ENGLISH LANGUAGE TEST")
        print ("\n INSTRUCTION: READ THE PASSAGE TO ANSWER THE QUESTIONS BELLOW")
        print ("\n A well-dressed young man entered a big textile shop one evening. He was able to draw the attention of the salesmen who thought him rich and likely to make heavy purchases. He was shown the superior varieties of suit lengths and sarees. But after casually examining them, he kept moving to the next section, where readymade goods were being sold and further on to the hosiery section. By them, the salesmen had begun to doubt his intentions and drew the attention of the manager. The manager asked him what exactly he wanted and he replied that he wanted courteous treatment. He explained that he had come to the same shop in casual dress that morning and drawn little attention. His pride was hurt and he wanted to assert himself. He had come in good dress only to get decent treatment, not for getting any textiles. He left without making any purchase.")

        #Ask the user a question
        question1 = input("\n 1. The young man was well-dressed because \n(a)it was his habit to dress well \n(b)it was his wedding day \n(c)he wanted to meet the manager of the shop \n(d)he wanted to impress the salesmen\n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question1.lower()== "d"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question2 = input("\n 2. The salesmen in the shop are described as people who pay attention to \n(a)only young men and women \n(b)pretty women \n(c)wanted better clothes \n(d)was restless\n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question2.lower()== "c"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question3 = input("\n 3. The young man moved away to the hosiery section because he \n(a)was not interested in purchasing anything now \n(b)did not like the readymade clothes \n(c)wanted better clothes \n(d)was restless\n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question3.lower()== "a"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question4 = input("\n 4. The manager asked the young man what he wanted because \n(a)he would give him exactly what he was looking for \n(b)the salesman had drawn his attention to the indifferent attitude of the young man \n(c)he thought they could do more business with him that way \n(d)he thought the visitor was dissatisfied\n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question4.lower()== "b"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question5 = input("\n 5. The young man left without making purchases because he \n(a)did not have money \n(b)could not find any item of his choice \n(c)had come only to make a point about the indifferent attitude of the salesmen towards casually dressed customers \n(d)decided to come to make the purchases later on\n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question5.lower()== "c"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Print instructions for the next set of questions
        print("\n Choose the best word to fit the gap.")

        #Ask the user a question
        question6 = input("\n 6. Your body ________________ usually gives other people information about how you really feel. \n(A) appearance \n(B) impression \n(C) language \n(D) relationship\n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question6.lower()== "c"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question7 = input("\n 7. If someone looks me straight in the eye without __________ I tend to think they are honest. \n(A) yawning \n(B) sighing \n(C) blinking \n(D) sniffing\n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question7.lower()== "c"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question8 = input("\n 8. You must ___________ your application by the end of the week. \n(A) submit \n(B) subject \n(C) give \n(D) subcontract\n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question8.lower()== "a"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question9 = input("\n 9. There has been a ______________ agreement to supply Texmills with our products and services. \n(A) long-winded \n(B) long-lasting \n(C) long-lived \n(D) long-standing\n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question9.lower()== "d"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question10 = input("\n 10. Managers should staff to maintain the no-smoking policy throughout the building. \n(A) suggest \n(B) encourage \n(C) support \n(D) co-operate\n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question10.lower()== "b"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")
    
    if(beginwith.lower()== "b"):
        print ("\n MATHEMATICS")
        print ("\n INSTRUCTION: Attempt all questions")

        #Ask the user a question
        question11 = input("\n 11. Which is the smallest? \n(A) -1 \n(B) -1/2 \n(C) 0 \n(D) 3\n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question11.lower()== "b"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question12 = input("\n 12. Combine terms: 12a+26b-16a \n(A) 4a+22b \n(B) -28a+30b \n(C) -4a+22b \n(D) -4a+22b\n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question12.lower()== "c"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question13 = input("\n 13. Simplfy: (4-5)-(13-18+2) \n(A) -1 \n(B) -2 \n(C) 1 \n(D) 2\n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question13.lower()== "d"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")
        
        #Ask the user a question
        question14 = input("\n 14. What is |-26|? \n(A) -26 \n(B) 26 \n(C) 0 \n(D) 1\n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question14.lower()== "b"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question15 = input("\n 15. Factor: 5x2-15x-20. \n(A) 5(x-4)(x+1) \n(B) -2(x-4)(x+5) \n(C) -5(x+4)(x-1) \n(D) 5(x-4)(x+1)\n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question15.lower()== "a"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question16 = input("\n 16. Factor: 3y(x-3)-2(x-3). \n(A) (x-3)-(x-3)  \n(B) (x-3)2 \n(C) (x-3)(3y-2) \n(D) 3y(x-3)\n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question16.lower()== "c"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question17 = input("\n 17. Solve for x: 2x-y=(3/4)x+6. \n(A) (y+6)/5 \n(B) 4(y+6)/5 \n(C) (y+6) \n(D) 4(y-6)/5 \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question17.lower()== "b"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question18 = input("\n 18. Find the value of 3+2(8-3). \n(A) 25 \n(B) 15 \n(C) 17(D) 24 \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question18.lower()== "d"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question19 = input("\n 19. Which is greater than 4? \n(A) 5 \n(B) -5 \n(C) -1/2(D) -25 \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question19.lower()== "a"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question20 = input("\n 20. What is the radius of a circle that has a circumference of 3.14 meters? \n(A) 5 \n(B) 1.5 \n(C) 0.5 \n(D) 5.2 \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question20.lower()== "a"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

    if(beginwith.lower()== "c"):
        print ("\n LOGIC")
        print ("\n INSTRUCTION: Attempt all questions")

        #Ask the user a question
        question21 = input("\n 21. Look at this series: 2, 4, 6, 8, 10, . . . What number should come next? \n(A) 11 \n(B) 12 \n(C) 13 \n(D) 14 \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question21.lower()== "b"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question22 = input("\n 22. Look at this series: 58, 52, 46, 40, 34, . . . What number should come next? \n(A) 26 \n(B) 28 \n(C) 30 \n(D) 32 \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question22.lower()== "b"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question23 = input("\n 23. Look at this series: 40, 40, 47, 47, 54, . . . What number should come next? \n(A) 40 \n(B) 44 \n(C) 54 \n(D) 61 \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question23.lower()== "c"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question24 = input("\n 24. Look at this series: 544, 509, 474, 439, . . . What number should come next? \n(A) 404 \n(B) 414 \n(C) 420 \n(D) 445 \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question24.lower()== "a"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question25 = input("\n 25. Look at this series: 201, 202, 204, 207, . . . What number should come next? \n(A) 205 \n(B) 208 \n(C) 210 \n(D) 211 \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question25.lower()== "d"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question26 = input("\n 26. Look at this series: 8, 43, 11, 41, __, 39, 17, . . . What number should fill in the blank? \n(A) 8 \n(B) 14 \n(C) 43 \n(D) 44 \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question26.lower()== "b"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question27 = input("\n 27. Look at this series: 15, __, 27, 27, 39, 39, . . . What number should fill the blank? \n(A) 51 \n(B) 39 \n(C) 23 \n(D) 15 \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question27.lower()== "d"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question28 = input("\n 28. Look at this series: 83, 73, 93, 63, __, 93, 43, . . . What number should fill the blank? \n(A) 33 \n(B) 53 \n(C) 73 \n(D) 93 \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question28.lower()== "b"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question29 = input("\n 29. QPO NML KJI _____ EDC \n(A) HGF \n(B) CAB \n(C) JKL \n(D) GHI \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question29.lower()== "a"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question30 = input("\n 30. JAK KBL LCM MDN _____ \n(A) OEP \n(B) NEO \n(C) MEN \n(D) PFQ \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question30.lower()== "b"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

    if(beginwith.lower()== "d"):
        print ("\n GENERAL KNOWLEDGE")
        print ("\n INSTRUCTION: Attempt all questions")

        #Ask the user a question
        question31 = input("\n 31. Epsom (England) is the place associated with \n(A) Horse racing \n(B) Polo \n(C) Shooting \n(D) Snooker \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question31.lower()== "a"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question32 = input("\n 32. Grand Central Terminal, Park Avenue, New York is the world's \n(A) largest railway station \n(B) highest railway station \n(C) longest railway station \n(D) None of the above \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question32.lower()== "a"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question33 = input("\n 33. Entomology is the science that studies \n(A) Behavior of human beings \n(B) Insects \n(C) The origin and history of technical and scientific terms \n(D) The formation of rocks \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question33.lower()== "b"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question34 = input("\n 34. Eritrea, which became the 182nd member of the UN in 1993, is in the continent of \n(A) Asia \n(B) Africa \n(C) Europe \n(D) Australia \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question34.lower()== "b"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question35 = input("\n 35. Garampani sanctuary is located at \n(A) Junagarh, Gujarat \n(B) Diphu, Assam \n(C) Kohima, Nagaland \n(D) Gangtok, Sikkim \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question35.lower()== "b"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question36 = input("\n 36. For which of the following disciplines is Nobel Prize awarded? \n(A) Physics and Chemistry \n(B) Physiology or Medicine \n(C) Literature, Peace and Economics \n(D) All of the above \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question36.lower()== "d"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question37 = input("\n 37. Hitler party which came into power in 1933 is known as \n(A) Labour Party \n(B) Nazi Party \n(C) Ku-Klux-Klan \n(D) Democratic Party \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question37.lower()== "b"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question38 = input("\n 38. FFC stands for \n(A) Foreign Finance Corporation \n(B) Federation of Football Council \n(C) Film Finance Corporation \n(D) None of the above \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question38.lower()== "c"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question39 = input("\n 39. Fastest shorthand writer was \n(A) Dr. G. D. Bist \n(B) J.R.D. Tata \n(C) J.M. Tagore \n(D) Khudada Khan \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question39.lower()== "c"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

        #Ask the user a question
        question40 = input("\n 40. Galileo was an Italian astronomer who \n(A) developed the telescope \n(B) discovered four satellites of Jupiter \n(C) discovered that the movement of pendulum produces a regular time measurement \n(D) All of the above \n")

        #Wait for the answer

        #If the question is correct, display: “Correct” and add 1 to the score
        if (question40.lower()== "c"):
            print("Correct\n")
            score = score + 1
        else:
            print("Wrong\n")

    if (beginwith.lower() == "e"):
        done = True

#Print the score of the user
print("Your score is", score)

if (score <= 24):
    print( " Sorry, you can not proceed to the next step. \n You suck! \n Olodo!")

if (score >= 25):
    print ( " Congratulations! \n You made it to the next step. \n Kindly exit the hall and wait to be contacted.")


