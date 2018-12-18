print ("Ogunfowora sodiq \nsodiqogunfowora@gmail.com \n07033265442")
print ("A guessing Game")
leaveprogram=0
score=0
while leaveprogram != "q":
    import random 
    number1 = random.randint(1,6)
    print ("This is a guessing game where you guess a number ranging from (1,6) and the program will roll a die for you")
    print ("if you guess right you are a winner and if guess wrongly you are a loser")
    guess = int(input("make a guess"))           
    print ("press enter to roll")
    input()
    number2 = random.randint(1,6)
    if guess==number2:
                print("winner")
    else:
                print ("loser")
    if number2 ==1:
        print ("[----------------]")
        print ("[                ]")
        print ("[       O        ]")
        print ("[                ]")
        print ("[----------------]")
        print ()
        print ("Type 'q' to quit")
        leaveprogram=input()
    if number2 ==2:
        print ("[----------------]")
        print ("[                ]")
        print ("[      O  O      ]")
        print ("[                ]")
        print ("[----------------]")
        print ()
        print ("Type 'q' to quit")
        leaveprogram=input()
    if number2 ==3:
        print ("[----------------]")
        print ("[        O       ]")
        print ("[       O O      ]")
        print ("[                ]")
        print ("[----------------]")
        print ()
        print ("Type 'q' to quit")
        leaveprogram=input()
    if number2 ==4:
        print ("[----------------]")
        print ("[       O O      ]")
        print ("[       O O      ]")
        print ("[                ]")
        print ("[----------------]")
        print ()
        print ("Type 'q' to quit")
        leaveprogram=input()
    if number2 ==5:
        print ("[----------------]")
        print ("[       O O      ]")
        print ("[        O       ]")
        print ("[       O O      ]")
        print ("[----------------]")
        print ()
        print ("Type 'q' to quit")
        leaveprogram=input()
    if number2 ==6:
        print ("[----------------]")
        print ("[       O O      ]")
        print ("[       O O      ]")
        print ("[       O O      ]")
        print ("[----------------]")
        print ()
        print ("Type 'q' to quit")
        leaveprogram=input()

    
