"""
1. Display the purpose of the program
2. Dipslay the instructions
3. Display a numbered list of Command for the User
4. Ask the user to pick the desired Options
5. Ask the user for the activities to be carried out by the command
6. Execute the activities
"""
print ("This is a Program to EXECUTE some basic ATM operations")
print ("Welcome to LADE SAVINGS AND LOANS")
print ("PLEASE INSERT YOUR CARD")
amount1= 45987.65
print ("Enter your 4 digit PIN")
print ("You have just 3 attempts")
pin1 = int(input(""))
if (pin1 == 1234):
    menu1 = input("please select an ACCOUNT TYPE\n1)SAVINGS\n2)CURRENT\n3)CREDIT\n")
    if ((menu1 != "1")and (menu1 != "2") and (menu1 != "3")):
        print ("Invalid Selection, Please re-insert your card and try again")
    else:        
        menu = int(input("please select an option\n1)WITHDRAWAL\n2)TRANSFER\n3)CHANGE PIN\n4)ENQUIRY\n5)RECHARGE\n6)CANCEL\n"))
        if (menu==1):
            menu2 = int(input("please select an amount\n1)500\n2)1000\n3)3000\n4)5000\n5)10000\n6)20000\n"))
            if (menu2 == 1):
                print ("Please wait, Your 500 Cash is Dispensing")
            elif (menu2 == 2):
                print ("Please wait, Your 1000 Cash is Dispensing")
            elif (menu2 == 3):
                print ("Please wait, Your 3000 Cash is Dispensing")
            elif (menu2 == 4):
                print ("Please wait, Your 5000 Cash is Dispensing")
            elif (menu2 == 5):
                print ("Please wait, Your 10000 Cash is Dispensing")
            elif (menu2 == 6):
                print ("Please wait, Your 20000 Cash is Dispensing")
            else:
                print ("Invalid Option")
        elif (menu ==2):
            menu3 = int(input("please select an ACCOUNT TYPE you wish to transfer to \n1)SAVINGS\n2)CURRENT\n3)CREDIT\n"))
            if (menu3 ==1):
                account=input ("Enter the RECIPENT'S 10 digit SAVINGS account number\n")
                strl2 =len(account)
                if (strl2>10) or (strl2<10):
                    print ("Incorrect Account Number, Please Re-Insert your Card and Try again\n")
                else:
                    menu7 = input("please select the RECIPENT'S BANK \n1)ACCESS\n2)GTB\n3)FIRST BANK\n4)DIAMOND\n5)UNION\n6)UBA\n7)STANBIC\n8)ECOBANK\n9)POLARIS\n")
                    if ((menu7 != "1")and (menu7 != "2") and (menu7 != "3")and (menu7 != "4") and (menu7 != "5")and (menu7 != "6") and (menu7 != "7") and (menu7 != "8") and (menu7 != "9")):
                        print ("invalid BANK selection, Please re-insert your card and try again")
                    else:
                        print ("Enter the amount")
                        amount = int(input("")) 
                        print (amount, "has been transfered to", account)
            if (menu3 ==2):
                account=input ("Enter the RECIPENT'S 10 digit CURRENT account number\n")
                strl2 =len(account)
                if (strl2>10) or (strl2<10):
                    print ("Incorrect Account Number, Please Re-Insert your Card and Try again\n")
                else:
                    menu7 = input("please select the RECIPENT'S BANK \n1)ACCESS\n2)GTB\n3)FIRST BANK\n4)DIAMOND\n5)UNION\n6)UBA\n7)STANBIC\n8)ECOBANK\n9)POLARIS\n")
                    if ((menu7 != "1")and (menu7 != "2") and (menu7 != "3")and (menu7 != "4") and (menu7 != "5")and (menu7 != "6") and (menu7 != "7") and (menu7 != "8") and (menu7 != "9")):
                        print ("invalid BANK selection, Please re-insert your card and try again")
                    else:
                        print ("Enter the amount")
                        amount = int(input("")) 
                        print (amount, "has been transfered to", account)
            if (menu3 ==3):
                account=input ("Enter the RECIPENT'S 10 digit SAVINGS account number\n")
                strl2 =len(account)
                if (strl2>10) or (strl2<10):
                    print ("Incorrect Account Number, Please Re-Insert your Card and Try again\n")
                else:
                    menu7 = input("please select the RECIPENT'S BANK \n1)ACCESS\n2)GTB\n3)FIRST BANK\n4)DIAMOND\n5)UNION\n6)UBA\n7)STANBIC\n8)ECOBANK\n9)POLARIS\n")
                    if ((menu7 != "1")and (menu7 != "2") and (menu7 != "3")and (menu7 != "4") and (menu7 != "5")and (menu7 != "6") and (menu7 != "7") and (menu7 != "8") and (menu7 != "9")):
                        print ("invalid BANK selection, Please re-insert your card and try again")
                    else:
                        print ("Enter the amount")
                        amount = int(input("")) 
                        print (amount, "has been transfered to", account)
        elif (menu ==3):
            print ("Enter your pin")
            pin2 = int(input(""))
            if pin2==pin1:
                print ("Enter your new pin")
                pin3 = int(input(""))
                print ("Confirm your new pin")
                pin4 = int(input(""))
                if pin4==pin3:
                    print ("Your pin has been changed SUCCESSFULLY")
                else:
                    print ("Incorrect Pin Combination, Please Re-insert your card and Start again")
            else:
                print("Incorrect Pin, Re-insert your card and start again")
        elif (menu ==4):
            print ("Your account balance is", amount1)
        elif (menu==5):
            menu4 = int(input("please select the NETWORK PROVIDER to be credited \n1)MTN\n2)GLO\n3)AIRTEL\n4)ETISALAT\n"))
            if (menu4 ==1):
                number = input ("Enter your 11 digit MTN mobile number\n")
                strl = len(number)
                if (strl>11) or (strl<11):
                    print ("Your mobile number is incorrect, Please re-insert card and try again")
                else:
                    print ("Enter the amount to be recharged")
                    amount2 = int(input("")) 
                    print (amount2, "has been credited to", number)
            if (menu4 ==2):
                number = input ("Enter your 11 digit GLO mobile number\n")
                strl = len(number)
                if (strl>11) or (strl<11):
                    print ("Your mobile number is incorrect, Please re-insert card and try again")
                else:
                    print ("Enter the amount to be recharged")
                    amount2 = int(input("")) 
                    print (amount2, "has been credited to", number)
            if (menu4 ==3):
                number = input ("Enter your 11 digit AIRTEL mobile number\n")
                strl = len(number)
                if (strl>11) or (strl<11):
                    print ("Your mobile number is incorrect, Please re-insert card and try again")
                else:
                    print ("Enter the amount to be recharged")
                    amount2 = int(input("")) 
                    print (amount2, "has been credited to", number)
            if (menu4 ==4):
                number = input ("Enter your 11 digit ETISALAT mobile number\n")
                strl = len(number)
                if (strl>11) or (strl<11):
                    print ("Your mobile number is incorrect, Please re-insert card and try again")
                else:
                    print ("Enter the amount to be recharged")
                    amount2 = int(input("")) 
                    print (amount2, "has been credited to", number)
        elif (menu ==6):
            print("You have chosen to cancel the transaction, Please remove your card")
            print ("HAVE A NICE DAY")
