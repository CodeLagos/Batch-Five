print("PROGRAM TITLE: SALE'S REP CALCULATOR")
print("NAME: ROSEMARY ONYEBUENYI")
print("EMAIL ADRRESS: ronyebuenyi4real@yahoo.com")

print("This is a program written after a comprenhensive CodeLagos Python Tutorial organised by the Lagos State Government.\n This Program will enable Sale's Rep calculate the total amount of books sold in their store and then generate Receipt for customers")
print("FUNCTIONALITY OF PROGRAM: -Collect the information of the customer -Calculate the total goods bought, -Generate Receipt")



print("WELCOME TO THE ROSEY BOOK STORE\n")
while True:
    print("Select either '1' or '2' or '3'\n1.Available Books in Store:\n2.Enter Orders taken:\n3.Generate Receipt\n")
    print("\n")
    select = int(input("Enter either '1' or '2' and '3 to generate receipt': "))
    if select == 1:        
         print("List of Available Books in Store;\n\nScience\nChemistry and atoms=1500\tNuclear Physics=2500\tGeneral Anatomy=15000\nModern Chemistry=1700\tRandom Physics=6500\tAtomic Physics=15000\n\nEngineering\nIons and Numbers=7500\tAbout Science=30000\tPetrol Physics=2500\nDifferential Calculus=7500\tRobotics and Artificial Intelligence=30000\tMachine and Oil Engines=25000\n\nLiterature\nLook Before you Leap=2300\tThis Year=1800\tStar Signs=1500\nLion and the jewels=2300\tIsunike and her goat=1200\tThings fall Apart=4500\n\nEcomomics\nKarl Max Theory=11350\tBetter Decision Making=1100\tSocial Diversification=5000\nMacroEconomics=1350\tAdvanced Economics=7100\tCapitalism=5000\n\nPolitics\nThe Transition by GEJ=1000\tThe Principles of Election and Political Party=2300\tAdaption of Power and Economic Reforms=1500\nThe Big Plan=1000\tThe Table Turners=2000\tModern Politics=3500\n\nReligion\nShiloh 2018 Bulletin=2000\tDaily Manner=1100\tHoly Spirit and Tithing=2400\nAbout the Modern Church=2700\tTheology=12100\tFinance and Ministry=2400")
         print("\n")  
    elif select == 2:
        print("ENTER ORDER NOW: \n")
        name = input("Enter Customer's name: ")
        phoneno = input("Enter Customer's phone number: ")
        bookname= input("Enter Book name: " )
        bookquan =int(input("Its quantity: " ))
        bookprice =float(input("Price: " ))
        tot = bookquan*bookprice
        print(bookquan,'quantity(s) of',bookname,'costs',tot,'Naira Only')
        

    if select == 3:

        import random
        a=random.randint(20110,100610)
        
        print("Receipt about to be printed, re-check Customer's details")
        name = input("Enter Customer's name: ")
        bookname= input("Enter Book name: " )
        bookquan =int(input("Its quantity: " ))
        bookprice =float(input("Price: " ))
        tot = bookquan*bookprice
        day = int(input('Enter day of issue(numbers are only allowed): '))
        month = int(input('Enter month of issue(numbers are only allowed): '))
        year = int(input('Enter year of issue(numbers are only allowed): '))
        b= day,month,year
        print("Receipt printed successfully")
        print("********************************************************************************")
        print("*****                                                                      *****")
        print("                         **** ROSEY BOOK STORE****                              ")
        print("          giving you the best services and best books in town        ",a         )
        print("                         www. roseybookstore.com                                ")
        print("________________________________________________________________________________")
        print("                                   RECEIPT                                      ")
        print("                                 ",name,"                                       ")
        print("Received from ------------------------------------------------------------------")
        print("                              ",tot,                 "                          ")
        print("the sum of ---------------------------------------------------------------------")
        print("----------------------------------Naira-------------------------------------kobo")
        print("                         ",bookquan,'quantity(s) of',bookname                    )
        print("being paid for------------------------------------------------------------------")
        print("                  ",a,"              " ,     "         " ,b, "                  ")
        print("Receipt No:----------------------------- Date:----------------------------------")
        print("                         Thanks for your patronage                              ")
        print("*****                                                                      *****")
        print("********************************************************************************")
