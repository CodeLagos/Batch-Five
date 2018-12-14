#Author:OLAPADE OLUWAFUNMILAYO OLAKITIKE
print("OLAPADE OLUWAFUNMILAYO OLAKITIKE")
#Contact:ola1182006@gmail.com
print("ola1182006@gmail.com")
print("================================================================================")
#Description: This code helps to calculate the exponential of any number.
#             You can use it to compute twenty operations consecutively.
#Welcome the user
print("Welcome to the Exponential Machine")
#print out the instructions
print("please enter a number as Base and Exponent")
#ask the user to enter a value
def power(base, exp):
    if(exp == 0):
       return(1)
    if(exp!=0):
        return(base*power(base,exp-1))
stop = 1
while (stop != 0):
#prompt the user to enter the base
        base = int(input("\nEnter base : "))
#prompt the user to enter the exponential or power
        exp = int(input("Enter exponential value : "))
        print("%d ^ %d is : " %(base, exp), power(base, exp))
        stop = int(input("\n Enter 0 to stop: "))
#stop
