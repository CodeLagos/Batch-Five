print ('Welcome to First Bank of Nigeria Plc. ATM\n')
restart = ('Yes')
chances = 3
balance = 100000.0
while chances >= 0:
    pin = int(input ('Please Enter You 4 Digit Pin: \n\n\n>>>'))
    if pin == (1234):
        print()
        while restart not in ('NO','no','No'):
            print ('>>>Press 1 For  Balance:\n')
            print ('>>>Press 2  For Withdrawl:\n')
            print ('>>>Press 3 For Transfer:\n')
            print ('>>>Press 4 For Quick Teller:\n')
            print ('>>>Press 5 For Deposite:\n')
            option = int(input ('Please select an Option:\n\n'))
            if option == 1:
                print ('Your Balance is',balance,'\n')
                restart = input ('Would you like to go back ? (Yes or No)''\n\n')
                if restart in ('NO','no','No'):
                    print ('Take your Card:\n\n')
                    print ('Thank you for Banking with us:\n')
                    break

            elif option == 2:
                option2 = ('2')
                withdrawl = float(input ('How Much Would you like to withdraw ? \n''\n>>>1000\n\n>>>2000\n\n>>>5000\n\n>>>10000\n\n>>>15000\n\n>>>20000\n\n>>>Others\n\n '))
                if withdrawl in [500, 1000, 2000, 3000, 4000, 5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000,16000,17000,18000,19000,20000,25000,30000,35000,40000]:
                    balance = balance - withdrawl
                    print ('Take Your Cash:\n\n')
                    print ('Transaction Successful:\n\n')
                    restart = input ('Would You you like to go back ? (Yes or No)\n\n')
                    if restart in ('NO','no','No'):
                        print ('Take your Card:\n\n')
                        print ('Thank You for Banking wsith us:\n')
                        break
                    elif withdrawl != [500, 1000, 2000, 3000, 4000, 5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000,16000,17000,18000,19000,20000,25000,30000,35000,40000]:
                        restart = ('yes')
                    elif withdrawl == 1:
                            withdrawl = float(input ('Please Enter Desired amount:'))
                            break
            elif option == 3:
                option=('3')
                print ('>>>Press 1 For First Bank:\n')
                print ('>>>Press 2 For Eco Bank:\n')
                print ('>>>Press 3 For UBA  Bank:\n')
                print ('>>>Press 4 For Sterling Bank:\n')
                print ('>>>Press 5 For Diamond  Bank:\n')
                print ('>>>Press 6 For  Access Bank:\n')
                print ('>>>Press 7 For Wema Bank:\n')
                print ('>>>Press 8 For Union Bank:\n')
                print ('>>>Press 9 For FCMB Bank:\n')
                print ('>>>Press 10 For GTB Bank:\n')
                print ('>>>Press 11 For Fidelity Bank:\n')
                print ('>>>Press 12 For Key Stone Bank:\n')
                destination_bank = float(input('Please Select an Option:\n\n'))
                destination_acount = float(input('Please Enter Destination Account Number:\n\n'))
                Transfer = float(input('How Much Would You Like To Transfer ?\n\n'))
                balance = balance - Transfer
                print ('Transfer Successful:\n\n')
                restart = input('Would You you like to go back ? (Yes or No)\n\n')
                if restart in ('NO','no','No'):
                            print('Take your Card:\n\n')
                            print ('Thank you for Banking with us:\n')
                            break
                        

            elif option == 4:
                            print ('>>>Press 1 for MTN:\n')
                            print ('>>>Press 2 for 9MOBILE:\n')
                            print ('>>>Press 3 for AIRTEL:\n')
                            print ('>>>Press 4 for GLO:\n')
                            network = (input ('Please select an Option:\n'))
                            phone_number = (input ('Please Enter Phone Number:\n\n'))
                            amount = float(input('Please Enter Amount:\n\n'))
                            balance = balance - amount
                            print ('Recharg Succesful:\n\n')
                            restart = input ('Would You you like to go back ? (Yes or No)\n\n')
                            if restart in ('NO','no','No'):
                                print ('Take your Card:\n\n')
                                print ('Thank you for Banking with us:\n')
                                break

            elif option == 5:
                option == ('5')
                print ('>>>Press 1 For First Bank:\n')
                print ('>>>Press 2 For Eco Bank:\n')
                print ('>>>Press 3 For UBA  Bank:\n')
                print ('>>>Press 4 For Sterling Bank:\n')
                print ('>>>Press 5 For Diamond  Bank:\n')
                print ('>>>Press 6 For  Access Bank:\n')
                print ('>>>Press 7 for Wema Bank:\n')
                print ('>>>Press 8 for Union Bank:\n')
                print ('>>>Press 9 for FCMB Bank:\n')
                print ('>>>Press 10 for GTB Bank:\n')
                print ('>>>Press 11 for Fidelity Bank:\n')
                print ('>>>Press 12 for Key Stone Bank:\n')
                deposit_bank = float (input('Please select an Option:\n\n'))
                deposit_acount = float(input('Enter Acount Number:\n\n'))
                deposit = float(input('How Much Whould You Like To Deposit ?\n\n'))
                balance = balance + deposit
                print ('Deposite Successful:\n')
                restart = input ('Would you like to go back ? (Yes or No)\n\n')
                if restart in ('NO', 'no', 'No'):
                    print ('Take your Card:\n\n')
                    print ('Thank you for Banking with us:\n')
                    break

                
          
