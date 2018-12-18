#Display the purpose of the program
print ("\nWelcome to First Bank")

#Display the instructions to the user
print ("Please insert your card with the gold plated side facing up")
print ("Please, make sure that nobody is watching closely while you enter your pin")
print ("\nThis ATM Dispense N1000 notes only")

#Prompt the user to enter their name for welcome message with + name
name = input("Please, enter your Name: ")


def verify_pin(pin):
    if pin == 1234:
        return True
    else:
        return False

def log_in():
    tries = 0
    while tries < 4:
        pin = int(input("Please, Enter Your 4 Digit Pin: "))
        if verify_pin(pin):
            print("\nWelcome To First Bank", name)
            return True
        else:
            print("Invalid Pin")
            tries += 1
    print("To Many Attempts, Can not Log You In")
    return False

def another_t():
    answer = input("Would you like to do another transaction? \n(1)Yes \n(2)No \n ")
    if answer == '1':
        menu()
        return True
    else:
        print("Thank You For Using This Service")
        
        
 

def menu():
    if log_in():
        while True:
            Quick_Cash = input("Do you want to make a quick withdraw of 10,000 from this ATM? \n(1)Yes \n(2)No\n")
            if (Quick_Cash == '1'):
                while True:
                    rcpt = input("Would you like a receipt for this transaction? \n(1)Yes \n(2)No \n ")
                    if rcpt == '1':
                        break
                    elif rcpt == '2':
                        break
                    else:
                        print ("Invalid Selection")
                        continue
        
                print("Please take your cash!")
                break
        
            elif (Quick_Cash == '2'):
                break
            
            else:
                print("Invalid Input")
                continue
            
        menu = input("\nWhat would you like me to help you with? \n(1)Cash Withdrawal \n(2)Cash Deposit \n(3)Transfer \n(4)Balance Inquiry \n(5)Recharge or Top Up Your Line \n(6)Change Pin\n")
        if(menu == '1'):
            input("\n(1)Savings \n(2)Current \n ")
            maxi = 40000
            mini = 1000
            withdrawal = int(input("How much would you like to withdraw? \n(1)1000 \n(2)2000 \n(3)5000 \n(4)10000 \n(5)20000 \n(6)Other\n"))
            if (withdrawal == 6):
                while True:
                    other = int(input("Please, enter amount you want to withdraw: "))
                    if (other > maxi):
                        print("Invalid Amount, You can Only Withdraw a Maximum of 40000 per Transaction")
                        continue
                    elif (other < mini):
                        print("Invalid Amount, You can Only Withdraw a Minimum of 1000 per Transaction")
                        continue
                    else:
                        break
                while True:
                    rcpt = input("Would you like a receipt for this transaction? \n(1)Yes \n(2)No \n ")
                    if rcpt == '1':
                        break
                    elif rcpt == '2':
                        break
                    else:
                        print ("Invalid Selection")
                        continue
                print("Please take your cash!")
            else:
                while True:
                    rcpt = input("Would you like a receipt for this transaction? \n(1)Yes \n(2)No \n ")
                    if rcpt == '1':
                        break
                    elif rcpt == '2':
                        break
                    else:
                        print ("Invalid Selection")
                        continue
                print("Please take your cash!")
            another_t()

        elif(menu == '2'):
            print("Sorry, cash deposit is not available at this moment ")
            r_dr = input("I Can Direct you to other ATMs Nearby\nDo You Want Direction To Other ATMs Nearby? \n(1)Yes \n(2)No\n")
            if r_dr == '1':
                print("Still On Development, Will be Available on The Next Update")
            another_t()

        elif(menu == '3'):
            while True:
                Transfer = int(input("\n(1)Bank Transfer \n(2)QuickTeller \n "))
                trans = 1
                tran = 2
                if(Transfer == trans):
                    break
                elif(Transfer == tran):
                    break
                else:
                    print ('Invalid Input')
                    continue
            Banks = input("\nPlease, select your Bank: \n(1)Access \n(2)Diamond \n(3)Eco \n(4)Fidelity \n(5)First Bank \n(6)Guarrantee Trust \n(7)Heritage \n(8)Polarris \n(9)Stanbic IBTC \n(10)Standered Chartered \n(10)United Bank of Africa \n(12)Union \n(13)Wema \n(14)Zennith \n")

            if(Banks == "5"):
                print("Not more than 9 digit numbers,")
                while True:
                    acc_no = int(input("Enter Account number: "))
                    if (len(str(acc_no)) == 9):
                        break
                    else:
                        print("Receivers Account Number Must Be a 9 Digit Number Only")
                        continue
                while True:
                    r_name = input("Enter name of Recipient: ")
                    if(len(r_name) > 3):
                        break
                    else:
                        print("Please, Type name of the fund receiver correctly")
                        continue
                while True:
                    Amount = int(input("Enter Amount to transfer: "))
                    maxi_am = 250000
                    if Amount > maxi_am:
                        print("You Can Transfer A Maximum Amount of 250,000 Per Transaction")
                        continue
                    else:
                        break
                while True:
                    print("\nTransfer", Amount, "To", r_name)
                    conf = input("(1)Proceed \n(2)Cancel \n")
                    if conf == '1':
                        while True:
                            rcpt = input("Would you like a receipt for this transaction? \n(1)Yes \n(2)No \n ")
                            if rcpt == '1':
                                break
                            elif rcpt == '2':
                                break
                            else:
                                print ("Invalid Selection")
                                continue
                        print("Transfer Successful")
                        break
                    else:
                        break

            else:
                print("Not more than 9 digit numbers,")
                while True:
                    acc = int(input("Enter Account number: "))
                    if (len(str(acc)) == 9):
                        break
                    else:
                        print("Receivers Account Number Must Be a 9 Digit Number Only")
                        continue
                while True:
                    rc_name = input("Enter name of Recipient: ")
                    if(len(rc_name) > 3):
                        break
                    else:
                        print("Please, Type name of the fund receiver correctly")
                        continue
                while True:
                    tr_amount = int(input("Enter Amount to transfer: "))
                    maxi_am = 250000
                    if tr_amount > maxi_am:
                        print("You Can Transfer A Maximum Amount of 250,000 Per Transaction")
                        continue
                    else:
                        break
                while True:
                    print("\nTransfer",tr_amount, "to", rc_name, "a service fee of N100 will be deducted from your account:")
                    confirm = input("(1)Proceed \n(2)Cancel \n")
                    if confirm == '1':
                        while True:
                            rcpt = input("Would you like a receipt for this transaction? \n(1)Yes \n(2)No \n ")
                            if rcpt == '1':
                                break
                            elif rcpt == '2':
                                break
                            else:
                                print ("Invalid Selection")
                                continue
                        print("Transfer Successful")
                        break
                    elif confirm == '2':
                        print("Thank You For Using This Service!")
                        break
                    else:
                        print("Invalid Input")
                        continue
            another_t()

        elif(menu == '4'):
            while True:
                rcpt = input("Would you like a receipt for this transaction? \n(1)Yes \n(2)No \n ")
                if rcpt == '1':
                    break
                elif rcpt == '2':
                    break
                else:
                    print ("Invalid Selection")
                    continue
            import random
            print("Hello! Your Balance is",random.randrange(1, 11000000))
            another_t()

        elif(menu == '5'):
            while True:
                network = input("Select Your Network \n(1)9Mobile \n(2)Airtel Top Up \n(3)Glo Top Up \n(4)MTN VTU \n ")
                if network in ('1', '2', '3', '4'):
                    number = input("Please, Enter phone number: ")
                    if (len(str(number)) == 11):
                        while True:
                            r_am = float(input("Please, Enter Amount: "))
                            r_mx = 20000
                            r_mn = 100
                            if (r_am > r_mx):
                                print("You can only recharge a maximum of 20000 worth of airtime per Transaction")
                                continue
                            elif (r_am < r_mn):
                                print("You can only recharge a minimum of 100 worth of airtime per Transaction")
                                continue
                            else:
                                print('Transaction Successful')
                                break
                        break

                    else:
                        print("Invalid Phone Number")
                        continue
                else:
                    A_O = input("Invalid Option!\nWe only provide services to networks in the options\nWill you like to inform us about a new network provider?\n(1)Yes\n(2)No\n")
                    if (A_O == '1'):
                        print("\nPlease, Do Send us Mail at Prosper.sopuruchi@gmail.com\nThank You For Helping Us Improve Our Service To Serve You More Better\n")
                        break
                    elif (A_O == '2'):
                        print("Your Feedback Helps Us to Improve Our Service To Serve You More Better, Please Send Us Mail at Prosper.sopuruchi@gmail.com For More Feedback")
                        break
                    else:
                        print("Thank You For Using This Service")
                        break
            another_t()

        elif(menu == '6'):
            pin1 = 1234
            tries = 0
            while tries < 3:
                old_pin = int(input("Please, Enter Old Pin: "))
                new1 = int(input("Please, Enter New Pin: "))
                new2 = int(input("Please, Enter New Pin Again: "))
                if(old_pin == pin1):
                    if(new1 == new2):
                        print("Pin Changed Successfully")
                        break
                    else:
                        print("New Pins did not Match")
                        tries +=1
                        continue
                
                else:
                    print("Incorrect Old Pin")
                    tries +=1
                    continue
            else:
                print("You have Exceed the number of attempts, Please contact your Bank if you have forgotten your old pin or contact prosper.sopuruchi@gmail.com if you think this is error. \nGood Bye!")
            another_t()

        else:
            print("Invalid input. Good Bye!")

menu()



'''
Code written by Prosper Sopuruchi, One of CodeLagos Out Of School Batch 5 Student.

Bugs Still Plenty ('.') if you happen to find any and don't have Snipper, }:-)
Chat me on Whatsapp @ 09031288147 or send a mail to me at prosper.sopuruchi@gmail.com
I have this bad habbit of not taking :-) calls from numbers not saved on this line 09031288147.
I owe alot of peeps so I dont know who might call with another phone number to
remind me that December is here so as to pay them. lols!!

Or you can call me on 09065745787

'''