#second attempt
elif print("Wrong PIN!!!"):
    amount1= 45987.65
print ("Please Re-Enter your 4 digit PIN")
print ("you have just 2 attempts left!!!")
pin1 = int(input(""))
if (pin1 == 1234):
    menu1 = input("please select an ACCOUNT TYPE\n1)SAVINGS\n2)CURRENT\n3)CREDIT\n")
    if ((menu1 != "1")and (menu1 != "2") and (menu1 != "3")):
        print ("Invalid Selection, Please re-insert your card and try again")
    else:        
        menu = int(input("please select an option\n1)WITHDRAWAL\n2)TRANSFER\n3)CHANGE PIN\n4)ENQUIRY\n5)RECHARGE\n6)CANCEL\n"))
        if (menu==1):
            menu2 = int(input("please select an amount\n1)500\n2)1000\n3)3000\n4)5000\n5)10000\n6)20000\n"))
            if (menu2 == 1):
                print ("Please wait, Your 500 Cash is Dispensing")
            elif (menu2 == 2):
                print ("Please wait, Your 1000 Cash is Dispensing")
            elif (menu2 == 3):
                print ("Please wait, Your 3000 Cash is Dispensing")
            elif (menu2 == 4):
                print ("Please wait, Your 5000 Cash is Dispensing")
            elif (menu2 == 5):
                print ("Please wait, Your 10000 Cash is Dispensing")
            elif (menu2 == 6):
                print ("Please wait, Your 20000 Cash is Dispensing")
            else:
                print ("Invalid Option")
        elif (menu ==2):
            menu3 = int(input("please select an ACCOUNT TYPE you wish to transfer to \n1)SAVINGS\n2)CURRENT\n3)CREDIT\n"))
            if (menu3 ==1):
                account=input ("Enter the RECIPENT'S 10 digit SAVINGS account number\n")
                strl2 =len(account)
                if (strl2>10) or (strl2<10):
                    print ("Incorrect Account Number, Please Re-Insert your Card and Try again\n")
                else:
                    menu7 = input("please select the RECIPENT'S BANK \n1)ACCESS\n2)GTB\n3)FIRST BANK\n4)DIAMOND\n5)UNION\n6)UBA\n7)STANBIC\n8)ECOBANK\n9)POLARIS\n")
                    if ((menu7 != "1")and (menu7 != "2") and (menu7 != "3")and (menu7 != "4") and (menu7 != "5")and (menu7 != "6") and (menu7 != "7") and (menu7 != "8") and (menu7 != "9")):
                        print ("invalid BANK selection, Please re-insert your card and try again")
                    else:
                        print ("Enter the amount")
                        amount = int(input("")) 
                        print (amount, "has been transfered to", account)
            if (menu3 ==2):
                account=input ("Enter the RECIPENT'S 10 digit CURRENT account number\n")
                strl2 =len(account)
                if (strl2>10) or (strl2<10):
                    print ("Incorrect Account Number, Please Re-Insert your Card and Try again\n")
                else:
                    menu7 = input("please select the RECIPENT'S BANK \n1)ACCESS\n2)GTB\n3)FIRST BANK\n4)DIAMOND\n5)UNION\n6)UBA\n7)STANBIC\n8)ECOBANK\n9)POLARIS\n")
                    if ((menu7 != "1")and (menu7 != "2") and (menu7 != "3")and (menu7 != "4") and (menu7 != "5")and (menu7 != "6") and (menu7 != "7") and (menu7 != "8") and (menu7 != "9")):
                        print ("invalid BANK selection, Please re-insert your card and try again")
                    else:
                        print ("Enter the amount")
                        amount = int(input("")) 
                        print (amount, "has been transfered to", account)
            if (menu3 ==3):
                account=input ("Enter the RECIPENT'S 10 digit SAVINGS account number\n")
                strl2 =len(account)
                if (strl2>10) or (strl2<10):
                    print ("Incorrect Account Number, Please Re-Insert your Card and Try again\n")
                else:
                    menu7 = input("please select the RECIPENT'S BANK \n1)ACCESS\n2)GTB\n3)FIRST BANK\n4)DIAMOND\n5)UNION\n6)UBA\n7)STANBIC\n8)ECOBANK\n9)POLARIS\n")
                    if ((menu7 != "1")and (menu7 != "2") and (menu7 != "3")and (menu7 != "4") and (menu7 != "5")and (menu7 != "6") and (menu7 != "7") and (menu7 != "8") and (menu7 != "9")):
                        print ("invalid BANK selection, Please re-insert your card and try again")
                    else:
                        print ("Enter the amount")
                        amount = int(input("")) 
                        print (amount, "has been transfered to", account)
        elif (menu ==3):
            print ("Enter your pin")
            pin2 = int(input(""))
            if pin2==pin1:
                print ("Enter your new pin")
                pin3 = int(input(""))
                print ("Confirm your new pin")
                pin4 = int(input(""))
                if pin4==pin3:
                    print ("Your pin has been changed SUCCESSFULLY")
                else:
                    print ("Incorrect Pin Combination, Please Re-insert your card and Start again")
            else:
                print("Incorrect Pin, Re-insert your card and start again")
        elif (menu ==4):
            print ("Your account balance is", amount1)
        elif (menu==5):
            menu4 = int(input("please select the NETWORK PROVIDER to be credited \n1)MTN\n2)GLO\n3)AIRTEL\n4)ETISALAT\n"))
            if (menu4 ==1):
                number = input ("Enter your 11 digit MTN mobile number\n")
                strl = len(number)
                if (strl>11) or (strl<11):
                    print ("Your mobile number is incorrect, Please re-insert card and try again")
                else:
                    print ("Enter the amount to be recharged")
                    amount2 = int(input("")) 
                    print (amount2, "has been credited to", number)
            if (menu4 ==2):
                number = input ("Enter your 11 digit GLO mobile number\n")
                strl = len(number)
                if (strl>11) or (strl<11):
                    print ("Your mobile number is incorrect, Please re-insert card and try again")
                else:
                    print ("Enter the amount to be recharged")
                    amount2 = int(input("")) 
                    print (amount2, "has been credited to", number)
            if (menu4 ==3):
                number = input ("Enter your 11 digit AIRTEL mobile number\n")
                strl = len(number)
                if (strl>11) or (strl<11):
                    print ("Your mobile number is incorrect, Please re-insert card and try again")
                else:
                    print ("Enter the amount to be recharged")
                    amount2 = int(input("")) 
                    print (amount2, "has been credited to", number)
            if (menu4 ==4):
                number = input ("Enter your 11 digit ETISALAT mobile number\n")
                strl = len(number)
                if (strl>11) or (strl<11):
                    print ("Your mobile number is incorrect, Please re-insert card and try again")
                else:
                    print ("Enter the amount to be recharged")
                    amount2 = int(input("")) 
                    print (amount2, "has been credited to", number)
        elif (menu ==6):
            print("You have chosen to cancel the transaction, Please remove your card")
            print ("HAVE A NICE DAY")
