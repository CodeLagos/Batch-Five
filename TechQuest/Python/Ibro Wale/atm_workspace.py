print("IBROTECH BANK PLC ATM")
print("")
print("")
def MY_ATM():
    attempt=0
    try:
        while attempt < 3:
            pin=int(input("PLEASE ENTER YOUR 4 DIGIT PIN: ")) 
            if pin==1234:    
                print("ACCESS GRANTED")
                print("")
                print("")
                print("WELCOME DEAR COSTUMER")
                print("")
                print("")
                balance=100000
                request=input("PLEASE SELECT AN OPTION \n \n(a) WITHDRAWAL \n(b) DEPOSIT \n(c) CHECK BALANCE \n(d) QUICKTELLER \n(e) CHANGE PIN \n(f) EXIT\n")
                if (request=="a") or (request=="A"):
                    account=input("PLEASE SELECT AN ACCOUNT TYPE \n(a) SAVINGS \n(b) CURRENT \n(c) CREDIT\n")
                    if (account=="a") or (account=="A"):
                        amount=int(input("Select from the options to withdraw: \n(1) 1000 \n(2) 5000 \n(3) 10000 \n(4) 20000 \n(5) OTHERS\n"))
                        if (amount == 1):
                            change=balance-1000
                            print("")
                            print("")
                            if amount>balance:
                                print("INSUFFICIENT FUND")
                            elif amount<=balance:
                                print("TAKE YOUR CASH")
                                print ("your balance is =",change)
                                print("")
                                print("THANK YOU")
                        elif (amount==2):
                            change=balance-5000
                            print("")
                            print("")
                            if amount>balance:
                                print("INSUFFICIENT FUND")
                            elif amount<=balance:
                                print("TAKE YOUR CASH")
                                print ("your balance is =",change)
                                print("")
                                print("THANK YOU")
                        elif (amount==3):
                            change=balance-10000
                            print("")
                            print("")
                            if amount>balance:
                                print("INSUFFICIENT FUND")
                            elif amount<=balance:
                                print("TAKE YOUR CASH")
                                print ("your balance is =",change)
                                print("")
                                print("THANK YOU")
                        elif (amount==4):
                            change=balance-20000
                            print("")
                            print("")
                            if amount>balance:
                                print("INSUFFICIENT FUND")
                            elif amount<=balance:
                                print("TAKE YOUR CASH")
                                print ("your balance is =",change)
                                print("")
                                print("THANK YOU")
                        elif (amount==5):
                            change=balance-amount
                            print("")
                            print("")
                            am=int(input("PLEASE ENTER THE THE AMOUNT YOU WANT TO WITHDRAW: "))
                            change=balance-am
                            if am>balance:
                                print("INSUFFICIENT FUND")
                            elif am<=balance:
                                print("TAKE YOUR CASH")
                                print ("your balance is =",change)
                                print("")
                                print("THANK YOU")
                        else:
                            print("please select amount")

                    elif (account=="b") or (account=="B"):
                        amount=int(input("Enter the Amount you want to withdraw: "))
                        change=balance-amount
                        print("")
                        print("")
                        if amount>balance:
                            print("INSUFFICIENT FUND")
                        elif amount<=balance:
                            print("TAKE YOUR CASH")
                            print ("your balance is =",change)
                            print("")
                            print("THANK YOU")
                        else:
                            print("please enter amount")
                

                    elif account=="c":
                        amount=int(input("Enter the Amount you want to withdraw: "))
                        change=balance-amount
                        print("")
                        print("")
                        if amount>balance:
                            print("INSUFFICIENT FUND")
                        elif amount<=balance:
                            print("TAKE YOUR CASH")
                            print ("your balance is =",change)
                            print("")
                            print("THANK YOU")
                        else:
                            print("please enter amount")
                    else:
                        print("PLEASE SELECT AN ACCOUNT TYPE AND TRY AGAIN")
                    anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                    if (anotherTransaction == "a") or (anotherTransaction == "A"):
                        return MY_ATM()
                    else:
                        print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")
                        exit()

                elif (request=="b") or (request=="B"):
                        account=input("PLEASE SELECT AN ACCOUNT TYPE \n(a) SAVINGS \n(b) CURRENT \n(c) CREDIT\n")
                        if (account=="a")or (account=="A"):
                            deposit=int(input("Enter the Amount you want to Deposit ="))
                            result=balance+deposit
                            print("")
                            print("")
                            print("Your money Has been saved succesfully and your balance now is =",result)
                            print("")
                            print("THANK YOU")
                            
                        elif (account=="b") or (account=="B"):
                            deposit=int(input("Enter the Amount you want to deposit ="))
                            change=balance+deposit
                            print("")
                            print("")
                            print("TAKE YOUR CASH")
                            print("your balance is =",change)
                            print("")
                            print("THANK YOU")
                            
                        elif (account=="c") or (account=="C"):
                            deposit=int(input("Enter the Amount you want to deposit ="))
                            change=balance+deposit
                            print("")
                            print("")
                            print("TAKE YOUR CASH")
                            print ("your balance is =",change)
                            print("")
                            print("THANK YOU")
                        else:

                            print("PLEASE SELECT AN ACCOUNT TYPE AND TRY AGAIN")
                        anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                        if (anotherTransaction == "a") or (anotherTransaction == "A"):
                            return MY_ATM()
                        else:
                            print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")
                            exit()
                            
                            
                elif (request=="c") or (request=="C"):
                        account=input("PLEASE SELECT AN ACCOUNT TYPE \n(a) SAVINGS \n(b) CURRENT \n(c) CREDIT\n")
                        if (account=="a") or (account=="A"):
                            print("YOUR BALANCE IS =",balance)
                            print("")
                            print("THANK YOU")
                        if (account=="b") or (account=="B"):
                            print("YOUR BALANCE IS =",balance)
                            print("")
                            print("THANK YOU")
                        if (account=="c") or (account=="C"):
                            print("YOUR BALANCE IS =",balance)
                            print("")
                            print("THANK YOU")
                        else:
                            print("PLEASE SELECT AN ACCOUNT TYPE AND TRY AGAIN")
                        anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                        if (anotherTransaction == "a") or (anotherTransaction == "A"):
                            return MY_ATM()
                        else:
                            print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")
                            exit()
                            
                            
                elif (request=="d") or (request=="D"):
                        teller=input("PLEASE SELECT FROM THE UNERLISTED OPTIONS \n \n(a) AIRTIME RECHARGE \n \n(b) BANK TRANSFER \n \n(c) PAY BILLS\n")
                        if (teller=="a") or (teller=="A"):
                            name=input("SELECT THE LINE YOU WISH TO RECHARGE \n(a) AIRTEL \n(b) MTN \n(c) GLO \n(d) ETISALAT\n")
                            if (name=="a") or (name=="A"):
                                amount=int(input("PLEASE ENTER THE AMOUNT YOU WANT TO RECHARGE: "))
                                print("")
                                phone=input("PLEASE ENTER THE PHONE NUMBER YOU WANT TO RECHARGE: ")
                                leftover=balance-amount
                                while(len(phone))==11:
                                            break
                                            print("")
                                else:
                                    print("")
                                    print("INVALID PHONE NUMBER")
                                    print("")
                                    anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                                    if (anotherTransaction == "a") or (anotherTransaction == "A"):
                                                return MY_ATM()
                                    else:
                                        print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")
                                        exit()
                                print("")
                                print("NOTIFICATION WILL BE SENT TO YOU SHORTLY")
                                print("")
                                print("")
                                print ("your balance is =",leftover)
                                print("")
                                print("PLEASE TAKE YOUR CARD")
                                print("")
                                print("THANK YOU")
                                
                            elif (name=="b") or (name=="B"):
                                amount=int(input("PLEASE ENTER THE AMOUNT YOU WANT TO RECHARGE: "))
                                print("")
                                phone=input("PLEASE ENTER THE PHONE NUMBER YOU WANT TO RECHARGE: ")
                                leftover=balance-amount
                                while(len(phone))==11:
                                    break
                                    print("")
                                else:
                                    print("")
                                    print("INVALID PHONE NUMBER")
                                    print("")
                                    anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                                    if (anotherTransaction == "a") or (anotherTransaction == "A"):
                                        return MY_ATM()
                                    else:
                                        print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")
                                        exit()

                                print("")
                                print("NOTIFICATION WILL BE SENT TO YOU SHORTLY")
                                print("")
                                print("")
                                print ("your balance is =",leftover)
                                print("")
                                print("THANK YOU")
                                
                            elif (name=="c") or (name=="C"):
                                amount=int(input("PLEASE ENTER THE AMOUNT YOU WANT TO RECHARGE: "))
                                print("")
                                phone=input("PLEASE ENTER THE PHONE NUMBER YOU WANT TO RECHARGE: ")
                                leftover=balance-amount
                                while(len(phone))==11:
                                    break
                                    print("")
                                else:
                                    print("")
                                    print("INVALID PHONE NUMBER")
                                    print("")
                                    anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                                    if (anotherTransaction == "a") or (anotherTransaction == "A"):
                                        return MY_ATM()
                                    else:
                                        print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")
                                        exit()

                                print("")
                                print("NOTIFICATION WILL BE SENT TO YOU SHORTLY")
                                print("")
                                print("")
                                print ("your balance is =",leftover)
                                print("")
                                print("THANK YOU")
                                
                            elif (name=="d") or (name=="D"):
                                amount=int(input("PLEASE ENTER THE AMOUNT YOU WANT TO RECHARGE: "))
                                print("")
                                phone=input("PLEASE ENTER THE PHONE NUMBER YOU WANT TO RECHARGE: ")
                                leftover=balance-amount
                                print("")
                                print("NOTIFICATION WILL BE SENT TO YOU SHORTLY")
                                print("")
                                print("")
                                print ("your balance is =",leftover)
                                print("")
                                print("THANK YOU")
                                
                        
                        if (teller=="b") or (teller=="B"):
                                    transfer=input("SELECT THE BANK YOU WISH TO TRANFER TO \n \n(a) ACCESS BANK \n \n(b) DIAMOND BANK \n \n(c) FIRST BANK \n \n(d) JAIZ BANK \n \n(e) FCMB BANK \n \n(f) AFRI BANK \n \n(g) PP BANK \n \n(h) HABIB BANK \n \n(i) UNION BANK \n \n(j) GT BANK \n \n(k) POLARIS BANK \n \n(l) STERLING BANK \n \n(m) ECO BANK \n \n(n) UBA BANK \n \n(o) WEMA BANK \n \n(p) ZENITH BANK\n")
                                    if (transfer=="a"or"b"or"c"or"d"or"e"or"e"or"f"or"g"or"h"or"i"or"j"or"k"or"l"or"m"or"n"or"o"or"p")or (transfer=="A"or"B"or"C"or"D"or"E"or"G"or"F"or"G"or"H"or"I"or"J"or"K"or"L"or"M"or"N"or"O"or"P"):
                                        print("")
                                        account=input("PLEASE SELECT AN ACCOUNT TYPE \n(a) SAVINGS \n(b) CURRENT \n(c) CREDIT\n")
                                        if (account=="a" or "A")or(account=="b" or "B")or(account=="c" or "C"):
                                            types=input("WHAT IS THE DESTINATION ACCOUNT TYPE \n(a) SAVINGS \n(b) CURRENT \n(c) CREDIT\n")
                                            if(types=="a" or "A")or(types=="b" or "B")or(types=="c" or "C"):
                                                names=input("PLEASE ENTER THE ACCOUNT NUMBER YOU WISH TO TRANSFER TO: ")
                                                while(len(names))==10:
                                                    break
                                                    print("")
                                                else:
                                                    print("")
                                                    print("INVALID ACCOUNT NUMBER")
                                                    print("")
                                                    anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                                                    if (anotherTransaction == "a") or (anotherTransaction == "A"):
                                                        return MY_ATM()
                                                    else:
                                                        print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")
                                                        exit()
                                                    
                                                Num=input("PLEASE ENTER YOUR PHONE NUMBER: ")
                                                while(len(Num))==11:
                                                    break
                                                    print("")
                                                else:
                                                    print("")
                                                    print("INVALID PHONE NUMBER")
                                                    print("")
                                                    anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                                                    if (anotherTransaction == "a") or (anotherTransaction == "A"):
                                                        return MY_ATM()
                                                    else:
                                                        print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")
                                                        exit()
                                                print("")
                                                amounts=int(input("PLEASE ENTER THE AMOUNT: "))
                                                print("")
                                                print("PLEASE CONFIRM YOUR DETAILS")
                                                print("")
                                                print("ACCOUNT NUMBER: ",names)
                                                print("PHONE NUMBER: ",Num)
                                                print("AMOUNT: " ,amounts)
                                                print("")
                                                cont=input("DO YOU WISH TO CONTINUE \n(a) YES \n(b) NO\n")
                                                print("")
                                                newBalance=balance-amounts
                                                if (cont=="a")or(cont=="A"):
                                                            
                                                    print("")
                                                    print("TRANSACTION SUCCESFULL")
                                                    print("")
                                                            
                                                    print("YOUR BALANCE IS",newBalance)
                                                    print("")
                                                    print("THANK YOU")
                                                else:
                                                    print("TRANSACTION CANCELLED")
                                                    print("")
                                                    return(MY_ATM())
                                                
                                            else:
                                                print("PLEASE SELECT AN OPTION")
                                        else:
                                            print("PLEASE SELECT AN OPTION")
                                    else:
                                        print("PLEASE SELECT AN OPTION")
                                        
                        if (teller=="c") or (teller=="C"):
                                    bills=input("SELECT THE BILL YOU WANT TO PAY \n(a) PHCN \n(b) WATER BILL \n(c) FIRS \n(d) DSTV \n(e) GOTV\n")
                                    if (bills=="a") or (bills=="A"):
                                        print("")
                                        number=input("PLEASE ENTER YOUR METER NUMBER: ")
                                        while(len(number))==10:
                                            break
                                            print("")
                                        else:
                                            print("")
                                            print("INVALID METER NUMBER")
                                            print("")
                                            anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                                            if (anotherTransaction == "a") or (anotherTransaction == "A"):
                                                return MY_ATM()
                                            else:
                                                print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")
                                                exit()
                                        name=input("PLEASE ENTER YOUR SURNAME: ")
                                        price=input("PLEASE ENTER THE AMOUNT: ")
                                        print("PLEASE CONFIRM YOUR DETAILS: ")
                                        print("")
                                        print("METER NUMBER: ",number)
                                        print("SURNAME: ",name)
                                        print("AMOUNT:" ,price)
                                        print("")
                                        cont=input("DO YOU WISH TO CONTINUE \n(a) YES \n(b) NO\n")
                                        print("")
                                        if (cont=="a") or (cont=="A"):
                                            print("TRANSACTION SUCESSFULL")
                                        else:
                                            print("TRANSACTION CANCELLED")
                                            print("")
                                            return(MY_ATM())
                                    elif (bills=="b") or (bills=="B"):
                                        meter=input("PLEASE ENTER YOUR METER NUMBER: ")
                                        while(len(meter))==10:
                                            break
                                            print("")
                                        else:
                                            print("")
                                            print("INVALID METER NUMBER")
                                            print("")
                                            anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                                            if (anotherTransaction == "a") or (anotherTransaction == "A"):
                                                return MY_ATM()
                                            else:
                                                print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")
                                                exit()
                                        name=input("PLEASE ENTER YOUR SURNAME: ")
                                        price=input("PLEASE ENTER THE AMOUNT: ")
                                        print("PLEASE CONFIRM YOUR DETAILS: ")
                                        print("")
                                        print("METER NUMBER: ",meter)
                                        print("SURNAME: ",name)
                                        print("AMOUNT:", price)
                                        print("")
                                        cont=input("DO YOU WISH TO CONTINUE \n(a) YES \n(b) NO\n")
                                        print("")
                                        if (cont=="a") or (cont=="A"):
                                            print("TRANSACTION SUCESSFULL")
                                        else:
                                            print("TRANSACTION CANCELLED")
                                            print("")
                                            return(MY_ATM())
                                    elif(bills=="c") or (bills=="C"):
                                        reg=input("PLEASE ENTER YOUR REGISTRATION NUMBER: ")
                                        while(len(reg))==10:
                                            break
                                            print("")
                                        else:
                                            print("")
                                            print("INVALID REGISTRATION NUMBER")
                                            print("")
                                            anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                                            if (anotherTransaction == "a") or (anotherTransaction == "A"):
                                                return MY_ATM()
                                            else:
                                                print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")
                                                exit()
                                        name=input("PLEASE ENTER YOUR SURNAME: ")
                                        price=input("PLEASE ENTER THE AMOUNT: ")
                                        print("PLEASE CONFIRM YOUR DETAILS: ")
                                        print("")
                                        print("REGISTRATION NUMBER: ",reg)
                                        print("SURNAME: ",name)
                                        print("AMOUNT:" ,price)
                                        print("")
                                        cont=input("DO YOU WISH TO CONTINUE \n(a) YES \n(b) NO\n")
                                        print("")
                                        if (cont=="a") or (cont=="A"):
                                            print("TRANSACTION SUCESSFULL")
                                        else:
                                            print("TRANSACTION CANCELLED")
                                            print("")
                                            return(MY_ATM())
                                    elif(bills=="d" or "D")or(bills=="e" or "E"):
                                        card=input("PLEASE ENTER YOUR CARD NUMBER: ")
                                        while(len(card))==10:
                                            break
                                            print("")
                                        else:
                                            print("")
                                            print("INVALID CARD NUMBER")
                                            print("")
                                            anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                                            if (anotherTransaction == "a") or (anotherTransaction == "A"):
                                                return MY_ATM()
                                            else:
                                                print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")
                                                exit()
                                        name=input("PLEASE ENTER YOUR SURNAME: ")
                                        price=input("PLEASE ENTER THE AMOUNT: ")
                                        print("PLEASE CONFIRM YOUR DETAILS: ")
                                        print("")
                                        print("CARD NUMBER: ",card)
                                        print("SURNAME: ",name)
                                        print("AMOUNT:" ,price)
                                        print("")
                                        cont=input("DO YOU WISH TO CONTINUE \n(a) YES \n(b) NO\n")
                                        print("")
                                        if (cont=="a") or (cont=="A"):
                                            print("TRANSACTION SUCESSFULL")
                                        else:
                                            print("TRANSACTION CANCELLED")
                                            print("")
                                            return(ATM())
                                    else:
                                        print("PLEASE SELECT AN OPTION")
                                        print("")
                                        return (MY_ATM())
                        anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                        if (anotherTransaction == "a") or (anotherTransaction == "A"):
                            return MY_ATM()
                        else:
                            print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")
                            exit()
                            
                    
                elif (request=="e") or (request=="E"):
                    oldPin =int(input("PLEASE ENTER YOUR OLD PIN: "))
                    while (oldPin==pin):
                        break
                    else:
                        print("WRONG OLD PIN ")
                        anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                        if (anotherTransaction == "a") or (anotherTransaction == "A"):
                            return MY_ATM()
                        else:
                            print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")
                            exit()
                    newPin =input("PLEASE ENTER YOUR NEW PIN: ")
                    confirmPin =input("PLEASE ENTER RE-ENTER YOUR NEW PIN: ")
                    if newPin == confirmPin:
                        pin=confirmPin
                        print("PIN CHANGED SUCESSFULLY")
                        print("THANK YOU")
                        anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                        if (anotherTransaction == "a") or (anotherTransaction == "A"):
                            return MY_ATM()
                        else:
                            print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")
                            exit()
                    else:
                        print("NEW PIN NOT SAME AS RE-ENTER PIN")
                        anotherTransaction=input("DO YOU WANT TO PERFORM ANOTHER TRANSACTION \n(a) YES \n(b) NO\n")
                        if (anotherTransaction == "a") or (anotherTransaction == "A"):
                            return MY_ATM()
                        else:
                            print("THANK YOU FOR BANKING WITH US! HAVE A NICE DAY")
                            exit()

                        
                elif(request=="f") or (request=="F"):
                    print("PLEASE TAKE YOUR CARD")
                    print("THANK YOU FOR BANKING WITH US")
                    exit()
                else:
                    print("please select an option")
    
                
            else:
                print("")
                print("INCORRECT PIN! DEAR CUSTOMER, PLEASE CALM DOWN AND GIVE A THOUGHT ABOUT YOUR PIN THEN RE-ENTER IT")
                print("")
                attempt+= 1
        if attempt == 3:
            print("CARD BLOCKED AND RETAINED")
    except KeyboardInterrupt:
        print("closing good bye")
       
print(MY_ATM())
