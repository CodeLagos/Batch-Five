#PYTHON PROGRAM TO DISLAY THE OPERATION A USER WOULD PERFORM IN AN ATM
#Name: KISSINGER EDWARD
#Email: kisswitu4life@gmail.com
#Phone: 08026558067/09063892834

print ("")
print ("KISSINGER EDWARD PROJECT")
print ("")
print ("You are welcome to CODE LAGOS ATM service")
print ("")
print ("The Default Pin is: 1111 \nThe Default Account number: 1111")
print ("")

B= "Thank you for banking with us."
Account_Details= "Access Bank Plc \nAccount Name: Edward Ndubuisi Kissinger \nAccount Number: 0000706065"

step1= input("Perform your operation by choosing from options below:\n1 Transaction \n2 Enquiry \n: ")
if (step1 == "1"):     
    Options= input("Select your operation: \n1 Bank Transaction \n2 Airtime Recharge \n: ")  
    if (Options == "1"):        
        print ("Type in your Pin")      
        Pin= input(": ")     
        if (Pin == "1111"):            
            Transaction= input("Transaction type: \n1 Cash Withdrawal \n2 Cash Transfer \n3 Check Acct Balance \n: ")                  
            if (Transaction == "1"):      
                Acct_Type= input("Account Type: \n1 Savings \n2 Current \n: ")
                if (Acct_Type == "1"):
                    print ("Choose amount to withdraw or push ENTER button for other options:")
                    SelectAmount= input("a N1,000 \nb N2,000 \nc N5,000 \n: ")
                    if (SelectAmount.lower () == "a"):
                        print ("Your withdrawal of N1,000 was successful")
                        print (B)
                    elif (SelectAmount.lower () == "b"):
                        print ("Your withdrawal of N2,000 was successful")
                        print (B)
                    elif (SelectAmount.lower () == "c"):
                        print ("Your withdrawal of N1,000 was successful")
                        print (B)
                    else:
                        Others= input("Type in the amount: \n: N")    
                        print ("Your withdrawal of", Others, "was successful")            
                        print (B)
                elif (Acct_Type == "2"):
                    print ("The service is currently unavailable")                  
                    print (B)                    
                else:
                    print ("You have not made any selection \nSelect Account Type to continue")
            elif (Transaction == "2"):
                Acct_Type= input("1 Savings \n2 Current \n: ")
                if (Acct_Type == "1"):
                    Select_Bank= input("Select bank to transfer cash to: \n1 Access Bank \n2 Zenith Bank \n: ")
                    if (Select_Bank == "1"):
                        Account_Number= input("Enter the Acct Number you want to trasfer to: ")
                        if (Account_Number == "1111"):
                            print ("Access Bank, \nEdward Kissinger.")
                            print ("Account Number:", Account_Number)
                            Amount= int(input("Type the amount to transfer: "))                        
                            print ("The cash transfer of", Amount, "was successful")
                            print (B)
                        else:
                            print ("The Account you entered does not exist")
                            print (B)                
                    elif (Select_Bank == "2"):
                        Account_Number= input("Enter the Acct Number you want to trasfer to: ")
                        if (Account_Number == "1111"):
                            print ("Zenith Bank \nFatai Oloko")
                            print ("Account Number:", Account_Number)
                            Amount= int(input("Type the amount to transfer: "))                        
                            print ("The cash transfer of", Amount, "was successful")
                            print (B)
                        else:
                            print ("The Account you entered does not exist")
                            print (B)
                    else:
                        print ("You have not made any selection")                
                        print ("Please select your Bank to continue")                                                                            
                else:
                    print ("The Service is currently unavailable")              
            elif (Transaction == "3"):   
                Acct_Type= input("Account Type: \n1 Savings \n2 Current \n: ") 
                if (Acct_Type == "1"):   
                    print (Account_Details)            
                    print ("Your account balance is:____?")
                    print ("Transaction is Processing...")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                else:
                    print ("The service is currently unavailable")           
                    print (B)
            else:
                print ("Exit")
                print (B)
        else:
            print ("Incorrect Pin")
            print (B)
    elif (Options == "2"):
        Network= input("Sellect your Network: \n1 Airtel NG \n2 MTN NG \n3 Etisalat NG \n4 Glo NG \n: ")
        if (Network == "1"):
            card1= int(input("Type the amount:N"))
            print ("Your requested Airtel recharge of", card1, "is succefull.")
            print (B)
        elif (Network == "2"):
            card2= int(input("Type the amount:N"))
            print ("Your requested MTN recharge of", card2, "is succefull.")
            print (B)
        elif (Network == "3"):
            card3= int(input("Type the amount: "))
            print ("Your requested Etisalat recharge of", card3, "is succefull.")
            print (B)
        elif (Network == "4"):
            card4= int(input("Type the amount: "))
            print ("Your requested Etisalat recharge of", card4, "is succefull.")
            print (B)
        else:
            print ("exit")               
    else:
        print ("exit")
else:
    print ("For inquiry, contact our customer care agent; 09063892834")
    print ("Thank you for Banking with us.")



