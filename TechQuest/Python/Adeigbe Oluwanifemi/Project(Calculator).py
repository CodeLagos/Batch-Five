#Adeigbe Oluwanifemi
#Tech Quest Batch 5

#calculator
import math
print("This is a Simple Calculator")
#function to add two numbers
def add(x,y):
 return x + y
#function to subtract two numbers
def subtract(x,y):
 return x - y
#function to multiply two numbers
def multiply(x,y):
 return x * y
#function to divide two numbers
def divide(x,y):
 return x / y
#function to square a number
def index(x,y):
 return x**y
#function to find the square root of a number
def sqrt():
    return sqrt(x)
 
print("select operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.index")
print("6.square root")
print("7.sine")
print("8.cosine")
print("9.tangent")
print("10.logarithm")

#take users choice
choice=input("Enter choice(1/2/3/4/5/6/7/8/9/10):")


if choice=='1':
    first=float(input("Enter first number:"))
    second=float(input("Enter second number:"))
    print(first,"+",second,"=", add (first,second))

elif choice=='2':
    first=float(input("Enter first number:"))
    second=float(input("Enter second number:"))
    print(first,"-",second,"=", subtract (first,second))

elif choice=='3':
    first=float(input("Enter first number:"))
    second=float(input("Enter second number:"))
    print(first,"*",second,"=", multiply (first,second))

elif choice=='4':
    first=float(input("Enter first number:"))
    second=float(input("Enter second number:"))
    print(first,"/",second,"=", divide (first,second))

elif choice=='5':
    first=float(input("Enter first number:"))
    second=float(input("Enter second number:"))
    print(first,"**",second,"=", index (first,second))

elif choice == '6':
    first = float(input("Enter the number:-"))
    if first >= 0:
        print(u"\u221A", first,"=",math.sqrt(first))
    else:
        print('Syntax Error')

elif choice == '7':
    print('\u03B8 is measured in radians')
    first = float(input("Enter the value of \u03B8:-"))
    sine = (math.sin(math.radians(first)))
    print("sin",(first),"=",round(sine, 4))

elif choice == '8':
    print('\u03B8 is measured in radians')
    first = float(input("Enter the value of \u03B8:-"))
    cosine = (math.cos(math.radians(first)))
    print("cos",(first),"=",round(cosine, 4))

elif choice == '9':
    print('\u03B8 is measured in radians')
    first = float(input("Enter the value of \u03B8:-"))
    tangent = (math.tan(math.radians(first)))
    print("tan",(first),"=",round(tangent, 4))

elif choice == '10':
    base= float(input("Enter the logarithm base:-"))
    number = float(input("Enter the number:-"))
    log = math.log(number, base)
    print("The logarithm of", number, "in base", base, "is",round(log, 5))

    
else:
 print('syntax error')
