#Display the purpose of the program
print("FOOTBALL QUIZ")
#Display the instructions
print("Select the correct option")
#initialize the score variable
score = 0
#Ask the user a question
question1 = input("Which of these players won the Ballon d'Or in 2016? \n(a)Kylian Mbappe\n (b)Cristiano Ronaldo\n (c)Lionel Messi\n")
if(question1.lower()== "b"):
    print("correct")
    score = score +10
else:
    print("wrong")
question2 = input("In what did Liverpool win the EPL title last? \n(a)2005\n (b)2012\n (c)2006\n")
if(question2.lower()== "a"):
    print("correct")
    score = score +10
else:
    print("wrong")
question3 = input("Who holds the record for most assists in an EPL season? \n(a)Paul Scholes\n (a)Cesc Febragas\n (c)Thierry Henry\n")
if(question3.lower()== "c"):
    print("correct")
    score = score +10
else:
    print("wrong")
question4 = input("Who has had the most appearance for one club in the EPL? \n(a)David Silva\n (b)David Beckham\n (c)Ryan Giggs\n")
if(question4.lower()== "c"):
    print("correct")
    score = score +10
else:
    print("wrong")
question5 = input("Who scored the fastest hat-trick in the Premier League? \n(a)Robbie Fowler\n (b)Cristiano Ronaldo\n (c)Robin Van Persie\n")
if(question5.lower()== "a"):
    print("correct")
    score = score +10
else:
    print("wrong")
print("END OF TEST")
print("Your score is", score)