#third pin attempt
elif print("Wrong PIN!!!"):
    amount1= 45987.65
print ("Please Re-Enter your 4 digit PIN")
print ("you have just 1 attempts left!!!")
pin1 = int(input(""))
if (pin1 == 1234):
    menu1 = input("please select an ACCOUNT TYPE\n1)SAVINGS\n2)CURRENT\n3)CREDIT\n")
    if ((menu1 != "1")and (menu1 != "2") and (menu1 != "3")):
        print ("Invalid Selection, Please re-insert your card and try again")
    else:        
        menu = int(input("please select an option\n1)WITHDRAWAL\n2)TRANSFER\n3)CHANGE PIN\n4)ENQUIRY\n5)RECHARGE\n6)CANCEL\n"))
        if (menu==1):
            menu2 = int(input("please select an amount\n1)500\n2)1000\n3)3000\n4)5000\n5)10000\n6)20000\n"))
            if (menu2 == 1):
                print ("Please wait, Your 500 Cash is Dispensing")
            elif (menu2 == 2):
                print ("Please wait, Your 1000 Cash is Dispensing")
            elif (menu2 == 3):
                print ("Please wait, Your 3000 Cash is Dispensing")
            elif (menu2 == 4):
                print ("Please wait, Your 5000 Cash is Dispensing")
            elif (menu2 == 5):
                print ("Please wait, Your 10000 Cash is Dispensing")
            elif (menu2 == 6):
                print ("Please wait, Your 20000 Cash is Dispensing")
            else:
                print ("Invalid Option")
        elif (menu ==2):
            menu3 = int(input("please select an ACCOUNT TYPE you wish to transfer to \n1)SAVINGS\n2)CURRENT\n3)CREDIT\n"))
            if (menu3 ==1):
                account=input ("Enter the RECIPENT'S 10 digit SAVINGS account number\n")
                strl2 =len(account)
                if (strl2>10) or (strl2<10):
                    print ("Incorrect Account Number, Please Re-Insert your Card and Try again\n")
                else:
                    menu7 = input("please select the RECIPENT'S BANK \n1)ACCESS\n2)GTB\n3)FIRST BANK\n4)DIAMOND\n5)UNION\n6)UBA\n7)STANBIC\n8)ECOBANK\n9)POLARIS\n")
                    if ((menu7 != "1")and (menu7 != "2") and (menu7 != "3")and (menu7 != "4") and (menu7 != "5")and (menu7 != "6") and (menu7 != "7") and (menu7 != "8") and (menu7 != "9")):
                        print ("invalid BANK selection, Please re-insert your card and try again")
                    else:
                        print ("Enter the amount")
                        amount = int(input("")) 
                        print (amount, "has been transfered to", account)
            if (menu3 ==2):
                account=input ("Enter the RECIPENT'S 10 digit CURRENT account number\n")
                strl2 =len(account)
                if (strl2>10) or (strl2<10):
                    print ("Incorrect Account Number, Please Re-Insert your Card and Try again\n")
                else:
                    menu7 = input("please select the RECIPENT'S BANK \n1)ACCESS\n2)GTB\n3)FIRST BANK\n4)DIAMOND\n5)UNION\n6)UBA\n7)STANBIC\n8)ECOBANK\n9)POLARIS\n")
                    if ((menu7 != "1")and (menu7 != "2") and (menu7 != "3")and (menu7 != "4") and (menu7 != "5")and (menu7 != "6") and (menu7 != "7") and (menu7 != "8") and (menu7 != "9")):
                        print ("invalid BANK selection, Please re-insert your card and try again")
                    else:
                        print ("Enter the amount")
                        amount = int(input("")) 
                        print (amount, "has been transfered to", account)
            if (menu3 ==3):
                account=input ("Enter the RECIPENT'S 10 digit SAVINGS account number\n")
                strl2 =len(account)
                if (strl2>10) or (strl2<10):
                    print ("Incorrect Account Number, Please Re-Insert your Card and Try again\n")
                else:
                    menu7 = input("please select the RECIPENT'S BANK \n1)ACCESS\n2)GTB\n3)FIRST BANK\n4)DIAMOND\n5)UNION\n6)UBA\n7)STANBIC\n8)ECOBANK\n9)POLARIS\n")
                    if ((menu7 != "1")and (menu7 != "2") and (menu7 != "3")and (menu7 != "4") and (menu7 != "5")and (menu7 != "6") and (menu7 != "7") and (menu7 != "8") and (menu7 != "9")):
                        print ("invalid BANK selection, Please re-insert your card and try again")
                    else:
                        print ("Enter the amount")
                        amount = int(input("")) 
                        print (amount, "has been transfered to", account)
        elif (menu ==3):
            print ("Enter your pin")
            pin2 = int(input(""))
            if pin2==pin1:
                print ("Enter your new pin")
                pin3 = int(input(""))
                print ("Confirm your new pin")
                pin4 = int(input(""))
                if pin4==pin3:
                    print ("Your pin has been changed SUCCESSFULLY")
                else:
                    print ("Incorrect Pin Combination, Please Re-insert your card and Start again")
            else:
                print("Incorrect Pin, Re-insert your card and start again")
        elif (menu ==4):
            print ("Your account balance is", amount1)
        elif (menu==5):
            menu4 = int(input("please select the NETWORK PROVIDER to be credited \n1)MTN\n2)GLO\n3)AIRTEL\n4)ETISALAT\n"))
            if (menu4 ==1):
                number = input ("Enter your 11 digit MTN mobile number\n")
                strl = len(number)
                if (strl>11) or (strl<11):
                    print ("Your mobile number is incorrect, Please re-insert card and try again")
                else:
                    print ("Enter the amount to be recharged")
                    amount2 = int(input("")) 
                    print (amount2, "has been credited to", number)
            if (menu4 ==2):
                number = input ("Enter your 11 digit GLO mobile number\n")
                strl = len(number)
                if (strl>11) or (strl<11):
                    print ("Your mobile number is incorrect, Please re-insert card and try again")
                else:
                    print ("Enter the amount to be recharged")
                    amount2 = int(input("")) 
                    print (amount2, "has been credited to", number)
            if (menu4 ==3):
                number = input ("Enter your 11 digit AIRTEL mobile number\n")
                strl = len(number)
                if (strl>11) or (strl<11):
                    print ("Your mobile number is incorrect, Please re-insert card and try again")
                else:
                    print ("Enter the amount to be recharged")
                    amount2 = int(input("")) 
                    print (amount2, "has been credited to", number)
            if (menu4 ==4):
                number = input ("Enter your 11 digit ETISALAT mobile number\n")
                strl = len(number)
                if (strl>11) or (strl<11):
                    print ("Your mobile number is incorrect, Please re-insert card and try again")
                else:
                    print ("Enter the amount to be recharged")
                    amount2 = int(input("")) 
                    print (amount2, "has been credited to", number)
        elif (menu ==6):
            print("You have chosen to cancel the transaction, Please remove your card")
            print ("HAVE A NICE DAY")
else:
    print ("FRAUD ALERT!!!")
    print("You have entered an incorrect pin 3 times, Please Visit our nearest branch to claim your card")

    

    
