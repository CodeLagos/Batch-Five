print ("______WELCOME TO CODELAGOS 2O18 BATCH 5 Project______\n")
print ("__This project belongs to Joshua Ibironke___")
print ("Email: ibironkejoshua@gmail.com\nCenter: Ikeja Old Secretariat Library\n")
print ("            ***********************")
print ("            * S.I UNIT CONVERTER  *")
print ("            ***********************")
print ("\nThis program to convert between various S.I Units\n")

print ("Select which option you want below \na) Meter to Kilometer \nb)Gramme to Kilogramme \nc)Celcius to Farenheit")

option = input("Enter Option here: ")

if option == "a":
    print ("Meter to Kilometer Coversion")
    meter = int(input("Please enter the Meter value: "))
    kilometer = meter / 1000
    print (meter, " meters is equivalent to ", kilometer, " kilometer")

elif option == "b":
    print ("Gramme to Kilogramme Conversion")
    gramme = int(input("Please enter the Gramme Value: "))
    kilogramme =  gramme / 1000
    print (gramme, "gramme is equivalent to ", kilogramme, " kilogramme")

elif option == "c":
    print ("Celcius to Farenheit Calculator")
    celcius = int(input("Please enter the Celsuis value: "))
    fahrenheit = celcius * 1.8
    print (celcius, " degree celcius is equivalent to ", fahrenheit, " fahrenheit")


else:
    print ("Please enter the correct value")
                

