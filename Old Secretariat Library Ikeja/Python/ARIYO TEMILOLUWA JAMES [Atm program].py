#This code is developed during codelagos programm by ARIYO TEMILOLUWA

#please modify to suite your application. Welcome to ATM_Guide

import time
print("ARIYO TEMILOLUWA JAMES")
print("temijames8@gmail.com")
print("old secretariat ikeja")
print("Atm programm")
print("welcome to bank world")
print("swipe your card here:")
atm_pin=1234
transcation=("balance enquiry", "withdrawal money", "deposit", "change your pin", "transfer of money", "quit")
"""so here we are storing all your transcation"""
pin=int(input("enter your pin to proceed:"))
if pin==1234:
 print("choose your transcation: \n 1.balance enquiry\n 2.withdrawal money\n 3. change of pin")
 print("4. deposit")
 print("5. transfer of money")
 print("6. quit")
else:
  trans=input("transcation")
if(trans =="balance enquiry"):
    acct_bal=input("do you want check your acct bal? yes or no")
    if acct_bal=="yes":
         print("here is ur acct. balance!thank for using bankworld")
    elif trans=="withdrawal money":
        amount=input("enter your amount to proceed")
    else:
        print("thanks for using bankworld")
    if amount>0:
            print("collect your cashthanks for  using bankworld")
    else:
            print("enter valid amount to proceed")
    if trans=="deposit":
            deposit=input("enter your amount deposit")
    if deposit>0:
            print("your deposit has been succefully deposit, thank for using bankworld")
    else:
            print("enter valid amount to proceed")
    if trans=="change of pin":
        if trans>=0:
            print("your pin has been succefully chang,thank for using bankworld")
    else:
             print("enter valid pin to proceed")
    if trans=="transfer money":
            transfer_money=input("enter your amount to transfer:")
    if transfer_money>o:
                print("your money has been transfered! thank for using bankworld")
    else:
             print("enter valid amount to proceed")
    if trans=="quiz":
            quiz_1=input("press yes to quit")
    if quiz_1=="yes":
                print("quit")
    else:
              print("choose any transcation please:")
   

