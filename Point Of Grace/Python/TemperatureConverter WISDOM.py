#Wisdom Abraham
print( "" )
print("THIS IS A TEMPERATURE CONVERTER.")
print( "" )
print("Please choose your temperature scale.")
hello = input("Please Select The Desired Option: \n(A)Celsius to Fahrenheit \n(B)Fahrenheit to Celsius \n(C)Kelvin to Celsius \n(D)Celsius to Kelvin \n(E)Fahrenheit to Kelvin \n(F)Kelvin to Fahrenheit \n")
if(hello.lower() == "a"):
    Celsius = float(input("Enter the value of the Celsius: "))
    Fahrenheit = 9 / 5 * Celsius + 32
    Fahrenheit = round(Fahrenheit, 2)
    print("Temperature: ", Celsius, "Celsius =", Fahrenheit, "F")
    
elif(hello.lower() == "b"):
    Fahrenheit = float(input("Enter the value of the Fahrenheit: "))
    Celsius = (Fahrenheit - 32) * 5 / 9
    Celsius = round(Celsius, 2)
    print("Temperature: ", Fahrenheit, "Fahrenheit =", Celsius, "C")

elif(hello.lower() == "c"):
     Kelvin = float(input("Enter the value of the Kelvin: "))
     Celsius =  Kelvin - 273
     print("Temperature: ", Kelvin, "Kelvin =", Celsius, "C")

elif(hello.lower() == "d"):
     Celsius = float(input("Enter the value of the Celsius:"))
     Kelvin = Celsius + 273
     print("Temperature: ",Celsius, "Celsius =", Kelvin, "K")

elif(hello.lower() == "e"):
     Fahrenheit = float(input("Enter the value of the Fahrenheit: "))
     Kelvin = (Fahrenheit + 459.67) * 5/9
     Kelvin = round(Kelvin,2)
     print("Temperature: ",Fahrenheit, "Fahrenheit =", Kelvin, "K")

else:
     Kelvin = float(input("Enter the value of Kelvin: "))
     Fahrenheit = 9 / 5 * Kelvin - 459.67
     Fahrenheit = round(Fahrenheit, 2)
     print("Temperature: ", Kelvin, "Kelvin =", Fahrenheit, "F")
