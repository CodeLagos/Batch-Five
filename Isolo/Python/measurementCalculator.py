print("name= OKORO EGHONGHON")
print("email= eghonghonokoro@gmail.com")
print("project topic= DETERMINATION OF MATHEMATICAL VARIABLES IN MENSURATION")
print("CODE LAGOS BATCH 5")

while True:
    print("thia program will do calculations in mathematical mensuratiion")
    select=int(input("1.Area of circle \n2.Circumference of a circle \n3.Area of triangle \n4.Area of a square \n5.Perimeter of a square \n6.Area of rectanagle \n7.Area of a trapezium"))

    if(select==1):
        radius=float(input("enter radius"))
        pi=3.143
        areaofcircle=round(pi*radius**2)
        print(areaofcircle)
        
    elif(select==2):
        radius=float(input("enter radius"))
        pi=3.143
        circumferenceofcircle=round(2*pi*radius)
        print(circumferenceofcircle)
                     
    elif(select==3):
        base=float(input("enter base"))
        height=float(input("enter height"))
        areaoftriangle=round((base*height)/2)
        print(areaoftriangle)
        
    elif(select==4):
        length=float(input("enter length"))
        areaofsquare=round(length**2)
        print(areaofsquare)

    elif(select==5):
        length=float(input("enter length"))
        perimeterofsquare=round(length*4)
        print(perimeterofsquare)
        
    elif(select==6):
        length=float(input("enter length"))
        breath=float(input("enter breath"))
        areaofrectangle=round(length*breath)
        print(areaofrectangle)

    else:
        (select==7)
        length_x=float(input("enter length_x"))
        length_y=float(input("enter length_y"))
        height=float(input("enter height"))
        areaoftrapezium=round(1/2*(length_x+length_y)*height)
        print(areaoftrapezium)
        
