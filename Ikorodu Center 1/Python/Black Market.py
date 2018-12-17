print("CodeLagos 5.0 Python Class (Afternoon) Presentation")
print('')
print("Welcome to Joseph Danel Naira 2 Dollar Converter -- A USSD Approach a.k.a Aboki Calculator")
print('')
print("This platform helps you to convert Naira 2 Dollar & Vice Versa without you stressing yourself using USSD approach \n")
while True:
    menu = int(input("Choose your option \n1) Naira to Dollar \n2) Dollar to Naira \n3) Exit \n"))
    if menu == 1:
        n2d = float(input('Please Enter The Amount You Would Want To Convert to Dollar: #'))
        koko = n2d*0.0028
        print('Please wait...')
        print('#', n2d, 'is equivalent to', '$', round(koko, 2))
        print('')
        sub_menu = int(input("Do you want to \n1) Go to the Previous Menu \n2) Terminate \n"))
        if sub_menu == 2:
            print('Loading...')
            print('')
            print('Thank for choosing Joseph Daniel Naira 2 Dollar USSD Converter')
            break
    if menu == 2:
        d2n = float(input('Please Enter The Amount You Would Want To Convert to Naira: $'))
        kko = d2n*362.92
        print('Please wait...')
        print('$', d2n, 'is equivalent to', '#', round(kko, 2))
        print('')
        sub_menu = int(input("Do you want to \n1) Go to Previous Menu \n2) Terminate \n"))
        if menu == 2:
            print('Loading...')
            print('')
            print('Thank you for choosing Joseph Daniel Naira 2 Dollar USSD Converter')
            break
    elif menu == 3:
        print('Loading...')
        print('Thank you for choosing Joseph Daniel Naira 2 Dollar USSD Converter')
        quit()
