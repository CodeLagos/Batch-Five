#print out the purpose of the program
print("This program is to render customer service to Digital Marketers")

#welcome message to customers
print("welcome to kiffy glam! how may we serve you?")




#ask customer to select an option
options = int(input("please select an option\n1) list of available goods\n2) price of goods\n3) quantity at the moment\n4) view our nearest shop to your location\n"))

#print the customer's option
if(options == 1):
    print("(1)Bags")
    print("(2)waist trimmers")
    print("(3)shoes")
    print("(4)Bridal accessories")
elif(options == 2):
    
    print("Bags - 50,000 and above, shoes - 2500/6000, jewelries - 50000/150,000,waist trimmers - 10,000, Bridal accessories - 100,000 and above")

elif(options == 3):
  print("10 different types of bags,50 pieces from size 38 to 41, M and D Jewelries,9 pieces of waist trimmers from medium to large size,10 brands on bridal accessories")

elif(options == 4):
    print("iyana paja, lasu road,akesan bus stop,muritala muhammed airport")

else:
    print("invalid option")

#ask customers if they want to place an order
customer = int(input("will you like to place an order now? \n(1)yes \n(2) no\n"))

if(customer == 1):
    name=input("please enter your name ")
    address =input("please enter your address")
    Name_item  = input("please enter name of goods ")
    Phone_number  =int(input("please enter your phone"))
    number_item  = int(input("please enter the quntity of goods"))
    print("Thank you " ,name ,"of address ", address,"you order", number_item, "of", Name_item," your  order has been placed. It will get to you in the next 24/48hours")

    
else:
    print("Thanks for checking by!")
