#this is a program to calculate Trigonomentry(shapes)
#By Dahunsi Samuel
#Phone number : 08180703226

print(" A Trigonomentry calculator")
print("please note: The answers r in 2 decimal point")
print("------------------------------------------------------------------------------------")
      
def area_square(L):
    return L * L
def area_rectangle(width , height):
    return width * height
def area_circle(radius):
    return 3.14159 * radius ** 2
def area_triangle(base , height):
    return 0.5 * base * height
def surface_area_sphere(radius):
    return 4 * 3.14159 * radius * radius
def area_parallelogram(base , height):
    return base * height
def area_trapezoid(L1 ,L2 , height):
    return L1 + L2 / 2 * height
def surface_area_cylinder(radius, height):
    return (2 * 3.14159 ** radius) + (2 * 3.14159 * height)
def surface_area_cone(radius, slant_height):
    return (3.14159 * radius * slant_height) + (3.14159 ** radius)
def area_rectangular_prism(lenght, width, height):
    return (2 * lenght * width) + (2 * lenght * height) + (2 * width * height)
def area_triangular_prism(lenght, base, slant_height, height):
    return (base * height) + (2 * lenght * slant_height) + (lenght * base)
def area_pyramid(base, slant_height):
    return (2 * base * slant_height) + (base * base)
def perimeter_square(L):
    return 4 * L
def perimeter_rectangle(lenght, width):
    return lenght * 2 + width * 2
def perimeter_triangle(L1, L2, L3):
    return L1 + L2 + L3
def perimeter_circle(radius):
    return 2 * 3.14159 * radius
def volume_sphere(radius):
    return 4/3 * (3.14159 * radius * radius * radius)
def volume_cylinder(radius, height):
    return 3.14159 *radius * radius * height
def volume_cone(radius, height):
    return 1/3 * (3.14159 * radius * radius * height)
def volume_rectangular_prism(lenght, width, height):
    return lenght * width * height
def volume_triangular_prism(lenght, base, height):
    return 0.5 * (base * lenght) * height
def volume_pyramid(base, height):
    return 1/3 * base * base * height
def options():
    print()
    print("Options:")
    print("The following options below are to calculate the area of some shapes")
    print("1 = calculate the area of a square.")
    print("2 = calculate the area of a circle.")
    print("3 = calculate the area of a rectangle.")
    print("4 = calculate the area of a triangle.")
    print("5 = calculate the area of a parallelogram")
    print("6 = calculate the area of a trapezoid")
    print("7 = calculate the surface area of a sphere")
    print("8 = calculate the surface area of a cylinder")
    print("9 = calculate the surface area of a cone")
    print("10 = calculate the surface area of a rectangular prism")
    print("11 = calculate the surface area of a triangular prism")
    print("12 = calculate the surface area of a pyramid")
    print("                                      ")
    print("The following options below are to calculate the perimeter of some shapes")
    print("13 = calculate the perimeter of a square")
    print("14 = calculate the perimeter of a rectange")
    print("15 = calculate the perimeter of a triangle")
    print("16 = calculate the perimeter of a circle")
    print("                                     ")
    print("The following options below are to calculate volume of some solid shape")
    print("17 = calculate the volume of a sphere")
    print("18 = calculate the volume of a cylinder")
    print("19 = calculate the volume of a cone")
    print("20 = calculate the volume of a rectangular prism")
    print("21 = calculate the volume of a triangular prism")
    print("22 = calculate the volume of a pyramid")
    print("q = please select the alphabet q to quit")
    print()
