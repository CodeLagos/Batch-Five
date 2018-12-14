#-*-coding:utf8;-*-
#qpy:3
#qpy:console
#BALOGUN LUKMAN PROJECT #CODE LAGOS #2018
print("This is console module")
user_name = input("Please Enter Your Name: ")
print ("Insert Your Card To Perform Any Transaction")
print ("Please Input Your 4 Digit Pin")
pin=int(input("Your 4 digit pin: "))
if pin ==1010:
       print ("Welcome To Stels Bank", user_name)
else:
        print("Wrong Pin And Operation Cancelled")
transaction=input("What Transaction Do You Wish To Perform : (a) Withdrawal (b) Cash transfer (c) Buy Airtime (d) Cancel transaction:      ")
if transaction.lower()== 'a' :
    withdrawal=input("Type Of Withdrawal: (a) Cash Withdrawal (b) Credit withdrawal:   ")
    if withdrawal.lower()=='a':
        Cash_withdrawal=input("Account Type: (a) Current Account (b) Savings Account: ")
        if Cash_withdrawal.lower()=='a':
           print("Only Three Type Of Cash Withdrawal Available")
           current_account=input ("Chose The Amount You Wish To Withdraw:  \n (a) 10000 \n  (b) 20000 (c) 50000: ")
           if current_account.lower()=='a' or 'b' or'c':
             print("Transaction In Progress")
             print ("Take Your Cash")
             print("Transaction Ended")
        elif Cash_withdrawal.lower()=='b':
            print("Only Four Types Of Transactions Available")
            savings_account=input ("Select The Amount You Wish To Withdraw:  \n(a) 1000 \n  (b)2000 \n  (c) 5000 \n  (d) 10000:")
            if savings_account.lower()=='a' or 'b' or 'c' or 'd' :
               print("Transaction In Progress")
               print ("Take Your Cash")
               print("Transaction Ended")
    elif withdrawal.lower()=='b':
           print("This Service Is Not Currently Available")
           print ("Try Again Later")
   
elif transaction.lower()=='b' :
       Cash_transfer=int(input("Receiver Account Number: "))
       if Cash_transfer==1010101010:
           confirm=input("Name :Mr Oluwole \n Acct number: 1010101010: \n(a)Do You Wish To Proceed \n(b)Cancel Transfer: ")
           if confirm.lower()=='a':
               amount=(input("Please Input The Amount You Wish To Transfer: "))
               if amount=='10000' or'20000' or'30000'or'40000'or'50000':
                         print("Transfer In Progress")
                         print("Transaction In Progress")
                         print ("Transaction Completed")
           else:
                  print("Transaction Cancelled")
elif transaction.lower()=='c':
       Buy_Airtime=(input("Amount Of Recharge Card (a) 100 (b) 500 (c) 1000 (d) Others : "))
       if Buy_Airtime=='a' :
            print("Transaction In Progress")
            print("Transaction Completed")
       elif Buy_Airtime=='b':
              print("Transaction In Progress")
              print("Transaction Completed")
       elif Buy_Airtime=='c':
              print("Transaction In Progress")
              print("Transaction Completed")
       else:
               print("Only 2000 Airtime Available")
               Others=(input("Type The Amount Of Airtime You Wish To Recharge: "))
               if Others=='2000':
                   print ("Transaction In Progress")
               
