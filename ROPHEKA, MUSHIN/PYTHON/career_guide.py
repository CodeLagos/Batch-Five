#AUTHOR: Mudathir Dhukrullah O.
#This program is the complementary app to the Career Guide Website

import time
print ("\nWelcome to CareerGuide App\n")
time.sleep(2)
users = {}
status = ""

def displayMenu():
    status = input ("You are highly welcome to our Platform . You can choose the below for your prefered option  \n 1. Register on the Platform \n 2. Login into your Account \n 3. Who we are \n 4. Contact Us \n 5. Quit \n")
    if status == "2":
        OldUser()
    elif status == "1":
        NewUser()
    elif status == "3":
        AboutUs()
    elif status == "4":
        ContactUs()
        
def NewUser():
    firstName = input('Please enter you First name: \n')
    lastName = input('Please enter you Last name: \n')
    createLogin = input("Please enter your preffered username: \n")
    if createLogin in users:
        print ("Login name created succefully")
    else:
        createPass = input ("Please, create password here: \n")
        users[createLogin] = createPass
        print("Please, wait for 5 seconds . . . . .  ")
        time.sleep(5)
        print ("\nMr.", firstName, "You are now a member on our platfrom, Login Below:\n") 
        OldUser()
        
def OldUser():

    print ("We have been waitng for you. Ride on with Our service")
    time.sleep(2)
    Login = input("Please Enter you Username")
    PassW = input("Enter you Password")
    if Login in users and users[Login] == PassW:
        print ("You are welcome. Select you Category by entering the number: \n\n1. Basic Education.\n2. Senior Sec. School. \n3. Out of School. \n4. Exit\n\n")
        category = int(input("Enter your the numebr of your catgory here\n"))
        if category == 1:
                    print ("Basic Education Categories. \nAvailabe Professions are: \n1.Accountant \n2. Banker \n3. Counsellor \n4. Back \n5. Exit \n ")
                    bE = input("Choose your prefered option\n")
                    if bE == "1":
                        print ("\nAccounting \n\nCourses:  Bla Bla Bla Bla \nInstitution: Bla Bla Bla \nOlevel Subject: Bla Bla Bla \nUTME Subjects: Bla Bla Bla \n" )
                        further = input("\nWill you like to go back to the Main menu? \n 1. Yes, I will \n 2. No, Thank You \n")
                        if further == "1":
                            displayMenu()      
                        elif further == "2":
                            print ("Thank you for visiting us here. Bye")
                    elif bE == "2":
                        print ("\\nBanker \n\nCourses:  Bla Bla Bla Bla \nInstitution: Bla Bla Bla \nOlevel Subject: Bla Bla Bla \nUTME Subjects: Bla Bla Bla \n " )
                        further = input("\n  Will you like to go back to the Main menu? \n 1. Yes, I will \n 2. No, Thank You \n")
                        if further == "1":
                            displayMenu()        
                        elif further == "2":
                            print ("Thank you for visiting us here. Bye")
                    elif bE == "3":
                        print ("\nCounsellor \n\nCourses:  Bla Bla Bla Bla \nInstitution: Bla Bla Bla \nOlevel Subject: Bla Bla Bla \nUTME Subjects: Bla Bla Bla \n" )
                        further = input("\n  Will you like to go back to the Main menu? \n 1. Yes, I will \n 2. No, Thank You \n")
                        if further == "1":
                            displayMenu()        
                        elif further == "2":
                            print ("Thank you for visiting us here. Bye")
                    elif bE == "4":
                        category = int(input("Enter your the numebr of your catgory here\n 1. Basic Education.\n2. Senior Sec. School. \n3. Out of School. \n4. Exit\n\n "))
                    elif bE == "5":
                        print ("\ Thanks For visiting our platfrom, Bye" )
                    else:
                        print ("You have enter the wrong option, try again:\n \n Availabe Professions are: \n1.Accountant \n 2. Banker \n3. Counsellor \n4. Back \n5. Exit \n ")
        elif category == 2:
            print ("Senior Secondary School Categories. \nAvailabe Courses are: \n1.Accounting (Acc) \n2. Banking and Finance (BF) \n3. Counselling Psychology (CP) \n4. Back (bk) \n5. Exit (et) \n ")
            bE = input("Type teh abbrevation in the bracket\n")
            if bE == "Acc":
                    print ("\nAccounting \n\nCourses:  Bla Bla Bla Bla \nInstitution: Bla Bla Bla \nOlevel Subject: Bla Bla Bla \nUTME Subjects: Bla Bla Bla \n" )
                    further = input("\nWill you like to go back to the Main menu? \n 1. Yes, I will \n 2. No, Thank You \n")
                    if further == "1":
                        displayMenu()      
                    elif further == "2":
                            print ("\nThank you for visiting us here. Bye")
            elif bE == "BF":
                    print ("\\nBanking and finance \n\nCourses:  Bla Bla Bla Bla \nInstitution: Bla Bla Bla \nOlevel Subject: Bla Bla Bla \nUTME Subjects: Bla Bla Bla \n " )
                    further = input("\nWill you like to go back to the Main menu? \n 1. Yes, I will \n 2. No, Thank You \n")
                    if further == "1":
                         displayMenu()        
                    elif further == "2":
                         print ("\nThank you for visiting us here. Bye")
            elif bE == "CP":
                    print ("\nCounselling Pyschology \n\nCourses:  Bla Bla Bla Bla \nInstitution: Bla Bla Bla \nOlevel Subject: Bla Bla Bla \nUTME Subjects: Bla Bla Bla \n" )
                    further = input("\n Will you like to go back to the Main menu? \n 1. Yes, I will \n 2. No, Thank You \n")
                    if further == "1":
                        displayMenu()        
                    elif further == "2":
                        print ("\nThank you for visiting us here. Bye")
            elif bE == "bk":
                category = int(input("Enter your the numebr of your catgory here\n 1. Basic Education.\n2. Senior Sec. School. \n3. Out of School. \n4. Exit\n\n "))
            elif bE == "ex":
                print ("\nThanks For visiting our platfrom, Bye" )
            else:
                print ("You have enter the wrong option, try again:\n \n Availabe Professions are: \n1.Accountant \n 2. Banker \n3. Counsellor \n4. Back \n5. Exit \n ")
        elif category == 3:
            time.sleep(5)
            print ("\nOut of School Catgeoires\n KINDLY BEAR WITH US, WE ARE STILL UNDER CONSTRCUTION")
            time.sleep(2)
            further = input("\nWill you like to go back to the Main menu? \n 1. Yes, I will \n 2. No, Thank You \n")
            if further == "1":
                displayMenu()        
            elif further == "2":
                    print ("\nThank you for visiting us here. Bye")
        elif category == 4:
                OldUser()
    else:
        print ("\nOops! You have entered a wrong passwords or username\n Try more. . . ")
        OldUser()
def AboutUs():
        print (" Lorem ipsum dolor sit amet, consectetur adipisicing elit, \n sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris \nnisi ut aliquip ex ea commodo")
        further = input("\nWill you like to go back to the Main menu? \n 1. Yes, I will \n 2. No, Thank You \n")
    
        if further == "1":
            displayMenu()        
        elif further == "2":
            print ("\nThank you for visiting us here. Bye")
def ContactUs():
    print("You can reach us on: \n mail: CareerGuide@yahoo.com \n Phone number: 08124152312, 09022554349 \n Instagram: #CareerGuide \n Facebook: www.facebook.com\\careerguide")
    further = input("\nWill you like to go back to the Main menu? \n 1. Yes, I will \n 2. No, Thank You \n")
    
    if further == "1":
        displayMenu()        
    elif further == "2":
        print ("\nThank you for visiting us here. Bye")
while status != "5":
    displayMenu()
    break
