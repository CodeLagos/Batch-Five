#Welcome message
print('Name: Olukanyinsola Olomi')
print('Center: Ikeja Old Secreteriat Library')
print('Email: kanyinb@gmail.com')

name=input('Hello! What is your name? ')
print('Hi', name, ', Welcome to a lit calculator!\n')

#Menu options
cont = "y"
while cont.lower() == "y":
    print('\nWhat Mathematical Operation would you like to perform?')
    print('\n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Area of Shapes \n 6. Conversion \n 7. Quadratic Equation \n 8. Number tester \n 9. Exit \n')
    choice=int(input('Enter an option: '))
    #Define
    if (choice>=1 and choice<=4):
        print('Enter two numbers\n')
        num1=float(input('Enter the first number: '))
        num2=float(input('Enter the second number: '))
    if choice==1:
        addition=num1+num2
        print(num1, '+', num2)
        print('Ans = ', addition)
    if choice==2:
        subtraction=num1-num2
        print(num1, '-', num2)
        print('Ans = ', subtraction)
    if choice==3:
        multiplication=num1*num2
        print(num1, 'x', num2)
        print('Ans = ', multiplication)
    if choice==4:
        division=num1/num2
        print(num1, '/', num2)
        print('Ans = ', division)

    elif choice==5:
        #Display welcome message
        print('Welcome to The Area Calculator!\n')
                                  
        #Display shape menu
        shape=input('What shape would you like to calculate its area? \n 1) Triangle \n 2) Circle \n 3) Square \n 4) Rectangle \n')
        #Use the shape number to calculate its area
        if (shape=='1'):
            print('Area of a Triangle')
            base=int(input('Enter the base of the Triangle: '))
            height=int(input('Enter the height of the Triangle: '))
            area=base*height*0.5
            print('0.5', '*', base, '*', height)
            print('The area of the Triangle is: ', area)
        elif (shape=='2'):
            print('Area of a Circle')
            pi=3.142
            radius=int(input('Enter the radius of the Circle: '))
            area=radius*radius*pi
            print(radius, '*', radius, '*', pi)
            print('The area of the Circle is: ', area)
        elif shape=='3':
            print('Area of a Square')
            length=int(input('Enter the length of the Square: '))
            area=length*length
            print('The area of the Square is: ', area)
        elif shape=='4':
            print('Area of a Rectangle')
            length=int(input('Enter the length of the Rectangle: '))
            breadth=int(input('Enter the breadth of the Rectangle: '))
            area=length*breadth
            print('The area of the Rectangle is: ', area)
        else:
            print('INVALID SELECTION')

    elif choice==6:
        print('Welcome to the Converter \n')
        print('What would you like to convert? \n 1. Metres to Centimetres \n 2. Centimetres to Metres \n 3. Celsius to Fahrenheit \n 4. Fahrenheit to Celsius \n 5. Exit \n')
        conv=int(input('Enter an option: '))
        if conv==1:
            metre=float(input('Enter the figure in Metres: '))
            centimetre=metre*100
            print(metre,'m = ', centimetre, 'cm')
        elif conv==2:
            centimetre=float(input('Enter the figure in Centimetre: '))
            Metre=centimetre/100
            print(centimetre,'cm = ', Metre, 'm')
                    
        elif conv==3:
            Celsius=int(input('Enter a temperature in Celsius: '))
            Fahrenheit=9.0/5.0 * Celsius + 32
            print('Temperature:', Celsius, 'Celsius = ', Fahrenheit, 'F')
        elif conv==4:
            Fahrenheit=int(input('Enter a temperature in Fahrenheit: '))
            Celsius=(Fahrenheit-32)*(5/9)
            print('Temperature: ', Fahrenheit, 'F= ', Celsius, 'Celsius')

    elif choice==7:
        #Display welcome message
        print('Hello! Welcome To The Quadratic Equation Calculator!\n')
        import cmath
        import math
            
        #Request for users name
        name=input('Enter your name: ')

        #Display the purpose of the message
        print(name, ', This program solves quadratic equations to the degree of two.\nMeaning there are only THREE needed variables, a, b, c.\nEnter them accordingly \n ')

        #Request for the parameters
        a=float(input('Kindly enter the coefficient with the highest power: '))
        b=float(input('Kindly enter the next coefficient of X: '))
        c=float(input('Kindly enter the constant: '))
                
        d=math.sqrt((b**2)-(4*a*c))
            
        if d==0:
            print(r1 or r2)
        elif d<0:
            print('The equation has no real solution')
        else:
            r1=((-b+d)/(2*a))
            r2=((-b-d)/(2*a))
            print('\nr1 = ', r1, 'and' 'r2 = ', r2,)

    elif choice==8:
        print(name, ', Welcome to the Number Tester!')
        number=int(input("Enter a number:"))
        if(number%2==0):
            print(number,"is an even number")
        else:
            print(number,"is an odd number")

    else:
        print('INVALID SELECTION, you will be redirected to the menu\n')

        
