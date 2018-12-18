print("Name: Nnamdi Ikediuwa, Email: nnamdibility@gmail.com, Phone: 08067119097")
print("codelagos batch 5")
print("In a rural environment where there is no bank, neither ATM Machines. And you would have to depend on business owners how use POS, in place of an ATM. Most of")
print("these agents may not operate during weekends. So this program was written to stand between the ATM and the POS. The project is called EasyPay. This system")
print("would be afflicted to other banks, and would have its owned Easypay card, and serve two major functions: Withdrawal, and Pay in. but you can also check you")
print("balance.  Advantages: Unlike the ATM machine which charges you N65, after every third withdrawal, this doesn’t, it would only charge you N200 at the end of")
print("every month. If you want to withdraw use a POS in such place you get charged N200, but with Easypay you don’t get charged. So if you just have N500 in your")
print("account and that’s the only cash you have, with Easypay, you can get your money. Unlike the POS where you would have to pay extra N200.")


print('Welcome to EasyPay Mini ATM')
restart=('Y')
chances = 3
balance = 67000
while chances >= 0:
    pin = int(input('Please Enter You 4 Digit Pin: '))
    if pin == (1234):
        print('You entered you pin Correctly\n')
        while restart not in ('n','NO','no','N'):
            print('Please Press 1 For Your Balance\n')
            print('Please Press 2 To Make a Withdrawl\n')
            print('Please Press 3 To Pay in\n')
            print('Please Press 4 To Cancel\n')
            option = int(input('What Would you like to choose?'))
            if option == 1:
                print('Your Balance is N',balance,'\n')
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How Much Would you like to withdraw? \nN500/N1000/N2000/N5000/N10000:'))
                if withdrawl in [500, 1000, 2000, 5000, 10000]:
                    balance = balance - withdrawl
                    print ('\nYour Balance is now N',balance)
                    restart = input('Would You you like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawl != [500, 1000, 2000, 5000, 1000]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Desired amount:'))    

            elif option == 3:
                Pay_in = float(input('How Much Would You Like To Pay In? '))
                balance = balance + Pay_in
                print ('\nYour Balance is now N',balance)
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 4:
                print('Please wait whilst your card is Returned...\n')
                print('Thank you for you service')
                break
            else:
                print('Please Enter a correct number. \n')
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break
