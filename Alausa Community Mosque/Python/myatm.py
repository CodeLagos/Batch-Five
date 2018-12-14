print("Access Bank")
print("Please Insert your Card")
print("Please enter your 4-digit pin")

password=(input(""))
user=20000
strl2=len(password)
if (strl2>4) or (strl2<4):
    print( "Invalid Pin, please re-insert your Card")
else:
    print("Welcome Praise")
    print("Enter a number for the option in the menu")
    menu=int(input("1. WITHDRAWAL\n2. TRANSFER\n3. ENQUIRY\n4. CHANGE PIN\n"))
    if(menu==1):
        print("Withdrawal Selected")
        print("Please select an ACCOUNT TYPE")
        types=int(input("1. Current\n2. Saving\n"))
        if(types!=1)and(types!=2):
            print("Invalid Selection")    
        else:
            print("Please select an AMOUNT")
            Withdrawal=int(input("1. #500\n2. #1000\n3. #2000\n4. #5000\n5. #10000\n6. #15000\n7. #20000\n8. OTHERS\n"))
            if(Withdrawal==1):
                if(500>user):
                    print("Insuficient Fund")
                else:
                    print("Please wait...")
                    print("Please take your cash")
                    sum1=user-500
                    print("Your new Balance is",sum1)
                
            elif(Withdrawal==2):
                if(1000>user):
                    print("Insuficient Fund")
                else:
                    print("Please wait...")
                    print("Please take your cash")
                    sum2=user-1000
                    print("Your new Balance is",sum2)
               
            elif(Withdrawal==3):
                if(2000>user):
                    print("Insuficient Fund")
                else:
                    print("Please wait...")
                    print("Please take your cash")
                    sum3=user-2000
                    print("Your new Balance is",sum3)
               
            elif(Withdrawal==4):
                if(5000>user):
                    print("Insuficient Fund")
                else:
                    print("Please wait...")
                    print("Please take your cash")
                    sum4=user-5000
                    print("Your new Balance is",sum4)
               
            elif(Withdrawal==5):
                if(10000>user):
                    print("Insuficient Fund")
                else:
                    print("Please wait...")
                    print("Please take your cash")
                    sum5=user-10000
                    print("Your new Balance is",sum5)
              
            elif(Withdrawal==6):
                if(15000>user):
                    print("Insuficient Fund")
                else:
                    print("Please wait...")
                    print("Please take your cash")
                    sum6=user-15000
                    print("Your new Balance is",sum6)
               
            elif(Withdrawal==7):
                if(20000>user):
                    print("Insuficient Fund")
                else:
                    print("Please wait...")
                    print("Please take your cash")
                    sum7=user-20000
                    print("Your new Balance is",sum7)
                    
            elif(Withdrawal==8):
               a=int(input("Enter an Amount\n"))
               if(a>user):
                    print("Insuficient Fund")
               else:
                    print("Please wait...")
                    print("Please take your cash")
                    sum8=user-a
                    print("Your new Balance is",sum8)
    elif(menu==2):
       print("TRANSFER Selected")
       account=input("Enter Recipient Account number\n")
       strl2=len(account)
       if (strl2>10) or (strl2<10):
           print( "Invalid Account number, please re-insert your Card")
       else:
           print("")
           acctype=int(input("Select an ACCOUNT TYPE\n1. CURRENT\n2. SAVINGS\n"))
           if (acctype!=1)and(acctype!=2):
               print("Invalid Type")
           else:
               bank=int(input("RECIPIENT's BANK\n1. ACCESS BANK\n2. GTBANK\n3. UBA\n4. FIRSTBANK\n5. FIDELITY\n6. SKYE BANK\n7. DIAMOND BANK\n8. ECO BANK\n"))
               if (bank!=1)and(bank!=2)and(bank!=3)and(bank!=4)and(bank!=5)and(bank!=6)and(bank!=7)and(bank!=8):
                   print("Invalid Bank Selection, please re-insert your Card")
               else:
                   print("Enter Amount")
                   amount=int(input(""))
                   Done=user-amount
                   print(amount, "has been TRANSFERED to", account)
                   print(amount,"has been deducted from your ACCOUNT","and your new ACCOUNT BALANCE is",Done)
                   bg=int(input("Would you like to make another transfer\n1. YES\n2. NO\n"))
                   
                   
    elif(menu==3):
        print("ENQUIRY selected")
        Balance=int(input("Select an ACCOUNT TYPE\n1. CURRENT\n2. SAVINGS\n"))
        if (Balance!=1) and(Balance!=2):
            print("Invalid Selection")
        else:
            print("Your ACCOUNT BALANCE is",user)
    elif(menu==4):
        print("CHANGE PIN selected")
        K=int(input("Select an ACCOUNT TYPE\n1. CURRENT\n2. SAVINGS\n"))
        if (K!=1) and(K!=2):
            print("Invalid Selection")
        else:
            p=input("Enter NEW PIN\n")
            p1=input("Confirm NEW PIN\n")
            strl2=len(p1)
            p=p1
            if (strl2>4) or (strl2<4):
                print( "Invalid Pin, please re-insert your Card")
            else:
                print("This is your old PIN",password)
                print("Your PIN has been successfully changed to",p1)
            print("Thank you for banking we us")
