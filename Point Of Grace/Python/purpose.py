#taofiq abdul azeez
#display the purpose of the program
print ("welcome to the BMI calculator")
#display the instructions to the user
print ("please enter your weight in kilograms and your height in metres")
#prompt the user to enter their weight
weight = float(input("please enter your weight: "))
#prompt the user to enter their height
height = float (input("please enter your height: "))
#calculate the BMI of the user
BMI = weight / (height * height)
#round up the BMI to 1 decimal place 
BMI = round (BMI, 1 )
#display the BMI
print ("your BMI is", BMI)
#evaluate the BMI and give a verdict 
if (BMI<18.5) :
    print ("underweight")
elif ((BMI>18.5) and (BMI<25)) :
    print ("normal")
elif ((BMI>=25) and (BMI<30)):
    print ("overweight")
else:
    print ("obese")  
