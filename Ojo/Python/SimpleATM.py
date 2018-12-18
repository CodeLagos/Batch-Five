try:
    print('THIS IS A BASIC SIMULATION OF AN ATM\n\n')

    #ATM PROCESS
    print('    PYTHON BANK ATM \n     ')
    int(input('Insert Card (Number)...\n'))

    print("""
            1)        Savings account
            2)        Current account

    """)

    account_type = input('Select your account type: \n')
    if (account_type == '1'):
        print('You are running a Savings account')
    else:
        print('You are running a Current account\n')
            
    #display the user choice
    language = int(input('\nWELCOME! please Select your language \n1)English \n2)Italian \n3)German \n'))
    if (language == 1):
        print('Your language is English')
    elif (language == 2):
        print('Your language is Italian')
    elif (language == 3):
        print('Your language is German')   
    else:
        print('please selct your language!!')
        
    pin = int(input('\nEnter your four digit PIN...\n'))


    def trans():
        balance = 5000
            
        print("""
        1)        Withdraw
        2)        Deposit
        3)        Transfer Funds
        4)        Balance
        5)        Quit


        """)
        transaction = input('Select a Transaction: \n')
            
        if transaction == '1':
            print('your current balance is #{}'.format(balance))        
            #ask the user to Choose the amount they want to withdraw
            withdraw = int(input('how much would you like withdraw?... \n'))
            if withdraw <= balance:
                currentbalance =  balance - withdraw
                print('You have withdrawn #',withdraw, 'from your Python bank account \nyour current balance is', currentbalance)
            elif Withdraw > balance:
                print("Not enough funds in account")
            else:
                print("No withdrawal made")
                print(currentbalance)
            
            
            receipt = print("""
                1)        YES
                2)        NO

                """)
            receipt = input('Do you want a receipt? \n')
            if receipt == '1':
                print('receipt printed!')

            print("""
                    --NEW TRANSACTION--
                
            1)        YES
            2)        NO
            """)    
            x = input('\ndo you want to perform another Transaction?... \n')
            
            if x == '1':
                return trans()
            else:
               print('Please remove you card... \nTHANK YOU FOR BANKING WITH US, GOODBYE! ')
                  
                              
        elif transaction == '2':
            print('your current balance is #',balance)        
            #ask the user to Choose the amount they want to deposit
            deposit = int(input('\nhow much would you like to deposit?... \n'))
            print('processing....\n')
            currentbalance2 =  balance + deposit
            balance = currentbalance2
            print('you have deposited #',deposit,'your new account balance is #',currentbalance2)

            print("""
                --NEW TRANSACTION--
                
            1)        YES
            2)        NO
            """)
            y = input('\ndo you want to perform another Transaction?... \n')
            
            if y == '1':
                return trans()
            else:
               print('Please remove you card... \nTHANK YOU FOR BANKING WITH US, GOODBYE! ')
               
        elif transaction == '3':
            print('your current balance is #',balance)
            #ask the user to Choose the amount they want to transfer 
            transfer = int(input('\nhow much would you like to transfer?... \n'))
            name = input('Enter Account name... \n')
            int(input('Enter receipient Account number... \n'))
            
            def newpin():
                pin2 = int(input('Enter your four digit PIN again...\n'))
                if pin2 != pin:
                    print('FALSE! Please try again.\nYour PIN is',pin)
                    return newpin()
                else: 
                    print('processing....\n')
                    currentbalance =  balance - transfer
                    print('you have transfered #',transfer,'your new account balance is #',currentbalance)
                    print("""
                        --NEW TRANSACTION--
                        
                    1)        YES
                    2)        NO
                    """)
                    y = input('\ndo you want to perform another Transaction?... \n')
                    
                    if y == '1':
                        return trans()
                    else:
                       print('Please remove you card... \nTHANK YOU FOR BANKING WITH US, GOODBYE! ')
                       

            print("""
                    --CHARGES--
            {Note: you will be charged N100 for each transfer you want to make}\n
            1)        Proceed
            2)        Back
            """) 
            charge = input('Click {1} to proceed if you accept the N100 Charge...\n')
            if charge == '1':
                return newpin()
            else:
                print("""
                    --NEW TRANSACTION--
                    
                1)        YES
                2)        NO
                """) 
                z = input('\ndo you want to perform another Transaction?... \n')
                
                if z == '1':
                    return trans()
                else:
                   print('Please remove you card... \nTHANK YOU FOR BANKING WITH US, GOODBYE! ')
               
        elif transaction == '4':
            print('your current balance is #{}'.format(balance))

            print("""\n
                --NEW TRANSACTION--
                    
            1)        YES
            2)        NO
            """)
            
            x = input('\nDo you want to perform another Transaction?... \n')
            if x == '1':
               return trans()
            else:
               print('Please remove you card... \nTHANK YOU FOR BANKING WITH US, GOODBYE! ')
                   
        else:
            print('Please remove you card... \nGOODBYE! ')
            
    trans()
except:
       print('\nINVALID INPUT!!')


    

#Write a basic simulation of an ATM which
#displays the operations a user would perform
#and works the user through the operations

           #ATM PROCESS
#Step 1 : Insert Card
#WELCOME ROSELYN EMEKA
#Step 2 : Select your language
#Step 3 : Enter your PIN
#Step 4 : Transaction Type - Withdraw Money, Deposit Money, Balance Enquiry, Bill Pay, Transfer
#Step 5 : Select your account type : SAVING ACCOUNT - CURRENT ACCOUNT
#Step 6 : enter amount - 500-1000-5000-10,000-15,000-20,000
#Step 7 : DO YOU WANT A RECEIPT - YES/NO, Press yes to proof that you withdrew money and check the balance
#Step 8 : DO YOU WANT TO PERFORM ANOTHER TRANSACTION? - YES/NO -EJECT
#Step 9 : THANK YOU FOR BANKING WITH US!

#Follow the instructions below to transfer money to other accounts using ATM.
#STEP2: Enter your ATM pin and press proceed.
#STEP3: Press Quick Teller.
#STEP4: Press inter bank Transfers.
#STEP5: select funding Account Type {Be it savings or current account}.
#STEP6: select Receiving Account Type {Be it savings or current account}.
#STEP7: select Recipient’s Bank.
#STEP8: Enter Account Number you wish to transfer to.
#STEP9: Enter Amount and Click proceed.
#STEP10: Click proceed if you accept the N100 Charge{Note: you will be charged N100 for each transfer you want to make}.
#STEP11: Confirm details and click proceed if okay.
#STEP12: You’ll get the massage ” Transaction completed ” please check the receipt for your reference number. Note: where there is no receipt, check your sms alert for the reference number.
#STEP13: Remove your card from the ATM…