print("This program will calculate the area, perimeter and volume of some shapes .")
choice = "x"
options()
while choice != "q":
    choice = input("Please enter your choice: ")
    if choice == "1":
        print("you have selected to calculate the area of a square")
        print("                    ")
        L = float(input("Length of square side: "))
        print("The area of this square is",round (area_square(L), 2))
        options()
    elif choice == "2":
        print("you have selected to calculate the area of a circle")
        print("                    ")
        radius = float(input("Radius of the circle: "))
        print("The area of the circle is",round (area_circle(radius), 2))
        options()
    elif choice == "3":
        print("you have selected to calculate the area of a rectangle")
        print("                    ")
        width = float(input("Width of the rectangle: "))
        height = float(input("Height of the rectangle: "))
        print("The area of the rectangle is",round (area_rectangle(width, height), 2))
        options()
    elif choice == "4":
        print("you have selected to calculate the area of a triangle")
        print("                    ")
        base = float(input("Base of the triangle: "))
        height = float(input("Height of the triangle: "))
        print("The area of the triangle is",round (area_triangle(base, height), 2))
        options()
    elif choice == "5":
        print("you have selected to calculate the area of a parallelogram")
        print("                    ") 
        base = float(input("base of the parallelogram: "))
        height = float(input("Height of the parallelogram: "))
        print("The area of the parallelogram is",round (area_parallelogram(base , height), 2))    
        options()
    elif choice == "6":
        print("you have selected to calculate the area of a trapezoid")
        print("                    ")
        L1 = float(input("first lenght of the trapezoid: "))
        L2 = float(input("second lenght of the trapezoid: "))
        height = float(input("height of the trapezoid: "))
        print("The area of the trapezoid is",round (area_trapezoid(L1, L2 , height), 2))    
        options()
    elif choice == "7":
        print("you have selected to calculate the surface area of a sphere")
        print("                    ") 
        radius = float(input("Radius of the sphere: "))
        print("The area of the sphere is",round (surface_area_sphere(radius), 2))
        options()
    elif choice == "8":
        print("you have selected to calculate the surface area of a square")
        print("                    ") 
        radius = float(input("Radius of the cylinder: "))
        height = float(input("height of the cylinder: "))
        print("The area of the cylinder is",round (surface_area_cylinder(radius, height), 2))
        options()
    elif choice == "9":
        print("you have selected to calculate the surface area of a cone")
        print("                    ") 
        radius = float(input("Radius of the cone: "))
        slant_height = float(input("slant_height of the cone: "))
        print("The area of the cone is",round (surface_area_cone(radius, slant_height), 2))
        options()
    elif choice == "10":
        print("you have selected to calculate the surface area of a rectangular prism")
        print("                    ") 
        width = float(input("Width of the rectangular prism: "))
        height = float(input("Height of the rectanglar prism: "))
        lenght = float(input("Lenght of the rectangular prism: "))
        print("The surface area of the rectanglar prism is",round (area_rectangular_prism(lenght, width, height), 2))
        options()
    elif choice == "11":
        print("you have selected to calculate the surface area of a triangular prism")
        print("                    ") 
        base = float(input("base of the triangular prism: "))
        height = float(input("Height of the triangular prism: "))
        lenght = float(input("Lenght of the triangular prism: "))
        slant_height = float(input("slant height of the triangular prism"))
        print("The surface area of the triangular prism is",round (area_triangular_prism(lenght, base, slant_height, height), 2))
        options()
    elif choice == "12":
        print("you have selected to calculate the surface area of a pyramid")
        print("                    ") 
        base = float(input("base of the pyramid: "))
        slant_height = float(input("slant_height of the pyramid: "))
        print("The suface area of the pytamid is",round (area_pyramid(base, slant_height), 2))
        options()
    elif choice == "13":
        print("you have selected to calculate the perimeter of a square")
        print("                    ") 
        L = float(input("Length of square side: "))
        print("The perimeter of this square is",round (perimeter_square(L), 2))
        options()
    elif choice == "14":
        print("you have selected to calculate the perimeter of a rectangle")
        print("                    ") 
        lenght = float(input("Width of the rectangle: "))
        height = float(input("lenght of the rectangle: "))
        print("The perimeter of the rectangle is",round (perimeter_rectangle(lenght, height), 2))
        options()
    elif choice == "15":
        print("you have selected to calculate the perimeter of a triangle")
        print("                    ")   
        L1 = float(input("Lenght 1 of the triangle: "))
        L2 = float(input("lenght 2 of the triangle: "))
        L3 = float(input("Lenght 3 of the triangle: "))
        print("The perimeter of the triangle is",round (perimeter_triangle(L1, L2, L3), 2))
        options()
    elif choice == "16":
        print("you have selected to calculate the perimeter of a circle")
        print("                    ") 
        radius = float(input("Radius of the circle: "))
        print("The perimeter of the circle is",round (perimeter_circle(radius), 2))
        options()
    elif choice == "17":
        print("you have selected to calculate the volume of a sphere")
        print("                    ") 
        radius = float(input("Radius of the sphere: "))
        print("The volume of the sphere is",round (volume_sphere(radius), 2))
        options()
    elif choice == "18":
        print("you have selected to calculate the volume of a cylinder")
        print("                    ") 
        radius = float(input("Radius of the cylinder: "))
        height = float(input("height of the cylinder: "))
        print("The volume of the cylinder is",round (volume_cylinder(radius, height), 2))
        options()
    elif choice == "19":
        print("you have selected to calculate the volume of a cone")
        print("                    ")  
        radius = float(input("Radius of the cone: "))
        height = float(input("height of the cone: "))
        print("The volume of the cone is",round (volume_cone(radius, height), 2))
        options()
    elif choice == "20":
        print("you have selected to calculate the volume of a rectangular prism")
        print("                    ") 
        width = float(input("Width of the rectangular prism: "))
        height = float(input("Height of the rectanglar prism: "))
        lenght = float(input("Lenght of the rectangular prism: "))
        print("The volume of the rectanglar prism is",round (volume_rectangular_prism(lenght, width, height), 2))
        options()
    elif choice == "21":
        print("you have selected to calculate the volume of a triangular prism")
        print("                    ") 
        base = float(input("base of the triangular prism: "))
        height = float(input("Height of the triangular prism: "))
        lenght = float(input("Lenght of the triangular prism: "))        
        print("The volume of the triangular prism is",round (volume_triangular_prism(lenght, base, height), 2))
        options()
    elif choice == "22":
        print("you have selected to calculate the volume of a pyramid")
        print("                    ") 
        base = float(input("base of the pyramid: "))
        height = float(input("Height of the pyramid: "))
        print("The volume of the pyramid is",round (volume_pyramid(base , height), 2))     
        options()    

    elif choice == "q":
        print(" Thank you for using the trig calculator",end="")
    else:
        print("Unrecognized option.")
        options()
