print(" A test assement compiled by;\n Abdulraheem Sodiq Abiola\n Email:sodiqraheem29@yahoo.com\n Telephone Number:08059589083\n")
print("     Codelagos Batch 5 Python")
print("This program want to test academic ability of stundents in Secomdary schools        ")
print("     WELCOME TO EASY BOOK SHELVE  ")
surname=input("enter your surname\n")
firstname=input("enter your firstname\n")
phonenumber=float(input("enter your phonenumber\n+234"))
email=input("enter your email\n")
username=input("enter your username\n")
print(username,"it study time")
score=0
Category=input("select category\nA. Junior category\t B. Senior category\n").upper()
if(Category=="A"):
 Question1=input("1.What is the prime factor of 24\n (a) 4 and 3\n (b) 2 and 3\n (c) 8\n").lower()
 if(Question1=='b'):
    print("correct")
    score=score+1
 else:
    print("wrong, b is the corect answer")
 Question2=input("2.What is the prime number between 23 to 50\n (a) 27,31,47\n (b) 29,31,41\n (c) 29,31,37,41,43,47\n").lower()
 if(Question2=="c"):
    print("correct")
    score=float(score+1)
 else:
    print("wrong, c is the corect answer")
 Question3=input("3.What is the prime factor of 55\n (a) 5 and 11\n (b) 5\n (c) none\n").lower()
 if(Question3=="a"):
    print("correct")
    score=float(score+1)
 else:
    print("wrong, a is the corect answer")
 Question4= input("4.The position of 3 in 3002504 is______\n (a) hundred thousand\n (b) ten thousand\n (c) millions\n").lower()
 if(Question4=="c"):
    print("correct")
    score=float(score+1)
 else:
    print("wrong, c is the corect answer")
 Question5=input("5.Write six hundred thousand, five hundred and two in figures\n (a) 60005002\n (b) 600502\n (c) 605002\n").lower()
 if(Question5=="b"):
    print("correct")
    score=score+1
 else:
    print("wrong, b is the corect answer")
 Question6=input("6.Change 4/8 to decimal\n (a) 0.4\n (b) 0.25\n (c) 0.5\n").lower()
 if(Question6=="c"):
    print("correct")
    score=score+1
 else:
    print("wrong, c is the corect answer")
 Question7=input("7.Change 0.07 to fraction in lowest term\n (a) 7/100\n (b) 7/10\n (c) 70\n").lower()
 if(Question7=="a"):
    print("correct")
    score=score+1
 else:
    print("wrong, a is the corect answer")
 Question8=input("8.Find the value of 50% of 140m\n (a) 70m\n (b) 7m\n (c) 700m\n.").lower()
 if(Question8=="a"):
    print("correct")
    score=score+1
 else:
    print("wrong, a is the corect answer")
 Question9=input("9.What is 3% of 50?\n (a) 1.5\n (b) 15\n (c) 150\n").lower()
 if(Question9=="a"):
    print("correct")
    score=score+1
 else:
    print("wrong, a is the corect answer")
 Question10=input("10. what is the area of a cicle whose diameter is 10cm\n (a) 78.5\n (b) 78.8m\n (c) 78.2\n").lower()
 if(Question10=="a"):
    print("correct")
    score=score+1
 else:
    print("wrong, a is the corect answer")
 print(username, 'you have', score, 'marks')
 Option=input("Do you want to retry Y/N\n") .upper()
 if(Option=="N"):
    print('Thank you', username, 'goodbye')
 else:
    print
