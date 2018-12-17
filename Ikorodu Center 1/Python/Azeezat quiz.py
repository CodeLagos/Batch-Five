#NAME: AREMU AZEEZAT
#PHONE_NUM: 08161528402, 08085002192
#EMAIL: olayinka.aremu@yahoo.com

total_score = {}
can_name = {}
name = input('ENTER YOUR NAME: ')
can_name.update({'NAME':name})
#display the purpose of the program
print(" this is trivia quiz")
#display the instruction
print("select the letter with the correct answer")
#initialize the score variable
score= 0
#ask user questions
print('QUESTION ONE')
question1 = input (" Who is the governor of taraba state? \n(a) ambode \n(b) sanwolu \n(c) isiaku dairus\n")
if (question1.lower ()=="c"):
    score= score + 1
else:
 score = score
print('QUESTION TWO')
question2 = input ("----- is the cpital of Lagos? \n(a)agege \n(b)oshodi \n(c) ikeja \n")
if (question2.lower ()== "c"):
    score = score + 1
else:
    score = score
print('QUESTION THREE')
question3= input ("The color of nigeria flag is ______ and _______\n (a)blue and white \n(b)white and green \n(c)red and yelow \n")
if (question3.lower ()=="b"):
                   score = score + 1
else:
    score = score
print('QUESTION FOUR')
question4= input("Nigeria is made up of ____ states \n(a)40 \n(b)32 \n(c)36 \n ")
if (question4.lower ()=="c"):
    score = score + 1
else:
    score = score
print('QUESTION FIVE')
question5=input("Christmas is celebratedon which date of december? \n(a)31 \n(b)25)\n(c)26\n")
if(question5.lower()=="b"):
    score = score + 1
else:
    score = score
print('QUESTION SIX')
question6= input (" Code lagos batch 5.0 ends its lecture on _____ 2018 \n(a)12 dec \n(b)15dec \n(c)21dec \n")
if (question6.lower ()=="a"):
    score = score + 1
else:
    score = score
print('QUESTION SEVEN')
question7= input ("Lagos has ______ number of local government \n(a)60 \n(b)20 \n(c) 36 \n")
if (question7.lower () == "b"):
    score = score + 1
else:
    score = score
print('QUESTION EIGHT')
question8= input ("The Nigeria president is from ______ part of the country \n(a)katsina \n(b)kano \n(c)kaduna \n")
if(question8.lower ()=="a"):
    score = score + 1
else:
    score= score
print('QUESTION NINE')
question9=input("The total number of nigeria currency note is \n(a)10 \n(b)5 \n(c)7 \n")
if (question9.lower ()=="c"):
    score =score + 1
else:
    score = score
print('QUESTION TEN')
question10=input("The scheme code lagos is  an initiation of which of the following body \n(a)lagos state ministry of education \n(b) federal ministry of housing \n(c)state ministry of teaching\n")
if(question10.lower ()=="a"):
    score = score + 1
else:
    score = score
    print ("your score is: ", score )

total_score.update({'SCORE':score})
print(can_name)
print(total_score)
    
    
