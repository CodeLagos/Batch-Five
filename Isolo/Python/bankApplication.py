print("Name:\tSam Ubong Ita")
print("Email:\tsamubong96@gmail.com")
print("Phone NO.:\t07051585211\n")
print("This program works as a bank application.")
print("Batch 5, Code Lagos\n")
import random
Customers = {}
class Bank:
    def __init__(self, name,balance):
       self.name=name
       self.balance=balance
       self.account_no =random.randint(1000000000,9999999999)
       self.pin = input("Please input a four digit Pin:\n")
    def checkBalance(self):
        return self.balance
    def deposit(self,amount):
        self.balance+=amount
    def Withdrawal(self,amount):
        self.balance-=amount
    def AccountDetails(self):
        return self.name,self.balance,self.account_no
    def changeName(self,name):
        self.name=name
def CreateAccount():
    name = input("Enter Account Name:\n")
    balance = float(input("Enter Initial Deposit:\n"))
    c1 = Bank(name,balance)
    Customers[c1.account_no] = c1
    print("Account Created Successfully!\nYour Account Number is {}".format(c1.account_no))
def checkBalance(id):
    pin = input("Please Enter Your Pin:\n")
    if(pin==Customers[id].pin):
        return Customers[id].balance
    else:
        print("Incorrect Pin")
def Withdraw(id,amount):
    pin = input("Please Enter Your Pin:\n")
    if(pin==Customers[id].pin):
        Customers[id].Withdraw(amount)
    else:
        print("Incorrect Pin")
def Deposit(id,amount):
    pin = input("Please Enter Your Pin:\n")
    if(pin==Customers[id].pin):
        return Customers[id].Deposit(amount)
    else:
        print("Incorrect Pin")
def AccountDetails(id):
    pin = input("Please Enter Your Pin:\n")
    if(pin==Customers[id].pin):
        return Customers[id].AccountDetails()
    else:
        print("Incorrect Pin")
def changeName(id,name):
    pin = input("Please Enter Your Pin:\n")
    if(pin==Customers[id].pin):
        return Customers[id].changeName(name)
    else:
        print("Incorrect Pin")

while(True):   
    print("Welcome to Klapton Bank\n")
    print("Please Choose a response from the list below;\n")
    print("1. \tCreate Account\n2. \tCheck Balance\n3. \tDeposit\n4. \tWithdrawal\n5. \tAccount Details\n6. \tChange Account Name\n")
    response = input("Enter Response:\n")
    if(response=='1'):
        CreateAccount()
    elif(response=='2'):
        ID = int(input("Enter Your Account Number:\n"))
        print(checkBalance(ID))
    elif(response=='3'):
        ID = int(input("Enter Your Account Number:\n"))
        amount = float(input("Enter the amount for deposit:\n"))
        Deposit(ID,amount)
        print("Amount Deposited Succesfully!")
    elif(response=='4'):
        ID = int(input("Enter Your Account Number:\n"))
        amount = float(input("Enter the amount for withdrawal:\n"))
        Withdraw(ID,amount)
        print("Withdrawal Successful!")
    elif(response=='5'):
        ID = int(input("Enter Your Account Number:\n"))
        print(AccountDetails(ID))
    elif(response=='6'):
        ID = int(input("Enter Your Account Number:\n"))
        name =input("Enter your new Account Name:\n")
        changeName(ID,name)
        print("Account Name changed Succesfully!")
    else:
        print("Invalid Response")
    ext=input("Do you want to carry out another operation?.\tYes/No: ")
    if(ext=='No'):
        print("Thank You for Banking with Us.\n")
        break
