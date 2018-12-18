while True:
    print ("options: ")
    print("Enter 'add' to add two numbers")
    print("Enter 'sub' to add subtract numbers")
    print("Enter 'mul' to multiply two numbers")
    print("Enter 'div' to divide two numbers")
    print("Enter 'root' to find square root of a number")
    print("Enter 'sqr' to find square of a number")
    print("Enter 'quit' to end the program")
    
    user_input = input(": ")
    if user_input== "quit":
        break
    elif user_input == "add":...
    elif user_input == "sub":...
    elif user_input == "mul":...
    elif user_input == "div":...
    elif user_input == "root":...
    elif user_input == "sqr":...
    else:
        print("WRONG CHOICE")
        
    if user_input == "add":
        num1= float(input("Enter a number: "))
        num2= float(input("Enter another number: "))
        result= str(num1 + num2)
        print("The answer is " + result)

    if user_input == "sub":
        num1= float(input("Enter a number: "))
        num2= float(input("Enter another number: "))
        result= str(num1 - num2)
        print("The answer is " +result)
        
    if user_input == "Mul":
        num1= float(input("Enter a number: "))
        num2= float(input("Enter another number: "))
        result= str(num1 * num2)
        print("The answer is " + result)

    if user_input == "div":
        num1= float(input("Enter a number: "))
        num2= float(input("Enter another number: "))
        result= str(num1 / num2)
        print("The answer is " + result)
        
    if user_input == "root":
        num1= float(input("Enter a number: "))
        result= str(num1**0.5)
        print("The answer is " + result)

    if user_input == "sqr":
        num1= float(input("Enter a number: "))
        result= str(num1**2)
        print("The answer is " + result)

        
        
