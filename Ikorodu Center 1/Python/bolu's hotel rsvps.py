print("THE MARIOS EXECUTIVE HOTEL")
print("WELCOME TO THE MARIOS MOBILE KITCHEN")
total = 0
while True:
    menu = input("KITCHEN MENU")
    print("*****************************")
    print("CHOOSE FROM OUR WIDE RANGE OF DISHES")
    option = int(input("option 1: EUROPEAN DISHES\noption 2: AFRICAN DISHES\noption 3: NIGERIAN DISHES\noption 4: TODAY'S SPECIAL\n"))
    if option == 1:
        print("ENTER YOUR PREFERRED DISH (#1,500 PER PLATE)")
        option_1 = int(input("EUROPEAN DISHES:\n1. German sausages and cheese     2. Bulgarian beef soup\n3. Yorkshire pudding     4. Swedish Meatballs\n5. Portuguese Chourico and Kale Soup     6. Gyro Meat with Tzatziki Sauce\n7. Chicken Marsala     8. Gravlax with Mustard Sauce\n"))
        plates = int(input("number of plates: "))
        print("YOUR DISH WOULD BE SERVED SHORTLY...")
        total += plates*1500
    elif option == 2:
        print("ENTER YOUR PREFERRED DISH (#800 PER PLATE)")
        option_2 = int(input("AFRICAN DISHES:\n1. Bobotie        2. FUFU\n3. Kachumbari     4. Kitfo(spiced raw beef dish)\n5. Alloco         6. Biltong\n"))
        plates = int(input("number of plates: "))
        print("YOUR DISH WOULD BE SERVED SHORTLY...")
        total += plates*800
    elif option == 3:
        print("ENTER YOUR PREFERRED DISH (#1,200 PER PLATE)")
        option_3 = int(input("NIGERIAN DISHES:\n1. Tuwo Shinkafa     2. Ewa Aganyin\n3. Jollof Rice     4. Amala and Ewedu Soup\n5. Moin-Moin     6. Pounded Yam and Egusi Soup\n7. Adalu     8. Abacha and Ugba\n"))
        plates = int(input("number of plates: "))
        print("YOUR DISH WOULD BE SERVED SHORTLY...")
        total += plates*1200
    elif option == 4:
        option_4 = input("*Chettinad Fish fry (#1,000)")
        plates = int(input("number of plates: "))
        print("YOUR DISH WOULD BE SERVED SHORTLY...")
        total += plates*1000
    restart = input("WOULD YOU LIKE TO RE-ENTER YOUR ORDER?\n")
    if restart in ('yes','YES'):
        print("************************")
    else:
        break
mobile = print("ENTER YOUR LOCATION AND MOBILE NUMBER")
address = input("ADDRESS:")
phone_no = input("MOBILE NUMBER:")
print("YOUR TOTAL IS #",total)
restart = input("WOULD YOU LIKE TO CONTINUE WITH YOUR ORDER?\n")
if restart in ('yes', 'YES'):
    print("THANKS...YOUR ORDER WOULD BE RECEIVED SHORTLY")
else:
    print("THANKS FOR YOUR PATRONAGE...")
print("FOR ANY COMPLAINTS, ENQUIRIES, RECOMMENDATIONS...CALL: +2349087183982")
    
