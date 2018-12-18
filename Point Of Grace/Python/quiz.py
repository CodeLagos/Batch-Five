#Project Submitted By: Hannah Jesuloluwa
#Display the purpose of the program
print("This is a CowBellpedia quiz")
#Display the instructions
print("Select the letter withe the correct option")
#Initialize the score variable
score = 0
#Ask the user a question
question1 = input("Which of the following groups of raw materials are used in textile industries?\n(a)guinea corn, wheat and kenaf\n(b)cotton, jute and wool\n(c)coffee, cotton and cocoa\n(d)wool, palm kernel and maize\n")
#Wait for the answer
#If the question is correct, display: "Correct" and add 1 to the score
if(question1. lower()=="b"):
    print("Correct")
    score = score + 1
#Else display: "Wrong"
else:
    print("Wrong")
#Ask the user a question
question2 = input("The source of energy required by plants during food production is?\n(a)photosynthesis\n(b)chlorophyll\n(c)sunlight\n(d)microorganism\n")
#Wait for the answer
#If the question is correct, display: "Correct" and add 1 to the score
if(question2. lower()=="c"):
    print("Correct")
    score = score + 1
#Else display: "Wrong"
else:
    print("Wrong")
#Ask the user a question
question3 = input("Which of the following methods can be used to separate blood cells from plasma?\n(a)centrifugation\n(b)filtration\n(c)chromatography\n(d)distillation\n")
#Wait for the answer
#If the question is correct, display: "Correct" and add 1 to the score
if(question3. lower()=="a"):
    print("Correct")
    score = score + 1
#Else display: "Wrong"
else:
    print("Wrong")
#Ask the user a question
question4 = input("Frequency is measured in?\n(a)metre per second\n(b)second\n(c)hertz\n(d)farad\n")
#Wait for the answer
#If the question is correct, display: "Correct" and add 1 to the score
if(question4. lower()=="c"):
    print("Correct")
    score = score + 1
#Else display: "Wrong"
else:
    print("Wrong")
#Ask the user a question
question5 = input("Which of the following cannot be classified as a natural resource?\n(a)iron rod\n(b)wild life\n(c)solar energy\n(d)gold\n")
#Wait for the answer
#If the question is correct, display: "Correct" and add 1 to the score
if(question5. lower()=="a"):
    print("Correct")
    score = score + 1
#Else display: "Wrong"
else:
    print("Wrong")
#Go back to step 3 until all the questions have been answered
#Print the score of the user
print("Your score is", score)
        




