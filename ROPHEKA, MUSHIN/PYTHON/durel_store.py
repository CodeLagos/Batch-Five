#Author: Oladeji Damilare
#Durel Online Store

import time
print("You Are Welcome To Durel king Online Shopping!!!",time.ctime())
restart = 'yes'
Bag_Rice = 17,000
Palm_oil = 13,000
Groundnut_oil = 15,000
Spaghetti = 6,000
Maggi = 2,000
amount = 0
print("Where Edible Food Stuff Are Sold!!!")
time.sleep(2)
name = input("Please your Name: ")
print('Hello' , name)
while True:
    time.sleep(1)
    print('This are the list of items we can afford to sell!!! ')
    print('Bag of Rice\n''Palm oil\n''Groundnut oil\n''Spaghetti\n''Maggi.\n')
    request = input('What would you like to buy? ')
    if request.lower() == 'bag of rice':
        number = int(input('How many?'))
        bag_rice = 17000
        selling_price = number*bag_rice
        print(selling_price)
        amount = amount + selling_price
        print(amount)
        request = input('will you like to shop more?')
        if request == 'yes':
            continue
        else:
             time.sleep(2)
             print('Your Total Amount Is' , amount)
             print('For more info,you log onto:durelkingfoodstuffENTERPRISE@gmail.com ')
             print('Thank you')
             break
    elif request.lower() == "spaghetti":
        number = int(input('How many cartons?'))
        pack_spaghetti = 6000
        selling_price = number*pack_spaghetti
        print(selling_price)
        amount = amount + selling_price
        print(amount)
        request = input('will you like to shop more?')
        if request == 'yes':
            continue
        else:
             time.sleep(2)
             print('Your Total Amount Is' , amount)
             print('For more info,you log onto:durelkingfoodstuffENTERPRISE@gmail.com ')
             print('Thank you')
             break
    elif request.lower() == "groundnut oil":
        print('We only sell 25 litres')
        number = int(input('so,how many keg of 25 litres will you like to buy?'))
        groundnut_oil = 15000
        selling_price = number*groundnut_oil
        print(selling_price)
        amount = amount + selling_price
        print(amount)
        request = input('will you like to shop more?')
        if request == 'yes':
            continue
        else:
             time.sleep(2)
             print('Your Total Amount Is' , amount)
             print('For more info,you log onto:durelkingfoodstuffENTERPRISE@gmail.com ')
             print('Thank you')
             break
    elif request.lower() == "palm oil":
        print('We only sell 25 litres')
        number = int(input('so,how many keg of 25 litres will you like to buy?'))
        palm_oil = 13000
        selling_price = number*palm_oil
        print(selling_price)
        amount = amount + selling_price
        print(amount)
        request = input('will you like to shop more?')
        if request == 'yes':
            continue
        else:
             time.sleep(2)
             print('Your Total Amount Is' , amount)
             print('For more info,you log onto:durelkingfoodstuffENTERPRISE@gmail.com ')
             print('Thank you')
             break
    elif request.lower() == "maggi":
        print('Every Woman With Maggi Is A STAR')
        number = int(input('so,how many pack?'))
        maggi = 2000
        selling_price = number*maggi
        print(selling_price)
        amount = amount + selling_price
        print(amount)
        request = input('will you like to shop more?')
        if request == 'yes':
            continue
        else:
             time.sleep(2)
             print('Your Total Amount Is' , amount)
             print('For more info,you log onto:durelkingfoodstuffENTERPRISE@gmail.com ')
             print('Thank you')
             break
            
        

        

