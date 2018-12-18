#!/usr/bin/python

import getpass

import string

import time


#Print Developer details




print("ADEGBITE AYOADE ABEL")

print("tripleaceme@gmail.com")

print("OLD SECRETARIAT LIBRARY, IKEJA CODE LAGOS CENTER")


# creating a lists of users, their PINs and bank statements


users = ["user1", "user2", "user3"]

pins = ["1234", "2222", "3333"]

amounts = [10000, 20000, 30000]

count = 0


# while loop checks existance of the enterd username

while True:
    user = input("\nEnter usename: ")
	
    user = user.lower()
	
    if user in users:
        if user == users[0]:
            n = 0
    elif user == users[1]:
            n = 1
    else:
	    n = 2
	    break
print("INVALID USERNAME")


# comparing pin

while count < 3:
    pin = str(getpass.getpass("PLEASE ENTER PIN: "))

	
    if pin.isdigit():
		
       if user == "user1":
			
           if pin == pins[0]:
				
              break
			
else:
				
   count += 1

				
print("INVALID PIN")

		
if user == "user2":
    if pin == pins[1]:
       break

else:
				
     count += 1
				
				
print("INVALID PIN")

		
if user == "user3":
			
   if pin == pins[2]:
				
      break
			
else:
				
 count += 1
	
	

		
 print("PIN CONSISTS OF 4 DIGITS")

		
 count += 1
	

# in case of a valid pin continuing, or exiting

if count == 3:
    print("3 UNSUCCESFUL PIN ATTEMPTS, EXITING")
	
    print("!!!!!YOUR CARD HAS BEEN LOCKED!!!!!")
	
exit()



print("LOGIN SUCCESFUL, CONTINUE")

time.sleep(2)

print()	

print(users[n], "WELCOME TO ACE BANK ATM")


# Main menu

while True:
    response = input("SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \Deposit(D)  \nChange PIN_(P)  \nQuit_______(Q) \n: ").lower()


#valid_responses = ["s", "w", "d", "p", "q"]
	
    response = response.lower()
	
    if response == "s":
				
		
        print(users[n], "YOU HAVE ", amounts[n],"NAIRA ON YOUR ACCOUNT.")

	
    elif response == "w":

		
       cash_out = int(input("ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: "))

       if cash_out%10 != 0:

			
            print("AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 1000 NAIRA NOTES")

		
       elif cash_out > amounts[n]:
			
			
			
            print("YOU HAVE INSUFFICIENT BALANCE")

		
       else:
			
            amounts[n] = amounts[n] - cash_out

			
       print("YOUR NEW BALANCE IS: ", amounts[n], "NAIRA")

	
       if response == "d":

		
         cash_in = int(input("ENTER AMOUNT YOU WANT TO DEPOSIT: "))

		
       if cash_in%10 != 0:
	
			
         print("AMOUNT YOU WANT TO DEPSOIT MUST TO MATCH 10 NAIRA NOTES")
	
		
       else:
			
         amounts[n] = amounts[n] + cash_in
	
			
         print("YOUR NEW BALANCE IS: ", amounts[n], "NAIRA")

	
       if response == "p":

	
          new_pin = str(getpass.getpass("ENTER A NEW PIN: "))

		
       if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
                        
			
          new_ppin = str(getpass.getpass("CONFIRM NEW PIN: "))

			
       if new_ppin != new_pin:

				
          print("PIN MISMATCH")

			
       else:
				
          pins[n] = new_pin
				
       print("NEW PIN SAVED")
		
else:

			
     print("NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN")
			
			
	
     if response == "q":
		
        exit()
		
	
     else:
                
		
        print("RESPONSE NOT VALID")
		
		
