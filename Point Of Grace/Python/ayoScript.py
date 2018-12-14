#Author:AFOLAYAN AYOMIDE
print("AFOLAYAN AYOMIDE")

print("================================================================================")
#Description: This code helps to determine even numbers between two intervals.
#Display the purpose of the programme
print("Finding even numbers between an interval")
print("please enter the interval")
#print out the instructions
stop = 1
while (stop != 0):
    #ask the user to enter a value
    i = int(input("\n Please enter the initial number: "))
    j = int(input("Please enter the final number: "))
    print("The even number(s) between %d and %d are listed below : " %(i,j))
    for i in range(i, j+1, 1):
        if(i % 2 == 0):
            print( i , end =' ')
    stop = int(input("\n\n Enter 0 to stop: "))
    
    
