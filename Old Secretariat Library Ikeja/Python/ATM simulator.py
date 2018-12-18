#Write a Basic Simulation of an Atm which displays the operations a user would perform and works the user through the operation
#This programs simulate a First Bank ATM machine it asks a user for their pin to withdraw money from their bank account with a current balance of 5000 naira and print's a reciept for them on shell interface
#inputs card
print("Welcome Back Patrick\n")
currentamt=5000
minbal=500
minimumwithdrawal = 500
currentpin=2000
useracct="savings"
currentacct="savings"
try:
 pincheck=int(input("Welcome,\nPlease Enter Your Secret Number"))
except ValueError:
  print("Please Enter a Valid Integer Pin")
account=input("Select Your account Type \n CURRENT\nSAVINGS")
try:
 amount=int(input("Select the amount you want to Withdraw \n 500 \n 1000 \n 2000 \n 5000 \n 10000 \n 20000 \n"))
except ValueError:
   print("Invalid Command")
balance=currentamt-amount
if pincheck!=currentpin:
    print("Incorrect Pin")
    #checks if pin is correct
elif account.lower()==useracct:
    print("You do not own a Current Account Sorry")
    #checks if user acct is savings or not
elif amount>currentamt:
    print("Insufficent Funds")
    #checks if amount been withdrawn by user is  not greater than current cash in bank
elif amount < minimumwithdrawal:
    print("Minimum amount to be withdrawn from this ATM is 500")
#checks if amount been withdrawn by user is  not lesser than 500
elif balance < minbal:
    print("Insufficient Funds")
    #disturbs user from withdrawing an amount less than 500 naira  bank  reserve anyway
else:
    print("Transaction Sucessful \n You can now take your reciept from the Printer\n")
    balance=currentamt-amount
    
    reciept=print("Debit Alert \n DESC 2018 | 22 | 11 \n ATM 6 FIRST BANK \n Oba Akinjobi Area Old Secteriat Ikeja,\n Ikeja Lagos \n amount:",amount,"\nBal\n",balance)
   

