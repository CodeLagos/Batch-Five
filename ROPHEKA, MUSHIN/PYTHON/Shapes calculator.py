#Author: Fele Ayodeji
#This program is a 2D shapes calculator

import time
print("Area of a shape calculator")
n = input("enter your name: ")
print("hey",n ,"this is a machine for calculating the area of some selcted 2D shapes")
time.sleep(2)
shapes = int(input("\n1.square\n2.circle\n3.triangle\n4.parallelogram\n"))
if shapes == 1:
    y = int(input("enter the length:  "))
    area = y**2
    print("the area of the square is" , area ,"cm")
    print("thank you")
elif shapes == 3:
    b = int(input("enter the breadth: "))
    a = int(input("enter the height: "))
    area = b*a
    print("the area of the triangle is" , area, "cm")
    print("thank you")
elif shapes == 2:
    from math import pi
    r =input("please input your radius: ")
    r = float (r)
    x = pi*r**2
    print("the answer is " , round(x,3))
    print("thank you")
elif shapes == 4:
    s = int(input("enter the breadth: "))
    h = int(input("enter the height: "))
    area = s*h
    print("the area of the parallelogram is", area,"cm")
    print("thank you")
else:
    print("this shape does not exist on the list")
    print("thank you")

    