elif(Category=="B"):
 Department=input("What's your department?\nA. Science\t B. Art\t C. Commercial\n") .upper()
 if(Department=="A"):
   Question1=input("1. A body of mass 4Kg moves through a distance 80m. Calculate the work done on the body on the body(g=10ms^2)\n a.32J\n b. 42J\n c. 320J\n d. 0.016J\n").lower()
   if(Question1=="a"):
        print("correct")
        score=score+1
   else:
       print("wrong, a is the corect answer")
   Question2=input("2. The maximum  power disspated by a 100ohms resistor in a current is 4W. Calculate the voltage across the resistor\n a. 10v\n b. 20v\n c. 25v\n d. 450v\n") .lower
   if(Question2=="b"):
        print("correct")
        score=score+1
   else:
       print("wrong, b is the corect answer")
    
   Question3=input("3. A metal rod of length 100cm is heated through 100C. calulate the change in the length of the rod{a=3x10^-5 K^-1}\n a. 4mm\n b. 3mm\n c. 2mm\n"). lower()
   if(Question3=="b"):
        print("correct")
        score=score+1
   else:
       print("wrong, b is the corect answer")
   Question4=input("4. A moving object is said to have Uniform acceleration if it's________\n a. Displacement decreases at constant rate\n b. Speed is directly proportional to time\n c. Velocity increases by equal amount in equal time interval\n") .lower()
   if(Question4=="b"):
        print("correct")
        score=score+1
   else:
       print("wrong, b is the corect answer")
   Question5=input("5. In the periodic table, alkaline earth metals can be found in group\n a. I\n b. I\n c. VI\n") .lower()
   if(Question5=="a"):
        print("correct")
        score=score+1
   else:
       print("wrong, a is the corect answer")
   Question6=input("6. Which of the following elements is diatomic?\n a. Sodium\n b. Oxygen\n c. Iron\n")
   if(Question6=="b"):
        print("correct")
        score=score+1
   else:
       print("wrong, b is the corect answer")
   Question7=input("7. Consider the reaction reprentened by the folloing quation: C2H2 + yH2 – C2H6. The value of y in the reaction is___?\n a. 4\n b. 3\n c. 2\n") .lower()
   if(Question7=="c"):
        print("correct")
        score=score+1
   else:
       print("wrong, c is the corect answer")
   Question8=input("8. The gas law which describes the reationship between volume of a liquid and temperature in an open container?\n a. Boyle's law\n b. Chales's law\n c. Dalton's law\n") .lower()
   if(Question8=="b"):
        print("correct")
        score=score+1
   else:
       print("wrong, b is the corect answer")
   Question9=input("9. In  which of the follwoing series are the atoms arranged in order of increasing boiling point of water?\n a. Metallic Bond\n b. Covalent Bond \n c. Ionic Bond\n") .lower()
   if(Question9=="b"):
        print("correct")
        score=score+1
   else:
       print("wrong, b is the corect answer")
   Question10=input("10. Which of the halogens is liquid at room temperature?\n a. Iodine\n b. Chlorine\n c. Fluorine\n") .lower()
   if(Question10=="b"):
        print("correct")
        score=score+1
   else:
       print("wrong, b is the corect answer")
   print(username, 'you have', score, 'marks')
   Option=input("Do you want to retry Y/N\n") .upper()
   if(Option=="N"):
      print('Thank you', username, 'goodbye')
   else:
      print
 elif(Department=='B'):
     Question1=input("1. Paul's letter to Philemon is about \n a. simplicity\n b. truthfulness\n c. forgiveness\n").lower()
     if(Question1=="c"):
        print("correct")
        score=score+1
     else:
       print("wrong, c is the corect answer")
     Question2=input("2. Which of the following Gospels best presents Jesus as a man yet with authority?\n a.John\n b.Luke\n c.Matthew\n").lower()
     if(Question2=="b"):
        print("correct")
        score=score+1
     else:
       print("wrong, b is the corect answer")
     Question3=input("3. The Lord told Solomon his kingdom would be divided after his death because_____\n a. He had married foriegn woman\n b.Be built the temple\n c.He followed other gods\n").lower()
     if(Question3=="c"):
        print("correct")
        score=score+1
     else:
       print("wrong, c is the corect answer")
     Question4=input("4. When Jesus sent out the seventy disciples on a mission, He charged them to ____\n a. raise the lame and the paralytic\n b. open the eyes of the blind and raise the dead\n c heal the sick and preach the message of the kingdom\n").lower()
     if(Question4=="c"):
        print("correct")
        score=score+1
     else:
       print("wrong, c is the corect answer")
     Question5=input("5. What did King Josiah do to the idolatrous priests of Judah?\n a. He sent all of them on exile\n b. He killed all of them\n c.He demoted all of them\n").lower()
     if(Question5=="b"):
        print("correct")
        score=score+1
     else:
       print("wrong, b is the corect answer")
     Question6=input("6. This question is based on General Literature Principles and Literary Appreciation.\n'I die, yet depart not,\nI am bound, yet soar free;\nThou art and thou art not,\nAnd ever shall be!'\n'The City of Dreams' by Robert Buchanan. The literary device consciously used in the above extract is____?\n a. metaphysical conceit\n b. paradox\n c. oxymoron\n").lower()
     if(Question6=="c"):
        print("correct")
        score=score+1
     else:
       print("wrong, c is the corect answer")
     Question7=input("7. Government by the few is____\n a. dictatorship\n b. monarchy\n c.oligarchy\n").lower()
     if(Question7=="c"):
        print("correct")
        score=score+1
     else:
       print("wrong, c is the corect answer")
     Question8=input("8. Accountability is an act of worship\n a. though it is not mentioned in the Qur’an\n b. because it is specifically mentioned in the Qur’an\n c.being one of the fundamental principles of Islam\n").lower()
     if(Question8=="b"):
        print("correct")
        score=score+1
     else:
       print("wrong, b is the corect answer")
     Question9=input("9. The complexity and technical nature of some legislative matters have created the need for____?\n a. checks and balances\n b. delegated legislation\n c.regulatory committee\n").lower()
     if(Question9=="b"):
        print("correct")
        score=score+1
     else:
       print("wrong, b is the corect answer")
     Question10=input("10. The complexity and technical nature of some legislative matters have created the need for____?\n a. checks and balances\n b. delegated legislation\n c.regulatory committee\n").lower()
     if(Question10=="b"):
        print("correct")
        score=score+1
     else:
       print("wrong, b is the corect answer")
     print(username, 'you have', score, 'marks')
     Option=input("Do you want to retry Y/N\n") .upper()
     if(Option=="N"):
        print('Thank you', username, 'goodbye')
     else:
        print
 elif(Department=="C"):
     Question1=input("1. What was the cost of materials available for use during the period?\n a. N440,300\n b. N449,500\n c. 448,500\n").lower()
     if(Question1=="a"):
        print("correct")
        score=score+1
     else:
       print("wrong, a is the corect answer")
     Question2=input("2. Determine the total expenses of department P?\n a. 9,760\n b. 2,500\n c.2,860\n").lower()
     if(Question2=="b"):
        print("correct")
        score=score+1
     else:
       print("wrong, b is the corect answer")
     Question3=input("3. Receipt and payments account is a summary of the?\n a. budget\n b. trading account\n c.cash book\n").lower()
     if(Question3=="c"):
        print("correct")
        score=score+1
     else:
       print("wrong, c is the corect answer")
     Question4=input("4. The process of cost apportionment is carried out so that___?\n a. common costs are shared among cost centres\n b. cost units could gather overhead as they pass through cost centres\n c.variable costs may be controlled\n").lower()
     if(Question4=="a"):
        print("correct")
        score=score+1
     else:
       print("wrong, a is the corect answer")
     Question5=input("5. Given:\n Cash purchases ..............................N25000\n Trading creditors............................N45000\n Opening balance of trade creditors...........N35000\n Calculate the purchases for the period?\n a. N80,000\n b. N70,000\n c.N105,000\n").lower()
     if(Question5=="b"):
        print("correct")
        score=score+1
     else:
       print("wrong, b is the corect answer")
     Question6=input("6. Banks are engaged in the business of buying and selling of?\n a. bills of exchange\n b. instruments of credit\n c. intangible products\n").lower()
     if(Question6=="a"):
        print("correct")
        score=score+1
     else:
       print("wrong, a is the corect answer")
     Question7=input("7. Life insurance companies contribute to economic development by holding a part of their assets in ___?\n a. long-term financial instruments\n b. money market instruments\n c. cash and near money\n").lower()
     if(Question7=="c"):
        print("correct")
        score=score+1
     else:
       print("wrong, c is the corect answer")
     Question8=input("8. Which of the following occupations come under the extractive industry? i. Cattle-rearing,lumbering,farming\n ii. Mining, quarrying, hunting\n iii.Ship building, road construction, iron bending\n iv. Singing, dancing, barbing\n a. i, ii and iii only\n b. i, ii and iv only\n c. i and ii only\n").lower()
     if(Question8=="c"):
        print("correct")
        score=score+1
     else:
       print("wrong, c is the corect answer")
     Question9=input("9.Industrial occupation does not involve the___?\n a. movement of people and goods\n b. use of machinery\n C.construction and manufacturing of goods\n").lower()
     if(Question9=="a"):
        print("correct")
        score=score+1
     else:
       print("wrong, a is the corect answer")
     Question10=input("10. In a primary market, new shares are issued through?\n a. personal selling, publicity and advertising\n b. a prospectus, an offer for sale and bill of exchange\n c.advertising a prospectus, and bill of exchange\n").lower()
     if(Question10=="b"):
        print("correct")
        score=score+1
     else:
       print("wrong, b is the corect answer")
     print(username, 'you have', score, 'marks')
     Option=input("Do you want to retry Y/N\n") .upper()
     if(Option=="N"):
        print('Thank you', username, 'goodbye')
     else:
        print
