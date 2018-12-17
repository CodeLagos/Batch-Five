print ("ADEWUNMI OLUSEYI JAMES PROJECT ON")
print("==================================")
print ("Simple Resturant Management Billing systm Program")
print ("=============================================")
print ("1. African Dishes")
print ("2. Continental Dishes")
print ("3. Cat fish Peppersoup Dishes")
print ("4. Meat peppersoup Dishes")
print ("5. Snacks with drinks")
print ("6. Ordinary Drinks")
print ("7. Quit")
# Get the user’s choice:
menu = input("Please select a Menu number 1-7: ")
# Calculate The Menu Cunsumed by customers:
if menu == "1":
    Eba = float(input("Enter price for Eba with Egusi soup: "))
    Drinks = float(input("Enter price for water/soft drinks: "))
    Vat = (Eba+Drinks)*0.05
    Plate = Eba+Drinks+Vat
    print ("The Plate of food is ",Plate,"Naira VAT Inclusive")   
if menu == "2":
    Rice = float(input("Enter price for fried/jollof rice: "))
    Chicken = float(input("Enter price for Chiken/Beef: "))
    Drinks = float(input("Enter price for water/soft drinks: "))
    Vat = (Rice+Chicken+Drinks)*0.05
    Plate  =Rice+Chicken+Drinks+Vat
    print  ("The Plate of food is",Plate,"Naira VAT Inclusive")
if menu == "3": 
    CatFish = float(input("Enter Price for CatFish Peppasoup: "))
    Drinks = float(input("Enter price for Drinks: "))
    Vat =CatFish+Drinks*0.05 
    Plate = (CatFish+Drinks)+Vat
    print ("The Plate of CatFish Peppasoup is",Plate,"Naira VAT Inclusive")
if menu == "4":
    Meat = float(input("Enter price for Meat Peppasoup: "))
    Drinks = float(input("Enter price for Drinks: "))
    Vat =Meat+Drinks*0.05 
    Plate = (Meat+Drinks)+Vat
    print ("The Plate of Meat Peppasoup is",Plate,"Naira VAT Inclusive")
if menu == "5":
    Snacks = float(input("Enter price for Snaks: "))
    Drinks = float(input("Enter price for Drinks: "))
    Vat =(Snacks+Drinks)*0.05 
    SnacksDrinks = Snacks+Drinks+Vat
    print ("The Snaks/Drinks is",SnacksDrinks,"Naira VAT Inclusive")
if menu == "6":
    Drinks = float(input("Enter price for Drinks: "))
    Vat =Drinks*0.05 
    Drinks =Drinks+Vat
    print ("The Drinks Value is",Drinks,"Naira VAT Inclusive")
if menu == "7":
    exit()
#This is a simple resturant Managment billing system that will process a simple billing calculation

