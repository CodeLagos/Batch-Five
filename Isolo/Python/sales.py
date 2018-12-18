print("Nwakpakpa, Queen Salome")
print("Queensally18@yahoo.com")
print("07038864145")
name=input("enter ur name")
print(name,"you are welcome to","WUNNABUYRESTURANT how may we serve you?")
price=0
print(" list of food available,\n S/N\t food \t prices \n 1.\trice\t #1800\n 2.\tbeans\t #1500 \n 3.\tsemo\t #2000\n 4.\tmoi moi\t #600\n")
option=input("choose your option between 1 to 4: ")
if(option=="1"):
    print(name,"you are ordering for rice")
    print("Amount==#1800")
    price1=price+1800
    option=input("would you love to make more order?")
elif(option=="2"):
    print(name,"you are ordering for beans")
    print("Amount==#1500")
    price1=price+1500
    option=input("would you love to make more order?")
elif(option=="3"):
    print(name,"you are ordering for semo")
    print("Amount==#2000")
    price1=price+2000
    option=input("would you love to make more order?")
elif(option=="4"):
    print(name,"you are ordering for moi moi")
    print("Amount==#600")
    price1=price+600
    option=input("would you love to make more order?")
if(option=="yes"):
    print("choose your option")
    input("list of drinks,\ncoke \nfanta\nholandia\nmalt\npepsi\n")
    if(option=="fanta"):
        print("#500")
        price2=price1+500
    elif(option=="pepsi"):
        print("#600")
        price2=price1+600
    elif(option=="malt"):
        print("#350")
        price2=price1+350
    elif(option==4,"coke"):
        print("#600")
        price2=price1+600
else:
    print("order not available at the moment")
print("Your bill is " + str(price2) + " thank you for your patronage, merry xmas and prosperous new year")
