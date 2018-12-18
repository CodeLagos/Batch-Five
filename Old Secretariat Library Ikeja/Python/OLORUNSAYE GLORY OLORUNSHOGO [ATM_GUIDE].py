#This code is developed during the CodeLagos programme by OLORUNSAYE GLORY OLORUNSHOGO

#Please modify to suite your application. Welcome to ATM_Guide

import time
print('OLORUNSAYE GLORY OLORUNSHOGO')
print('olorunsayeglory@gmail.com')
print('old secretariat ikeja, lagos.')

print('****************************************************')
print('             WELCOME TO YOUR BANK')
print('****************************************************')
print('----------------------------------------------------')
print('    INSERT YOUR CARD AND PRESS ENTER TO GET STARTED')
print('----------------------------------------------------')

#Get user ATM PIN and saved it into variable enterPassword

enterPassword = int(input("Enter your FOUR DIGIT PASSWORD and Press enter to continue: "))

password = 1234#Equating the value of the input as password
cash = 20000 
if password == enterPassword:
    time.sleep(2)
    print("1. WITHDRAW\n2. CHANGE PIN\n3. TRANSFER\n4. PAY BILLS")
    operation=int(input("Enter the value of desired  operation e.g 1 for making withdrawer: "))
    if operation == 1:
        print("1. 2000\n2. 3000\n3. 5000\n4.10000\n5.20000\n6.other")
        withdraw =int(input("Enter the value of desired  operation e.g 6 for any other specific amount : "))
        if withdraw==1:
                print("Please wait while your transaction is processing")
                time.sleep(2)
                print("Please take your cash")
                exit()
        if withdraw==2:
                print("Please wait while your transaction is processing")
                time.sleep(2)
                print("Please take your cash")
                exit()
        if withdraw==3:
                print("Please wait while your transaction is processing")
                time.sleep(2)
                print("Please take your cash")
                exit()
        if withdraw==4:
                print("Please wait while your transaction is processing")
                time.sleep(2)
                print("Please take your cash")
                exit()
        if withdraw==6:
                print("Please wait while your transaction is processing")
                time.sleep(2)
                print("Please take your cash")
                exit()
        if withdraw==6:
                sleep.time(1)
                print("Enter desired amount in terms of 1000 e.g 4000")
                otherWithdraw=int(input())
        if otherWithdraw > cash:
                        sleep.time(1)
                        print("Insufficient funds")
                        exit()
        else:
                        print("Please wait while your transaction is processing")
                        time.sleep(2)
                        print("Please take your cash")
                        time.sleep(2)
                        exit()

    elif operation == 2:
        print("Enter a new pin")
        newPin=int(input())
        print("Confirm new pin")
        confirmPin=int(input())
        if newPin == confirmPin:
                print("PIN changed successfully")
                exit()
        else:
                print("PIN do not MATCH")
                exit()

    elif operation == 3:
        print("\nSelect the bank you want to transfer to\n1. GTB\n2.Access Bank\n3.Fidelity Bank\n4.Wema Bank\n5.Sterling Bank\n6.First Bank")
        bank = int(input("Enter: "))
        if bank == 1 or bank == 2 or bank == 3 or bank == 4 or bank == 5 or bank == 6:
                    
                    print("Enter account number you wish to transfer to: ")
                    a = int(input(""))
                    maximum=10
        if a < maximum and a >= 11:
                        print("invalid account number.")
                        exit()
        else:
                        print("Enter amount: ")
                        transfer=int(input())
        if transfer > cash:
                                  print("Insufficient amount.")
                                  exit()
       # else:
       #                           print("Please wait while your transaction is processing")
       #                           time.sleep(3)
       #                           print("TRANSACTION SUCCESSFUL, {} has been transferred to {}".format(transfer,accountNumber)
    elif operation == 4:
                                print("Select the utility bill you wish to pay for\n1. DSTV\n2.GOTV\n3.STARTIME\n4.PHCN\n5.LAWMA")
                                payBills=int(input())
    if payBills == 1 or payBills == 2 or payBills == 3 or payBills == 4 or payBills == 5:
            
            print("FOLLOW THE INSTRUCTION PRINTED OUT ON THE SCREEN FOR GUIDE")
else:
    print("Incorrect PIN.. TRY AGAIN !")
    exit()
