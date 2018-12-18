while True:
    print ("options: ")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to add subtract numbers")
    print("Enter 'multiplication' to multiply two numbers")
    print("Enter 'division' to divide two numbers")
    
    
    user_input = input(": ")
    if user_input== "quit":
        break
    elif user_input == "add":...
    elif user_input == "subtract":...
    elif user_input == "multiplication":...
    elif user_input == "division":...
    else:
        print("wrong")
        
    if user_input == "add":
        num1= float(input("Enter a number: "))
        num2= float(input("Enter another number: "))
        result= str(num1 + num2)
        print("The answer is " + result)

    if user_input == "subtract":
        num1= float(input("Enter a number: "))
        num2= float(input("Enter another number: "))
        result= str(num1 - num2)
        print("The answer is " +result)
        
    if user_input == "Multiplication":
        num1= float(input("Enter a number: "))
        num2= float(input("Enter another number: "))
        result= str(num1 * num2)
        print("The answer is " + result)

    if user_input == "division":
        num1= float(input("Enter a number: "))
        num2= float(input("Enter another number: "))
        result= str(num1 / num2)
        print("The answer is " + result)
